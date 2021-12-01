try:
    obj = open("a.txt", 'r')
    obj.close()
except FileNotFoundError as e:
    print(e)
    
print("end of program")