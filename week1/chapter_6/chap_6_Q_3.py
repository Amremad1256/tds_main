with open("my_file.txt", "a+") as file:
    file.write("\nThis is a new line")
    file.seek(0)  # Move the file pointer to the beginning
    updated_contents = file.read()
    print(updated_contents)