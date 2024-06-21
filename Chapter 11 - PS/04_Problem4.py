class Complex:
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def show(self):
        print(f"{self.real} + {self.image}i")

    def __add__(self, num):
        self.real = self.real + num.real
        self.image = self.image + num.image
        return f"{self.real} + {self.image}i" 
    
    def __mul__(self, num):
        self.new_real = self.real*num.real - self.image*num.image
        self.new_image = self.real*num.image + self.image*num.real
        return f"{self.new_real} + {self.new_image}i"
    


num1 = Complex(3, 4)
num1.show()
num2 = Complex(7, 2)
num2.show()

print(num1 + num2)
print(num1 * num2)
num1.show()
num2.show()
