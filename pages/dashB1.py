import dash
from dash import html
from dash import dcc
from components import Header
import pandas as pd
from components import sidebar

dash.register_page(__name__, path='/dashB1')
df = pd.read_excel('testdata.xlsx')

junction_options = [
    {'label': 'T Junction', 'value': 'T Junction'},
    {'label': 'Y Junction', 'value': 'Y Junction'},
    {'label': 'Junction', 'value': 'Junction'}
]

severity_options = [
    {'label': 'Fatal', 'value': 'Fatal'},
    {'label': 'Grievous Injury', 'value': 'Grievous Injury'},
    {'label': 'Simple Injury', 'value': 'Simple Injury'},
    {'label': 'Damage Only', 'value': 'Damage Only'}
]



layout = html.Div([
    Header.header(df),sidebar.sidebar(),
            html.Div([
            dcc.Dropdown(
            id='junction-dropdown',
            options=junction_options,
            value='T Junction',
            clearable=False,
            style={'width': '200px', 'margin-left': '50px', 'margin-top': '10px'}
        ),

        dcc.Dropdown(
            id='severity-dropdown',
            options=severity_options,
            value='Fatal',
            clearable=False,
            style={'width': '200px', 'margin-left': '70px', 'margin-top': '10px'}
        )
        ], style={'display': 'flex'}),
        html.Div(id='table-container')
],style={'backgroundColor': '#192444' ,'height':'100vh'})

