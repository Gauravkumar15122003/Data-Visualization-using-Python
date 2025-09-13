#FILL BETWEEN PLOT
#1. "plt.fill_between(x,y)" ishse line ke niche ka area fill ho jayega color se
#2. "alpha=.5" ishse color blur ho jayega(yai 0 to 1 tak hi work karta  hai)
 

import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[1,2,3,4,5]

plt.title("PYTHON",fontsize=20)
plt.xlabel("X-Axis",fontsize=15)
plt.ylabel("Y-Axis",fontsize=15)

plt.plot(x,y, color="r")

plt.fill_between(x,y, color="g", alpha=.5)

plt.show()