with open("this.txt") as f:
    data = f.read()

with open("that.txt", "w") as f:
    f.write(data)