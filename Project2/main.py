import random

chance = 5
random_number = random.randint(1, 100)
is_win = False

while chance > 0:
    guess = int(input("Guess Number between 1 to 100 : "))
    chance -= 1

    if guess == random_number:
        print("Hurray! You won as you guessed right Number")
        print(f"Your Score : {chance+1}")
        is_win = True
        break
    elif guess > random_number:
        print("Too High!")
        print(f"Chance left : {chance}")
    elif guess < random_number:
        print("Too Low!")
        print(f"Chance Left : {chance}")


if not is_win:
    print("Sorry! You Loose the battle")