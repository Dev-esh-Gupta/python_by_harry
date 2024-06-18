message = input("Please Enter the comment message : ")

if (message.find("Make a lot of money") == -1) and (message.find("buy now") == -1) and (message.find("subscribe this") == -1) and (message.find("click this") == -1):
    print("Entered Comment is valid comment")
else:
    print("Entered comment is spam comment")


print(type(message.find("Make a lot of money")))