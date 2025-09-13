#BAR PLOT ( MULTIPLE BAR GRAPH in 1 BAR GRAPH )
# OVERLAP na hokar side mai aa jayega

# 1. "p=np.arange(len(x))" numpy mai ek arrange function hota hai jo array
#     form mai data ko store karta hai, and yaha hum uska length ko x kar diye hai  
# 2. "p1" ek variale declear kiye hai jiske andar "P" se aye hue value ko list mai convert karunga    
# 3. "plt.xticks(p+width/2,x)" yai karne se graph ke niche jo hum "x" variable mai declear
#     kiye hai wo aa jayega, and "/2" karne se yah graph ke center mai ayega      

import matplotlib.pyplot as plt
import numpy as np

x=["Python","C","C++","Java"]
y=[90,70,55,80]
z=[20,30,40,50]

p=np.arange(len(x))
p1=[j+width for j in p]

plt.title("Bar Plot",fontsize=25)
plt.ylabel("Popularity",fontsize=15)
plt.xlabel("Langauge",fontsize=15)

plt.bar(p,y, width=0.2, color = "r", label= "POPULARITY" )
plt.bar(p1,z, width=0.2, color = "g", label= "POPULARITY 1" ) 

plt.xticks(p+width/2,x)

plt.legend()
plt.show()