class Employee:
    language = "Python" # these are class attribute
    salary = 1500000

    def get_info(self):
        print(f"The language is {self.language} and salary is {self.salary}")

    #static method doesn't required that self argument
    @staticmethod #it is decorator
    def greet():
        print("Good Morning Sir!")

dev = Employee()
dev.salary = 1524000
dev.get_info()
dev.greet()