from functools import reduce


a = [234,235,1000,234,54670,215, 65]

def greater(a, b):
    if a>b:
        return a
    return b

print(reduce(greater,a))