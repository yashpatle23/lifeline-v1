import plotly.graph_objs as go

def donut_chart(df):
    # Filter the DataFrame for road type 'NH'
    nh_data = df[df['Road_Type'] == 'NH']

    # Group the filtered DataFrame by 'Severity' and calculate the count of each severity
    severity_counts = nh_data['Severity'].value_counts().reset_index(name='Count')

    # Define colors for each severity
    severity_colors = {
        'Fatal': 'red',
        'Grievous Injury': 'yellow',
        'Simple Injury': 'orange',
        'Damage Only': 'green',
        'Not Applicable': 'gray',
    }

    # Create the trace for the donut chart
    data = [
        go.Pie(
            labels=severity_counts['Severity'],
            values=severity_counts['Count'],
            marker=dict(colors=[severity_colors[severity] for severity in severity_counts['Severity']]),
            hoverinfo='label+value+percent',
            textinfo='label+value',
            textfont=dict(size=13),
            hole=0.7,
            rotation=45
        )
    ]

    # Create the layout for the donut chart
    layout = go.Layout(
        plot_bgcolor='#1f2c56',
        paper_bgcolor='#1f2c56',
         width=410,  # Set the width to 485 pixels
        height=370,
        margin=dict(t=38, r=0, b=5, l=0),
        hovermode='closest',
        title={
            'text': f"Severity Distribution for NH Road Type",
            'y': 0.96,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'color': 'white', 'size': 15}
        },
        legend={
            'orientation': 'h',
            'bgcolor': '#1f2c56',
            'xanchor': 'center', 'x': 0.5, 'y': -0.07
        },
        font=dict(family="sans-serif", size=12, color='white')
    )

    # Create the figure object
    fig = go.Figure(data=data, layout=layout)

    return fig
