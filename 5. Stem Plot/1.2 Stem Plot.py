#STEM PLOT
# 1. "linefmt=":"" ishse line, doted line mai change ho jayega
# 2. "markerfmt="r*"" ishse color red mai change ho jayega & * se dot shape * shape mai change ho jayega, and we also use + at the place of *
# 3. "basefmt="g"" ishse base ke line ka color Green color mai change ho jayega
# 4. "label="Python"" yai ek Python name ka label upar mai laga dega, 
# 4.1 label ko use karne ke liye "plt.legend()" ko lagana padega



import matplotlib.pyplot as plt

x=[1,2,3,4,5,6]
y=[2,2,5,6,4,3]

plt.stem(x,y, linefmt=":", markerfmt="r*", basefmt="g",
         label="Python") #orientation="horizontal" graph horizontal ho jayega

plt.legend()

plt.show()