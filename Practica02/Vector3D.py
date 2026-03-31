import math
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __add__(self, v):
        return Vector3D(self.x + v.x, self.y + v.y, self.z + v.z)
    
    def __mul__(self, k):
        return Vector3D(self.x * k, self.y * k, self.z * k)
    
    def longitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def normal(self):
        l = self.longitud()
        return Vector3D(self.x/l, self.y/l, self.z/l)
    
    def producto_escalar(self, v):
        return self.x*v.x + self.y*v.y + self.z*v.z
    
    def producto_vectorial(self, v):
        return Vector3D(
            self.y*v.z - self.z*v.y,
            self.z*v.x - self.x*v.z,
            self.x*v.y - self.y*v.x
        )
    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
#Aplicativo
v1 = Vector3D(1,2,3)
v2 = Vector3D(4,5,6)

print("Suma:", v1 + v2)
print("Escalar:", v1 * 2)
print("Longitud:", v1.longitud())
print("Normal:", v1.normal())
print("Producto escalar:", v1.producto_escalar(v2))
print("Producto vectorial:", v1.producto_vectorial(v2))