# BOX PLOT (More then 1 box)

import matplotlib.pyplot as plt

x=[10,20,30,40,50,60,70]
y=[10,20,40,50,30,60,90]

z=[x,y]

plt.boxplot(z)

plt.show()