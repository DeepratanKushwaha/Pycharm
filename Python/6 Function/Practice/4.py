# convert inches to cms

def cms(inches):
    return inches * 2.54 


value = int(input("Enter value in inches"))
converted = cms(value)
print("value in cms is", converted)
