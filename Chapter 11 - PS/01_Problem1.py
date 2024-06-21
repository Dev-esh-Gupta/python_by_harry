class Vector2D:
   def __init__(self, i, j) -> None:
        self.i = i
        self.j = j

class Vector3D(Vector2D):
    def __init__(self, i, j, k) -> None:
        super().__init__(i, j)
        self.k = k

o = Vector2D(4, 5)
print(o.i, o.j)

o2 = Vector3D(4, 5, 7)
print(o2.i, o2.j, o2.k)