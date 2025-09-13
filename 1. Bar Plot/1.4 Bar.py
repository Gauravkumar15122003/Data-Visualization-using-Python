#BAR PLOT
# 1. "label" yai upar mai ek name creat kar dega
#    jab bhi hum label lagayenge to uske liye "plt.legend()" name ke function declera karna hota hai
#    plt.legend(loc=2) ke andar "loc=2" ka matlab hai location 2 par label rakhna hai, isko hum 1,2,3,4,... kar dakte hai

import matplotlib.pyplot as plt

x=["Python","C","C++","Java"] 
y=[90,70,55,80]

plt.title("Bar Plot",fontsize=25)
plt.ylabel("Popularity",fontsize=15)
plt.xlabel("Langauge",fontsize=15)

plt.bar(x,y,width=0.4, color = ['r','g','b','y'], 
        label= "POPULARITY" ) 
plt.legend(loc=2)

plt.show()