'''
MAIN DATA FRAME THAT RUNS ALL PYTHON MODULES
'''

import pandas as pd
import clean_data
import overall_rating
import sentiment_analysis
import visualization

#LOAD DATA
MOVIE_DATA_PATH = "../data/movies.dat"
REVIEW_DATA_PATH = '../data/reviews.csv'
movies = pd.read_csv(MOVIE_DATA_PATH, delimiter='\t')
reviews = pd.read_csv(REVIEW_DATA_PATH)

#OVERALL LOOK
print('Please insert the start year of a range of interest')
start_year = int(input())
print('Please insert the end year of a range of interest')
end_year = int(input())
sub_movies = clean_data.clean_movies(movies)
overall_rating.draw_trend_line_median_year(sub_movies, start_year, end_year)

#CLEAN AND MERGE DATA
reviews_clean = clean_data.clean_reviews(reviews)
reviews_merge = clean_data.merge_movies_reviews(reviews_clean,sub_movies)

#TOP CRITICS IN YEAR OF INTEREST
print('Please input a year of interest to see critic activity that year: ')
interest_year = int(input())
top_critics = overall_rating.top5_critic_per_year(reviews_merge, interest_year)
print('The top critics that year are:')
print(top_critics)

#GRAB CRITIC REVIEWS
quotes = sentiment_analysis.grab_quotes(reviews_merge, top_critics, interest_year)

#ANALYZE QUOTES
emotion_array = sentiment_analysis.analyze_quote(quotes, top_critics)
visualization.visualize(emotion_array)
