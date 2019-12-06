import nltk
from wordcloud import WordCloud
from nltk.corpus import stopwords
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def vis_word_cloud(QUOTES):

    stop_words = stopwords.words("english")
    for i in range(len(QUOTES)):
        string = ''.join(QUOTES['quote'][i])
    wordcloud = WordCloud(width=500, height=500,

    stopwords=stop_words, 
    min_font_size=10).generate(string)
        
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud, interpolation='catrom')
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.show()


