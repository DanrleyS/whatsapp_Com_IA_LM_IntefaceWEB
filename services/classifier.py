# ==========================
# CLASSIFICAÇÃO DE MENSAGENS
# ==========================

import re
import joblib
from collections import Counter

modelo = joblib.load("modelo_classificacao.pkl")

def classificar_mensagem_ml(mensagem):
    """Classifica a mensagem usando o modelo de ML e ajusta a prioridade."""

    #print(f"Mensagem recebida: {mensagem}")  # Debugging

    # Expressão regular para dividir frases por ".", "?", "!", e ";" 
    partes = re.split(r"[.!?;]", mensagem)
    #print(f"Partes separadas: {partes}")  # Debugging

    # Classifica cada parte separadamente
    categorias_detectadas = [modelo.predict([p.strip()])[0] for p in partes if p.strip()]
    #print(f"Categorias detectadas: {categorias_detectadas}")  # Debugging

     # Contar quantas vezes cada categoria apareceu
    contagem = Counter(categorias_detectadas)
    #print(f"Frequência das categorias: {contagem}")  # Debugging

    # Dicionário de prioridade
    prioridades = {
        "Trabalho": 1,
        "Sugestões Locais": 2,
        "Perguntas Gerais": 3,
        "Outros": 4
    }

    # Selecionar a categoria mais frequente
    categoria_mais_frequente = contagem.most_common(1)[0][0]

    # Se houver empate, escolher a que tem maior prioridade
    categorias_com_maior_frequencia = [cat for cat, freq in contagem.items() if freq == contagem[categoria_mais_frequente]]
    
    if len(categorias_com_maior_frequencia) > 1:
        resultado = min(categorias_com_maior_frequencia, key=lambda c: prioridades.get(c, 5))
    else:
        resultado = categoria_mais_frequente

    # Senão, retorna a categoria com menor valor de prioridade
    #print(f"Categoria final: {resultado}")  # Debugging
    return resultado
