"""
OverallRating.py
"""
import altair as alt

def draw_trend_line_median_year(sub_movies, start_year, end_year):
    """
    @param: sub_movies: (DataFrame),start_year: (Integer),end_year: (Integer)  
    @return: a trendline showing the rating tredn over years 
    """
    year_median = sub_movies.groupby('year')['rtAllCriticsRating'].median().reset_index()
    year_show = year_median[year_median['year'] >= start_year]
    year_show = year_show[year_median['year'] <= end_year]
    selection = alt.selection_interval(bind='scales')
    chart_overall = alt.Chart(year_show).mark_line().encode(
        alt.Y('rtAllCriticsRating:Q',
              scale=alt.Scale(domain=(0, 10))
             ),
        x='year:N',
        tooltip=['rtAllCriticsRating:Q', 'year']).add_selection(selection).properties(
            width=500,
            height=200
        )

    chart_overall.save("overallchart.html")
    return chart_overall

def top5_critic_per_year(reviews_merge, interest_year):
    """
    @param: reviews_merge (DataFrame): the merged datasets of reviews and movies;
            interested_year (Integer): the year that users are interested in.
    @return: a DataFrame that shows the top 5 critics.
    """
    group_aggregation = reviews_merge[['critic', 'publication',
                                       'year',
                                       'quote']].groupby(['critic',
                                                          'year']).agg({'quote':
                                                                        ['count']}).reset_index()
    group_aggregation = group_aggregation[(group_aggregation['year'] == interest_year)]
    top_five = group_aggregation.sort_values(by=[('quote', 'count')],
                                             ascending=False)[:5].reset_index(drop=True)
    top_critics = list(top_five['critic'])
    return top_critics
