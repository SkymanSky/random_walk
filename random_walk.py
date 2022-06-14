from random import choice

class RandomWalk:
    """Rastgele yürüyüler üreten bir sınıf."""

    def __init__(self,num_points=5000):
        #Yürüyüşün niteliklerine ilk değer ata.
        self.num_points=num_points

        #Bütün yürüyüşler 0,0 noktasında başlar.
        self.x_values=[0]
        self.y_values=[0]

    def fill_walk(self):
        """Yürüyüşteki bütün noktaları hesapla."""
        #Yürüyüş istenen uzunluğa ulaşana kadar adım atmaya devam et.
        while len(self.x_values)<self.num_points:
            #Hangi yöne gidileceğine ve bu yönde ne kadar uzağa gidileceğine
            #karar ver.
            x_step=self.get_step()
            y_step=self.get_step()

            #Hiçbir yere gitmeyen hareketleri redded.
            if x_step==0 and y_step==0:
                continue
            #Yeni konumu hesapla
            x=self.x_values[-1]+x_step
            y=self.y_values[-1]+y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        direction=choice([1,-1])
        distance=choice([0,1,2,3,4])
        step=direction*distance
        return step

        