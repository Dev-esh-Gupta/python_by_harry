

from typing import List, Tuple, Dict, Union


n = 5

print(n)

n = "Hello"

print(n)

m : int = 4

print(m)

m = "Hi"

print(m)

def sum(a : int, b : int) -> int:
    return a + b

print(sum(13, 767))

numbers : List[int] = [1, 3, 4, 6, 12]
print(numbers)

person : Tuple[str, int] = ("Devesh", 25)
print(person)


score : Dict[str, int] = {"Devesh" : 96, "Ravi" : 77}
print(score)