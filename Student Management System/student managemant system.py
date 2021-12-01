from tkinter import *
import time
import random
from tkinter import Toplevel
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Treeview
import pymysql


root = Tk()
root.title("Student Management System")
root.geometry('1250x650+90+20')
root.config(bg='gold2')
# root.iconbitmap()
root.resizable(False, False)


def ClockTime():
    time_string = time.strftime('%H:%M:%S')
    date_string = time.strftime('%d/%m/%y')
    ClockLabel.config(text='Date :' + date_string + '\n' + 'Time :' + time_string)
    ClockLabel.after(200, ClockTime)


def IntroLabel():
    global count, text
    if count >= len(slideText):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text + slideText[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(200, IntroLabel)


colors = ['red', 'green', 'blue', 'yellow', 'pink', 'red2', 'gold2']


def IntroLabelColor():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(2, IntroLabelColor)


# functions for buttons inside data entry frame
def addStudent():
    def submitAdd():
        id = idVar.get()
        name = nameVar.get()
        mobile = mobileVar.get()
        email = emailVar.get()
        address = addressVar.get()
        gender = genderVar.get()
        dob = dobVar.get()
        addedTime = time.strftime('%H:%M:%S')
        addedDate = time.strftime('%d:%m:%y')
        try:
            strr = 'insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            myCursor.execute(strr, (id, name, mobile, email, address, gender, dob, addedTime, addedDate))
            con.commit()
            res = messagebox.askyesnocancel('Notification', 'ID {} NAME {} Added successfully... and want to clean the form'.format(id, name))
            if res:
                idVar.set('')
                nameVar.set('')
                mobileVar.set('')
                emailVar.set('')
                addressVar.set('')
                genderVar.set('')
                dobVar.set('')
        except:
            messagebox.showerror('Notification', 'Id already exists, try another id', parent=addRoot)

    addRoot = Toplevel(master=DataEntryFrame)
    addRoot.grab_set()
    addRoot.geometry('470x470+220+170')
    addRoot.title('Student Management System')
    addRoot.config(bg='powder blue')
    addRoot.resizable(0, 0)

    idLabel = Label(addRoot, text='Enter ID : ', bg='gold2', font='times 20 bold', relief=GROOVE, borderwidth=3,
                    width=14, anchor=W)
    idLabel.place(x=10, y=10)

    nameLabel = Label(addRoot, text='Enter Name : ', bg='gold2', font='times 20 bold', relief=GROOVE, borderwidth=3,
                      width=14, anchor=W)
    nameLabel.place(x=10, y=70)

    mobileLabel = Label(addRoot, text='Enter Mobile No. : ', bg='gold2', font='times 20 bold', relief=GROOVE,
                        borderwidth=3, width=14, anchor=W)
    mobileLabel.place(x=10, y=130)

    emailLabel = Label(addRoot, text='Enter Email : ', bg='gold2', font='times 20 bold', relief=GROOVE, borderwidth=3,
                       width=14, anchor=W)
    emailLabel.place(x=10, y=190)

    addressLabel = Label(addRoot, text='Enter Address : ', bg='gold2', font='times 20 bold', relief=GROOVE,
                         borderwidth=3,
                         width=14, anchor=W)
    addressLabel.place(x=10, y=250)

    genderLabel = Label(addRoot, text='Enter Gender : ', bg='gold2', font='times 20 bold', relief=GROOVE, borderwidth=3,
                        width=14, anchor=W)
    genderLabel.place(x=10, y=310)

    dobLabel = Label(addRoot, text='Enter D.O.B. : ', bg='gold2', font='times 20 bold', relief=GROOVE, borderwidth=3,
                     width=14, anchor=W)
    dobLabel.place(x=10, y=370)

    idVar = StringVar()
    idEntry = Entry(addRoot, font='roman 15 bold', bd=5, textvariable=idVar)
    idEntry.place(x=250, y=10)

    nameVar = StringVar()
    nameEntry = Entry(addRoot, font='roman 15 bold', bd=5, textvariable=nameVar)
    nameEntry.place(x=250, y=70)

    mobileVar = StringVar()
    mobileEntry = Entry(addRoot, font='roman 15 bold', bd=5, textvariable=mobileVar)
    mobileEntry.place(x=250, y=130)

    emailVar = StringVar()
    emailEntry = Entry(addRoot, font='roman 15 bold', bd=5, textvariable=emailVar)
    emailEntry.place(x=250, y=190)

    addressVar = StringVar()
    addressEntry = Entry(addRoot, font='roman 15 bold', bd=5, textvariable=addressVar)
    addressEntry.place(x=250, y=250)

    genderVar = StringVar()
    genderEntry = Entry(addRoot, font='roman 15 bold', bd=5, textvariable=genderVar)
    genderEntry.place(x=250, y=310)

    dobVar = StringVar()
    dobEntry = Entry(addRoot, font='roman 15 bold', bd=5, textvariable=dobVar)
    dobEntry.place(x=250, y=370)

    addStdBtn = Button(addRoot, text='Submit', font='roman 15 bold', bd=5, width=20, activebackground='blue',
                       activeforeground='white', command=submitAdd)
    addStdBtn.place(x=140, y=420)
    addRoot.mainloop()


def searchStudent():
    def submitSearch():
        pass
    searchRoot = Toplevel(master=DataEntryFrame)
    searchRoot.grab_set()
    searchRoot.geometry('470x530+220+150')
    searchRoot.title('Student Management System')
    searchRoot.config(bg='powder blue')
    searchRoot.resizable(0, 0)

    idLabel = Label(searchRoot, text='Enter ID : ', bg='gold2', font='times 20 bold', relief=GROOVE, borderwidth=3,
                    width=14, anchor=W)
    idLabel.place(x=10, y=10)

    nameLabel = Label(searchRoot, text='Enter Name : ', bg='gold2', font='times 20 bold', relief=GROOVE, borderwidth=3,
                      width=14, anchor=W)
    nameLabel.place(x=10, y=70)

    mobileLabel = Label(searchRoot, text='Enter Mobile No. : ', bg='gold2', font='times 20 bold', relief=GROOVE,
                        borderwidth=3, width=14, anchor=W)
    mobileLabel.place(x=10, y=130)

    emailLabel = Label(searchRoot, text='Enter Email : ', bg='gold2', font='times 20 bold', relief=GROOVE,
                       borderwidth=3, width=14, anchor=W)
    emailLabel.place(x=10, y=190)

    addressLabel = Label(searchRoot, text='Enter Address : ', bg='gold2', font='times 20 bold', relief=GROOVE,
                         borderwidth=3,
                         width=14, anchor=W)
    addressLabel.place(x=10, y=250)

    genderLabel = Label(searchRoot, text='Enter Gender : ', bg='gold2', font='times 20 bold', relief=GROOVE,
                        borderwidth=3, width=14, anchor=W)
    genderLabel.place(x=10, y=310)

    dobLabel = Label(searchRoot, text='Enter D.O.B. : ', bg='gold2', font='times 20 bold', relief=GROOVE, borderwidth=3,
                     width=14, anchor=W)
    dobLabel.place(x=10, y=370)

    dateLabel = Label(searchRoot, text='Enter Date : ', bg='gold2', font='times 20 bold', relief=GROOVE,
                      borderwidth=3, width=14, anchor=W)
    dateLabel.place(x=10, y=430)

    idVar = StringVar()
    idEntry = Entry(searchRoot, font='roman 15 bold', bd=5, textvariable=idVar)
    idEntry.place(x=250, y=10)

    nameVar = StringVar()
    nameEntry = Entry(searchRoot, font='roman 15 bold', bd=5, textvariable=nameVar)
    nameEntry.place(x=250, y=70)

    mobileVar = StringVar()
    mobileEntry = Entry(searchRoot, font='roman 15 bold', bd=5, textvariable=mobileVar)
    mobileEntry.place(x=250, y=130)

    emailVar = StringVar()
    emailEntry = Entry(searchRoot, font='roman 15 bold', bd=5, textvariable=emailVar)
    emailEntry.place(x=250, y=190)

    addressVar = StringVar()
    addressEntry = Entry(searchRoot, font='roman 15 bold', bd=5, textvariable=addressVar)
    addressEntry.place(x=250, y=250)

    genderVar = StringVar()
    genderEntry = Entry(searchRoot, font='roman 15 bold', bd=5, textvariable=genderVar)
    genderEntry.place(x=250, y=310)

    dobVar = StringVar()
    dobEntry = Entry(searchRoot, font='roman 15 bold', bd=5, textvariable=dobVar)
    dobEntry.place(x=250, y=370)

    dateVar = StringVar()
    dateEntry = Entry(searchRoot, font='roman 15 bold', bd=5, textvariable=dateVar)
    dateEntry.place(x=250, y=430)

    searchStdBtn = Button(searchRoot, text='Submit', font='roman 15 bold', bd=5, width=20, activebackground='blue',
                          activeforeground='white', command=submitSearch)
    searchStdBtn.place(x=140, y=480)

    searchRoot.mainloop()


def deleteStudent():
    pass


def updateStudent():
    def submitUpdate():
        pass
    updateRoot = Toplevel(master=DataEntryFrame)
    updateRoot.grab_set()
    updateRoot.geometry('470x590+220+90')
    updateRoot.title('Student Management System')
    updateRoot.config(bg='powder blue')
    updateRoot.resizable(0, 0)

    idLabel = Label(updateRoot, text='Enter ID : ', bg='gold2', font='times 20 bold', relief=GROOVE, borderwidth=3,
                    width=14, anchor=W)
    idLabel.place(x=10, y=10)

    nameLabel = Label(updateRoot, text='Enter Name : ', bg='gold2', font='times 20 bold', relief=GROOVE, borderwidth=3,
                      width=14, anchor=W)
    nameLabel.place(x=10, y=70)

    mobileLabel = Label(updateRoot, text='Enter Mobile No. : ', bg='gold2', font='times 20 bold', relief=GROOVE,
                        borderwidth=3, width=14, anchor=W)
    mobileLabel.place(x=10, y=130)

    emailLabel = Label(updateRoot, text='Enter Email : ', bg='gold2', font='times 20 bold', relief=GROOVE,
                       borderwidth=3, width=14, anchor=W)
    emailLabel.place(x=10, y=190)

    addressLabel = Label(updateRoot, text='Enter Address : ', bg='gold2', font='times 20 bold', relief=GROOVE,
                         borderwidth=3, width=14, anchor=W)
    addressLabel.place(x=10, y=250)

    genderLabel = Label(updateRoot, text='Enter Gender : ', bg='gold2', font='times 20 bold', relief=GROOVE,
                        borderwidth=3, width=14, anchor=W)
    genderLabel.place(x=10, y=310)

    dobLabel = Label(updateRoot, text='Enter D.O.B. : ', bg='gold2', font='times 20 bold', relief=GROOVE, borderwidth=3,
                     width=14, anchor=W)
    dobLabel.place(x=10, y=370)

    dateLabel = Label(updateRoot, text='Enter Date : ', bg='gold2', font='times 20 bold', relief=GROOVE,
                      borderwidth=3, width=14, anchor=W)
    dateLabel.place(x=10, y=430)

    timeLabel = Label(updateRoot, text='Enter Time : ', bg='gold2', font='times 20 bold', relief=GROOVE,
                      borderwidth=3, width=14, anchor=W)
    timeLabel.place(x=10, y=490)

    idVar = StringVar()
    idEntry = Entry(updateRoot, font='roman 15 bold', bd=5, textvariable=idVar)
    idEntry.place(x=250, y=10)

    nameVar = StringVar()
    nameEntry = Entry(updateRoot, font='roman 15 bold', bd=5, textvariable=nameVar)
    nameEntry.place(x=250, y=70)

    mobileVar = StringVar()
    mobileEntry = Entry(updateRoot, font='roman 15 bold', bd=5, textvariable=mobileVar)
    mobileEntry.place(x=250, y=130)

    emailVar = StringVar()
    emailEntry = Entry(updateRoot, font='roman 15 bold', bd=5, textvariable=emailVar)
    emailEntry.place(x=250, y=190)

    addressVar = StringVar()
    addressEntry = Entry(updateRoot, font='roman 15 bold', bd=5, textvariable=addressVar)
    addressEntry.place(x=250, y=250)

    genderVar = StringVar()
    genderEntry = Entry(updateRoot, font='roman 15 bold', bd=5, textvariable=genderVar)
    genderEntry.place(x=250, y=310)

    dobVar = StringVar()
    dobEntry = Entry(updateRoot, font='roman 15 bold', bd=5, textvariable=dobVar)
    dobEntry.place(x=250, y=370)

    dateVar = StringVar()
    dateEntry = Entry(updateRoot, font='roman 15 bold', bd=5, textvariable=dateVar)
    dateEntry.place(x=250, y=430)

    timeVar = StringVar()
    timeEntry = Entry(updateRoot, font='roman 15 bold', bd=5, textvariable=timeVar)
    timeEntry.place(x=250, y=490)

    updateStdBtn = Button(updateRoot, text='Submit', font='roman 15 bold', bd=5, width=20, activebackground='blue',
                          activeforeground='white', command=submitUpdate)
    updateStdBtn.place(x=140, y=540)

    updateRoot.mainloop()


def showStudent():
    pass


def exportStudent():
    pass


def exitStudent():
    res = messagebox.askyesno('Notification', 'Do you want to exit')
    if res:
        root.destroy()


# function for database button
def connectDb():
    def submitDb():
        global con, myCursor
        host = hostVar.get()
        user = userVar.get()
        password = passwordVar.get()
        try:
            con = pymysql.connect(host=host, user=user, password=password)
            myCursor = con.cursor()

        except:
            messagebox.showerror('Notification', 'Data is incorrect, please try again')
            return
        try:
            strr = 'create database studentmanagementsystem'
            myCursor.execute(strr)
            strr = 'use studentmanagementsystem'
            myCursor.execute(strr)
            strr = 'create table studentdata(id int, name varchar(20), mobile varchar(12), email varchar(30), ' \
                   'address varchar(100), gender varchar(50), dob varchar(50), time varchar(50))'
            myCursor.execute(strr)
            strr = 'alter table studentdata modify column id int not null'
            myCursor.execute(strr)

            strr = 'alter table studentdata modify column id int primary key'
            myCursor.execute(strr)
            messagebox.showinfo('Notification', 'database created and now you are connected to the database...', parent=rootDb)
        except:
            strr = 'use studentmanagementsystem'
            myCursor.execute(strr)
            messagebox.showinfo('Notification', 'Now you are connected to the database...', parent=rootDb)
        rootDb.destroy()

    rootDb = Toplevel()
    rootDb.grab_set()
    rootDb.geometry('470x250+800+230')
    rootDb.resizable(False, False)
    rootDb.config(bg='powder blue')

    # connect labels
    hostLabel = Label(rootDb, text='Enter Host : ', bg='gold2', font='times 18 bold', relief=GROOVE, borderwidth=3,
                      width=13, anchor=W)
    hostLabel.place(x=10, y=10)

    userLabel = Label(rootDb, text='Enter User : ', bg='gold2', font='times 18 bold', relief=GROOVE, borderwidth=3,
                      width=13, anchor=W)
    userLabel.place(x=10, y=70)

    passwordLabel = Label(rootDb, text='Enter Password : ', bg='gold2', font='times 18 bold', relief=GROOVE,
                          borderwidth=3, width=13, anchor=W)
    passwordLabel.place(x=10, y=130)

    # connect labels entry
    hostVar = StringVar()
    hostEntry = Entry(rootDb, textvariable=hostVar, font='roman 15 bold', bd=5)
    hostEntry.place(x=250, y=10)

    userVar = StringVar()
    userEntry = Entry(rootDb, textvariable=userVar, font='roman 15 bold', bd=5)
    userEntry.place(x=250, y=70)

    passwordVar = StringVar()
    passwordEntry = Entry(rootDb, textvariable=passwordVar, font='roman 15 bold', bd=5)
    passwordEntry.place(x=250, y=130)

    # submit button
    submitButton = Button(rootDb, text='Submit', font='roman 15 bold', bg='red', width=20,
                          activebackground='blue', activeforeground='white', command=submitDb)
    submitButton.place(x=150, y=180)
    rootDb.mainloop()


# creating data entry frame
DataEntryFrame = Frame(root, bg='gold2', relief=GROOVE, borderwidth=5)
DataEntryFrame.place(x=10, y=80, width=500, height=550)

# creating label & button inside data entry frame
frontLabel = Label(DataEntryFrame, text='--------------------Welcome--------------------', width=30,
                   font='arial 20 bold', bg='gold2')
frontLabel.pack(side=TOP, expand=True)

addBtn = Button(DataEntryFrame, text='1. Add Student', width=25, font='roman 20 bold', bd=6, bg='skyblue3',
                activebackground='blue', activeforeground='white', relief=RIDGE, command=addStudent)
addBtn.pack(side=TOP, expand=True)

searchBtn = Button(DataEntryFrame, text='2. Search Student', width=25, font='roman 20 bold', bd=6, bg='skyblue3',
                   activebackground='blue', activeforeground='white', relief=RIDGE, command=searchStudent)
searchBtn.pack(side=TOP, expand=True)

deleteBtn = Button(DataEntryFrame, text='3. Delete Student', width=25, font='roman 20 bold', bd=6, bg='skyblue3',
                   activebackground='blue', activeforeground='white', relief=RIDGE, command=deleteStudent)
deleteBtn.pack(side=TOP, expand=True)

updateBtn = Button(DataEntryFrame, text='4. Update Student', width=25, font='roman 20 bold', bd=6, bg='skyblue3',
                   activebackground='blue', activeforeground='white', relief=RIDGE, command=updateStudent)
updateBtn.pack(side=TOP, expand=True)

showBtn = Button(DataEntryFrame, text='5. Show All', width=25, font='roman 20 bold', bd=6, bg='skyblue3',
                 activebackground='blue', activeforeground='white', relief=RIDGE, command=showStudent)
showBtn.pack(side=TOP, expand=True)

exportBtn = Button(DataEntryFrame, text='6. Export Data', width=25, font='roman 20 bold', bd=6, bg='skyblue3',
                   activebackground='blue', activeforeground='white', relief=RIDGE, command=exportStudent)
exportBtn.pack(side=TOP, expand=True)

exitBtn = Button(DataEntryFrame, text='7. Exit', width=25, font='roman 20 bold', bd=6, bg='skyblue3',
                 activebackground='blue', activeforeground='white', relief=RIDGE, command=exitStudent)
exitBtn.pack(side=TOP, expand=True)

# creating show data frame
ShowDataFrame = Frame(root, bg='gold2', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=600, y=80, width=642, height=550)

# creating scrollbar inside show data frame
scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)

