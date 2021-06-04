import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import punkt
from nltk.corpus import stopwords
from nltk.probability import FreqDist


from string import punctuation
from heapq import nlargest

from collections import defaultdict


def sumarizador(texto, lang):

    sentencas = sent_tokenize(texto)
    palavras = word_tokenize(texto.lower())

    if lang == 'pt-br':
        sw = set(stopwords.words('portuguese') + list(punctuation))
    elif lang == 'en':
        sw = set(stopwords.words('english') + list(punctuation))
    palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in sw]

    frequencia = FreqDist(palavras_sem_stopwords)

    sentencas_importantes = defaultdict(int)

    for i, sentenca in enumerate(sentencas):
        for palavra in word_tokenize(sentenca.lower()):
            if palavra in frequencia:
                sentencas_importantes[i] += frequencia[palavra]

    idx_sentencas_importantes = nlargest(4, sentencas_importantes, sentencas_importantes.get)

    texto_resumido = []
    for i in idx_sentencas_importantes:
        texto_resumido.append(''.join(sentencas[i]))

    return texto_resumido
