with open("my_file.txt", "r") as file:
    contents = file.read()

with open("copy_of_file.txt", "w") as copy_file:
    copy_file.write(contents)