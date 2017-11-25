with open("../file_handling/example.txt", "a+") as file:
    file.seek(0)
    lines = file.readlines()
    file.write("Line " + str(len(lines) + 1) + "\n")
