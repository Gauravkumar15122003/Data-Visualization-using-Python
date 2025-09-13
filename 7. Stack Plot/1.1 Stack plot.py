#STACK PLOT(AREA PLOT)
# When we do multiple Plot and show it in 1 diagram then its called Stack Plot

import matplotlib.pyplot as plt
 
x=[1,2,3,4,5]
area=[2,3,2,5,4]

plt.stackplot(x,area)
plt.show()