class Vector:
    def __init__(self, l):
        self.l = l

    
    def __len__(self):
        return len(self.l)
    

# Testing of implimentation
v1 = Vector([1, 3, 4])
print(len(v1))
