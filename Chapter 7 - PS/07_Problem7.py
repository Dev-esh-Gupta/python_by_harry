n = int(input("Enter Value of : "))

star = 1
gap = n - 1

while n:
    print(" "*gap, end="")

    print("*"*star, end="")

    print()
    star += 2
    gap -= 1
    n -= 1