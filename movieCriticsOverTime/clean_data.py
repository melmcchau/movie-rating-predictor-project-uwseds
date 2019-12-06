"""
CleanData.py
"""

import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def clean_reviews(REVIEWS):
    '''pre data cleaning for reviews data'''
    REVIEWS = REVIEWS[~REVIEWS.quote.isnull()]
    REVIEWS = REVIEWS[REVIEWS.fresh != 'none']
    REVIEWS = REVIEWS[REVIEWS.quote.str.len() > 0]
    REVIEWS['review_date'] = pd.to_datetime(REVIEWS['review_date']).dt.date
    REVIEWS_CLEAN = REVIEWS.drop(['link'], axis=1)
    return REVIEWS_CLEAN

def clean_movies(MOVIES):
    '''pre data cleaning for movies data'''
    MOVIES = MOVIES.drop(['imdbPictureURL', 'spanishTitle', 'rtPictureURL'], axis=1)

    MOVIES['rtAllCriticsRating'] = MOVIES['rtAllCriticsRating'].apply(pd.to_numeric, errors='coerce')
    MOVIES['rtAllCriticsNumReviews'] = MOVIES['rtAllCriticsNumReviews'].apply(pd.to_numeric, errors='coerce')
    MOVIES.dropna()
    SUB_MOVIES = MOVIES[['title', 'imdbID', 'year', 'rtID', 'rtAllCriticsRating', 'rtAllCriticsNumReviews', 'rtAudienceNumRatings', 'rtAudienceScore']]
    return SUB_MOVIES

def merge_movies_reviews(REVIEWS_CLEAN, SUB_MOVIES):
    '''merge movie and critic data'''
    REVIEWS_MERGE = REVIEWS_CLEAN.merge(SUB_MOVIES, left_on='imdb',
                                        right_on='imdbID', how='left',
                                        suffixes=('_review', '_movie'))
    return REVIEWS_MERGE
