file = open("fruits.txt")
content = file.read()

print(content)

file.seek(0)

lines = file.readlines()
lines = [i.rstrip("\n") for i in lines]
for line in lines:
    line = line.rstrip("\n")
    print(line + " - ", str(len(line)))

file.close()
