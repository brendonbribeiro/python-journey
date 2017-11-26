from datetime import datetime
def read_file(file_name):
    with open(file_name) as file:
        return file.read()

file_names = ["content_1.txt", "content_2.txt", "content_3.txt"]
file_contents = []
for file_name in file_names:
    file_contents.append(read_file(file_name))

date_now = datetime.now()
merged_file_name = date_now.strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt"

with open(merged_file_name, "w") as merged_file:
    merged_file.writelines(file_contents)
