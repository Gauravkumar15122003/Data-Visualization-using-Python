#SUB PLOT
# More then 1 graph in 1 pic
# 1. "plt.subplot(2,2,1)" isko every diagram complete hone ke badh laga hai,
#     and next diagram mai jab lagayenge to ush time last mai 1 digit increase kar denge

import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[1,2,3,4,5]
plt.subplot(2,2,1)
plt.plot(x,y, color="r")
#
x1=[10,20,30,40]
y1=["C","C++","java","Python"]
plt.subplot(2,2,2)
plt.pie(x1)
#
x2=["Python","C","C++","Java"] 
y2=[90,70,55,80]
plt.subplot(2,2,3)
plt.bar(x2,y2)
#
x3=[1,2,3,4,5]
area=[2,3,2,5,4]
plt.subplot(2,2,4)
plt.stackplot(x3,area)


plt.show()