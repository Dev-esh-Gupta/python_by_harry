class Programmer:
    company = "Microsoft"
    def __init__(self, name, age, salary, post):
        self.name = name
        self.age = age
        self.salary = salary
        self.post = post

    def get_info(self):
        print(f"Hey! {self.name}, I am aware you are {self.age} years old. And Earning {self.salary} at {self.company} office\n and your post is {self.post}")


programmer1 = Programmer("Devesh Gupta", 25, 2500000, "Software Engineer")
programmer1.get_info()