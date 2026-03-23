import streamlit as st
from datetime import datetime
from services.sheets_service import read_sheet
from services.calculations import (
    calcular_prejuizo_do_dia,
    calcular_necessario_hoje,
    calcular_progresso_meta,
    registros_do_mes
)

st.title("📊 Dashboard")

usuarios = read_sheet("usuarios")
registros = read_sheet("registros")

if usuarios.empty:
    st.warning("Nenhum usuário encontrado na planilha.")
    st.stop()

nomes = usuarios["nome"].tolist()
usuario_nome = st.selectbox("Selecione o usuário", nomes)

usuario = usuarios[usuarios["nome"] == usuario_nome].iloc[0]
user_id = usuario["id"]
meta_mensal = float(usuario["meta_mensal"])

registros_mes = registros_do_mes(registros, user_id)

total_ganho_mes = registros_mes["ganhou"].sum() if not registros_mes.empty else 0
total_gasto_mes = registros_mes["gastou"].sum() if not registros_mes.empty else 0
saldo_mes = total_ganho_mes - total_gasto_mes

dia_atual = datetime.today().day
prejuizo_hoje = calcular_prejuizo_do_dia(meta_mensal, total_ganho_mes, dia_atual)
necessario_hoje = calcular_necessario_hoje(meta_mensal, total_ganho_mes, dia_atual)
progresso = calcular_progresso_meta(total_ganho_mes, meta_mensal)

col1, col2, col3 = st.columns(3)

col1.metric("💸 Perdendo / atrasado", f"R$ {prejuizo_hoje:,.2f}")
col2.metric("💰 Ganho no mês", f"R$ {total_ganho_mes:,.2f}")
col3.metric("📉 Gasto no mês", f"R$ {total_gasto_mes:,.2f}")

st.progress(min(int(progresso), 100))
st.write(f"Progresso da meta: **{progresso:.1f}%**")

st.error(f"Hoje você precisa gerar **R$ {necessario_hoje:,.2f}** para perseguir a meta.")

if saldo_mes < 0:
    st.warning("Você está negativo no mês. Seu comportamento está destruindo sua meta.")
else:
    st.success(f"Saldo do mês: R$ {saldo_mes:,.2f}")
