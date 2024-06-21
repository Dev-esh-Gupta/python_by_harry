class Employee:
    a = 1
    @classmethod  # It won't allow instance to change clss value
    def show(cls):
        print(f"The class attribute of a is {cls.a}")


obj = Employee()
obj.a = 5 #it changes the value of a 

obj.show()