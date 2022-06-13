import matplotlib.pyplot as plt
from random_walk import RandomWalk
#Program aktif olduğu sürece yeni yürüyüşler yapmayı sürdür.
while True:
    rw=RandomWalk()
    rw.fill_walk()
    #Yürüyüşteki noktaları çiz.
    plt.style.use('classic')
    fig, ax= plt.subplots()
    point_numbers=range(rw.num_points)
    ax.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=15)
    #İlk ve son noktaları vurgula.
    ax.scatter(0,0,c='green',edgecolors='none',s=100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',s=100,edgecolors='none')
    plt.show()

    keep_running=input("Make another walk? (y/n): ")
    if keep_running=='n':
        break
