with open("definition.txt") as f:
    line_no = 1
    list_of_presence = []
    line = f.readline()
    while line != "":
        if "Python".lower() in line.lower():
            list_of_presence.append(line_no)
        line = f.readline()
        line_no += 1

print(list_of_presence)