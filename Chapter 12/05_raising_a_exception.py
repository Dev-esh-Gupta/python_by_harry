a = int(input("Enter a number :"))
b = int(input("Enter a second number :"))

if(b == 0):
    raise ZeroDivisionError("Hey this program is not meant to divide by zero")
else:
    print(f"The Division a/b is {a/b}")

print("Thank you")