from tkinter import *
from tkinter import Text
import tkinter  as tk
from tkinter import messagebox
from tkinter.font import Font
import requests



def weather_data():
    api_key = "a4673e62937015fbbf7b968cfbf0a0ce"
    city = location_erea.get()

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
    response = requests.get(url)

    data= response.json()

    Temperature = data['main']['temp']

    humutid = data['main']["humidity"]

    wind_speeeed= data['wind']['speed']

    pressure = data['main']['pressure']
    
    precipetation = 0
    if 'rain' in data:
        precipetation = data['rain'].get('1h', 0)  
    elif 'snow' in data:
        precipetation = data['snow'].get('1h', 0)  

    lab_tepr.config(text=f"Temperature: {Temperature}°C")
    Humidity.config(text=f"Humidity: {humutid}%")
    Wind_Speed.config(text=f"Wind Speed: {wind_speeeed} KM/H")
    Pressure.config(text=f"Pressure: {pressure} hPa")
    Precipitation.config(text=f"pricipitation : {precipetation} % ")
        
    
     
window = tk.Tk()
window.title("  برنامج  عثـمان  للاحوال الجوية  ")
window.geometry("570x400")

fram = tk.Frame(window)
fram.pack(pady=20, padx=20)


sereach_button = tk.Button(window,text="Search", font=35,command=weather_data)
sereach_button.pack()

labol_loc_erea= tk.Label(fram,text="location", bg="#00FF00",font=("Arial", 20))
labol_loc_erea.pack(side=tk.LEFT, pady=10,padx=10)

location_erea = tk.Entry(fram)
location_erea.pack(side=tk.LEFT,pady=10,padx=20)


lab_tepr= tk.Label(window,text=f"Temperature: °C",font=25 ,bg="gray")
lab_tepr.pack(padx=10 ,pady=15,anchor="nw")

Humidity= tk.Label(window,text=f"Humidity :  % ",font=25 ,bg="gray",)
Humidity.pack(padx=10 ,pady=15,anchor="nw")

Wind_Speed= tk.Label(window,text=f"Wind Speed :  KM/H",font=25 ,bg="gray")
Wind_Speed.pack(padx=10 ,pady=15,anchor="nw")

Pressure= tk.Label(window,text=f"Pressure :  hPa",font=25 ,bg="gray")
Pressure.pack(padx=10 ,pady=15,anchor="nw")

Precipitation= tk.Label(window,text="Precipitation : ",font=25 ,bg="gray")
Precipitation.pack(padx=10 ,pady=15,anchor="nw")


window.mainloop()