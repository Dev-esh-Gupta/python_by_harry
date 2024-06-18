message = input("Please Enter the comment message : ")

if message.find("Make a lot of money") or message.find("buy now") or message.find("subscribe this") or \
    message.find("click this"):
    print("Entered Comment is spam comment")
else:
    print("Entered comment is valid comment")