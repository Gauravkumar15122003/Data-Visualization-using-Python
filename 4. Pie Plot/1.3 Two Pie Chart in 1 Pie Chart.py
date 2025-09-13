#PIE PLOT
# 2 Pie Chart in 1 Pie Chart

import matplotlib.pyplot as plt

x=[10,20,30,40]
w=[15,25,35,25]
y=["C++","C","java","Python"]

plt.title("POPULARITY",fontsize=15)

plt.pie(x, labels = y, radius=2,colors = ["y","b","g","r"])
plt.pie(w, labels = y, radius=1,colors = ["y","b","g","r"])

plt.show() 