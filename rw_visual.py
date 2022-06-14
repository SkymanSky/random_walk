import matplotlib.pyplot as plt
from random_walk import RandomWalk
#Program aktif olduğu sürece yeni yürüyüşler yapmayı sürdür.
while True:
    rw=RandomWalk(50000)
    rw.fill_walk()
    #Yürüyüşteki noktaları çiz.
    plt.style.use('classic')
    fig, ax= plt.subplots(figsize=(10,6),dpi=128)
    point_numbers=range(rw.num_points)
    ax.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=1)
    #İlk ve son noktaları vurgula.
    ax.scatter(0,0,c='green',edgecolors='none',s=100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',s=100,edgecolors='none')
    #Eksenleri kaldır.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    #plt.savefig('random_walk.png',bbox_inches='tight')

    keep_running=input("Make another walk? (y/n): ")
    if keep_running=='n':
        break
