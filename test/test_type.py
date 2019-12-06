"""
Unit tests for checking the availability of data
"""

import unittest
import pandas as pd
import numpy as np
import CleanData

class TestTypes(unittest.TestCase):
    """
    Unit tests data type
    """
    def test_data_type(self):
        """
        Checking if the selected keywords are in the Dataset
        """
        movie_data = pd.read_csv("../data/movies.dat", delimiter='\t')
        review_data = pd.read_csv('../data/reviews.csv')
        movie = CleanData.clean_movies(movie_data)
        review = CleanData.clean_reviews(review_data)
        movies_reviews = CleanData.merge_movies_reviews(review,movie)
 
        self.assertTrue(movies_reviews['year'].dtype == np.int64)
        self.assertTrue(movies_reviews['rtAllCriticsRating'].dtype == np.float64)
        self.assertTrue(movies_reviews['rtAllCriticsNumReviews'].dtype == np.float64)
        self.assertTrue(movies_reviews['rtAudienceNumRatings'].dtype == np.float64)
        self.assertTrue(movies_reviews['rtAudienceScore'].dtype == np.float64)

if __name__ == '__main__':
    unittest.main()
