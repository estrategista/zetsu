
import streamlit as st
import hashlib
import datetime
import base64
import pandas as pd
from zetsu_ai import classificar_resposta, registrar_novo_teste

# Áudio simbólico
sound = 'data:audio/wav;base64,UklGRiQAAABXQVZFZm10IBAAAAABAAEAESsAACJWAAACABAAZGF0YQAAAAA='

def play_sound():
    st.audio(sound, format="audio/wav")

def interface_login():
    st.title("ZETSU TERMINAL PLUS")
    st.markdown("> _A sombra aguarda a senha do general._")
    senha = st.text_input("Digite a senha do general:", type="password")
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    senha_correta = hashlib.sha256("sombra123".encode()).hexdigest()
    return senha_valida(senha)

def menu_principal():
    return st.selectbox("Escolha a versão Zetsu:", ["Zetsu V1", "Zetsu V2", "Zetsu V3", "Diagnóstico API"])

def versao_v1():
    st.markdown("**Zetsu V1 — Núcleo Simbólico**")
    if st.button("Ativar V1"):
        play_sound()
        st.markdown("> *A raiz foi plantada no silêncio.*")

def versao_v2():
    st.markdown("**Zetsu V2 — IA + Criptografia**")
    user_input = st.text_input("Envie uma mensagem para Zetsu:")
    if st.button("Ativar V2"):
        play_sound()
        response = "O plano não é visível. Mas age." if "plano" in user_input.lower() else "A pergunta foi registrada no silêncio."
        hashed = hashlib.sha256(user_input.encode()).hexdigest()
        st.markdown(f"**Resposta IA:** {response}")
        st.markdown(f"**Mensagem criptografada:** `{hashed}`")

import csv

LOG_FILE = "zetsu_logs.csv"

def salvar_log(acao):
    timestamp = datetime.datetime.now().isoformat()
    with open(LOG_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, acao])
    return f"Log salvo: {acao}"

import csv
from collections import Counter

LOG_FILE = "zetsu_logs.csv"

def salvar_log(acao):
    timestamp = datetime.datetime.now().isoformat()
    with open(LOG_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, acao])
    return f"Log salvo: {acao}"

def interpretar_logs(path=LOG_FILE):
    if not os.path.exists(path):
        return "Nenhum log encontrado."

    df = pd.read_csv(path, header=None, names=["timestamp", "acao"])
    if df.empty:
        return "Arquivo de log está vazio."

    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df = df.dropna(subset=["timestamp"])
    df["dia"] = df["timestamp"].dt.date

    total_entradas = len(df)
    dias_unicos = df["dia"].nunique()
    entradas_por_acao = Counter(df["acao"])

    mensagem = []

    if dias_unicos == 1 and total_entradas > 10:
        mensagem.append("ALERTA: Alta atividade concentrada. Pico de decisões detectado.")
    if dias_unicos > 5 and total_entradas < 10:
        mensagem.append("OBSERVAÇÃO: Longo silêncio com poucas ações. O plano está adormecido.")
    if any(count > 3 for count in entradas_por_acao.values()):
        repetidas = [acao for acao, count in entradas_por_acao.items() if count > 3]
        mensagem.append(f"PADRÃO DETECTADO: Comando(s) repetido(s) com intensidade: {', '.join(repetidas)}")

    if not mensagem:
        mensagem.append("O fluxo está equilibrado. A sombra acompanha em silêncio.")

    return "\n".join(mensagem)

def versao_v3():
    st.markdown("**Zetsu V3 — Estratégia e Logs**")
    if "logs" not in st.session_state:
        st.session_state.logs = []
    action = st.text_input("Descreva uma ação estratégica:")
    if st.button("Registrar Ação"):
        timestamp = datetime.datetime.now().isoformat()
        entry = f"{timestamp} - {action}"
        st.session_state.logs.append(entry)
        st.success("Ação registrada.")\n        salvar_log(action)
        play_sound()
    if st.button("Exibir Logs"):
        for log in st.session_state.logs:
        interpretacao = interpretar_logs()
        st.markdown("### Leitura Simbólica dos Logs")
        st.info(interpretacao)

    if st.button("Baixar Logs (.csv)"):
        with open(LOG_FILE, "rb") as log_file:
            st.download_button(label="Clique para baixar", data=log_file, file_name="zetsu_logs.csv", mime="text/csv")

            st.markdown(f"`{log}`")

def diagnostico_api():
    st.markdown("**Zetsu Intelligence — Diagnóstico de APIs**")
    resposta_api = st.text_area("Cole a resposta da API para análise:")
    if st.button("Classificar"):
        if resposta_api.strip():
            resultado = classificar_resposta(resposta_api)
            st.markdown(f"**Diagnóstico:** `{resultado.upper()}`")
            registrar_novo_teste(resposta_api, resultado)
            st.success("Registrado no aprendizado do Zetsu.")

# Execução principal
st.set_page_config(page_title="Zetsu Terminal Plus", layout="centered", page_icon="☯")
st.image("A_digital_graphic_design_displays_the_logo_and_nam.png", width=300)
st.markdown("<h3 style='text-align: center;'>A Sombra se Revela</h3>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(
    """
    <style>
    body {
        background-color: #000;
        color: #33ffcc;
        font-family: 'Courier New', monospace;
    }
    .stButton>button {
        background-color: #33ffcc;
        color: black;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True
)

if interface_login():
    st.success("Autorizado. A sombra reconhece o general.")
    play_sound()
    versao = menu_principal()
    if versao == "Zetsu V1":
        versao_v1()
    elif versao == "Zetsu V2":
        versao_v2()
    elif versao == "Zetsu V3":
        versao_v3()
    elif versao == "Diagnóstico API":
        diagnostico_api()
else:
    st.warning("Acesso restrito. A senha da sombra é necessária.")
