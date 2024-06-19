class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        return self.num**2
    
    def cube(self):
        return self.num**3
    
    def square_root(self):
        return self.num**(1/2)
    
    @staticmethod
    def greet():
        print("Hello")
    

calci = Calculator(5)
calci.greet()
print(calci.square())
print(calci.cube())
print(calci.square_root())