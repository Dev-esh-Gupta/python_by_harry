l = ["Devesh", "Dev", "Mukesh", "Ravi", "Hari"]


def remove_word(word):
    global l
    n = []
    for item in l:
        if not (item == word):
            n.append(item.strip(word))
    return n

word = input("Enter a word to remove : ")
print(remove_word(word))
