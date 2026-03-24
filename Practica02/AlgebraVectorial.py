import math
class AlgebraVectorial:
    def producto_punto(self, a, b):
        return sum(x*y for x, y in zip(a, b))
    def magnitud(self, v):
        return math.sqrt(sum(x*x for x in v))
    def perpendicular(self, a, b):
        return self.producto_punto(a, b) == 0

    def paralelo(self, a, b):
        k = None
        for x, y in zip(a, b):
            if y != 0:
                k = x / y
                break
        if k is None:
            return False
        for x, y in zip(a, b):
            if y != 0 and x / y != k:
                return False
        return True
    
    def proyeccion(self, a, b):
        escalar = self.producto_punto(a, b) / self.producto_punto(b, b)
        return [escalar * x for x in b]
    def componente(self, a, b):
        return self.producto_punto(a, b) / self.magnitud(b)

av = AlgebraVectorial()
a = [2, 4]
b = [4, -2]
print("Perpendicular:", av.perpendicular(a, b))
print("Paralelo:", av.paralelo(a, b))
print("Proyeccion:", av.proyeccion(a, b))
print("Componente:", av.componente(a, b))