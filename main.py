from fastapi import FastAPI
from pydantic import BaseModel
from services.classifier import classificar_mensagem_ml
from services.chatbot import gerar_resposta # Importa a função de gerar resposta pela IA
from services.grouping import agrupar_conversas  # Importa a função de agrupamento
from services.google_maps import buscar_melhores_locais # Importa a função do google maps
import joblib # carregar a ML
from utils.train_endpoint import router as train_router # função para treinar o modelo LM
from services.conversational_chatbot import router as conversational_router  # função do chat conversation

modelo = joblib.load("modelo_classificacao.pkl")

app = FastAPI()

# ==========================
# MODELOS DE DADOS
# ==========================
class ConversaInput(BaseModel):
    conversa: list
    pergunta: str

class MensagemInput(BaseModel):
    mensagem: str

class ChatRequest(BaseModel):
    mensagem: str
    contexto: str = None

class Mensagem(BaseModel):
    usuario: str
    mensagem: str
    hora_envio: str

class ConversaRequest(BaseModel):
    conversa: list[Mensagem]
    pergunta: str

# ==========================
# FUNÇÃO PARA IDENTIFICAR O GRUPO MAIS RELEVANTE
# ==========================
def encontrar_grupo_relevante(grupos, pergunta):
    """Seleciona o grupo de conversa mais relevante para responder a pergunta."""
    pergunta = pergunta.lower()

    melhor_grupo = None
    maior_relevancia = 0

    for grupo in grupos:
        relevancia = sum(1 for mensagem in grupo if any(palavra in pergunta for palavra in mensagem.mensagem.lower().split()))

        if relevancia > maior_relevancia:
            maior_relevancia = relevancia
            melhor_grupo = grupo

    return melhor_grupo


# ==========================
# ENDPOINT PARA PROCESSAR CONVERSAS DO WHATSAPP
# ==========================
@app.post("/processar_conversa/")
async def processar_conversa(request: ConversaRequest):
    grupos = agrupar_conversas(request.conversa)  # Agrupar mensagens antes de buscar a relevante
    grupo_relevante = encontrar_grupo_relevante(grupos, request.pergunta)

    if not grupo_relevante:
        return {"resposta": "Não foi possível encontrar informações relevantes na conversa."}

    # Transformar as mensagens do grupo relevante em um contexto textual
    contexto = "\n".join([f"{msg.usuario}: {msg.mensagem}" for msg in grupo_relevante])

    # Chamar o GPT para gerar a resposta com base no contexto
    resposta = gerar_resposta(request.pergunta, contexto)

    return {"resposta": resposta}


# ==========================
# ENDPOINT PARA CLASSIFICAÇÃO DE MENSAGENS
# ==========================
@app.post("/classificar_mensagem")
def classificar(mensagem_input: MensagemInput):
    categoria = classificar_mensagem_ml(mensagem_input.mensagem)
    #categoria = modelo.predict([mensagem_input.mensagem])[0]
    #categoria = classificar_mensagem(mensagem_input.mensagem)

    # Garante que 'categoria' seja sempre uma string, caso a função retorne uma tupla
    if isinstance(categoria, tuple):
        categoria = categoria[0]

    if categoria == "Trabalho":
        resposta = "Mensagem classificada como trabalho. Nenhuma consulta externa necessária."
    
    elif categoria == "Sugestões Locais":
        resposta = buscar_melhores_locais(mensagem_input.mensagem)

    elif categoria == "Perguntas Gerais":
        resposta = gerar_resposta(mensagem_input.mensagem)
        
    elif categoria == "Outros":
        resposta = "Mensagem classificada como outros. Nenhuma ação necessária."
    
    else:
        resposta = "nenhuma ação necessária"

    return {"categoria": categoria, "resposta": resposta}

# ==========================
# ENDPOINT DO CHATBOT
# ==========================
@app.post("/chatbot/")
async def chatbot(request: ChatRequest):
    resposta = gerar_resposta(request.mensagem, request.contexto)
    return {"resposta": resposta}

# Incluindo o novo endpoint sem modificar lógica existente
app.include_router(train_router)

# Registrar o novo endpoint do chat conversation
app.include_router(conversational_router)