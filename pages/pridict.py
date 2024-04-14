import dash
from dash import html
from components import Header
import components
import pandas as pd
from dash import dcc
from components.Scatterplot import create_Scatterplot_map
from components.table import create_table  # Import the function to create the table
from dash.dependencies import Input, Output
from fun_style import *
from components import sidebar



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


dash.register_page(__name__, path='/pridict')
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

# Create the Dash app
app = dash.Dash(__name__)

layout = html.Div([
    Header.header(df),
    sidebar,
   
    
    html.Div([
       html.Div([
        html.Img(src='/assets/FeatureImportance.png', style={'width': '100%', 'height': '500px'}),
        html.Div(create_table(df, None), style={'overflowX': 'auto', 'overflowY': 'auto'}),  # Include the DataTable here
    ], style={'display': 'flex', 'flexDirection': 'column', 'height': '100%', 'width': '25%', 'margin-top': '10px','margin-left': '40px'}),
        dcc.Graph(
            id='scatterplot-map',
            figure=create_Scatterplot_map(df),
            style={'width': '70%', 'height': '85vh', 'margin-left': '10px', 'margin-right': '0', 'display': 'inline-block'}
        ),
    ], style={'margin-top': '5px', 'height': 'calc(85vh - 43px)', 'width': '100%', 'display': 'flex', 'position': 'relative', 'z-index': '0','margin-left': '20px'}),

], style={'backgroundColor': '#192444', 'height': '100vh','width': '100%','overflowX': 'hidden','margin-left': '15px'}),
# Define callback to update table content
@app.callback(
    Output('table-container', 'children'),
    [Input('junction-dropdown', 'value'),
     Input('severity-dropdown', 'value')]
)
def update_table(junction_value, severity_value):
    # Filter DataFrame based on selected options
    filtered_df = df[(df['Junction_Control'] == junction_value) & (df['Severity'] == severity_value)]
    return create_table(filtered_df),

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
