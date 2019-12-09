"""
Visualization.py
"""
import altair as alt

def visualize(emotion_array):
    '''Visualize the sentiment analysis using altair
       Parameters: DataFrame: emotion_array, the dataframe about emotions of each critic
       Returns: BarChart: a mutiple barchart to show the emtions of each critic'''
    alt.renderers.enable('notebook')
    emotions = ['positive', 'negative', 'anger', 'anticipation', 'disgust',
                'fear', 'joy', 'sadness', 'surprise', 'trust']
    input_dropdown = alt.binding_select(options=emotions)
    selection = alt.selection_single(fields=['EMOTION'], bind=input_dropdown, name='Type of')
    color = alt.condition(selection,
                          alt.Color('EMOTION:N', legend=None),
                          alt.value('lightgray'))
    chart_final = alt.Chart(emotion_array).mark_bar().encode(
        x='PERCENT:Q',
        y=alt.Y(
            'EMOTION:N',
            sort=alt.EncodingSortField(field='PERCENT', op='count', order='ascending')
            ),
        facet='name:N',
        color=color,
        tooltip='PERCENT:Q',
        ).properties(
            width=150,
            height=150,
            title='Sentiment for Top 5 Critics',
            columns=5,
        ).add_selection(
            selection)
    chart_final.save('finalchart.html')
    return chart_final
