import plotly.graph_objs as go

def line_graph(df):
    # Group the DataFrame by year and calculate the sum of latitude for each year
    year_latitude_sum = df.groupby('Year')['Latitude'].sum().reset_index(name='SumLatitude')

    # Create the trace for the line graph
    data = [
        go.Scatter(
            x=year_latitude_sum['Year'],
            y=year_latitude_sum['SumLatitude'],
            mode='lines+markers',  # Show both lines and markers
            name='Sum of Latitude',
            text=year_latitude_sum['SumLatitude'],  # Add text to show sum on hover
            hoverinfo='text',  # Show hover text
            marker=dict(color='blue'),  # Marker color
            line=dict(width=2, color='blue')  # Line color and width
        )
    ]

    # Create the layout for the line graph
    layout = go.Layout(
        plot_bgcolor='#1f2c56',
        paper_bgcolor='#1f2c56',
        title={
            'text': 'Sum of Latitude by Year',
            'y': 0.93,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'bottom',
            'font': {'color': 'white', 'size': 15}
        },
        hovermode='x',
        width=505,  # Set the width to 485 pixels
        height=210,
       margin=dict(t=38, r=5, b=5, l=5), 
        xaxis=dict(
            title='<b>Year</b>',
            color='white',
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor='white',
            linewidth=2,
            ticks='outside',
            tickfont=dict(family='Arial', size=12, color='white')
        ),
        yaxis=dict(
            title='<b>Sum of Latitude</b>',
            color='white',
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor='white',
            linewidth=2,
            ticks='outside',
            tickfont=dict(family='Arial', size=12, color='white')
        )
    )

    # Create the figure object
    fig = go.Figure(data=data, layout=layout)

    return fig
