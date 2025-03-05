from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from utils.train_handler import treinar_modelo  # Chama a função de treino

router = APIRouter()

# Definição do formato da entrada
class TreinamentoInput(BaseModel):
    dados: list[dict]  # Lista de mensagens e categorias

@router.post("/train_model")
def train_model(input_data: TreinamentoInput):
    """Endpoint para treinar o modelo com novos dados"""
    try:
        mensagem = treinar_modelo(input_data.dados)
        return {"status": mensagem}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
