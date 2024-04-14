import dash
from dash import html
from dash import dcc
from components import Header
import pandas as pd
from components import sidebar
from fun_style import SIDEBAR_STYLE

dash.register_page(__name__, path='/dashB1')
df = pd.read_excel('testdata.xlsx')




sidebar = html.Div(
    [
        html.Div(
            children=[
                html.Div(
                    html.Img(src="/assets/dsdsdd.png", height=55, style={"width": "80%", "display": "block"})
                )
            ],
            style={"display": "flex", "flex-direction": "column", "justify-content": "flex-end", "align-items": "center"}
        ),
        html.Div(
            children=[
                html.A(
                    html.Img(src="/assets/pridict.png", height=45, style={"width": "60%",  "display": "block", "position": "absolute", "bottom": "180px"}),
                    href="http://127.0.0.1:8050/pridict",  # Set the href attribute to the desired URL
                )
            ],
            style={"display": "flex", "flex-direction": "column", "justify-content": "flex-end", "align-items": "center"}
        ),
        html.Div(
            children=[
                html.A(
                    html.Img(src="/assets/dashboard.png", height=45, style={"width": "60%", "margin": "auto", "display": "block", "position": "absolute", "bottom": "100px" }),
                    href="https://lookerstudio.google.com/s/pdbCPDa2Hmg",  # Set the href attribute to the desired URL
                )
            ],
            style={"display": "flex", "flex-direction": "column", "justify-content": "flex-end", "align-items": "center"}
        ),
        html.Div(
            children=[
                html.A(
                    # Set the href attribute to the desired URL
                    html.Img(src="/assets/upload.jpg", height=45, style={"width": "60%", "margin": "auto", "display": "block", "position": "absolute", "bottom": "20px"}),
                    href="http://127.0.0.1:8050/upload", 
                )
            ],
            style={"display": "flex", "flex-direction": "column", "justify-content": "flex-end", "align-items": "center"}
        ),
        html.Div(
            children=[
                html.A(
                    # Set the href attribute to the desired URL
                    html.Img(src="/assets/admin.png", height=45, style={"width": "60%", "margin": "auto", "display": "block", "position": "absolute", "bottom": "260px"}),
                    href="http://127.0.0.1:8050/", 
                )
            ],
            style={"display": "flex", "flex-direction": "column", "justify-content": "flex-end", "align-items": "center"}
        )
    ],
    style=SIDEBAR_STYLE,
)

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
    Header.header(df),sidebar,
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

