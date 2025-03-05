import joblib

modelo = joblib.load("modelo_classificacao.pkl")

testes = [
    "Preciso enviar um relatório para o chefe.",
    "Quero pedir uma pizza para jantar.",
    "Onde tem um restaurante bom aqui perto?",
    "Qual a capital da França?",
    "Preciso de uma folga no trabalho.",
    "O que é inteligencia IA?."
]

for mensagem in testes:
    categoria = modelo.predict([mensagem])[0]
    print(f"Mensagem: {mensagem} -> Categoria: {categoria}")
