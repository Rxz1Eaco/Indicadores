import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="SLA Atendimentos", page_icon="🏍️")
st.title("Controle SLA Atendimentos 🏍️💨")
df_SLA = pd.read_excel("Database\IndicadorSLA.xlsx")
st.markdown("Dados Originais")
st.write(df_SLA)

st.markdown("Cálculo da diferença entre meta e realizado")
df_SLA["Diferença (%)"] = df_SLA["SLA Atendimento Realizado (%)"] - df_SLA["SLA Atendimento Meta (%)"]
st.write(df_SLA)

# Iterar sobre cada semana e criar visualizações
for semana in range(1, 6):  # de semana 1 a semana 5
    df_SLA_Semana = df_SLA[df_SLA['Semana'] == semana]

    # Mostrar os dados específicos da semana
    st.write(f'Dados da Semana {semana}')

    # Criar o gráfico para a semana específica
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df_SLA_Semana['Data'], df_SLA_Semana['SLA Atendimento Meta (%)'], label='SLA Atendimento Meta (%)', marker='o')
    ax.plot(df_SLA_Semana['Data'], df_SLA_Semana['SLA Atendimento Realizado (%)'], label='SLA Atendimento Realizado (%)', marker='o')

    # Adicionar título e rótulos
    ax.set_title(f'SLA Atendimento - Semana {semana} de Julho')
    ax.set_xlabel('Data')
    ax.set_ylabel('Porcentagem (%)')
    ax.legend()
    ax.grid(True)

    # Mostrar o gráfico no Streamlit
    st.pyplot(fig)
