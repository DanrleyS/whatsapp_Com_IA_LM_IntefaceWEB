from django.shortcuts import render
import requests

BASE_API_URL = "http://127.0.0.1:8001"  # Endereço local da API FastAPI

def home(request):
    return render(request, 'core/home.html')


def processar_conversa(request):
    resposta = None
    if request.method == "POST":
        conversa = request.POST.get("conversa")
        pergunta = request.POST.get("pergunta")

        try:
            conversa_json = eval(f"[{conversa}]")  # Converte o texto para lista de dicionários
            response = requests.post(
                f"{BASE_API_URL}/processar_conversa",
                json={"conversa": conversa_json, "pergunta": pergunta}
            )
            resposta = response.json().get("resposta", "Erro ao processar conversa.")
        except Exception as e:
            resposta = f"Erro ao processar JSON: {e}"

    return render(request, "core/processar_conversa.html", {"resposta": resposta})


def classificar_mensagem(request):
    resposta = None
    if request.method == "POST":
        mensagem = request.POST.get("mensagem")
        if mensagem:
            response = requests.post(f"{BASE_API_URL}/classificar_mensagem", json={"mensagem": mensagem})
            if response.status_code == 200:
                resposta = response.json()
    return render(request, "core/classificar_mensagem.html", {"resposta": resposta})


def chatbot(request):
    resposta = None
    if request.method == "POST":
        mensagem = request.POST.get("mensagem")
        response = requests.post(f"{BASE_API_URL}/chatbot", json={"mensagem": mensagem})
        resposta = response.json().get("resposta", "Erro no chatbot.")
    return render(request, "core/chatbot.html", {"resposta": resposta})


def chatbot_conversacional(request):
    resposta = None
    if request.method == "POST":
        user_id = request.POST.get("user_id")  # Captura o user_id da interface
        mensagem = request.POST.get("mensagem")
        
        if user_id and mensagem:  # Verifica se os campos não estão vazios
            response = requests.post(
                f"{BASE_API_URL}/chatbot/conversational_chat",
                json={"user_id": user_id, "mensagem": mensagem}
            )
            resposta = response.json().get("resposta", "Erro na conversa.")
    
    return render(request, "core/chatbot_conversacional.html", {"resposta": resposta})


def treinar_modelo(request):
    resposta = None
    if request.method == "POST":
        mensagens = request.POST.getlist("mensagem")  # Pega todas as mensagens enviadas
        categorias = request.POST.getlist("categoria")  # Pega todas as categorias enviadas

        if mensagens and categorias and len(mensagens) == len(categorias):  # Valida se os dados estão corretos
            dados = [{"mensagem": msg, "categoria": cat} for msg, cat in zip(mensagens, categorias)]
            response = requests.post(f"{BASE_API_URL}/train_model", json={"dados": dados})

            if response.status_code == 200:
                resposta = response.json().get("status", "Treinamento concluído com sucesso.")
            else:
                resposta = "Erro ao treinar modelo."
    
    return render(request, "core/treinar_modelo.html", {"resposta": resposta})
