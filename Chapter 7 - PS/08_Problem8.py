n = int(input("Enter Value of : "))

star = 1

while n:
    for i in range(star):
        print("*", end="")
        
    print()
    star += 1
    n -= 1