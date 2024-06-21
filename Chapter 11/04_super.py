class Employee:
    a = 1
    def __init__(self) -> None:
        print("Constructor of Employee")

class Programmer(Employee):
    b = 2
    def __init__(self) -> None:
        print("Constructor of Programmer")

class Manger(Programmer):
    c = 3
    def __init__(self) -> None:
        super().__init__()
        print("Constructor of Manager")


obj = Manger()
print(obj.a, obj.b, obj.c)
