"""
CleanData.py
"""
import warnings
import pandas as pd
warnings.filterwarnings('ignore')

def clean_reviews(reviews):
    '''  
    @param: reviews (DataFrame): raw reviews data;
    @return: a DataFrame that include cleaned data.
    '''
    reviews = reviews[~reviews.quote.isnull()]
    reviews = reviews[reviews.fresh != 'none']
    reviews = reviews[reviews.quote.str.len() > 0]
    reviews['review_date'] = pd.to_datetime(reviews['review_date']).dt.date
    reviews_clean = reviews.drop(['link'], axis=1)
    return reviews_clean

def clean_movies(movies):
    '''  
    @param: movies (DataFrame): raw movies data;
    @return: a DataFrame that include cleaned data.
    '''
    movies = movies.drop(['imdbPictureURL', 'spanishTitle', 'rtPictureURL'], axis=1)
    movies['rtAllCriticsRating'] = movies['rtAllCriticsRating'].apply(pd.to_numeric, errors='coerce')
    movies['rtAllCriticsNumReviews'] = movies['rtAllCriticsNumReviews'].apply(pd.to_numeric, errors='coerce')
    movies.dropna()
    sub_movies = movies[['title', 'imdbID', 'year', 'rtID', 
                         'rtAllCriticsRating', 'rtAllCriticsNumReviews', 
                         'rtAudienceNumRatings', 'rtAudienceScore']]
    return sub_movies

def merge_movies_reviews(reviews_clean, sub_movies):
    '''
    @param: reviews_clean(DataFrame); data;sub_movies(DataFrame)
    @return: a DataFrame that include cleaned data.
    '''
    reviews_merge = reviews_clean.merge(sub_movies, left_on='imdb',
                                        right_on='imdbID', how='left',
                                        suffixes=('_review', '_movie'))
    return reviews_merge
