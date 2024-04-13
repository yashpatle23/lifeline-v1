import dash
from dash import html
from components import Header
import components
import pandas as pd



from clustermap_severity import create_cluster_map


from components import sidebar

dash.register_page(__name__, path='/form')
df = pd.read_excel('testdata.xlsx')

# prompt: function to give a dataframe which has the district give in passing variable 


layout = html.Div([
    Header.header(df),sidebar.sidebar()
],style={'backgroundColor': '#192444' ,'height':'100vh'})
# style={'backgroundColor': '#192444'})\

#print(centers)