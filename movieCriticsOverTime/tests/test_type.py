"""
Unit tests for checking the availability of data
"""
import numpy as np
import pandas as pd
import unittest
from os import path
from movieCriticsOverTime import clean_data

class TestTypes(unittest.TestCase):
    """
    Unit tests data type
    """
    def test_data_type(self):
        """
        Checking if the selected keywords are in the Dataset
        """
        movie_data = pd.read_csv(path.join("..", "..", "data", "movies.dat"), delimiter='\t')
        review_data = pd.read_csv(path.join("..", "..", "data", "reviews.csv"))
        movie = clean_data.clean_movies(movie_data)
        review = clean_data.clean_reviews(review_data)
        movies_reviews = clean_data.merge_movies_reviews(review,movie)
 
        self.assertTrue(movies_reviews['year'].dtype == np.int64)
        self.assertTrue(movies_reviews['rtAllCriticsNumReviews'].dtype == np.float64)
        self.assertTrue(movies_reviews['rtAudienceScore'].dtype == np.object)

if __name__ == '__main__':
    unittest.main()
