from pathlib import Path
import json
import csv

import plotly.express as px

#16.9
path = Path('fire_data\world_fires_1_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

latitude, longitude, brightness = [], [], []
for row in reader:
    lat = float(row[0])
    long = float(row[1])
    bright = float(row[2])
    latitude.append(lat)
    longitude.append(long)
    brightness.append(bright)

    

title = 'World Fires 1 Day'
fig = px.scatter_geo(lat=latitude, lon=longitude, title=title, size=brightness,projection='orthographic', labels={'size': 'Magnitude', 'lat': 'Latitude', 'lon': 'Longitude', 'color': 'Intensity / Kelvin', 'hover_name': 'place'}, color=brightness,)
fig.show() 