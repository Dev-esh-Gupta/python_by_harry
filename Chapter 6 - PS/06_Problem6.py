mark = int(input("Enter your overall marks out of 500 : "))

percentage = mark/5

if percentage > 90:
    print("Your grade is Ex")
elif percentage > 80:
    print("Your grade is A")
elif percentage > 70:
    print("Your grade is B")
elif percentage > 60:
    print("Your grade is C")
elif percentage > 50:
    print("Your grade is A")
else: 
    print("Sorry! You are fail")