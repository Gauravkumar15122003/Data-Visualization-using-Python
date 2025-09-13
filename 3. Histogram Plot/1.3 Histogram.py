#HISTOGRAM
# 1. "orientation="horizontal" This will change graph in horizontal
# 2. "rwidth=0.8" yai graph ka width change karta hai. isko "plt.hist" mai likhte hai
# 3. "label="Python"" yai top corner mai lable lagane ke liye use hota hai
#    jab bhi hum label lagayenge to "plt.legend()" lagana hoga
# 4. "plt.grid()" yai use karne se pura graph mai rectangle box aa jayega


import matplotlib.pyplot as plt
 
x=[87, 12, 56, 33, 78, 19, 45, 62, 4, 91, 27, 72, 9, 50, 68, 14, 77, 36, 93, 21, 60, 7, 82, 42, 55, 30, 89, 1, 65, 38, 83, 17, 71, 49, 95]

plt.title("wscube",fontsize=25) 
plt.xlabel("python",fontsize=20)
plt.ylabel("number",fontsize=20)

plt.hist(x, color = "r", bins=[10,20,30,40,50,60,70,80,90,100]
         , orientation="vertical", label="Python")

plt.legend()

plt.grid()

plt.show()