"""
Unit tests for checking the availability of data
"""
import unittest
import pandas as pd
from os import path
from .. import clean_data

class TestColumns(unittest.TestCase):
    """
    Unit tests data availability
    """
    def test_data_clean(self):
        """
        Checking if the selected keywords are in the Dataset
        """
        movie_data = pd.read_csv(path.join("..", "..", "data", "movies.dat"), delimiter='\t')
        review_data = pd.read_csv(path.join("..", "..", "data", "reviews.csv"))
        movie = clean_data.clean_movies(movie_data)
        review = clean_data.clean_reviews(review_data)
        expected_columns_movie = ('rtAllCriticsRating' and
                            'rtAllCriticsNumReviews' and
                            'rtAudienceRating' and
                            'title' and
                            'imdbID' and
                            'year' and
                            'rtID' and
                            'rtAudienceNumRatings' and
                            'rtAudienceScore')

        expected_columns_review = ('review_date' and
                             'critic' and
                            'fresh' and
                            'imdb' and
                            'publication' and
                            'quote' and
                            'review_date')

        test_columns_movie = movie.columns
        test_columns_review = review.columns
        self.assertTrue(expected_columns_movie in test_columns_movie)
        self.assertTrue(expected_columns_review in test_columns_review)

if __name__ == '__main__':
    unittest.main()
