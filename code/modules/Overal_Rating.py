#### interactive one: draw the trendline of the median rating given a time interval 
import pandas as pd
import altair as alt
from vega_datasets import data


def draw_trend_line_median_year(sub_movies):
    
    print('Please input the year range that you are interested in: ')
    

    start_year = int(input())
    end_year = int(input())
    
    year_median = sub_movies.groupby('year')['rtAllCriticsRating'].median().reset_index()
    year_show = year_median[year_median['year'] >= start_year]
    year_show = year_show[year_median['year'] <= end_year]
    
    
    selection = alt.selection_interval(bind='scales')

    chart = alt.Chart(year_show).mark_line().encode(
    x='year:N',
    y='rtAllCriticsRating:Q',
    tooltip='year:N').add_selection(selection)
   
    return chart
    