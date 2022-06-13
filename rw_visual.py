import matplotlib.pyplot as plt
from random_walk import RandomWalk
#Rastgele bir yürüyüş yap.
rw=RandomWalk()
rw.fill_walk()
#Yürüyüşteki noktaları çiz.
plt.style.use('classic')
fig, ax= plt.subplots()
ax.scatter(rw.x_values,rw.y_values,s=15)
plt.show()
