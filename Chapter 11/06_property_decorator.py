class Employee:
    a = 1
    @classmethod  # It won't allow instance to change clss value
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    

    @name.setter
    def name(self, value):
        self.fname = value.split()[0]
        self.lname = value.split()[1]


obj = Employee()
obj.name = "Devesh Gupta"

print(obj.fname, obj.lname)
print(obj.name)