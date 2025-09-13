#PIE PLOT
# 1. "labels = y" yai karne se har ek part ka name aa jayega
# 1.1 "rotatelabels=True" ishse har ek part ka name 90degree par rotate ho jayega
# 2. "explode=[.4,.0,.0,.0]" yai karne se ek par heighlight ho jayega and bahar ke side nikal jayega
# 3. "colors = " yai PIE CHART ka color change kar dega
# 4. "autopct = "%0.2f%%" isko use karne se PIE CHART ka % show karega
# 5. "shadow = True" yai use karne se shadow aa jayega
# 6. "wedgeprops={"linewidth":3}" yai shadow ka color ko light & dark karta hai
# 6.1 "wedgeprops={"edgecolor":"black"}"  yai shadow ka random color ko change kar dega, yai linewidth ke hi sath use hoga, agar hum chahe shadow ka color ko change karne ke liye to
# 7. "radius = 1.5" ishse PIE CHART ke circle ka Radius increase ho jayega
# 8. "labeldistance = 1.1" ishse labels ka name PIE CHART se close & far jayega, wo name jo #1 mai likhe hai, wo wala
# 9. "textprops={"fontsize":18}" ishse labels ka size increse & decrese hoga
# 10. "plt.legend()" yai ek label(matlab kon sa color kya repersent kar raha hai wo) show karega
# 10.1  "plt.legend(loc=3)" yaha "loc=3" ka matlab hai (loc=location) label ko 3rd corner mai rakhna hai. isko hum 1,2,3,4,... kar sakte hai

import matplotlib.pyplot as plt

x=[10,20,30,40]
y=["C++","C","java","Python"]

plt.title("POPULARITY",fontsize=15)

plt.pie(x, labels = y,rotatelabels=True, explode = [.5,.0,.0,.0],
        colors = ["y","b","g","r"], autopct = "%0.2f%%"
        ,shadow = True, wedgeprops={"linewidth":3, "edgecolor":"black"}, 
        radius = 1.1, labeldistance = 1.1, textprops={"fontsize":18})

plt.legend(loc=3)

plt.show() 