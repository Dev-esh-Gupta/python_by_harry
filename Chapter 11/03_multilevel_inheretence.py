class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manger(Programmer):
    c = 3

obj = Manger()
print(obj.c)
print(obj.b)
print(obj.a)