from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


#15-1
path = Path('weather_data/death_valley_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for key, value in enumerate(header_row):
    print(key, value)

# Extract dates and high temperatures.
dates, rains, title = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    rain = float(row[5])
    while len(title) < 1:
        title.append(row[1])
    dates.append(current_date)
    rains.append(rain)

print(title)

# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, rains, color='blue')

# Format plot.
ax.set_title(title[0], fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rain (inches)", fontsize=16)
ax.tick_params(labelsize=16)

# Ajust limits
ax.set_ylim(0, max(rains) + 1)

plt.show()