class Employee:
    company = "ITC"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"The name of Employee is {self.name} and the salary is {self.salary}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Your favourite language is {self.language}")
 
class Programmer(Employee, Coder): # it is a way for multiple inheretence
    def __init__(self, name, salary):
        super().__init__(name, salary)

    company = "ITC Infotech"
    def show_language(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee("Devesh Gupta", 1254200)
b = Programmer("Devesh Gupta", 1254200)

print(a.company, b.company)
a.show()
b.printLanguage()
b.show()