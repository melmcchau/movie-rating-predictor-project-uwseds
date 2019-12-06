"""
Visualization.py
"""
import altair as alt

def visualize(EMOTION_ARRAY):
    '''Visualize the sentiment analysis using altair'''
    alt.renderers.enable('notebook')
    EMOTIONS = ['positive', 'negative', 'anger', 'anticipation', 'disgust',
                'fear', 'joy', 'sadness', 'surprise', 'trust']
    input_dropdown = alt.binding_select(options=EMOTIONS)
    selection = alt.selection_single(fields=['EMOTION'], bind=input_dropdown, name='Type of')
    color = alt.condition(selection,
                          alt.Color('EMOTION:N', legend=None),
                          alt.value('lightgray'))
    chart_final = alt.Chart(EMOTION_ARRAY).mark_bar().encode(
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
