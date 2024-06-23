def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [234,235,1000,234,54670,215]

f = list(filter(divisible5, a))
print(f)