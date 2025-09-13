#HISTOGRAM
# 1. "color = "r"" It changes the color of graph
# 2. "edgecolor="b"" It changes the boundry color of graph

import matplotlib.pyplot as plt
 
x=[41,22,68,14,39,60,13,35,26,16,12,44,30,52,55,33,11,59,18,28,46,20,55,42,15,25,47,38,24,45,54,36,49,10,29,37,56,40,23,32,51,31,60,21,27,48,17,34,53,43]

plt.title("wscube",fontsize=25) 
plt.xlabel("python",fontsize=20)
plt.ylabel("number",fontsize=20)

plt.hist(x, color = "r", edgecolor="b")
plt.show()