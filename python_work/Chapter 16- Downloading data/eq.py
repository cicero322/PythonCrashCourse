from pathlib import Path
import json

import plotly.express as px

#16.6, 16.7, 16.8

#m1.
#path = Path('eq_data/eq_data_1_day_m1.geojson')
path = Path("eq_data\eq_data_1_day.m2dot5.geojson")

contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

place = [eq_dict['properties']['place'] for eq_dict in all_eq_dicts]
mags = [eq_dict['properties']['mag'] for eq_dict in all_eq_dicts]
lons = [eq_dict['geometry']['coordinates'][0] for eq_dict in all_eq_dicts]
lats = [eq_dict['geometry']['coordinates'][1] for eq_dict in all_eq_dicts]


title = all_eq_data['metadata']['title']
fig = px.scatter_geo(lat=lats, lon=lons, title=title, size=mags, hover_name=place,projection='orthographic', labels={'size': 'Magnitude', 'lat': 'Latitude', 'lon': 'Longitude', 'color': 'Magnitude', 'hover_name': 'place'}, color=mags,)
fig.show()