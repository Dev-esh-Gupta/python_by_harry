num = int(input("Enter a Number whose factorial you want to calculate : "))

fact = 1

while num != 0:
    fact *= num
    num -= 1

print("Factorial of a number : ", fact)