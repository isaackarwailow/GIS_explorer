import pandas as pd
import folium 

# replaced existing geojson file with an Australian one rendered for states
state_geo = "data/states.geojson"
state_unemployment = "data/aus_unemployment_rate.csv"
state_data = pd.read_csv(state_unemployment)

# drop the row for austrlaia at index 0 in the geojson file
print("Dropping row index 0 in dataframe...")
state_data.drop([0], axis=0, inplace=True)
assert state_data.Region.loc[1] != 'Australia', 'Unsuccessfully dropped Australia from csv file'

# You can copy the coordinates for the default location by going to google maps and right clicking Australia
# Then, copy the coordinates to the clipboard
m = folium.Map(location=[-23.877610095191628, 135.01297734173076], zoom_start=3)

'''note that key_on param in Choropleth function should specifiy
the level of granularity that matches the key value data in the csv file'''
folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_data,
    columns=["Region", "Unemployment Rate (15+)"],
    key_on="feature.properties.STATE_NAME",
    fill_color="PuBuGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Unemployment Rate in Australian States(%)",
).add_to(m)

folium.LayerControl().add_to(m)

m.save('choro_aus_unemployment.html')