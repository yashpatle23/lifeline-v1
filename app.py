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



global filtered_df
filtered_df = df.copy()


def filter_dataframe(selected_district, selected_year):
    filtered_df = df.copy()# Make a copy of the original DataFrame to avoid modifying it directly
    if selected_district != 'Select District' and selected_year != 'All Year':
        filtered_df = filtered_df[(filtered_df['DISTRICTNAME'] == selected_district) & (filtered_df['Year'] == int(selected_year))]
    elif selected_district != 'Select District':
        filtered_df = filtered_df[filtered_df['DISTRICTNAME'] == selected_district]
    elif selected_year != 'All Year':
        filtered_df = filtered_df[filtered_df['Year'] == int(selected_year)]
    return filtered_df


@app.callback(
    Output("total-accidents-count", "children"),
    Output("total-accidents-title", "children"),
    Input('district-dropdown', 'value'),
    Input('year-dropdown', 'value')
)
def update_sidebar_statistics(selected_district, selected_year):
    filtered_df = filter_dataframe(selected_district, selected_year)
    total_accidents = filtered_df.shape[0]
    title = f"Total accidents in {selected_district}" if selected_district != "Select District" else "Total accidents"
    return total_accidents, title

@app.callback(
    Output('bar-graph', 'figure'),
    Output('donut-chart', 'figure'),
    Output('line-graph', 'figure'),
    Input('district-dropdown', 'value'),
    Input('year-dropdown', 'value'),
)
def update_graphs(selected_district, selected_year):
    filtered_df = filter_dataframe(selected_district, selected_year)
    return bar_graph(filtered_df), donut_chart(filtered_df), line_graph(filtered_df)




# combined_sidebar = html.Div([sidebar, sidebar2], style={"display": "flex", "flex-direction": "column"})  # Adjust flex-direction to stack the sidebars vertically


# Define callback to render content for each tab
@app.callback(
    Output('tabs-content-inline', 'children'),
    Input('tabs-styled-with-inline', 'value'),
    Input('district-dropdown', 'value'),
    Input('year-dropdown', 'value'),  # Listen to changes in the district dropdown
 
)
def render_content(tab, selected_district,selected_year):
    df = filter_dataframe(selected_district, selected_year)
    if tab == 'tab-1':
    # Render content for tab 1 with selected district
        return html.Div([
        dcc.Graph(
            figure=map_road_type(df),
            style={'width': '67.87%', 'height': '410px','margin-left': 'auto', 'margin-right': '0'}
        )
        ], style={'textAlign': 'right'})
    elif tab == 'tab-2':
        # Render content for tab 2
        return html.Div([
                html.Iframe(srcDoc=create_cluster_map(selected_district,df).get_root().render(), style={'width': '67.87%', 'height': '410px'})
            ], style={'textAlign': 'right'})
    elif tab == 'tab-3':
        # Render content for tab 3
        return html.Div([
            html.H1("Content for Tab 3")
        ], style={'textAlign': 'right'})
    else:
        return html.Div([])
    


#VINAY    
@app.callback(
    Output('table-container', 'children'),
    Input('junction-dropdown', 'value'),
    Input('severity-dropdown', 'value'),
)
def update_table(junction_value, severity_value):
    filtered_df = df[(df['Accident_Spot'] == junction_value) & (df['Severity'] == severity_value)]
    print(filtered_df)
    # Create HTML table
    table = html.Table(
        # Table header
        [html.Tr([html.Th(col) for col in ['Collision_Type', 'Junction_Control', 'Road_Character', 'Road_Type']])] +
        # Table body
        [html.Tr([html.Td(filtered_df.iloc[i][col]) for col in ['Collision_Type', 'Junction_Control', 'Road_Character', 'Road_Type']]) for i in range(min(len(filtered_df), 10))]  # Show up to 10 rows
    )
    
    return table

# Main function
if __name__ == '__main__':
    app.run_server(debug=True)