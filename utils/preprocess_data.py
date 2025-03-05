import pandas as pd

def preprocess_data(file_path):
    """
    Carrega o dataset, remove valores NaN e faz o pré-processamento necessário.
    
    :param file_path: Caminho do arquivo CSV.
    :return: DataFrame limpo.
    """
    df = pd.read_csv(file_path, header=0)
    
    # Normaliza os nomes das colunas
    df.columns = df.columns.str.lower().str.strip()
    
    # Remover colunas duplicadas, mantendo apenas 'mensagem' e 'categoria'
    df = df[['mensagem', 'categoria']].copy() if 'categoria' in df.columns else df[['mensagem', 'Categoria']].copy()
    
    # Renomear 'Categoria' para 'categoria' caso necessário
    df = df.rename(columns={"Categoria": "categoria"})

    # Remover valores NaN
    df.dropna(subset=["mensagem", "categoria"], inplace=True)

    return df
