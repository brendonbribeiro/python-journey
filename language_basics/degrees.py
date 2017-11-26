"""
Trying some cool documentation
"""

def celsius_to_fahrenheit(celsius):
    """
    This funcion converts celsius to fahrenheit (C * 9/5 + 32)
    """
    return celsius * 9/5 + 32

celsius = float(input("Celsius degree: "))
if celsius >= -273.15:
    print(celsius_to_fahrenheit(celsius))
else:
    print("Too cooooold")
