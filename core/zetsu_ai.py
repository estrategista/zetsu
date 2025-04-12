
import pandas as pd
import os
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

DATASET_PATH = "api_responses.csv"
MODEL_PATH = "zetsu_model.pkl"

def load_dataset():
    if os.path.exists(DATASET_PATH):
        return pd.read_csv(DATASET_PATH)
    return pd.DataFrame({
        "resposta": [
            "erro 500 interno do servidor",
            "requisição concluída com sucesso",
            "tempo limite excedido",
            "autenticação falhou",
            "dados recebidos corretamente"
        ],
        "rotulo": ["falha", "esperado", "falha", "falha", "esperado"]
    })

def save_dataset(df):
    df.to_csv(DATASET_PATH, index=False)

def treinar_modelo():
    df = load_dataset()
    if df.empty:
        raise ValueError("Dataset vazio. Não é possível treinar.")
    modelo = make_pipeline(CountVectorizer(), MultinomialNB())
    modelo.fit(df["resposta"], df["rotulo"])
    joblib.dump(modelo, MODEL_PATH)
    return modelo

def carregar_modelo():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return treinar_modelo()

def classificar_resposta(resposta):
    modelo = carregar_modelo()
    return modelo.predict([resposta])[0]

def registrar_novo_teste(resposta, rotulo):
    if not resposta.strip():
        return
    df = load_dataset()
    novo = pd.DataFrame([{"resposta": resposta.strip(), "rotulo": rotulo}])
    df = pd.concat([df, novo], ignore_index=True)
    save_dataset(df)
    treinar_modelo()  # revalida o aprendizado com nova entrada
