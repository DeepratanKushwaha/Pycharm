try:
    a = int(input("Enter a number: "))
    c = 1/a
    print(c)

except ZeroDivisionError as e:
    print("Make sure you are not dividing by 0")

except ValueError as v:
    print("Please enter a valid number")

except Exception as ex:
    print(ex)

print("Thanks for using this code")
