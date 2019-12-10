"""
Unit tests for checking the availability of data
"""
# import sys
# sys.path.append("..")

import unittest
import pandas as pd
from os import path
from .. import clean_data, overall_rating, sentiment_analysis

class TestViz(unittest.TestCase):
    """
    Unit tests for quotes
    """
    def test_critic(self):
        """
        Checking if the quotes have right structure
        """
        movie_data = pd.read_csv(path.join("..", "..", "data", "movies.dat"), delimiter='\t')
        review_data = pd.read_csv(path.join("..", "..", "data", "reviews.csv"))
        movie = clean_data.clean_movies(movie_data)
        review = clean_data.clean_reviews(review_data)
        movies_reviews = clean_data.merge_movies_reviews(review,movie)
        top_critics = overall_rating.top5_critic_per_year(movies_reviews, 2000)

        self.assertTrue(type(top_critics) == list)
        
if __name__ == '__main__':
    unittest.main()
