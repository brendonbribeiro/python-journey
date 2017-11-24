def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

celsius = float(input("Celsius degree: "))
if celsius >= -273.15:
    print(celsius_to_fahrenheit(celsius))
else:
    print("Too cooooold")
