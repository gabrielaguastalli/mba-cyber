### Documentação Técnica - InsightBot Contabilizei

#### Descrição Geral
O código implementa uma aplicação web interativa utilizando o framework **Streamlit**. A aplicação, chamada **InsightBot Contabilizei**, gera insights sobre dados fictícios de vendas de produtos e exibe gráficos para visualização. O objetivo é permitir que o usuário obtenha informações úteis sobre os dados de vendas de forma simples e intuitiva.

---

### Estrutura do Código

#### Importação de Bibliotecas
```python
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
```
- **streamlit**: Framework para criação de aplicações web interativas.
- **matplotlib.pyplot**: Biblioteca para criação de gráficos.
- **pandas**: Biblioteca para manipulação de dados em formato tabular.
- **numpy**: Biblioteca para operações matemáticas e geração de dados aleatórios.

---

#### Funções

##### 1. `gerar_dados_vendas()`
```python
def gerar_dados_vendas():
    produtos = ['Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E']
    vendas = np.random.randint(10, 60, size=len(produtos))
    return pd.DataFrame({'Produto': produtos, 'Vendas': vendas})
```
- **Descrição**: Gera um conjunto fictício de dados de vendas para cinco produtos.
- **Entrada**: Não possui parâmetros de entrada.
- **Saída**: Retorna um `DataFrame` com duas colunas:
  - `Produto`: Nome dos produtos.
  - `Vendas`: Quantidade de vendas geradas aleatoriamente.

---

##### 2. `gerar_insight(df)`
```python
def gerar_insight(df):
    max_venda = df['Vendas'].max()
    min_venda = df['Vendas'].min()
    produto_mais_vendido = df[df['Vendas'] == max_venda]['Produto'].values[0]
    produto_menos_vendido = df[df['Vendas'] == min_venda]['Produto'].values[0]
    return f"O produto mais vendido foi o **{produto_mais_vendido}** com {max_venda} unidades, enquanto o **{produto_menos_vendido}** teve a menor venda com {min_venda} unidades."
```
- **Descrição**: Analisa os dados de vendas e gera um insight sobre o produto mais vendido e o menos vendido.
- **Entrada**: 
  - `df`: Um `DataFrame` contendo os dados de vendas.
- **Saída**: Retorna uma string formatada com o insight gerado.

---

##### 3. `app()`
```python
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
```
- **Descrição**: Função principal que define a interface da aplicação e a lógica de interação com o usuário.
- **Funcionalidades**:
  - Configura a página com título e layout centralizado.
  - Exibe um campo de texto para o usuário digitar uma pergunta.
  - Gera dados fictícios de vendas ao clicar no botão "Gerar Insight".
  - Exibe um gráfico de vendas por produto.
  - Mostra o insight gerado com base nos dados.
- **Bibliotecas Utilizadas**:
  - **Streamlit** para interface e interação.
  - **Matplotlib** para geração de gráficos.

---

### Fluxo de Execução
1. **Configuração da Página**:
   - Define o título e layout da aplicação.
2. **Entrada do Usuário**:
   - O usuário insere uma pergunta em linguagem natural.
3. **Geração de Dados**:
   - Dados fictícios de vendas são gerados pela função `gerar_dados_vendas()`.
4. **Visualização**:
   - Um gráfico de vendas por produto é exibido.
5. **Geração de Insight**:
   - A função `gerar_insight()` analisa os dados e exibe o insight na interface.

---

### Dependências
Certifique-se de instalar as seguintes bibliotecas antes de executar o código:
```bash
pip install streamlit matplotlib pandas numpy
```

---

### Execução
Para executar a aplicação, utilize o comando:
```bash
streamlit run insightbot.py.py
```

---

### Observações
- Os dados gerados são aleatórios e não representam informações reais.
- A aplicação é configurada para exibir insights simples e gráficos básicos. Para expandir a funcionalidade, é possível integrar dados reais ou adicionar novas análises.