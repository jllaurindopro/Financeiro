import streamlit as st
from services.sheets_service import read_sheet

st.title("🎯 Metas")

usuarios = read_sheet("usuarios")

if usuarios.empty:
    st.warning("Nenhum usuário encontrado.")
    st.stop()

nomes = usuarios["nome"].tolist()
usuario_nome = st.selectbox("Selecione o usuário", nomes)

usuario = usuarios[usuarios["nome"] == usuario_nome].iloc[0]

st.write(f"**Meta mensal:** R$ {float(usuario['meta_mensal']):,.2f}")
st.write(f"**Meta de economia:** R$ {float(usuario['meta_economia']):,.2f}")
st.write(f"**Meta de renda:** R$ {float(usuario['meta_renda']):,.2f}")
st.write(f"**Streak atual:** {usuario['streak']}")
st.write(f"**Nível:** {usuario['nivel']}")
st.write(f"**Pontos:** {usuario['pontos']}")
