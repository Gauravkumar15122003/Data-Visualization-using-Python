#STEP PLOT
# 1. "marker="o", ms=10" ishse dot mark ho jayega, iske place par hum *, + yai bhi use kar sakte hai
# 1.1 "ms=10" ishse marker ka size change hoga
# 2. "mfc="b"" ishse dot ka outer surface ka color change ho jayega
# 3. "label="Python"" works only with plt.legend()

import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[2,3,7,5,9]

plt.title("Python")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.step(x,y,color="r", marker="o", ms=10, mfc="b",
         label="Python")

plt.legend(loc=2)
plt.grid()

plt.show()