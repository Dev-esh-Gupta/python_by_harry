with open("poems.txt") as f:
    data = f.read()
    if "Tata" in data:
        print("Yes text Contain the Word \"Twinkle\"")
    else:
        print("Not Present")