import pandas as pd
import joblib
import nltk
import sys
import os
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.preprocess_data import preprocess_data
#from utils.train_csv import update_csv

# Baixar stopwords se necessário
nltk.download("stopwords")
stop_words = stopwords.words("portuguese")

# Carregar dataset
df = preprocess_data("conversas_unificadas.csv")
#df = pd.read_csv("conversas_unificadas.csv", header=0)
#df.columns = df.columns.str.lower().str.strip()

# Separar dados
X_train, X_test, y_train, y_test = train_test_split(df["mensagem"], df["categoria"], test_size=0.2, random_state=42)


# Criar pipeline de Machine Learning
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words=stop_words)),
    ("modelo", MultinomialNB())
])

# Treinar modelo
pipeline.fit(X_train, y_train)

# Avaliar modelo
y_pred = pipeline.predict(X_test)
print(f"Acurácia: {accuracy_score(y_test, y_pred):.2f}")

# Salvar modelo treinado
joblib.dump(pipeline, "modelo_classificacao.pkl")
print("Modelo salvo com sucesso!")


