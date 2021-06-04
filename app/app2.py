import streamlit as st
import pandas as pd
import random
import pickle
import zipfile

emojiHand = 'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/google/274/writing-hand_medium-dark-skin-tone_270d-1f3fe_1f3fe.png'
emojiText = 'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/google/274/scroll_1f4dc.png'


with zipfile.ZipFile("./model_df.zip","r") as zip_ref:
    zip_ref.extractall("nlpApp/app/")

@st.cache
def loadModel(path):
    with open(path, 'rb') as f:
        model = pickle.load(f)
    return model

def app():
    col1, col2 = st.beta_columns([6,2])
    col1.title('*Gerador de Poemas Aleatório*')
    col2.image(emojiText, width = 80)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.write('''Para gerar o poema basta clicar em _"Gerar Poema"_, pode demorar alguns minutos
    para gerar seu poema, e também seu poema pode não ter muito sentido, mas basta gerar outro.    
    ''')

    st.write('''Para saber como funciona ou entrar em contato ir na aba _Sobre_.
    ''')

    col1, col2, col3 = st.beta_columns([ 3 , 2 ,3 ])
    if col2.button('Gerar Poema'):

        st.write('Isso pode demorar um pouco... Estamos escrevendo seu poema...')
        st.image(emojiHand, width=25)

        model_df = loadModel('model_df.pkl')

        num_sents = 2
        current_bigram = ('<s>', '<s>')
        i = 0
        poema = []
        while i < num_sents:
            df = model_df.loc[model_df['bigram'] == current_bigram]
            words = df['lastword'].values
            probs = df['prob'].values
            last_word = random.choices(words, probs)[0]

            current_bigram = (current_bigram[1], last_word)

            if last_word == '</s>':
                i += 1
                st.image(emojiHand, width=25)

            if last_word != '<s>' and last_word != '</s>':
                poema.append(last_word)
        poemaFinal = ' '.join(poema)
        st.write(poemaFinal)




