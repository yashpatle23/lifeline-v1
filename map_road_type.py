import folium

def map_road_type(df):
    # Create a Folium map
    m = folium.Map(location=[15.05, 76.8], zoom_start=8, tiles='CartoDB Dark_Matter', attr='Map')

    # Define a colormap based on severity
    severity_colormap = {
        'Fatal': 'red',
        'Grievous Injury': 'yellow',
        'Simple Injury': 'orange',
        'Damage Only': 'green'
    }

    # Create LayerGroups for different road types
    road_type_layers = {road_type: folium.FeatureGroup(name=road_type) for road_type in df['Road_Type'].unique()}

    # Default LayerGroup for unrecognized road types
    default_layer_group = folium.FeatureGroup(name='Others')

    # Iterate over the data and add CircleMarkers to the corresponding LayerGroup
    for index, row in df.iterrows():
        road_type = row['Road_Type']
        severity = row['Severity']
        latitude = row['Latitude']
        longitude = row['Longitude']
        popup_content = f"Latitude: {latitude}, Longitude: {longitude}, Severity: {severity}"  # Popup content with severity
        color = severity_colormap.get(severity, 'gray')  # Default to gray for unknown severity
        circle_marker = folium.CircleMarker(
            location=[latitude, longitude],
            radius=2,  # Adjust the radius of the circle markers
            color=color,
            fill=True,
            fill_opacity=0.8,
            tooltip=popup_content  # Set tooltip to display popup content
        )
        # Add the circle marker to the corresponding LayerGroup or default LayerGroup
        layer_group = road_type_layers.get(road_type)
        if layer_group:
            layer_group.add_child(circle_marker)
        else:
            default_layer_group.add_child(circle_marker)

    # Add each LayerGroup to the map
    for layer_group in road_type_layers.values():
        layer_group.add_to(m)

    # Add default LayerGroup to the map
    default_layer_group.add_to(m)

    # Add LayerControl to toggle visibility of different road types
    folium.LayerControl(collapsed=False).add_to(m)

    return m
