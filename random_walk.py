from random import choice

class RandomWalk:
    """Rastgele yürüyüler üreten bir sınıf."""

    def __init__(self,num_points=5000):
        #Yürüyüşün niteliklerine ilk değer ata.
        self.num_points=num_points

        #Bütün yürüyüşler 0,0 noktasında başlar.
        self.x_values=[0]
        self.y_values=[0]

        