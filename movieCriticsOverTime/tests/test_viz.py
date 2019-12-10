"""
Unit tests for checking the availability of data
"""
# import sys
# sys.path.append("..")

import unittest
import pandas as pd
import altair
from os import path, remove
from .. import clean_data, overall_rating, sentiment_analysis

class TestViz(unittest.TestCase):
    """
    Unit tests for quotes
    """
    def test_viz_output_type(self):
        """
        Checking if the quotes have right structure
        """
        movie_data = pd.read_csv(path.join("..", "..", "data", "movies.dat"), delimiter='\t')
        #review_data = pd.read_csv(path.join("..", "..", "data", "reviews.csv"))
        movies = clean_data.clean_movies(movie_data)
        a = overall_rating.draw_trend_line_median_year(movies,2003,2010)

        self.assertTrue(type(a) == altair.vegalite.v3.api.Chart)
        if path.exists('overallchart.html'):
            remove('overallchart.html')

    def test_html_generated(self):
        movie_data = pd.read_csv(path.join("..", "..", "data", "movies.dat"), delimiter='\t')
        movies = clean_data.clean_movies(movie_data)
        overall_rating.draw_trend_line_median_year(movies,2003,2010)

        self.assertTrue(path.exists('overallchart.html'))
        remove('overallchart.html')
        self.assertFalse(path.exists('overallchart.html'))

if __name__ == '__main__':
    unittest.main()
