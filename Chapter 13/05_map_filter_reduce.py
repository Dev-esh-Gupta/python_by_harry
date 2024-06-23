# Map Example

from functools import reduce


l = [1,2,3,4,5]

square = lambda x: x*x

sqList = map(square, l)

print(list(sqList))

# Filter Example
def even(n):
    if n%2 == 0:
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))

# Reduce Example
sum = lambda a,b:a+b

red = reduce(sum, l)
print(red)