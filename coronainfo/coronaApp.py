from tkinter import *
from tkinter import messagebox, filedialog
import requests
import pandas
from bs4 import BeautifulSoup
import plyer
root = Tk()
root.title('Corona Virus Information')
root.geometry('530x300+200+80')
root.configure(bg='plum2')
root.wm_iconbitmap('corona.ico')


def Scrap():
    def notifyMe(title, message):
       plyer.notification.notify(title=title, message=message, app_icon='corona.ico', timeout=20)

    url = 'https://www.worldometers.info/coronavirus/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    tableBody = soup.find('tbody')
    ttt = tableBody.find_all('tr')
    notifyCountry = countryData.get()
    if notifyCountry == '':
        notifyCountry = 'india'

    countries, total_cases, new_cases, total_deaths, new_deaths, total_recovered, active_cases = [], [], [], [], [], [], []
    serious, totalCases_perMillion, totalDeaths_perMillion, total_tests, totalTests_perMillion = [], [], [], [], []

    headers = ['countries', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_recovered', 'active_cases',
               'serious', 'totalCases_perMillion', 'totalDeaths_perMillion', 'total_tests', 'totalTests_perMillion']

    for i in ttt:
        id = i.find_all('td')
        if id[1].text.strip().lower() == notifyCountry:
            total_cases1 = int(id[2].text.strip().replace(',', ''))
            total_deaths1 = id[4].text.strip()
            new_cases1 = id[3].text.strip()
            new_deaths1 = id[5].text.strip()
            notifyMe(f'Corona Virus Status In {notifyCountry}', f'Total Cases :{total_cases1}\nTotal Deaths :'
                     f'{total_deaths1}\nNew Cases :{new_cases1}\nNew Deaths : {new_deaths1}')

        countries.append(id[1].text.strip())
        total_cases.append(int(id[2].text.strip().replace(',', '')))
        new_cases.append(id[3].text.strip())
        total_deaths.append(id[4].text.strip())
        new_deaths.append(id[5].text.strip())
        total_recovered.append(id[6].text.strip())
        active_cases.append(id[7].text.strip())
        serious.append(id[8].text.strip())
        totalCases_perMillion.append(id[9].text.strip())
        totalDeaths_perMillion.append(id[10].text.strip())
        total_tests.append(id[11].text.strip())
        totalTests_perMillion.append(id[12].text.strip())

    df = pandas.DataFrame(list(zip(countries, total_cases, new_cases, total_deaths, new_deaths, total_recovered,
                                   active_cases, serious, totalCases_perMillion, totalDeaths_perMillion, total_tests,
                                   totalTests_perMillion)))
    sort = df.sort_values('total_cases', axis=0)
    for k in formatList:
        if k == 'html':
            path2 = '{}/alldata.html'.format(path)
            sort.to_html(r'{}'.format(path2))

        if k == 'json':
            path2 = '{}/alldata.json'.format(path)
            sort.to_json(r'{}'.format(path2))

        if k == 'csv':
            path2 = '{}/alldata.csv'.format(path)
            sort.to_csv(r'{}'.format(path2))
    if len(formatList) != 0:
        messagebox.showinfo('Notification', 'Record Is Saved{}'.format(path2), parent=root)


formatList = []


def html():
    formatList.append('html')
    InHtml.configure(state='disabled')


def json():
    formatList.append('json')
    InJson.configure(state='disabled')


def csv():
    formatList.append('csv')
    InCsv.configure(state='disabled')


path = ''


def download():
    global path
    if len(formatList) != 0:
        path = filedialog.askdirectory()
    else:
        pass
    Scrap()
    formatList.clear()
    InHtml.configure(state='normal')
    InJson.configure(state='normal')
    InCsv.configure(state='normal')


# Labels

IntroLabel = Label(root, text='Corona Virus Info', font="newroman 30 italic bold", bg='blue', width=22)
IntroLabel.place(x=0, y=0)

EntryLabel = Label(root, text='Notify Country :', font="arial 20 italic bold", bg='plum2')
EntryLabel.place(x=10, y=70)

FormatLabel = Label(root, text="Download In :", font="arial 20 italic bold", bg='plum2')
FormatLabel.place(x=10, y=150)

# Entry

countryData = StringVar()
entry1 = Entry(root, textvariable=countryData, font="arial 20 italic bold", relief=RIDGE, width=20)
entry1.place(x=220, y=70)

# buttons

InHtml = Button(root, text='Html', bg='green', font='arial 15 italic bold', relief=RIDGE, activebackground='blue',
                activeforeground='white', bd=5, width=5, command=html)
InHtml.place(x=210, y=150)

InJson = Button(root, text='Json', bg='green', font='arial 15 italic bold', relief=RIDGE, activebackground='blue',
                activeforeground='white', bd=5, width=5, command=json)
InJson.place(x=320, y=150)

InCsv = Button(root, text='Csv', bg='green', font='arial 15 italic bold', relief=RIDGE, activebackground='blue',
               activeforeground='white', bd=5, width=5, command=csv)
InCsv.place(x=430, y=150)

Submit = Button(root, text='Submit', bg='red', font="arial 15 italic bold", relief=RIDGE, activebackground='blue',
                activeforeground='white', bd=5, width=25, command=download)
Submit.place(x=110, y=230)


root.mainloop()
