# celsius to fahrenheit using function

def fahrenheit(celsius):
    return (celsius * (9/5)) + 32


temp = int(input("Enter temperature in celsius"))
converted = fahrenheit(temp)
print("Temperature in fahrenheit is", converted)
