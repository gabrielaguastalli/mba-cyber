import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def gerar_dados_vendas():
    produtos = ['Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E']
    vendas = np.random.randint(10, 60, size=len(produtos))
    return pd.DataFrame({'Produto': produtos, 'Vendas': vendas})

def gerar_insight(df):
    max_venda = df['Vendas'].max()
    min_venda = df['Vendas'].min()
    produto_mais_vendido = df[df['Vendas'] == max_venda]['Produto'].values[0]
    produto_menos_vendido = df[df['Vendas'] == min_venda]['Produto'].values[0]
    return f"O produto mais vendido foi o **{produto_mais_vendido}** com {max_venda} unidades, enquanto o **{produto_menos_vendido}** teve a menor venda com {min_venda} unidades."

def app():
    st.set_page_config(page_title="InsightBot Contabilizei", layout="centered")
    st.title("🤖 InsightBot Contabilizei")
    st.subheader("Faça uma pergunta sobre os dados da empresa:")

    pergunta = st.text_input("Digite sua pergunta em linguagem natural:", 
                             "Como estão as vendas do trimestre por produto e região?")
    
    if st.button("Gerar Insight"):
        df_vendas = gerar_dados_vendas()

        st.markdown("### 📊 Gráfico de Vendas por Produto")
        fig, ax = plt.subplots()
        ax.plot(df_vendas['Produto'], df_vendas['Vendas'], marker='o', linestyle='-', color='#008080')
        ax.set_xlabel("Produto")
        ax.set_ylabel("Vendas")
        ax.set_title("Vendas por Produto - Região Sul")
        st.pyplot(fig)

        st.markdown("### 💡 Insight Gerado")
        insight = gerar_insight(df_vendas)
        st.info(insight)

app()
