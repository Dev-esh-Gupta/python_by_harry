import random

class Train:
    
    def book_ticket(self, name):
        self.name = name
        self.fare = random.randint(150, 350)
        self.status = random.choice(["Confirmed", "Waiting", "RAC"])

    def get_info(self):
        print(f"Hey! {self.name} \nYour ticket Fare is {self.fare}\nAnd your seat status is {self.status}")


passenger1 = Train()

passenger1.book_ticket("Devesh Gupta")

passenger1.get_info()