import streamlit as st
from sumarizador import * 
from textblob import TextBlob

emojiText = 'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/google/274/scroll_1f4dc.png'

def app():
    col1, col2 = st.beta_columns([6,2])
    col1.title('*Resumos de Textos & Tradutor*')
    col2.image(emojiText, width = 80)

    lang = st.radio('Digite o idioma do texto:', ['Português', 'Inglês'])
    lang_translate = st.radio('Digite o idioma que você deseja ler o texto:', ['Português', 'Inglês'])
    text = st.text_area('Precione Ctrl+Enter para resumir')


    if lang == 'Português':
        if len(text) != 0:
            st.subheader('Texto Resumido')
            if lang_translate == 'Inglês':
                blob = TextBlob(''.join(sumarizador(text, 'pt-br')))
                texto_traduzido = str(blob.translate(to='en'))
                st.write(texto_traduzido)
            elif lang_translate == 'Português':
                st.write(''.join(sumarizador(text, 'pt-br')))

    elif lang == 'Inglês':
        if len(text) != 0:
            st.subheader('Texto Resumido')
            if lang_translate == 'Português':
                blob = TextBlob(''.join(sumarizador(text, 'en')))
                texto_traduzido = str(blob.translate(to='pt'))
                st.write(texto_traduzido)
            elif lang_translate == 'Inglês':
                st.write(''.join(sumarizador(text, 'en')))