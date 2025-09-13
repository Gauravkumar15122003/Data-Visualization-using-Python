#BAR PLOT
# 1. "edgecolor" yai bar ke color ke upar ek new color karta hai
# 2. "linewidth" yai bar ke color ke upar wale color ka size(thickness) change karta hai
# 3. "linestyle" yai bar ke color ke upar wale color ka design change karta hai 
# 4. "alpha" yai bar ke color ko blur kar dega (iska value 0 to 1 hi hoga)
# 5. "plt.xticks(rotation=10)" yai "x" mai declear names ko rotate kar dega

import matplotlib.pyplot as plt

x=["Python","C","C++","Java"] 
y=[90,70,55,80]

plt.title("Bar Plot",fontsize=25)
plt.ylabel("Popularity",fontsize=15)
plt.xlabel("Langauge",fontsize=15)

plt.bar(x,y,width=0.4, color = ['r','g','b','y'], 
        edgecolor = ['g','b','r','r'], linewidth = 5,
        linestyle = ":", alpha=0.5 ) 

plt.xticks(rotation=10)
plt.show()
