import tkinter as tk
from tkinter import *
import time
from numpy import size 
import requests
from PIL import ImageTk, Image
from platform import system

platformD = system()
if platformD == 'Darwin':

    logo_image = "/Users/adityakhowal/Codingprojects/WeatherApp/Cloud2.icns"

else:

    logo_image = "/Users/adityakhowal/Codingprojects/WeatherApp/Cloud2.ico"


def resize():
    w=200
    h=200
    #canvas.geometry(f"{w}x{h}")


def getWeather(canvas):
    city = textfield.get()
    key1= "5b2165dbd3b45843a63251f57082b91e"
    #key 2= 
    # api2 = "http://api.openweathermap.org/geo/1.0/direct?q="+city+"&limit={limit}&appid="+ key1
    #api2 = "http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid="+ key1
    api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid="+ key1
    json_data = requests.get(api).json()
    
    #city not found error
    if json_data['cod'] == "404":
        label1.config(text = "city not found")
        label2.config(text = "please try again")
        
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)    
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    timezone = json_data['timezone']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise']-timezone))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset']-timezone))
    
    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min Temp:: " + str(min_temp) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " +sunset
    label1.config(text = final_info)
    label2.config(text = final_data)


cloudyIcon = Image.open('/Users/adityakhowal/Codingprojects/WeatherApp/Cloudy.webp')#icon

#Define Canvas/GUI properties
canvas = tk.Tk()
#canvas.geometry("600x500")
canvas.title("Weather App")
# if condition == "cloudy":
#     Icon = Image.open("")
canvas.iconbitmap(logo_image)
#Fonts
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

Title = tk.Label(canvas, text="Weather app" + "\n" + "Enter City", font =t)
Title.pack()

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady= 20)
textfield.focus()

Cloud = ImageTk.PhotoImage(Image.open("Cloudy.webp").resize((100,100)))
imageLabel = tk.Label(canvas, image= Cloud)
imageLabel.pack()

textfield.bind('<Return>', getWeather)


#photoimage = cloudyIcon.subsample(1, 2)


label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()

button_quit = Button(canvas, text="Exit program", command=canvas.quit)
button_quit.pack()
canvas.mainloop()