import streamlit as st
from datetime import date
from services.sheets_service import read_sheet, append_row

st.title("📝 Registrar movimento")

usuarios = read_sheet("usuarios")

if usuarios.empty:
    st.warning("Nenhum usuário encontrado.")
    st.stop()

nomes = usuarios["nome"].tolist()
usuario_nome = st.selectbox("Usuário", nomes)
usuario = usuarios[usuarios["nome"] == usuario_nome].iloc[0]
user_id = usuario["id"]

data = st.date_input("Data", value=date.today())
ganhou = st.number_input("Quanto ganhou hoje?", min_value=0.0, step=1.0)
gastou = st.number_input("Quanto gastou hoje?", min_value=0.0, step=1.0)
observacao = st.text_area("Observação")

if st.button("Salvar registro"):
    novo_id = f"{user_id}_{data}"
    append_row("registros", [
        novo_id,
        str(user_id),
        str(data),
        float(ganhou),
        float(gastou),
        observacao
    ])
    st.success("Registro salvo com sucesso.")
