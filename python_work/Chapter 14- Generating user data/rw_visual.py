import matplotlib.pyplot as plt
from random_walk import RandomWalk

""" 15.3
# Make a random walk.
rw = RandomWalk(5_000)
rw.fill_walk()
# Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(16,9))
point_numbers = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, color="blue", linewidth=1)
ax.set_aspect('equal')
##
# Emphasize the first and last points.
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
    s=100)
##
# Remove the axes.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.savefig("15-3-Figure1.png",bbox_inches='tight')
plt.show()
"""
import plotly.express as px
from random_walk import RandomWalk

#15-10

# Make a random walk.
rw = RandomWalk(5000)
rw.fill_walk()

title="Random walk"
fig = px.scatter(x=rw.x_values, y=rw.y_values,title=title)

# Remove the axes.
fig.update_layout(xaxis_scaleanchor="y")
fig.show()

