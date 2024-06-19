class Employee:
    language = "Python" # these are class attribute
    salary = 1500000

dev = Employee()
# this one is called object attribute
dev.salary = 4500000 # it overtake class attribute value as it exist there
print(dev.language, dev.salary)

seema = Employee()
print(seema.salary)