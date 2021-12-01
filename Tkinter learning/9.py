from tkinter import *


def getvals():
    print("Submitting form")
    print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}")

    with open("records.txt", 'a') as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}\n")


root = Tk()
root.geometry("655x333")

# heading
Label(root, text="Welcome to Jai Travels", font="comicsansms 12 bold", pady=15).grid(row=0, column=3)
# text for a form
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency Contact")
paymentmode = Label(root, text="Payment Mode")

# pack texts for our forms
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

# tkinter variable for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

# Entries for our forms
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue)

# packing entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)

# checkbox
foodservice = Checkbutton(text="Want to prebook your meal?", variable=foodservicevalue)
foodservice.grid(row=6, column=3)

# button & packing it and assigning it a command
Button(text="Submit to Jai Travels", command=getvals).grid(row=7, column=3)


root.mainloop()
