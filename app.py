from dash import Dash, dcc, html, Input, Output, callback 
import base64
from dash.dependencies import Input, Output, State
import pandas as pd
import folium
from keplergl import *
import dash
import dash_bootstrap_components as dbc
from components.plot_functions import bar_graph
from map_road_type import map_road_type
from clustermap_severity import create_cluster_map
from components import Header
from components.donut_chart import donut_chart
from components.line_graph import line_graph
import geopandas as gpd
import folium
from folium import plugins
from fun_style import * 



app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True,use_pages=True)

df = pd.read_excel('testdata.xlsx')





@app.callback(
    Output('tabs-content-inline', 'children'),
    Input('tabs-styled-with-inline', 'value')
)
def render_content(tab):
    
    if tab == 'tab-1':
        m = map_road_type(df)
        # Get the HTML content of the map
        map_html_content = m.get_root().render()
        # Display the map HTML content in the Dash app
        return html.Div([
            html.Iframe(srcDoc=map_html_content, style={'width': '67.87%', 'height': '410px'})
        ], style={'textAlign': 'right'})
    elif tab == 'tab-2':
        m = create_cluster_map(df)
        # Get the HTML content of the map
        map_html_content = m.get_root().render()
        # Display the map HTML content in the Dash app

        return html.Div([
            html.Iframe(srcDoc=map_html_content, style={'width': '67.87%', 'height': '410px'})
        ], style={'textAlign': 'right'})
    elif tab == 'tab-3':
        m = create_cluster_map(df)
        # Get the HTML content of the map
        map_html_content = m.get_root().render()
        # Display the map HTML content in the Dash app

        return html.Div([
            html.Iframe(srcDoc=map_html_content, style={'width': '67.87%', 'height': '410px'})
        ], style={'textAlign': 'right'})
    
    
    else:
        return html.Div([])
    

# Main function
if __name__ == '__main__':
    app.run_server(debug=True)