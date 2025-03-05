import pandas as pd
import joblib
import os
from models.train_model import pipeline  # Importa o modelo treinado
from sklearn.model_selection import train_test_split

# Caminho do dataset
DATASET_PATH = "conversas_unificadas.csv"

def treinar_modelo(dados):
    """
    Treina o modelo de classificação de mensagens com novos dados recebidos via API.
    """
    try:
        # Carregar dataset existente, se existir
        if os.path.exists(DATASET_PATH):
            df = pd.read_csv(DATASET_PATH, header=0)
        else:
            df = pd.DataFrame(columns=["mensagem", "categoria"])

        # Converter para DataFrame e adicionar aos dados existentes
        novos_dados = pd.DataFrame(dados)
        df = pd.concat([df, novos_dados], ignore_index=True)

        # Salvar dataset atualizado
        df.to_csv(DATASET_PATH, index=False)

        # Separar dados para re-treinar o modelo
        X_train, X_test, y_train, y_test = train_test_split(df["mensagem"], df["categoria"], test_size=0.2, random_state=42)

        # Re-treinar o modelo com os novos dados
        pipeline.fit(X_train, y_train)

        # Salvar o modelo atualizado
        joblib.dump(pipeline, "modelo_classificacao.pkl")

        return "Modelo treinado com sucesso!"

    except Exception as e:
        return f"Erro no treinamento: {str(e)}"
