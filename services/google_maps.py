import os
import requests

import re


GOOGLE_MAPS_API_KEY = "chave_maps_API"

def buscar_melhores_locais(mensagem):
    """Busca locais no Google Maps com base na mensagem do usuário, detectando automaticamente a categoria."""

    mensagem = mensagem.lower()

    # Tenta encontrar uma localização com base em padrões comuns de escrita
    padrao_localizacao = r"no\s+([\w\s,]+)|em\s+([\w\s,]+)"
    match = re.search(padrao_localizacao, mensagem)

    if match:
        localizacao = match.group(1) if match.group(1) else match.group(2)
        localizacao = localizacao.strip()
    else:
        return "Não foi possível identificar a localização."

    # Remove a localização da mensagem para obter apenas o tipo de local desejado
    tipo_de_local = mensagem.replace(localizacao, "").strip(" ,?")

    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

    params = {
        "query": f"{tipo_de_local} em {localizacao}",  # Exemplo: "restaurante em São Paulo"
        "key": GOOGLE_MAPS_API_KEY
    }

    response = requests.get(url, params=params)
    dados = response.json()

    if "results" not in dados or not dados["results"]:
        return f"Nenhum local encontrado para '{tipo_de_local}' em '{localizacao}'."

    # Pegar o melhor local com base na avaliação
    melhor_local = max(dados["results"], key=lambda r: r.get("rating", 0))

    nome = melhor_local.get("name", "Nome não disponível")
    nota = melhor_local.get("rating", "Nota não disponível")
    endereco = melhor_local.get("formatted_address", "Endereço não disponível")

    return f"Sugestão: {nome} - Nota {nota}, localizado em {endereco}."
