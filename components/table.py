from dash import dash_table
import pandas as pd


def create_table(df, clicked_point):
    # Filter the DataFrame to include only the desired columns
    columns_to_display = ['Junction_Control', 'Collision_Type', 'Road_Character', 'Road_Type','Latitude', 'Longitude']
    
    filtered_df = df[columns_to_display]
    
    # Highlight the row corresponding to the clicked point
    if clicked_point is not None:
        clicked_lat = clicked_point['lat']
        clicked_lon = clicked_point['lon']
        df['highlight'] = (df['Latitude'] == clicked_lat) & (df['Longitude'] == clicked_lon)
    else:
        df['highlight'] = False
    
    return dash_table.DataTable(
        data=filtered_df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in filtered_df.columns]
    )
