class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        return self.num**2
    
    def cube(self):
        return self.num**3
    
    def square_root(self):
        return self.num**(1/2)
    

calci = Calculator(5)
print(calci.square())
print(calci.cube())
print(calci.square_root())