📩 WhatsApp AI - Processamento Inteligente de Mensagens
API desenvolvida para classificar e responder mensagens no WhatsApp com inteligência artificial. A API utiliza Machine Learning para classificar mensagens em categorias e fornece respostas contextuais utilizando OpenAI GPT.

🚀 Funcionalidades:

📌 Classificação Inteligente de Mensagens
A API classifica mensagens em:
trabalho: relacionadas a atividades profissionais.
sugestoes_locais: pedidos de recomendações de locais.
perguntas_gerais: perguntas gerais que podem ser respondidas pela IA.
outros: mensagens sem classificação específica.

💬 Geração de Respostas com OpenAI GPT
Responde automaticamente perguntas gerais.
📍 Integração com Google Maps
Sugere locais com base no contexto da mensagem.

🛠️ Tecnologias Utilizadas
FastAPI - Framework para criação da API REST.
scikit-learn - Treinamento do modelo de Machine Learning para classificação.
OpenAI GPT - Responde a perguntas gerais.
Google Maps API - Busca locais recomendados.
pandas & joblib - Manipulação de dados e persistência do modelo.

📥 Instalação e Configuração
1️⃣ Clone o repositório:
bash:
git clone https://github.com/seu-usuario/whatsapp_AI.git
cd whatsapp_AI

2️⃣ Crie um ambiente virtual e ative (opcional):
bash:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

3️⃣ Instale as dependências:
bash:
pip install -r requirements.txt

4️⃣ Crie um arquivo .env e configure suas chaves:
ini
OPENAI_API_KEY= "sua-chave-da-openai"
GOOGLE_MAPS_API_KEY= "sua-chave-do-google-maps"

5️⃣ Treine o modelo de Machine Learning:
bash:
python models/train_model.py

6️⃣ Execute a API:
bash:
uvicorn main:app --reload
A API estará disponível em http://127.0.0.1:8000.

📡 Endpoints da API
🔹 1. Classificação e Resposta de Mensagens
POST /classificar_mensagem

📌 Descrição: Classifica a mensagem e retorna a categoria com uma resposta adequada.

📥 Exemplo de Requisição:
json:

{
  "mensagem": "Onde fica um bom restaurante para almoçar? Preciso também revisar um relatório urgente para o cliente."
}

📤 Exemplo de Resposta:
json:
{
  "categoria": "trabalho",
  "resposta": "Mensagem classificada como trabalho. Nenhuma consulta externa necessária."
}

📤 Outras categorias:
Sugestões de Locais
Perguntas Gerais
Outros

🔹 2. Treinar o Modelo de Machine Learning
POST /train_model

📌 Descrição: Treina o modelo com novos dados para melhorar a classificação de mensagens.

📥 Exemplo de Requisição:

json:
{
  "dados": [
    {"mensagem": "Tem reunião hoje?", "categoria": "trabalho"},
    {"mensagem": "Sabe onde tem uma farmácia?", "categoria": "sugestoes_locais"},
    {"mensagem": "O que é inteligência artificial?", "categoria": "perguntas_gerais"}
  ]
}

📤 Exemplo de Resposta:
json
{
  "status": "Modelo treinado com sucesso!"
}

🔹 3. Processar conversas
POST /processar_conversa

📌 Descrição: Processa uma conversa e retorna respostas com relação a ela.

📥 Exemplo de Requisição:

json>
{
    "conversa": [
        {"usuario": "João", "mensagem": "Oi, pessoal! Vamos marcar a reunião?", "hora_envio": "2025-02-18T09:00:00"},
        {"usuario": "Maria", "mensagem": "Bom dia! Tudo bem. Que tal às 14h?", "hora_envio": "2025-02-18T09:01:00"},
        {"usuario": "Carlos", "mensagem": "14h está ótimo para mim.", "hora_envio": "2025-02-18T09:02:30"},
        {"usuario": "Ana", "mensagem": "Por mim também.", "hora_envio": "2025-02-18T09:03:15"},
        {"usuario": "João", "mensagem": "Perfeito! Então, reunião marcada para às 14h.", "hora_envio": "2025-02-18T09:04:00"},
        {"usuario": "Carlos", "mensagem": "Vocês viram o último jogo de xadrez do Magnus Carlsen?", "hora_envio": "2025-02-18T10:00:00"},
        {"usuario": "João", "mensagem": "Sim! Que partida incrível! Ele jogou muito bem.", "hora_envio": "2025-02-18T10:01:45"}
    ],
    "pergunta": "Que horas será a reunião?"
}

📤 Exemplo de Resposta:

json:
{
  "resposta": "A Reunião será as 14 horas, conforme sugerido por Maria"
}
🏗️ Estrutura do Projeto

whatsapp_AI/
│── models/         # Modelos de Machine Learning
│── services/       # Serviços de processamento de mensagens
│── utils/          # Funções auxiliares
│── main.py         # Arquivo principal da API
│── requirements.txt # Dependências do projeto
│── .env            # Configurações de API Keys

📝 Notas Finais
O modelo de Machine Learning é treinado com um conjunto de mensagens previamente classificadas.
A API pode ser expandida para suportar novas funcionalidades, como integração com outros serviços.
Feedbacks e melhorias são bem-vindos! 🚀
