import dash
from dash import html
from components import Header
import components
import pandas as pd

from components import sidebar

dash.register_page(__name__, path='/form')
df = pd.read_excel('testdata.xlsx')


layout = html.Div([
    Header.header(df),sidebar.sidebar()
],style={'backgroundColor': '#192444' ,'height':'100vh'})
# style={'backgroundColor': '#192444'})