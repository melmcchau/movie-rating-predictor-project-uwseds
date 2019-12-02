"""
OverallRating.py
"""
import pandas as pd
import altair as alt
from vega_datasets import data
import matplotlib.pyplot as plt
import mpld3
import webbrowser


def draw_trend_line_median_year(SUB_MOVIES,start_year,end_year):
    """
    Descripion:
    @param:
    @return:
    """
    
    year_median = SUB_MOVIES.groupby('year')['rtAllCriticsRating'].median().reset_index()
    year_show = year_median[year_median['year'] >= start_year]
    year_show = year_show[year_median['year'] <= end_year]

    selection = alt.selection_interval(bind='scales')

    chart_overall = alt.Chart(year_show).mark_line().encode(
    alt.Y('rtAllCriticsRating:Q',
        scale=alt.Scale(domain=(0, 10))
    ),
    x='year:N',
    tooltip=['rtAllCriticsRating:Q','year']).add_selection(selection).properties(
    width=500,
    height=200
    )
    
    chart_overall.save("overallchart.html")
    return chart_overall
    

def top5_critic_per_year(REVIEWS_MERGE,interest_year):
    """
    Descripion:
    @param:
    @return:
    """
    Group_Aggregation = REVIEWS_MERGE[['critic', 'publication', 
                       'year', 'quote']].groupby(['critic','year']).agg({ 
                         'quote': ['count']}).reset_index()
    
    Group_Aggregation = Group_Aggregation[(Group_Aggregation['year'] == interest_year)]
    Top_five = Group_Aggregation.sort_values(by=[('quote','count')], 
                                            ascending = False)[:5].reset_index(drop =True)

    top_critics = list(Top_five['critic'])
    
    
    
    return top_critics
    return REVIEWS_MERGE
