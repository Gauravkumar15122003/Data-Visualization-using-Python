# BOX PLOT
# 1.1 "notch=True" yai karne se box ka shape change ho jata hai
# 1.2 "vert=False" yai karne se graph wala box Vertical ho jayega
# 1.3 "patch_artist=True" ishse Box ke aandar color fill ho jayega


import matplotlib.pyplot as plt

x=[10,20,30,40,50,60,70]

plt.boxplot(x,notch=False, vert=True, labels=["Python"],
            patch_artist=True)

plt.show()