"""  15-1 & 15-2
import matplotlib.pyplot as plt

#x_values = range(1,6)
x_values = range(1,5001)
y_values = [x**3 for x in x_values]

fig,ax = plt.subplots()

ax.scatter(x_values,y_values,c=y_values, cmap=plt.cm.Blues, s=10)
ax.set_title("Numbers cubed", fontsize= 14)
ax.set_xlabel("Value")
ax.set_ylabel("Cube of value")
#ax.axis([0,5,0,5**3])
ax.axis([0,5000,0,5000**3])
#plt.savefig("15-1-Figure1.png",bbox_inches='tight')
#plt.savefig("15-1-Figure2.png",bbox_inches='tight')
plt.savefig("15-2-Figure1.png",bbox_inches='tight')
plt.show()
"""