#BAR PLOT (HORIZONTAL BAR) 
# 1. "plt.bar" yai use hota hai vertical bar ke liye (yaha "plt.bar" use nhi kiye hai)
# 2. "plt.barh" yai use hota hai horizontal bar ke liye
#NOTE= Horizontal bar jab creat karenge to "width" nhi denge

import matplotlib.pyplot as plt

x=["Python","C","C++","Java"] 
y=[90,70,55,80]

plt.title("Bar Plot",fontsize=25)
plt.ylabel("Popularity",fontsize=15)
plt.xlabel("Langauge",fontsize=15)

plt.barh(x,y, color = ['r','g','b','y'], 
        label= "POPULARITY" ) 
plt.legend()

plt.show()