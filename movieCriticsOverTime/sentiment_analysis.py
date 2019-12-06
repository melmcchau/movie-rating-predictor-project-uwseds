"""
SentimentAnalysis.py
"""

import pandas as pd
import re
import sentiment_setup
from sentiments_nrc import EMOTIONS

MOVIES = pd.read_csv("../data/movies.dat", delimiter='\t')
REVIEWS = pd.read_csv('../data/reviews.csv')

EMOTIONS = ['positive', 'negative', 'anger',
            'anticipation', 'disgust', 'fear',
            'joy', 'sadness', 'surprise', 'trust']

def grab_quotes(REVIEWS_MERGE, top_critics, interest_year):
    ''' Grab all quotes from specified year and put into one table to
        prep for sentiment analyisis'''
    quote = pd.DataFrame()
    for name in top_critics:
        critic_quote = REVIEWS_MERGE[['critic', 'quote', 'year']]
        sub_quote = critic_quote[(critic_quote['critic'] == name) &
                                 (critic_quote['year'] == interest_year)]
        quote = quote.append(sub_quote, ignore_index=True)
        quote = quote.groupby('critic')['quote'].apply(' '.join).reset_index()
    return quote

def analyze_quote(quote, top_critics):
    '''Send grabbed quotes/reviews for sentiment analysis'''
    res = pd.DataFrame()
    for name in top_critics:
        content = quote[quote['critic'] == name]['quote'].values[0]
        Split_String = re.split(r'\W+', content)
        lower_words = [word.lower() for word in Split_String]
        length_filtered = [word for word in lower_words if len(word) > 1]
        Total_Words = len(length_filtered)
        Words_List_for_Each_Emotion = sentiment_setup.words_list_for_each_emotion(length_filtered)
        result_list = []
        for i in EMOTIONS:
            result = {}
            example_words = [sentiment_setup.get_common_words_list(value)[:3]
                             for key, value in Words_List_for_Each_Emotion.items()
                             if key == i]
            result['EMOTION'] = i
            result['PERCENT'] = len(Words_List_for_Each_Emotion[i])/Total_Words
            result['EXAMPLE WORDS'] = example_words[0]
            result['name'] = name
            result_list.append(result)
            result = sorted(result_list, key=lambda k: k['PERCENT'], reverse=True)
            result = pd.DataFrame(result)
            res = res.append(result)

    return res
