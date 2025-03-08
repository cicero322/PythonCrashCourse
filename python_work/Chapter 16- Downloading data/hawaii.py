from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

#15-1
path = Path('weather_data/honolulu_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for key, value in enumerate(header_row):
    print(key, value)

# Extract dates and high temperatures.
dates, rains, title, tmin, tmax = [], [], [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    if row[5]:  # Verifica se a célula não está vazia
        rain = float(row[5])
    else:
        continue  # Pula a linha se a célula estiver vazia
    while len(title) < 1:
        title.append(row[1])
    if row[7] and row[8]:  # Verifica se as células não estão vazias
        max_temp = float(row[7])
        min_temp = float(row[8])
    else:
        continue  # Pula a linha se qualquer célula estiver vazia
    dates.append(current_date)
    rains.append(rain)
    tmin.append(min_temp)
    tmax.append(max_temp)

print(title)

# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, tmin, color='blue', label='Min Temp')
ax.plot(dates, tmax, color='red', label='Max Temp')

# Format plot.
ax.set_title(title[0], fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

# Ajust limits
ax.set_ylim(min(tmin) - 5, max(tmax) + 5)  # Ajusta os limites do eixo Y com base nos valores mínimos e máximos

# Add legend
ax.legend()

plt.show()