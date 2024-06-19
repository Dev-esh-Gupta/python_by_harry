class Employee:
    language = "Python" # these are class attribute
    salary = 1500000

dev = Employee()
# this one is called object attribute
dev.name = "Devesh Gupta"
print(dev.language, dev.name)

seema = Employee()
print(seema.salary)