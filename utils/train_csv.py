import pandas as pd

def update_csv(new_data, file_path="conversas_unificadas.csv"):
    """
    Atualiza o arquivo CSV com novos dados antes de treinar o modelo.
    
    :param new_data: Lista de dicionários com 'mensagem' e 'categoria'.
    :param file_path: Caminho do arquivo CSV.
    """
    # Carrega o CSV existente
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["mensagem", "categoria"])  # Cria um novo CSV se não existir

    # Converte os novos dados para DataFrame e adiciona ao arquivo
    new_df = pd.DataFrame(new_data)
    df = pd.concat([df, new_df], ignore_index=True)

    # Salva o CSV atualizado
    df.to_csv(file_path, index=False)
