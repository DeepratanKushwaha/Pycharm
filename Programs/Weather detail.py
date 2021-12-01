
import tkinter as tk
import requests
import json

win = tk.Tk()
win.title("weather")
win.geometry("500x500")

api = ""
url = "http://api.openweathermap.org"

def weather():
     location = entry.get()
     answer = url + "appid=0c2171fd387885b097b178ebc27611bd" + "" + location
     response = requests.get(answer)
     res = response.json()
     if res["cod"] != "404" :
         x = res["main"]
         temprature = x["temp"]
         pressure = x["pressure"]
         humidity = x["humidilty"]
         y = res["weather"]
         weather_description = y[0]["description"]
         label1 = tk.Label(win, text=f'Temprature(in kelvin unit) = {temp} ,\n'
                                     f'atmospheric pressure(in hPa unit) = {pre} ,\n'
                                     f'humadity(in percentage) = {hum} ,\n'   
                                     f'description = {weather_description}')
         label1.grid(row=2, column=0)
     else:
         label2 = tk.Label(win, text="Enter correct city")
         label2.grid(row=2, column=0)

     label = tk.Label(win,text="Enter City Name Here :", bg='#add8e6')
     label.grid(row=0, column=0)
     label.config(font=("times", 20, "bold"))

     entry = tk.Entry(win)
     entry.grid(row=1, column=1)

     button = tk.Button(win, text="Search", command=weather)
     button.grid(row=1, column=1)

     win.mainloop()
