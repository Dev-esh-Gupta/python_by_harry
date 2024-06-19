with open("definition.txt") as f:
    data = f.read()
    if "Python".lower() in data.lower():
        print("Yes Log contain text Python")
    else:
        print("Log doesn't contain text Python")