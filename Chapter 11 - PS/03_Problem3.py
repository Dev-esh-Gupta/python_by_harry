class Employees:
    salary = 125000
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary*(self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) - 1)*100    

o = Employees()
o.salaryAfterIncrement = 150000
print(o.increment)