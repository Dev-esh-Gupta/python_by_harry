for i in range(100):
    if i == 12:
        break
    print(i)
else:
    print("DOne") # as loop didn't completed due to break statement so else won't be executed


for i in range(10):
    if i == 4:
        continue
    print(i)