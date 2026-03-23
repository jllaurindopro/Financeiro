from datetime import datetime
import pandas as pd

def calcular_saldo(ganhou, gastou):
    return float(ganhou) - float(gastou)

def calcular_progresso_meta(total_atual, meta):
    if meta == 0:
        return 0
    return min((total_atual / meta) * 100, 100)

def calcular_prejuizo_do_dia(meta_mensal, total_ganho_mes, dia_atual):
    dias_no_mes = 30
    meta_esperada_ate_hoje = (meta_mensal / dias_no_mes) * dia_atual
    prejuizo = meta_esperada_ate_hoje - total_ganho_mes
    return round(prejuizo, 2)

def calcular_necessario_hoje(meta_mensal, total_ganho_mes, dia_atual):
    dias_no_mes = 30
    dias_restantes = max(dias_no_mes - dia_atual, 1)
    restante = max(meta_mensal - total_ganho_mes, 0)
    return round(restante / dias_restantes, 2)

def registros_do_mes(df, user_id):
    if df.empty:
        return df

    df = df.copy()
    df["data"] = pd.to_datetime(df["data"], errors="coerce")
    hoje = datetime.today()
    return df[
        (df["user_id"].astype(str) == str(user_id)) &
        (df["data"].dt.month == hoje.month) &
        (df["data"].dt.year == hoje.year)
    ]
