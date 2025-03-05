import os
import openai


openai.api_key = "sua_chave_API"

def gerar_resposta(pergunta, contexto=None):
    """Gera uma resposta com base no contexto da conversa, garantindo que a fonte da informação seja mencionada corretamente."""
    try:
        messages = [
            {"role": "system", "content": "Você é um assistente que responde perguntas baseado no contexto da conversa. Sempre mencione corretamente quem forneceu a informação."}
        ]
        
        if contexto:
            messages.append({"role": "user", "content": f"""
            Baseado na seguinte conversa:

            {contexto}

            Responda a pergunta: "{pergunta}"

            Se a resposta for baseada em uma mensagem de um usuário específico, mencione o nome dele corretamente.
            Se a resposta exigir inferência ou não houver uma resposta exata na conversa, explique isso.
            """})
        else:
            messages.append({"role": "user", "content": f"Pergunta: {pergunta}"})
        
        resposta = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=300
        )
        
        return resposta.choices[0].message.content.strip()
    
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"
