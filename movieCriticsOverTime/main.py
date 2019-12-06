'''
MAIN DATA FRAME THAT RUNS ALL PYTHON MODULES
'''

import pandas as pd
import clean_data
import overall_rating
import sentiment_analysis
import visualization

#LOAD DATA
MOVIES = pd.read_csv("../data/movies.dat", delimiter='\t')
REVIEWS = pd.read_csv('../data/reviews.csv')

#OVERALL LOOK
print('Please insert the start year of a range of interest')
start_year = int(input())
print('Please insert the end year of a range of interest')
end_year = int(input())
SUB_MOVIES = clean_data.clean_movies(MOVIES)
overall_rating.draw_trend_line_median_year(SUB_MOVIES, start_year, end_year)

#CLEAN AND MERGE DATA
REVIEWS_CLEAN = clean_data.clean_reviews(REVIEWS)
REVIEWS_MERGE = clean_data.merge_movies_reviews(REVIEWS_CLEAN, SUB_MOVIES)

#TOP CRITICS IN YEAR OF INTEREST
print('Please input a year of interest to see critic activity that year: ')
interest_year = int(input())
top_critics = overall_rating.top5_critic_per_year(REVIEWS_MERGE, interest_year)
print('The top critics that year are:')
print(top_critics)

#GRAB CRITIC REVIEWS
QUOTES = sentiment_analysis.grab_quotes(REVIEWS_MERGE, top_critics, interest_year)

#ANALYZE QUOTES
EMOTION_ARRAY = sentiment_analysis.analyze_quote(QUOTES, top_critics)
visualization.visualize(EMOTION_ARRAY)
