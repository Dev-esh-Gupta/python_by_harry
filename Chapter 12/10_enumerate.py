l = [3, 232, 124, 56]

# index = 0
# for item in l:
#     print(f"The item number {index} is {item}")
#     index += 1

# This can be simplified using enumerate
for index, item in enumerate(l):
    print(f"The item number {index} is {item}")
    index += 1