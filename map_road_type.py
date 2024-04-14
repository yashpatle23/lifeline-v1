import plotly.graph_objs as go

def map_road_type(df):
    # Calculate the mean latitude and longitude of the selected district
    mean_latitude = df['Latitude'].mean()
    mean_longitude = df['Longitude'].mean()

    # Define the access token for Mapbox
    mapbox_access_token = 'pk.eyJ1IjoicXM2MjcyNTI3IiwiYSI6ImNraGRuYTF1azAxZmIycWs0cDB1NmY1ZjYifQ.I1VJ3KjeM-S613FLv3mtkw'

    # Define a colormap based on severity
    severity_colormap = {
        'Fatal': 'red',
        'Grievous Injury': 'yellow',
        'Simple Injury': 'orange',
        'Damage Only': 'green'
    }

    # Create data for Scattermapbox trace
    trace = go.Scattermapbox(
        lat=df['Latitude'],
        lon=df['Longitude'],
        mode='markers',
        marker=dict(
            size=5,  # Adjust the size of the markers
            color=[severity_colormap.get(severity, 'gray') for severity in df['Severity']],  # Set marker color based on severity
            opacity=0.8
        ),
        text=[f"Latitude: {lat}, Longitude: {lon}, Severity: {severity}" for lat, lon, severity in zip(df['Latitude'], df['Longitude'], df['Severity'])],  # Define text for hover tooltip
    )

    # Define layout for the scatter plot
    layout = go.Layout(
        mapbox=dict(
            accesstoken=mapbox_access_token,
            center=dict(lat=mean_latitude, lon=mean_longitude),  # Set center location based on mean latitude and longitude
            zoom=8,  # Set initial zoom level
            style='dark'  # Set Mapbox style
        ),
        margin=dict(r=0, l=0, t=0, b=0),  # Set margin to remove unnecessary padding
    )

    # Create the figure
    fig = go.Figure(data=[trace], layout=layout)

    return fig
