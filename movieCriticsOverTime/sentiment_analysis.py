"""
SentimentAnalysis.py
"""
import re
import pandas as pd
from . import sentiment_setup
from .sentiments_nrc import EMOTIONS

def grab_quotes(reviews_merge, top_critics, interest_year):
    ''' Grab all quotes from specified year and put into one table to
        prep for sentiment analyisis
        Parameters: reviews_merge (DataFrame): a merged dataframe with reviews and movies 
                    top_critics(list): a list of top critics
                    interest_year(integer): the year that users are interesed in
        Returns: DataFrame: the combined quotes for each critic'''
    quote = pd.DataFrame()
    for name in top_critics:
        critic_quote = reviews_merge[['critic', 'quote', 'year']]
        sub_quote = critic_quote[(critic_quote['critic'] == name) &
                                 (critic_quote['year'] == interest_year)]
        quote = quote.append(sub_quote, ignore_index=True)
        quote = quote.groupby('critic')['quote'].apply(' '.join).reset_index()
    return quote

def analyze_quote(quote, top_critics):
    ''' Send grabbed quotes/reviews for sentiment analysis
        Parameters: quote(DataFrame): a DataFrame that includes critics and their combine quotes 
                    top_critics(list): a list of top critics
        Returns: DataFrame: sentiment analysis table for each critic'''
    res = pd.DataFrame()
    for name in top_critics:
        content = quote[quote['critic'] == name]['quote'].values[0]
        split_string = re.split(r'\W+', content)
        lower_words = [word.lower() for word in split_string]
        length_filtered = [word for word in lower_words if len(word) > 1]
        total_words = len(length_filtered)
        words_list_for_each_emotion = sentiment_setup.words_list_for_each_emotion(length_filtered)
        result_list = []
        for i in EMOTIONS:
            result = {}
            example_words = [sentiment_setup.get_common_words_list(value)[:3]
                             for key, value in words_list_for_each_emotion.items()
                             if key == i]
            result['EMOTION'] = i
            result['PERCENT'] = len(words_list_for_each_emotion[i])/ total_words
            result['EXAMPLE WORDS'] = example_words[0]
            result['name'] = name
            result_list.append(result)
            result = sorted(result_list, key=lambda k: k['PERCENT'], reverse=True)
            result = pd.DataFrame(result)
            res = res.append(result)

    return res
