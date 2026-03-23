import streamlit as st
from datetime import date
from services.sheets_service import read_sheet, append_row

st.title("🔥 Missões")

usuarios = read_sheet("usuarios")
missoes = read_sheet("missoes")

if usuarios.empty:
    st.warning("Nenhum usuário encontrado.")
    st.stop()

nomes = usuarios["nome"].tolist()
usuario_nome = st.selectbox("Usuário", nomes)
usuario = usuarios[usuarios["nome"] == usuario_nome].iloc[0]
user_id = usuario["id"]

st.subheader("Criar missão")

descricao = st.text_input("Descrição da missão")
recompensa = st.number_input("Recompensa em pontos", min_value=0, step=1)
penalidade = st.number_input("Penalidade em pontos", min_value=0, step=1)

if st.button("Adicionar missão"):
    novo_id = f"{user_id}_{date.today()}_{descricao[:8]}"
    append_row("missoes", [
        novo_id,
        str(user_id),
        str(date.today()),
        descricao,
        "pendente",
        recompensa,
        penalidade
    ])
    st.success("Missão criada.")

st.subheader("Missões do usuário")
missoes_user = missoes[missoes["user_id"].astype(str) == str(user_id)] if not missoes.empty else missoes
st.dataframe(missoes_user, use_container_width=True)
