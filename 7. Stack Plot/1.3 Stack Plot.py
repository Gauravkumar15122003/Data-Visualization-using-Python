#STACK PLOT
# 1. "plt.grid()" pura graph rectangle box ke aandar aa jayega

import matplotlib.pyplot as plt
 
x=[1,2,3,4,5]
area1=[2,3,2,5,4]
area2=[2,3,4,5,6]
area3=[1,3,2,4,2]

plt.title("Python",fontsize=25)
plt.xlabel("X-axis",fontsize=20)
plt.ylabel("Y-axis",fontsize=20)

plt.stackplot(x,area1,area2,area3, labels=["1st","2nd","3rd"],
              colors=['r','g','m'])

plt.legend(loc=2)

plt.grid()

plt.show()