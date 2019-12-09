"""
Unit tests for checking the availability of data
"""

import unittest
import pandas as pd

import clean_data 
import overall_rating
import sentiment_analysis


class TestSentiment(unittest.TestCase):
    """
    Unit tests for quotes
    """
    def test_quote(self):
        """
        Checking if the quotes have right structure
        """
        movie_data = pd.read_csv("./data/movies.dat", delimiter='\t')
        review_data = pd.read_csv('./data/reviews.csv')
        movie = clean_data.clean_movies(movie_data)
        review = clean_data.clean_reviews(review_data)
        movies_reviews = clean_data.merge_movies_reviews(review,movie)
        top_critics = overall_rating.top5_critic_per_year(movies_reviews, 2000)
        quote = sentiment_analysis.grab_quotes(movies_reviews, top_critics, 2000)
 
        self.assertEqual(len(quote.columns),2)


if __name__ == '__main__':
    unittest.main()
