#BAR PLOT ( MULTIPLE BAR GRAPH in 1 BAR GRAPH )
# yai OVERLAP wala bar graph hai

import matplotlib.pyplot as plt

x=["Python","C","C++","Java"] 
y=[90,70,55,80]
z=[20,30,40,50]

plt.title("Bar Plot",fontsize=25)
plt.ylabel("Popularity",fontsize=15)
plt.xlabel("Langauge",fontsize=15)

plt.bar(x,y, width=0.4, color = "r", label= "POPULARITY" )
plt.bar(x,z, width=0.4, color = "g", label= "POPULARITY 1" ) 

plt.legend()
plt.show()