#HISTOGRAM
# 1. "bins" jo number diye hai, ush range mai jo data aa raha hai usko show kar dega, for seeing diffrence look to file of "1.1 Histogram"
# 2. "cumulative = 1" yai graph ko reverse form mai repersent kar dega, in low to heigh order


import matplotlib.pyplot as plt
 
x=[87, 12, 56, 33, 78, 19, 45, 62, 4, 91, 27, 72, 9, 50, 68, 14, 77, 36, 93, 21, 60, 7, 82, 42, 55, 30, 89, 1, 65, 38, 83, 17, 71, 49, 95]

plt.title("wscube",fontsize=25) 
plt.xlabel("python",fontsize=20)
plt.ylabel("number",fontsize=20)

plt.hist(x, color = "r", edgecolor="b", bins=[10,20,30,40,50,60,70,80,90,100]
         , cumulative = 1)
plt.show()