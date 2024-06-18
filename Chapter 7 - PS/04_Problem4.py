number = int(input("Enter a number : "))

for i in range(2, int(number**(1/2))+1):
    if number%i == 0:
        print("Entered Number is not a Prime number")
        break
else:
    print("Entered Number is a Prime Number")