def div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return 0

print(div(1, 0))
print(div(6, 3))
