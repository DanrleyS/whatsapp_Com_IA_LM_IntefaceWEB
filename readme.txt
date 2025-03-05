📌 WhatsApp AI - Processamento Inteligente de Conversas 🤖💬
WhatsApp AI é um projeto que utiliza Inteligência Artificial para processar, classificar e responder mensagens no WhatsApp de forma automática. Com uma interface interativa em Django e uma API robusta em FastAPI, este sistema permite:

✅ Processar conversas e responder perguntas contextuais.
✅ Classificar mensagens automaticamente em categorias.
✅ Interagir com um chatbot inteligente.
✅ Treinar um modelo de aprendizado de máquina com novos dados.

🔥 Ideal para empresas, assistentes virtuais e automação de mensagens!

🚀 Recursos Principais
🔹 Processamento de Conversas – Envia uma conversa e recebe respostas com base no contexto.
🔹 Classificação de Mensagens – Categoriza mensagens automaticamente.
🔹 Chatbot – Um assistente de IA que responde a perguntas.
🔹 Chatbot Conversacional – Mantém contexto e interage de forma mais natural.
🔹 Treinamento de Modelo – Aprimore a IA treinando com novas mensagens e categorias.

🛠 Principais Tecnologias Utilizadas
Django – Framework Web para a interface gráfica.
FastAPI – Backend rápido para processamento das mensagens.
Python – Linguagem principal do projeto.
Machine Learning – Classificação de mensagens e respostas inteligentes.

📌 Como Executar o Projeto
🔹 1️⃣ Clonar o Repositório
sh
git clone https://github.com/DanrleyS/whatsapp_Com_IA_LM_IntefaceWEB
cd whatsapp-ai

🔹 2️⃣ Criar e Ativar um Ambiente Virtual
sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows

🔹 3️⃣ Instalar Dependências
sh
pip install -r requirements.txt

🔹 4️⃣ Iniciar o Servidor FastAPI (Backend)
sh
uvicorn main:app --reload --host 127.0.0.1 --port 8001

🔹 5️⃣ Iniciar o Servidor Django (Frontend)
sh
python manage.py runserver 8000
📌 Agora, acesse: http://127.0.0.1:8000 e comece a interagir com a interface!

🖥 Demonstração da Interface
A interface é simples e intuitiva. Veja alguns exemplos das telas principais:

📜 Processamento de Conversas
✅ Insira uma conversa em formato JSON
✅ Pergunte algo sobre a conversa
✅ Receba a resposta com base no contexto

🔹 Exemplo de Entrada:

json
{
    "conversa": [
        {"usuario": "João", "mensagem": "Oi, pessoal! Vamos marcar a reunião?", "hora_envio": "2025-02-18T09:00:00"},
        {"usuario": "Maria", "mensagem": "Bom dia! Tudo bem. Que tal às 14h?", "hora_envio": "2025-02-18T09:01:00"}
    ],
    "pergunta": "Que horas será a reunião?"
}
🔹 Saída Esperada:
json

{"resposta": "A reunião está marcada para às 14hm conforme sugerido por Maria"}

🏷️ Classificação de Mensagens
✅ Envie uma mensagem
✅ Receba a categoria correspondente

🔹 Exemplo de Entrada:
json
{"mensagem": "Tem reunião hoje?"}

🔹 Saída Esperada:
json
categoria: Trabalho
Mensagem classificada como trabalho. Nenhuma consulta externa necessária.
Existem outras categorias como "Sugestões locais": o qual fornece um endereço com base no google maps.
"perguntas gerais", que responde qualquer pergunta com tecnologia de IA.

🤖 Chatbot Inteligente
✅ Converse com a IA e receba respostas úteis.

🔹 Exemplo de Pergunta:
json
{"mensagem": "Qual o endereço da empresa?"}

🔹 Saída Esperada:
json
{"resposta": "A empresa fica na Rua Exemplo, 123, São Paulo - SP."}

💬 Chatbot Conversacional
✅ Mantém o contexto e responde de forma mais natural.
✅ Cada usuário tem um ID exclusivo.

🔹 Exemplo de Entrada:
json
{
    "user_id": "13",
    "mensagem": "Qual o endereço completo?"
}

🔹 Saída Esperada:
json
{"resposta": "O endereço é Av. Paulista, 1000, São Paulo - SP."}

📊 Treinar Modelo de IA
✅ Adicione novas mensagens e categorias para melhorar a IA.
🔹 Exemplo de Entrada:

json

mensagem: Tem reunião hoje?, categoria: Trabalho
mensagem: Onde tem uma farmácia?, categoria: Sugestões Locais
mensagem: O que é inteligência artificial?, categoria: Perguntas Gerais

🔹 Saída Esperada:

json
{"status": "Treinamento concluído com sucesso!"}

🔥 Possíveis Melhorias Futuras
✅ Autenticação de usuários para histórico de conversas.
✅ Integração com WhatsApp real via Twilio ou API oficial.
✅ Melhoria nos modelos de Machine Learning para mais precisão.

🎯 Contribuições
Quer contribuir com o projeto? Sinta-se à vontade para abrir uma Issue ou enviar um Pull Request!

