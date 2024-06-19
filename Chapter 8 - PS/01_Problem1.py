def maxi(a, b):
    if a > b:
        return a
    else:
        return b
    

num1 = input("Enter Number 1 : ")
num2 = input("Enter Number 2 : ")
num3 = input("Enter Number 3 : ")

max_number = maxi(maxi(num1, num2), num3)

print("Max Number " + max_number)