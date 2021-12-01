import time


def f1():
    print("f1 method called")
    for i in range(5):
        time.sleep(0.5)
        print("i is:", i)


def f2():
    print("f2 method is called")
    for j in range(5):
        time.sleep(0.5)
        print("j is:", j)


t = time.time()
f1()
print("--------------------------")
f2()

print("total time taken:", time.time()-t)
print("end of program")