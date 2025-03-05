""" 15.6
from random import randint
import plotly.express as px

class Die:
    def __init__(self,die_sides=6):
        self.die_sides = die_sides

    def roll(self):
        return randint(1, self.die_sides)

die_1 = Die(8)
die_2 = Die(8)
results = []

for roll_num in range(0,1000000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

print(results.count(1))

frequencies = []
max_result = die_1.die_sides + die_2.die_sides
possible_results = range(2,max_result+1)

for values in possible_results:
    frequency = results.count(values)
    frequencies.append(frequency)

title= "Sum of Rolling Two D8 1,000,000 Times"

fig= px.pie(values=frequencies, title=title, names=possible_results, labels={'values': 'Frequencies', 'names': 'Die Side'})
fig.show()
fig_1= px.bar(x=possible_results, y=frequencies, title=title, labels={'x': 'Dies Sum', 'y': 'Frequency'})
fig_1.update_layout(xaxis_dtick=1)
fig_1.show() """

""" 15.7
from random import randint
import plotly.express as px

class Die:
    def __init__(self,die_sides=6):
        self.die_sides = die_sides

    def roll(self):
        return randint(1, self.die_sides)

die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)
results = []

for roll_num in range(0,1000000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

print(results.count(1))

frequencies = []
max_result = die_1.die_sides + die_2.die_sides
possible_results = range(3,max_result+1)

for values in possible_results:
    frequency = results.count(values)
    frequencies.append(frequency)

title= "Sum of Three D6 1,000,000 Times"

fig= px.pie(values=frequencies, title=title, names=possible_results, labels={'values': 'Frequencies', 'names': 'Die Side'})
fig.show()
fig_1= px.bar(x=possible_results, y=frequencies, title=title, labels={'x': 'Dies Sum', 'y': 'Frequency'})
fig_1.update_layout(xaxis_dtick=1)
fig_1.show() """

""" 15.8    
from random import randint
import plotly.express as px

class Die:
    def __init__(self,die_sides=6):
        self.die_sides = die_sides

    def roll(self):
        return randint(1, self.die_sides)

die_1 = Die(6)
die_2 = Die(6)

results = []

for roll_num in range(0,1000000):
    result = die_1.roll() * die_2.roll() 
    results.append(result)

print(results.count(1))

frequencies = []
max_result = die_1.die_sides * die_2.die_sides
possible_results = range(1,max_result+1)

for values in possible_results:
    frequency = results.count(values)
    frequencies.append(frequency)

title= "Mutiplication of Two D6 1,000,000 Times"

fig= px.pie(values=frequencies, title=title, names=possible_results, labels={'values': 'Frequencies', 'names': 'Die Side'})
fig.show()
fig_1= px.bar(x=possible_results, y=frequencies, title=title, labels={'x': 'Dies Sum', 'y': 'Frequency'})
fig_1.update_layout(xaxis_dtick=1)
fig_1.show() """

""" 15.9
from random import randint
import plotly.express as px

class Die:
    def __init__(self,die_sides=6):
        self.die_sides = die_sides

    def roll(self):
        return randint(1, self.die_sides)

die = Die(6)

results = [die.roll() for roll_num in range(0,1000000)]

possible_results = range(1,die.die_sides+1)

frequencies = [results.count(value) for value in possible_results]

print(frequencies)
title= "Roll of D6 1,000,000 Times"

fig= px.pie(values=frequencies, title=title, names=possible_results, labels={'values': 'Frequencies', 'names': 'Die Side'})
fig.show()
fig_1= px.bar(x=possible_results, y=frequencies, title=title, labels={'x': 'Dies Sum', 'y': 'Frequency'})
fig_1.update_layout(xaxis_dtick=1)
fig_1.show() """

#15-10
from random import randint
import matplotlib.pyplot as plt

class Die:
    def __init__(self,die_sides=6):
        self.die_sides = die_sides

    def roll(self):
        return randint(1, self.die_sides)

die = Die(6)

results = [die.roll() for roll_num in range(0,1000000)]

possible_results = range(1,die.die_sides+1)

frequencies = [results.count(value) for value in possible_results]

print(frequencies)


title= "Roll of D6 1,000,000 Times"
fig,ax = plt.subplots()
ax.set_title(title)
ax.set_xlabel("Die side")
ax.set_ylabel("Frequency")
ax.bar(possible_results, frequencies)
ax.autoscale()
plt.show()