#BAR PLOT
# 1. Title, X, Y axis Name
# 2. Size if Title, X, & Y
# 3. change width of graph
# 4. change color of graphs

import matplotlib.pyplot as plt

x=["Python","C","C++","Java"] 
y=[90,70,55,80]

plt.title("Bar Plot",fontsize=25)
plt.ylabel("Popularity",fontsize=15)
plt.xlabel("Langauge",fontsize=15)

plt.bar(x,y,width=0.4,color = ['r','g','b','y']) #width change the size of graph
plt.show()