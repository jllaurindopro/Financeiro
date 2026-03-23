import streamlit as st

st.title("📊 Dashboard")

st.subheader("Seu status hoje")

col1, col2, col3 = st.columns(3)

col1.metric("💸 Perdendo hoje", "R$ 120,00")
col2.metric("💰 Ganho hoje", "R$ 80,00")
col3.metric("🎯 Meta diária", "R$ 200,00")

st.divider()

st.error("⚠️ Você está ATRASADO na sua meta.")

st.progress(40)

st.write("Progresso: 40%")

st.divider()

st.subheader("🚨 Ação obrigatória")

st.warning("Você precisa gerar pelo menos R$ 120 HOJE para não perder o dia.")

if st.button("EXECUTAR AGORA"):
    st.success("Ação iniciada. Sem desculpas.")
