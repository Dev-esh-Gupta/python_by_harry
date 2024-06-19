class Check:
    a = 5


obj = Check()

print(obj.a)
obj.a = 8
print(obj.a)
print(Check.a) #class attribute won't change