import pandas as pd
import folium
from folium.plugins import MarkerCluster
import json

def create_cluster_map(df):
    # Create a Folium Map centered at the mean latitude and longitude of the DataFrame
    m = folium.Map(location=[15.05, 76.8], zoom_start=7)

    # Create a MarkerCluster object
    marker_cluster = MarkerCluster().add_to(m)

    # Iterate through each row in the DataFrame and add markers with popups
    for index, row in df.iterrows():
        # Extract Severity, Latitude, and Longitude from the row
        severity = row['Severity']
        latitude = row['Latitude']
        longitude = row['Longitude']

        popup_text = f"Severity: {severity}"

        # Add marker with popup to MarkerCluster
        folium.Marker(location=[latitude, longitude], popup=popup_text).add_to(marker_cluster)

    # Add District Borders
        districts_geojson = 'District_Map.geojson'
    # Load the GeoJSON data
    with open(districts_geojson) as f:
        data = json.load(f)

    # Extract the features (districts)
    features = data['features']

    # Loop through each district and create a separate layer
    for feature in features:
        district_name = feature['properties']['name']
        district_geometry = feature['geometry']

        # Create a new Folium GeoJson layer for the current district
        district_layer = folium.GeoJson(district_geometry, name=district_name)

        # Add the district layer to the map
        m.add_child(district_layer)

    # Add LayerControl to toggle visibility of different layers
    folium.LayerControl().add_to(m)

    return m

# Example usage:
# cluster_map = create_cluster_map(df, '/content/drive/MyDrive/Colab Notebooks/coordinate/District_Map.geojson')
# cluster_map.save('/content/drive/MyDrive/Colab Notebooks/ClusterMap-Severity.html')
