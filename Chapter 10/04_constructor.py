class Employee:
    language = "Python" # these are class attribute
    salary = 1500000

    def __init__(self, name, salary, language): # it is donder method which is automatically called when object created
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def get_info(self):
        print(f"The language is {self.language} and salary is {self.salary}")

    #static method doesn't required that self argument
    @staticmethod #it is decorator
    def greet():
        print("Good Morning Sir!")

dev = Employee("Devesh", 1600000, "JavaScript")
# dev.salary = 1524000
dev.get_info()
dev.greet()