import streamlit as st

def app():
    st.title('Sobre')

    st.subheader('*Resumo de Textos & Tradutor*')
    st.write('''Para resumir os textos foi construido um algoritmo [sumarizador.py](/sumarizador.py), que utiliza
    a biblioteca _nltk_, onde ocorre o resumo dos textos, para isso é retiradas as stopwords e as pontuações, tanto para
    inglês quanto para português, e são encontradas as palavras mais importantes, uma palavra é considerada importante
    com base na frequência que ela aparece no texto, a partir dessas palavras importantes é que o resumo é construído.
    ''')

    st.write('''Para a tradução do texto foi utilizado a biblioteca _TextBlob_, que realiza a tradução automaticamente.
    ''')

    st.subheader('*Gerador de Poemas Aleatório*')

    st.write('''Para gerar os poemas foi realizado o download de vários poemas em português, que podem ser acessados
    no seguinte link, [Poems in Portuguese](https://www.kaggle.com/oliveirasp6/poems-in-portuguese), após o carregamento
    dos dados foi realizado o balanceamento dos dados para que no modelo final não fosse enviesado, o modelo final foi 
    construído com base na probabilidade dos bigramas gerados pelos poemas.
    ''')

    st.subheader('*Contato*')
    col1, col2 = st.beta_columns(2)

    col1.markdown('''
        * Email: [henriquevedoveli@gmail.com](mailto:henriquevedoveli@gmail.com) 

        * Linkedin: [https://www.linkedin.com/in/henrique-vedoveli/](https://www.linkedin.com/in/henrique-vedoveli/)

        ''', unsafe_allow_html=False)

    col2.write(
        '''
        * Site: [https://sites.google.com/view/henriquevedoveli](https://sites.google.com/view/henriquevedoveli/home)

        * Github: [https://github.com/henriquevedoveli](https://github.com/henriquevedoveli)
        '''
    )