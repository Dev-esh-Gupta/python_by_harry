def game():
    score = int(input("Enter a score : "))
    update(score)

def update(score):
    with open("Hi_Score.txt") as f:
        hi_score = int(f.read())
    
    if hi_score < score:
        with open("Hi_Score.txt", "w") as f:
            f.write(str(score))


game()