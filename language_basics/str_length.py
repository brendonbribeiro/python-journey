def str_length(text):
    if type(text) == str:
        return len(text)
    else:
        return "Sorry integers don't have length"


print(str_length("FooBar"))
print(str_length(2))
