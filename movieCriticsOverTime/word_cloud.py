'''
This module sets up and runs the process to create the word cloud visualization
'''
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def vis_word_cloud(QUOTES):
    '''create word cloud visualization'''
    stop_words = stopwords.words("english")
    for i in range(len(QUOTES)):
        string = ''.join(QUOTES['quote'][i])
    wordcloud = WordCloud(width=500,
                          height=500,
                          stopwords=stop_words,
                          min_font_size=10).generate(string)
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud, interpolation='catrom')
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.show()
