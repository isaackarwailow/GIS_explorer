import pandas as pd
from IPython.display import display
import folium
from folium import plugins
from folium.plugins import MeasureControl
from folium.plugins import HeatMap
import re
# Read SF Incidents data
crime_csv = 'data/SFPD_Incidents-Current_Year_2015.csv'
df = pd.read_csv(crime_csv)
print(df)

if df.Date.dtypes == 'O':
    print('Converting date object to datetime data type and setting date as index...')
    df.Date = pd.to_datetime(df.Date)
    df.set_index('Date', inplace=True)
    print('Successfully set date as index!')

def generateBaseMap(default_location=[37.76, -122.45], tiles='OpenStreetMap', default_zoom_start=12):
    '''
    Create a map
    '''
    base_map = folium.Map(
        location = default_location
        , control_scale = True
        , zoom_start = default_zoom_start
    )
    return base_map

# combine the longitudes and latitudes and assign it to a variable
long_lat = list(zip(df.X, df.Y))

# subset the first 100 rows for testing purposes
first_100 = long_lat[:100]

# combine long_lat with the description of incidents to include as pop-ups on the main map
coordinates = list(zip(first_100, df.Descript.values))

# create a feature group named my_map to layer onto the main map display
fg0 = folium.FeatureGroup(name="markers")

# input the marker parameters in the form of a loop to allocate coordinates for 100 rows
# popup param is assigned incident descript
for i in coordinates:
      fg0.add_child(folium.Marker(location=i[0], icon=folium.Icon(color='red')))
      fg0.add_child(folium.Circle(location=i[0], radius=500,
                    popup=i[1].capitalize().strip(), line_color='#3186cc',
                    fill_color='#3186cc'))

base_map = generateBaseMap(default_location=[37.76, -122.45])

base_map.add_child(fg0)

# adding an extra zoom tool with a folium plugin
base_map.add_child(MeasureControl())

# save marker map to map.html
base_map.save("map.html")

# print confirmation of saved map
print('Map generation for base_map successful!')

# Generate a new map
heat_map = folium.Map(location=[37.76, -122.45],
                        tiles = "Stamen Toner",
                        zoom_start = 12)
print('heat_map successfully created')

# Create a feature group for heat map
print("Applying HeatMap feature to new map...")

# list comprehension for longitudes and latitudes
heat_data = [list(ele) for ele in long_lat]

# slice first 100 rows for heatmap data
heat_data_100 = heat_data[:100]

print("Adding heat data to heat map for first 100 rows")
HeatMap(heat_data).add_to(heat_map)


# add zoom control widget to heat_map
heat_map.add_child(MeasureControl())

# save marker map to heat_map.html
heat_map.save("heat_map.html")

# print confirmation of saved map
print('Map generation for heat_map successful!')

