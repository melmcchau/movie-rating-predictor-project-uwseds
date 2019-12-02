import pandas as pd
import CleanData
import OverallRating
import SentimentAnalysis
import Visualization


'''LOAD DATA'''
MOVIES = pd.read_csv("../data/movies.dat", delimiter='\t')
REVIEWS = pd.read_csv('../data/reviews.csv')

'''OVERALL LOOK'''
start_year = 1990
end_year = 2013
SUB_MOVIES = CleanData.clean_movies(MOVIES)
OverallRating.draw_trend_line_median_year(SUB_MOVIES,start_year,end_year)

'''CLEAN AND MERGE DATA'''
REVIEWS_CLEAN = CleanData.clean_reviews(REVIEWS)
REVIEWS_MERGE = CleanData.merge_movies_reviews(REVIEWS_CLEAN,SUB_MOVIES)

'''TOP CRITICS IN YEAR OF INTEREST'''
print('Please input a year of interest to see critic activity that year: ')
interest_year = int(input())
top_critics = OverallRating.top5_critic_per_year(REVIEWS_MERGE,interest_year)
print(top_critics)

'''GRAB CRITIC REVIEWS'''
QUOTES = SentimentAnalysis.grab_quotes(REVIEWS_MERGE,top_critics,interest_year)
print(QUOTES)

'''ANALYZE QUOTES'''
EMOTION_ARRAY = SentimentAnalysis.analyze_quote(QUOTES,top_critics)
Visualization.visualize(EMOTION_ARRAY)
