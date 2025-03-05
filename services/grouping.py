from datetime import datetime, timedelta
from typing import List, Dict

def agrupar_conversas(conversa: List[Dict]) -> List[List[Dict]]:
    """
    Agrupa as mensagens em conversas coerentes, separando grupos 
    com base em 30 minutos de inatividade.
    """
    if not conversa:
        return []

    # Ordenar mensagens pelo horário de envio
    conversa.sort(key=lambda x: x.hora_envio)

    grupos = []
    grupo_atual = [conversa[0]]

    for i in range(1, len(conversa)):
        hora_atual = datetime.fromisoformat(conversa[i].hora_envio)
        hora_anterior = datetime.fromisoformat(conversa[i - 1].hora_envio)
        

        # Se a diferença entre mensagens for maior que 30 minutos, inicia novo grupo
        if hora_atual - hora_anterior >= timedelta(minutes=30):
            grupos.append(grupo_atual)
            grupo_atual = []

        grupo_atual.append(conversa[i])

    # Adiciona o último grupo
    if grupo_atual:
        grupos.append(grupo_atual)

    return grupos
