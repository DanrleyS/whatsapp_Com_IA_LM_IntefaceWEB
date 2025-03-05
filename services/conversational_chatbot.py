from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from utils.conversation_manager import ConversationManager
from services.google_maps import buscar_melhores_locais

import os
import pandas as pd 

# Carregar variáveis de ambiente

client = OpenAI(api_key="Sua_chave_OpenIA")

# Criar roteador do FastAPI
router = APIRouter()

# Carregar frases de Sugestões Locais
def carregar_frases_sugestoes_locais():
    df = pd.read_csv("conversas_unificadas.csv")
    df["mensagem"] = df["mensagem"].str.strip()  # Remove espaços extras que podem atrapalhar a comparação
    return df[df["categoria"] == "Sugestões Locais"]["mensagem"].tolist()

# Lista de frases carregadas
FRASES_SUGESTOES_LOCAIS = carregar_frases_sugestoes_locais()
#print(FRASES_SUGESTOES_LOCAIS)


# Inicializar o gerenciador de conversas
conversation_manager = ConversationManager()

# Modelo de entrada para requisições
class ChatRequest(BaseModel):
    user_id: str
    mensagem: str

@router.post("/chatbot/conversational_chat")
async def conversational_chat(request: ChatRequest):
    user_id = request.user_id
    mensagem = request.mensagem.lower()  # Normalizar para caixa baixa

    # Verificar se o chatbot está esperando uma localização
    if conversation_manager.is_waiting_for_location(user_id):
        # Usuário está respondendo com a localização
        resposta = buscar_melhores_locais(mensagem)  # Chama a API do Google Maps
        conversation_manager.clear_pending_location_request(user_id)  # Resetar o estado
        conversation_manager.add_message(user_id, mensagem)
        conversation_manager.add_message(user_id, resposta, role="assistant")
        return {"resposta": resposta}

    # Adicionar a mensagem ao histórico do usuário
    conversation_manager.add_message(user_id, mensagem)

    # Criar contexto da conversa
    context = conversation_manager.get_context(user_id)

    #print(f"Mensagem recebida: {mensagem.strip()}")
# Normaliza as frases e a mensagem do usuário
    mensagem_normalizada = mensagem.strip().lower()
    frases_normalizadas = [frase.strip().lower() for frase in FRASES_SUGESTOES_LOCAIS]

    #print(f"Frases disponíveis: {frases_normalizadas}")
    # Verificar se o usuário pediu sugestões de locais
    if mensagem_normalizada in frases_normalizadas:
        print("✅ Frase encontrada na lista de sugestões locais!")
        resposta = "Onde você está?"
        conversation_manager.set_pending_location_request(user_id)
        conversation_manager.add_message(user_id, resposta, role="assistant")

        return {"resposta": resposta}
    else:
        print("❌ Frase NÃO encontrada na lista de sugestões locais!")
    
    # Enviar para a OpenAI para respostas gerais
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=context,
            max_tokens=200
        )
        resposta = response.choices[0].message.content
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao obter resposta: {str(e)}")

    # Armazenar resposta no histórico
    conversation_manager.add_message(user_id, resposta, role="assistant")

    return {"resposta": resposta}
