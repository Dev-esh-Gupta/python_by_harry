def pattern(n):
    if n == 0:
        return
    else:
        for i in range(n):
            print("*", end=" ")
        print()
        pattern(n-1)


pattern(5)