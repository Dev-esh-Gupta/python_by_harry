with open("donkey.txt", "r+") as f:
    para = f.read()
    f.seek(0)
    para = para.replace("donkey","#####").replace("Donkey","#####")
    f.write(para)
    f.truncate()
    

