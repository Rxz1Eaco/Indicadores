import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Configurações iniciais do Streamlit
st.set_page_config(page_title="SLA Atendimentos", page_icon="🏍️")
st.title("Controle SLA Atendimentos 🏍️💨")

# Carregar os dados do arquivo Excel
df_SLA = pd.read_excel("IndicadorSLA.xlsx")

# Mostrar os dados brutos
st.write(df_SLA)

# Cálculo da diferença entre meta e realizado
df_SLA["Diferença (%)"] = df_SLA["SLA Atendimento Realizado (%)"] - df_SLA["SLA Atendimento Meta (%)"]

# Mostrar os dados com a coluna de diferença
st.write(df_SLA)

st.write(f"Gráficos da Semanas: Visualização dos dados de SLA Atendimento Meta(%) vs SLA Atendimento Realizado(%)")

# Criação da interface com colunas horizontais
col1, col2, col3, col4, col5 = st.columns(5)

for semana in range(1, 6):
    df_SLA_Semana = df_SLA[df_SLA['Semana'] == semana]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df_SLA_Semana['Data'], df_SLA_Semana['SLA Atendimento Meta (%)'], label='SLA Atendimento Meta (%)', marker='^',color='green')
    ax.plot(df_SLA_Semana['Data'], df_SLA_Semana['SLA Atendimento Realizado (%)'], label='SLA Atendimento Realizado (%)', marker='o',color='black')

    ax.set_title(f'SLA Atendimento - Semana {semana}')
    ax.set_xlabel('Data')
    ax.set_ylabel('Porcentagem (%)')
    ax.legend()
    ax.grid(True)

    # Mostrar o gráfico na coluna correspondente
    if semana == 1:
        col1.pyplot(fig)
    elif semana == 2:
        col2.pyplot(fig)
    elif semana == 3:
        col3.pyplot(fig)
    elif semana == 4:
        col4.pyplot(fig)
    elif semana == 5:
        col5.pyplot(fig)
    
