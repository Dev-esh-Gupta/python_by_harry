import os

# specify the directory path
path = "/Users"

# list the contents of the directory
contents = os.listdir(path)

# print the contents
for content in contents:
    print(content)
