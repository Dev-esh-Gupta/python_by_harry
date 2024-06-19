import random

'''
1 for snake
-1 for water
0 for gun
'''

random_number = random.choice([0, 1, -1])
computer = random_number
print("s for snake \nw for water\ng for gun")
you = input("Enter your choice: ")
youDict = {"s" : 1, "w" : -1, "g" : 0}
reverse_dict = {1 : "Snake", -1 : "Water", 0 : "Gun"}
younum = youDict[you]

print(f"You have choosen {reverse_dict[younum]} and Computer choosen {reverse_dict[computer]}")

if computer == younum:
    print("Draw!")

elif computer == -1 and younum == 1:
    print("You win!")

elif computer == -1 and younum == 0:
    print("You Loose!")

elif computer == 1 and younum == -1:
    print("You Loose!")

elif computer == 1 and younum == 0:
    print("You Win!")

elif computer == 0 and younum == 1:
    print("You Loose!")

elif computer == 0 and younum == -1:
    print("You Win!")

else:
    print("Something went wrong!")