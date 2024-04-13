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


dash.register_page(__name__, "/")
df = pd.read_excel('testdata.xlsx')




global filtered_df
filtered_df = df.copy()





sidebar = html.Div(
    [
        html.Div(
            children=[
                html.Div(
                    html.Img(src="/assets/dsdsdd.png", height=55, style={"width": "80%", "margin": "auto", "display": "block"})
                )
            ],
            style={"display": "flex", "flex-direction": "column", "justify-content": "center", "align-items": "center"}
        ),
        html.Hr(),
        html.Div(
          html.Img(src="/assets/admin.png", height=45, style={"width": "60%", "margin": "auto", "display": "block", "position": "absolute", "bottom": "12px"})
        )
    ],
    style=SIDEBAR_STYLE,
)



sidebar2 = html.Div(
    [
        # First row
        html.Div(
            [
                # First column
                html.Div(
                    [
                        # Title and count for the first box
                        html.Div(
                            [
                                html.Div("Total accidents", id="total-accidents-title", style={"color": "white", "font-weight": "bold","font-size": "20px"}),
                                html.Div(id="total-accidents-count", style={"color": "orange","font-size": "50px"})
                            ],
                            style={"background-color": "#1F2C56", "padding": "5px", "text-align": "center"}
                        )
                    ],
                    style={"flex": 1, "margin": "5px"}
                ),
                # Second column
                html.Div(
                    [
                        # Title and count for the second box
                        html.Div(
                            [
                                html.Div("Total accidents", style={"color": "white", "font-weight": "bold","font-size": "20px"}),
                                html.Div(df['Latitude'].count(), id="total-accidents-all", style={"color": "orange","font-size": "50px"})
                            ],
                            style={"background-color": "#1F2C56", "padding": "5px", "text-align": "center"}
                        )
                    ],
                    style={"flex": 1, "margin": "5px"}
                )
            ],
            style={"display": "flex", "flex-direction": "row", "justify-content": "center", "align-items": "center"}
        ),
        # Second row
        
    ],
    style=SIDEBAR_STYLE2
)



graphbar = html.Div(
    [
        # Small div with graph
        html.Div(
            children=[
                dcc.Graph(
                    id='bar-graph',  # Set the ID of the graph component
                    figure={},  # Initially empty figure
                    style={'width': '100%', 'height': '100%'}
                )
            ],           
            
        ),
    ],style=GRAPHBAR_STYLE,
)

graphbar1 = html.Div(
    [
        # Small div with graph
        html.Div(
            children=[
                dcc.Graph(
                    id='donut-chart',
                    figure={}
                )
            ],           
            
        ),
    ],style=GRAPHBAR_STYLE1,
)
graphbar2 = html.Div(
    [
        # Small div with graph
        html.Div(
            children=[
                dcc.Graph(
                    id='line-graph',
                    figure={}
                )
            ],            
            
        ),
    ],style=GRAPHBAR_STYLE2,
)

# combined_sidebar = html.Div([sidebar, sidebar2], style={"display": "flex", "flex-direction": "column"})  # Adjust flex-direction to stack the sidebars vertic



layout = html.Div([
    Header.header(df),sidebar,sidebar2, graphbar,graphbar1,graphbar2, # Navbar at the top
    html.Div([              
              html.Div([
                  dcc.Tabs(id="tabs-styled-with-inline", value='tab-1', children=[
                      dcc.Tab(label='Based On Road Types', value='tab-1', style=style_tabs, selected_style=tab_selected_style),
                      dcc.Tab(label='Based on Clusters', value='tab-2', style=style_tabs, selected_style=tab_selected_style),
                      dcc.Tab(label='Predicted Spots', value='tab-3', style=style_tabs, selected_style=tab_selected_style),

                  ], style=CONTENT_STYLE),
                  html.Div(id="tabs-content-inline")     
              ])
    ])
],style={'backgroundColor': '#192444' ,'height':'100vh'})
# style={'backgroundColor': '#192444'})