# creating Tree view in show data frame
studentTable = Treeview(ShowDataFrame, columns=('Id', 'Name', 'Mobile No.', 'Email', 'Address', 'Gender', 'D.O.B.',
                                                'Added Date', 'Added Time'), yscrollcommand=scroll_y.set,
                        xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=studentTable.xview)
scroll_y.config(command=studentTable.yview)

studentTable.heading('Id', text='Id')
studentTable.heading('Name', text='Name')
studentTable.heading('Mobile No.', text='Mobile No.')
studentTable.heading('Email', text='Email')
studentTable.heading('Address', text='Address')
studentTable.heading('Gender', text='Gender')
studentTable.heading('D.O.B.', text='D.O.B.')
studentTable.heading('Added Date', text='Added Date')
studentTable.heading('Added Time', text='Added Time')
studentTable['show'] = 'headings'   # it show only headings and remove index column given by tree view

studentTable.column('Id', width=50)
studentTable.column('Name', width=200)
studentTable.column('Mobile No.', width=170)
studentTable.column('Email', width=300)
studentTable.column('Address', width=100)
studentTable.column('Gender', width=70)
studentTable.column('D.O.B.', width=100)
studentTable.column('Added Date', width=100)
studentTable.column('Added Time', width=100)

#
style = ttk.Style()
style.configure('Treeview.Heading', font='chiller 20 bold', foreground='blue')
style.configure('Treeview', font='times 15 bold', background='cyan', foreground='black')


studentTable.pack(expand=True, fill=BOTH)


# creating slider
slideText = 'Welcome to Student Management System'
count = 0
text = ''
SliderLabel = Label(root, text=slideText, font='chiller 20 italic bold', width=40, borderwidth=4, bg='cyan',
                    relief=RIDGE)
SliderLabel.place(x=400, y=0)
IntroLabel()
IntroLabelColor()

# creating clock label
ClockLabel = Label(root, font='arial 16 bold', borderwidth=4, relief=RIDGE, bg='lawn green')
ClockLabel.place(x=0, y=0)
ClockTime()

# database button
connectButton = Button(root, text='Connect to Database', width=23, font='arial 16 italic bold', relief=RIDGE,
                       borderwidth=4, bg='green2', activebackground='blue', activeforeground='white', command=connectDb)
connectButton.place(x=935, y=0)

root.mainloop()
