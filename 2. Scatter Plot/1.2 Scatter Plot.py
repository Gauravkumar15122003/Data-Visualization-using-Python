# SCATTER PLOT
# 1. Names of Title, X and, Y axis
# 2. Size if Title, X, & Y axis
# 3. change color of graphs
# 4. "sizes = [75]"  change size of dots 
# 5. "alpha = .5"  dots blur hoga, uska transparency change hoga(between 0 to 1)
# 6. "marker = "*""  ishse parameter se dot shape Star shape mai change ho jayega
# 7. "edgecolors = "r"" ishse Dot or Star shape ke boundry ka color change ho jayega 
# 8. "linewidths = 2" yai Dot or star ke boundry ka color ka thickness ko increase or decrese karta hai

import matplotlib.pyplot as plt

day = [1, 2, 3, 4, 5, 6, 7]
no = [2, 3, 1, 4, 5, 3, 6]

plt.title("Scatter Plot", fontsize=20)
plt.xlabel("Day", fontsize=15)
plt.ylabel("Number", fontsize=15)

plt.scatter(day, no, color = ['r','g','b','y','r','g','b'], 
            sizes = [400], alpha = .5, marker = "*", edgecolors = "r", linewidths = 2 )
plt.show()
