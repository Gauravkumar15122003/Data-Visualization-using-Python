#PIE PLOT
# RING PIE CHART

import matplotlib.pyplot as plt

x=[10,20,30,40]
z=[25,25,25,25]
y=["C++","C","java","Python"]

plt.title("POPULARITY",fontsize=15)

plt.pie(x, labels = y, radius=1.5,colors = ["y","b","g","r"])
plt.pie([1],colors='w')

plt.show() 