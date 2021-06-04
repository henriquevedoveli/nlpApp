import streamlit as st
# texblob
# pandas
import app1
import app2
import app3

emoji = 'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/google/274/scroll_1f4dc.png'

st.set_page_config(page_title='NLP APP', page_icon=emoji)

pages = {
    'Resumo de Textos' : app1,
    'Gerador de Poemas' : app2,
    'Sobre' : app3
}

st.sidebar.title('Navegação')
selection = st.sidebar.radio(' ', list(pages.keys()))
page = pages[selection]
page.app()
