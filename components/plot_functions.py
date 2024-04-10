import plotly.graph_objs as go

def bar_graph(df):
    # Filter the DataFrame for 'NH' road type
    nh_data = df[df['Road_Type'] == 'NH']
    # Group the filtered DataFrame by 'Severity' and calculate the count of each severity
    severity_counts = nh_data['Severity'].value_counts().reset_index(name='Count')
    # Define colors based on severity
    # Modify severity_colors dictionary
    severity_colors = {
    'Fatal': 'red',
    'Grievous Injury': 'yellow',
    'Simple Injury': 'orange',
    'Damage Only': 'green',
    'Not Applicable': 'gray'  # Add a default color for 'Not Applicable' severity
    }


    # Create the trace for the bar graph
    data = [
        go.Bar(
            x=severity_counts['Severity'],
            y=severity_counts['Count'],
            text=severity_counts['Count'],  # Add text to show count on hover
            textposition='auto',  # Automatically position the count text
            marker=dict(
                color=[severity_colors[severity] for severity in severity_counts['Severity']]  # Assign colors based on severity
            )
        )
    ]

    # Create the layout for the bar graph
    layout = go.Layout(
        plot_bgcolor='#1f2c56',
        paper_bgcolor='#1f2c56',
        title={
            'text': 'Severity Count for NH Road Type',
            'y': 0.94,
            'x': 0.5,
            'xanchor': 'auto',
            'yanchor': 'top',
            'font': {'color': 'white', 'size': 15}
        },
        hovermode='x',
        width=515,  # Set the width to 485 pixels
        height=210,
        margin=dict(t=38, r=5, b=5, l=5), 
        xaxis=dict(
            title='<b>Severity</b>',
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
            title='<b>Road Type</b>',
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

    # Adjust the width and height of the graph


    return fig