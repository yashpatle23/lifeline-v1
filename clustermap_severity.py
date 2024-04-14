import geopandas as gpd
import folium
from folium.plugins import MarkerCluster
def create_cluster_map(district_name, df):
  # Load GeoJSON file with district borders of Karnataka
  geojson_file_path = 'District_Map.geojson'
  districts = gpd.read_file(geojson_file_path)

  # Create a map centered at Karnataka
  map_karnataka = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=7)

  # Create a MarkerCluster layer
  marker_cluster = MarkerCluster().add_to(map_karnataka)

  # Find district polygon based on district name
  district_polygon = districts[districts['name'] == district_name]

  # Check if the district polygon exists
  if not district_polygon.empty:
    # Add district borders to the map
    folium.GeoJson(district_polygon.to_json()).add_to(map_karnataka)

    # Iterate over each row in the dataframe and add markers to the MarkerCluster
    for index, row in df.iterrows():
      # Extract latitude and longitude
      latitude = row['Latitude']
      longitude = row['Longitude']

      # Create a GeoJSON representation of the point
      point_geojson = {
          "type": "Feature",
          "geometry": {
              "type": "Point",
              "coordinates": [longitude, latitude]
          }
      }

      # Add the point to the MarkerCluster layer
      folium.GeoJson(point_geojson).add_to(marker_cluster)

  # Save or display the map
  return map_karnataka