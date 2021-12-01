# finally block
# means guaranteed execution
# in the finally block we will write    like close the file and closing the database connection

num = input("Enter non zero value:")
try:
    i = int(num)
    print("i is:", i)
    print("we are in try block")
except Exception as ve:
    print("-----------------")
    print(ve)
    print("---------------------")
finally:
    print("we are in finally block")

print("end of program")
