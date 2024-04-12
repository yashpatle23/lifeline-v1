import dash
from dash import html
from components import Header
import components
import pandas as pd

from sklearn.cluster import KMeans

from clustermap_severity import create_cluster_map


from components import sidebar

dash.register_page(__name__, path='/form')
df = pd.read_excel('testdata.xlsx')

# prompt: function to give a dataframe which has the district give in passing variable 

def get_district_data(df, district):

    # Check if the district is in the DataFrame.
    if district not in df['DISTRICTNAME'].unique():
        raise ValueError(f"The district '{district}' is not in the DataFrame.")

    # Filter the DataFrame to only include rows where the 'DISTRICTNAME' column matches the given district.
    district_df = df[df['DISTRICTNAME'] == district]

    # Return the filtered DataFrame.
    return district_df

layout = html.Div([
    Header.header(df),sidebar.sidebar()
],style={'backgroundColor': '#192444' ,'height':'100vh'})
# style={'backgroundColor': '#192444'})\


district_df=get_district_data(df,'Ballari')
acc_locations = district_df.dropna(axis=0, subset=['Latitude','Longitude'])
kmeans = KMeans(n_clusters=20, random_state=0).fit(acc_locations[['Latitude', 'Longitude']])

centers = kmeans.cluster_centers_


create_cluster_map(centers)
#print(centers)