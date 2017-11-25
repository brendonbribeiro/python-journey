rgb_colors = ["Red", "Green", "Blue"]
cmyk_colors = ["Cyan", "Magenta", "Yellow", "Black"]

file = open("colors.txt", "w")
file.write("RGB COLORS\n")
for color in rgb_colors:
    file.write(color)
    index = rgb_colors.index(color)
    file.write("\n")
    if index == len(rgb_colors) - 1:
        file.write("\n")

file.write("CMYK COLORS\n")
for color in cmyk_colors:
    file.write(color)
    index = cmyk_colors.index(color)
    if index != len(cmyk_colors) - 1:
        file.write("\n")
