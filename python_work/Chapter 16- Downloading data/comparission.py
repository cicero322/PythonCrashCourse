""" 15-2
from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


path = Path('weather_data/death_valley_2021_full.csv')
path_2 = Path('weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()
lines_2 = path_2.read_text().splitlines()

reader = csv.reader(lines)
reader_2 = csv.reader(lines_2)
header_row = next(reader)
header_row_2 = next(reader_2)

# Extract dates and high temperatures.
dates_sitka,rains_sitka = [], []
dates_valley, rains_valley = [], []


for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    rain = float(row[5])
    dates_valley.append(current_date)
    rains_valley.append(rain)

for row in reader_2:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    rain = float(row[5])
    dates_sitka.append(current_date)
    rains_sitka.append(rain)


# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates_sitka, rains_sitka, color='blue')
ax.plot(dates_valley, rains_valley, color='red')

# Format plot.
ax.set_title("Rain comparission, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rain (inches)", fontsize=16)
ax.tick_params(labelsize=16)

# Ajust limits
ax.set_ylim(0, max(rains_sitka) + 1)

plt.show() """

from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


path = Path('weather_data/death_valley_2021_full.csv')
path_2 = Path('weather_data/sitka_weather_2021_full.csv')
path_3 = Path('weather_data/san_francisco_2021_full.csv')

lines = path.read_text().splitlines()
lines_2 = path_2.read_text().splitlines()
lines_3 = path_3.read_text().splitlines()

reader = csv.reader(lines)
reader_2 = csv.reader(lines_2)
reader_3 = csv.reader(lines_3)

header_row = next(reader)
header_row_2 = next(reader_2)
header_row_3 = next(reader_3)

# Extract dates and high temperatures.
dates_sitka,rains_sitka = [], []
dates_valley, rains_valley = [], []
dates_sf, rains_sf = [], []


for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    rain = float(row[5])
    dates_valley.append(current_date)
    rains_valley.append(rain)

for row in reader_2:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    rain = float(row[5])
    dates_sitka.append(current_date)
    rains_sitka.append(rain)

for row in reader_3:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    rain = float(row[5])
    dates_sf.append(current_date)
    rains_sf.append(rain)

# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates_sitka, rains_sitka, color='blue', label='Sitka')
ax.plot(dates_valley, rains_valley, color='red', label='Death Valley')
ax.plot(dates_sf, rains_sf, color='green', label='San Francisco')

# Format plot.
ax.set_title("Daily Rain comparission, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rain (inches)", fontsize=16)
ax.tick_params(labelsize=16)

# Ajust limits
ax.set_ylim(0, max(rains_sf) + 1)

ax.legend()
plt.show()