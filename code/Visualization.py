"""
Visualization.py
"""
def visualize(EMOTION_ARRAY):
    import altair as alt
    alt.renderers.enable('notebook')

    #input_dropdown = alt.binding_select(options= top_critics)
    #selection = alt.selection_single(fields=['name'], bind=input_dropdown, name='Critic of ')
    #color = alt.condition(selection,
                        #alt.Color('critic:N', legend=None),
                        #alt.value('lightgray'))
    chart_final = alt.Chart(EMOTION_ARRAY).mark_bar().encode(
         x='PERCENT:Q',
         y=alt.Y(
            'EMOTION:N',
            sort=alt.EncodingSortField(field='PERCENT', op='count', order='ascending')
            ),
        facet='name:N',
        color='EMOTION:N',
        tooltip='PERCENT:Q',
        ).properties(
        width=150,
        height=150,
        title = 'Sentiment for Top 5 Critics',
        columns=5,
        )
    chart_final.save('finalchart.html')

