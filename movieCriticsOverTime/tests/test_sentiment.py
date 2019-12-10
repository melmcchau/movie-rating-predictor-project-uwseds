"""
Unit tests for checking the availability of data
"""
# import sys
# sys.path.append("..")

import unittest
import pandas as pd
from os import path
from .. import clean_data, overall_rating, sentiment_analysis

class TestSentiment(unittest.TestCase):
    """
    Unit tests for quotes
    """
    def test_quote(self):
        """
        Checking if the quotes have right structure
        """
        movie_data = pd.read_csv(path.join("..", "..", "data", "movies.dat"), delimiter='\t')
        review_data = pd.read_csv(path.join("..", "..", "data", "reviews.csv"))
        movie = clean_data.clean_movies(movie_data)
        review = clean_data.clean_reviews(review_data)
        movies_reviews = clean_data.merge_movies_reviews(review,movie)
        top_critics = overall_rating.top5_critic_per_year(movies_reviews, 2000)
        quote = sentiment_analysis.grab_quotes(movies_reviews, top_critics, 2000)
 
        self.assertEqual(len(quote.columns),2)


if __name__ == '__main__':
    unittest.main()
