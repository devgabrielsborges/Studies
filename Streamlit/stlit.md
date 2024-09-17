# Introdução ao Streamlit

O **Streamlit** é uma biblioteca Python que facilita a criação de aplicativos web interativos e dashboards com simplicidade e agilidade. A principal vantagem é permitir a criação de aplicações com poucas linhas de código, sem necessidade de conhecimentos avançados em desenvolvimento web.

## Principais Características

- **Fácil de usar:** Crie interfaces interativas com poucas linhas de código.
- **Atualizações automáticas:** O Streamlit atualiza a interface em tempo real enquanto você altera o código.
- **Integração com bibliotecas de visualização:** Funciona bem com bibliotecas populares como Matplotlib, Plotly e Altair.

---

# Instalando o Streamlit

Para instalar o Streamlit, você pode usar o `pip`:

```bash
pip install streamlit
```

Após a instalação, você pode rodar um aplicativo Streamlit com o comando:

```bash
streamlit run nome_do_seu_script.py
```

---

# Criando o Primeiro Aplicativo

Vamos criar um simples "Hello, World!" com Streamlit para ver como é fácil começar.

```python
import streamlit as st

st.title('Hello, Streamlit!')
st.write('Este é o meu primeiro app usando Streamlit.')
```

Salve o código em um arquivo Python (ex: `app.py`) e rode com o comando:

```bash
streamlit run app.py
```

Isso vai abrir o aplicativo em seu navegador.

---

# Elementos Interativos

O Streamlit permite que você adicione elementos interativos, como botões, sliders, caixas de seleção e muito mais, de forma muito simples. Aqui estão alguns exemplos:

## Botões

```python
if st.button('Clique aqui'):
    st.write('Você clicou no botão!')
```

## Slider

```python
idade = st.slider('Selecione sua idade', 0, 100, 25)
st.write(f'Sua idade é: {idade}')
```

## Input de texto

```python
nome = st.text_input('Digite seu nome')
st.write(f'Olá, {nome}!')
```

---

# Criando Dashboards Interativos

Um dos maiores atrativos do Streamlit é a possibilidade de criar dashboards interativos de forma simples. Vamos criar um exemplo de dashboard básico para visualização de dados usando **Pandas** e **Matplotlib**.

## Exemplo: Dashboard de Visualização de Dados

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Dados de exemplo
dados = {
    'Ano': [2020, 2021, 2022],
    'Vendas': [100, 150, 200]
}
df = pd.DataFrame(dados)

st.title('Dashboard de Vendas')

# Mostrar tabela de dados
st.write('Dados de Vendas:')
st.dataframe(df)

# Gráfico de linhas
st.write('Gráfico de Vendas por Ano:')
fig, ax = plt.subplots()
ax.plot(df['Ano'], df['Vendas'], marker='o')
st.pyplot(fig)
```

Este exemplo mostra como você pode carregar e visualizar dados, além de gerar gráficos diretamente no aplicativo.

---

# Templates Úteis

Aqui estão alguns templates básicos para funcionalidades que você pode usar em diversos tipos de aplicações:

## Upload de Arquivos

```python
uploaded_file = st.file_uploader("Escolha um arquivo")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)
```

## Exibição de Gráficos Interativos com Plotly

```python
import plotly.express as px

df = px.data.iris()  # Dados de exemplo
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
st.plotly_chart(fig)
```

---

Para mais informações, consulte a [documentação oficial do Streamlit](https://docs.streamlit.io).

---