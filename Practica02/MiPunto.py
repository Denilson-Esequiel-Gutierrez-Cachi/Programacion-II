import math
class MiPunto:
    def __init__(self, *args):
        if len(args) == 0:
            self.x = 0
            self.y = 0
        else:
            self.x = args[0]
            self.y = args[1]
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distancia(self, *args):
        if len(args) == 1:  
            p = args[0]
            return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)
        elif len(args) == 2:  
            x = args[0]
            y = args[1]
            return math.sqrt((self.x - x)**2 + (self.y - y)**2)
#aplicativo
p1 = MiPunto()
p2 = MiPunto(10, 30.5)
print("Distancia:", p1.distancia(p2))