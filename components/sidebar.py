from dash import html, dcc

from fun_style import SIDEBAR_STYLE


def sidebar():
    
    sidebar = html.Div(
        [
            html.Div(
        children=[
            html.Img(src="/assets/dsdsdd.png", height=55, style={"width": "80%", "margin": "auto", "display": "block"})
        ],
        style={"display": "flex", "justify-content": "center", "align-items": "center"}
    ),
            html.Hr(),
        
            
            
        
            
        ],style = SIDEBAR_STYLE,
    
    )
    return sidebar