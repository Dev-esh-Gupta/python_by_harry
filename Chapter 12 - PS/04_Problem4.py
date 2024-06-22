a = int(input("Enter a number : "))
b = int(input("Enter a second number : "))

try:
    result = a/b
    print(result)
except ZeroDivisionError as z:
    print("Infinite")
    # print(z)