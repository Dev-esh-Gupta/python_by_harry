import os

current_file = "that.txt"
renamed_file = "this.txt"

os.rename(current_file, renamed_file)

print("File has been renamed")