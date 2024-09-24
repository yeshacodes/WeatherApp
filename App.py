from tkinter import *  # Use 'tkinter', not 'tinker'
import tkinter as tk   # Use 'tkinter', not 'tinker'
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox  # Use 'tkinter', not 'tinker'
from timezonefinder import TimezoneFinder
from datetime import datetime  # Correct the typo in 'datetime'
import requests
import pytz

root = tk.Tk()  # Use 'tk.Tk()' to initialize Tkinter window
root.title("Weather App")
root.geometry("900x500+300+200")  # Use 'x' instead of '*'
root.resizable(False, False)

def getWeather():
    try:
        city=textfield.get()
        #unit = unit_var.get() # Get the selected unit

        geolocator = Nominatim(user_agent="WeatherApp")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)


        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        api="https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=d5fbf96fcadcb94d8487be97b2f2a464"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure'] # Pressure in hPa
        pressure_mmHg = round(pressure * 0.75006, 2)  # Convert hPa to mmHg and round to 2 decimal places
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        wind_mph = round(wind * 2.23694, 2)  # Convert to mph and round to 2 decimal places
        t.config(text=(temp, "°"))
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))

        w.config(text=f"{wind_mph}")  # Display in mph
        #w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=f"{pressure_mmHg}")
        #p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!")


#search box
Search_image = PhotoImage(file="C:\\Users\yesha\OneDrive\Pictures\Camera Roll\Copy of Search.png")
myimage=Label(image=Search_image )
myimage.place(x=20, y=20)

textfield=tk.Entry(root,justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = PhotoImage(file="C:\\Users\yesha\OneDrive\Pictures\Camera Roll\Copy of search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

#logo
Logo_image = PhotoImage(file = "C:\\Users\yesha\OneDrive\Pictures\Camera Roll\Copy of logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=100)

#Bottom box
#Frame_image = PhotoImage(file = "C:\\Users\yesha\OneDrive\Pictures\Camera Roll\Copy of box.png")
#frame_myimage = Label(image = Frame_image)
#frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

bottom_frame = Frame(root, bg="#1ab5ef", width=900, height=100)  # Increase width and height as needed
bottom_frame.pack(padx=5, pady=5, side=BOTTOM)

#time
name=Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock=Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)
#label
label1 = Label(root, text="WIND (MPH)", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=50, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(root, text="PRESSURE (mmHg)", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t=Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c=Label(font=("arial", 15, 'bold'))
c.place(x=400, y=250)

w=Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=90, y=430)

h=Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)

d=Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=450, y=430)

p=Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)


root.mainloop()  # Correct the typo in 'mainloop'
