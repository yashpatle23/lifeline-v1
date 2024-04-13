from dash import dcc, html, Input, Output
from flask import app

from map_road_type import map_road_type


def header(df):
    # Generate district dropdown options
    district_options = [
        {'label': 'Select District', 'value': 'Select District'},
        * [{'label': district, 'value': district} for district in df['DISTRICTNAME'].unique()]
    ]

    # Generate year dropdown options
    year_options = [
        {'label': 'All Year', 'value': 'All Year'},
        * [{'label': str(year), 'value': str(year)} for year in df['Year'].unique()]
    ]

    # Define the header component layout
    return html.Div([
        html.Div([
            html.H3("Karnataka State Police Accident Data Analysis", style={'display': 'inline-block', 'margin-left': 100, 'color': 'white'})
        ], style={'display': 'flex', 'align-items': 'center'}),  # Align logo and text to the left

        html.Div([
            dcc.Dropdown(
                id='district-dropdown',
                options=district_options,
                value='Select District',
                multi=False,  # Changed to False since we're only selecting one district
                clearable=False,
                style={'width': '200px', 'margin-right': '10px'}
            ),
            dcc.Dropdown(
                id='year-dropdown',
                options=year_options,
                value='All Year',
                clearable=False,
                style={'width': '200px', 'margin-left': '0px'}
            )
        ], style={'display': 'flex', 'align-items': 'center', 'justify-content': 'flex-end'})  # Align sliders to the right
    ],
        style={'display': 'flex', 'justify-content': 'space-between', 'background-color': '#1F2C56', 'padding': '10px'}
    )