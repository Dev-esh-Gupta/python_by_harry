n = int(input("Enter a Number : "))

for i in range(n, 0, -1):
    for j in range(10, 0, -1):
        print(i*j, end=" ")
    print()