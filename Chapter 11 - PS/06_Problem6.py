class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    
    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result
    
    def __str__(self):
        return f"Vector({self.x}i + {self.y}j + {self.z}k)"
    

# Testing of implimentation
v1 = Vector(1, 3, 4)
v2 = Vector(4, -1, 4)
v3 = Vector(6, 7, 4)

print(v1 + v2)
print(v1 * v2)
