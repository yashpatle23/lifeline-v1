
color_box = 'black'

SIDEBAR_STYLE = {
    "position": "fixed",
    "left": 0,
    "bottom": 0,
    "width": "4.5rem",
    
    "background-color": "#101010",
    "height" :"100vh",
}
SIDEBAR_STYLE2 = {
    "position": "fixed",
    "top": 65.5,
    "left": "4rem",
    "width": "27rem",
     "height" :"350px",
    "padding": "0.5rem 1rem",

}

GRAPHBAR_STYLE ={
    
                'width': '545px',  # Adjust width as needed
                'height': '200px',  # Adjust height as needed
                'position': 'fixed',
                'bottom': '2px',
                'left': '490px',
               
              
    
}
GRAPHBAR_STYLE1 ={
    
                'width': '400px',  
                'height': '290px',  
                 'margin-top':'10px',
               'position': 'fixed',
                'overflow': 'hidden', 
                 'bottom': '2px',
                'left': '80px',
                   
              
    
}
GRAPHBAR_STYLE2 ={
    
                  'width': '535px',  # Adjust width as needed
                'height': '200px',  # Adjust height as needed
                'position': 'fixed',
                'bottom': '0.5px',
                'left': '1015px',
              
              
    
}

CONTENT_STYLE = {
    "margin-left": "29.55rem",
    "margin-right": "0rem",
    "padding": "0.5rem 1rem",
    "display": "flex",  
    "flexDirection": "row", 
}
CONTENT_BOX_TITLES = {
    'height': '40px', 
    'font-size': '21px',  
    'background-color': "#1f2c56",
    'border-radius': '15px',
    'margin': '5px',
    'padding': '7px',
    'position': 'relative',
    'overflow-y': 'auto',
    'text-align': 'center', 
    'color': 'white', 
}
def style_COLONIAS(feature):
    return {
        'fillColor': None,   
        'color': '#00A322',      
        'weight': 1,           
        'fillOpacity': 0   
    }
def style_alcaldias(feature):
    return{
        'color': 'red',      
        'weight': 2.5,           
        'fillOpacity': 0,
        'dashArray': '5, 5'
    }

style_tabs = {
            'font-size': '16px', 
            'border-bottom': '1px outset #ccc',  
            'margin-bottom': '3px',  
            'backgroundColor': '#1f2c56',  
            'color': 'white', 
            'padding': '3px'
        } 
tab_selected_style = {
    'font-size': '18px',  
    'borderTop': '2px solid #119DFF', 
    'borderBottom': '0px outset #d6d6d6',
    'backgroundColor': '#1f2c56' , 
    'color': 'white', 
    'padding': '5px', 
}
tipo_colors = {
        'Bares' : '#FF0000',
        'Centros nocturnos' : '#FF6E00',
    }
