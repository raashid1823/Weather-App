# # python3 -- Weather Application using API

# # importing the libraries
# from tkinter import *
# from tkinter import Label
# from tkinter import Tk
# from tkinter import StringVar
# from tkinter import Entry
# from tkinter import Button
# from tkinter import W
# from tkinter import E
# from tkinter import N
# from tkinter import S
# import requests
# import json
# import datetime
# from PIL import ImageTk, Image
# from tkinter import messagebox



# # necessary details
# root = Tk()
# root.title("Weather App")
# root.geometry("450x700")
# root['background'] = "white"

# # Image
# new = ImageTk.PhotoImage(Image.open('C:\\Users\\1raas\\OneDrive\\Desktop\\weather.jpg'))
# panel = Label(root, image=new)
# panel.place(x=0, y=520)

# # Load and display background image
# bg_image = ImageTk.PhotoImage(Image.open('C:\\Users\\1raas\\OneDrive\\Desktop\\bg.jpg'))
# bg_label = Label(root, image=bg_image)
# bg_label.place(relwidth=1, relheight=1)  # Fill the entire window

# # Overlay image for theme
# dt = datetime.datetime.now()
# def update_theme():
#     current_hour = int(dt.strftime('%H'))
#     if 8 <= current_hour <= 17:
#         img = ImageTk.PhotoImage(Image.open('C:\\Users\\1raas\\OneDrive\\Desktop\\sun.png'))
#     else:
#         img = ImageTk.PhotoImage(Image.open('C:\\Users\\1raas\\OneDrive\\Desktop\\moon.png'))
#     theme_panel.configure(image=img)
#     theme_panel.image = img

# theme_panel = Label(root)
# theme_panel.place(x=210, y=200)
# update_theme()

# # Dates
# dt = datetime.datetime.now()
# date = Label(root, text=dt.strftime('%A--'), bg='white', font=("bold", 15))
# date.place(x=5, y=130)
# month = Label(root, text=dt.strftime('%m %B'), bg='white', font=("bold", 15))
# month.place(x=100, y=130)

# # Time
# hour = Label(root, text=dt.strftime('%I : %M %p'),bg='white', font=("bold", 15))
# hour.place(x=10, y=160)

# # Theme for the respective time the application is used
# if int((dt.strftime('%H'))) >= 8 and int((dt.strftime('%H'))) <= 17:
# 	img = ImageTk.PhotoImage(Image.open('C:\\Users\\1raas\\OneDrive\\Desktop\\moon.png'))
# 	panel = Label(root, image=img)
# 	panel.place(x=210, y=200)
# else:
# 	img = ImageTk.PhotoImage(Image.open('C:\\Users\\1raas\\OneDrive\\Desktop\\sun.png'))
# 	panel = Label(root, image=img)
# 	panel.place(x=210, y=200)


# # City Search
# city_name = StringVar()
# city_entry = Entry(root, textvariable=city_name, width=45)
# city_entry.grid(row=1, column=0, ipady=10, stick=W+E+N+S)

# api_key = "db61e7a02ac693f2ce7de8c9ce65278e"

# def get_weather():
#     try:
#         api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
#                                    + city_entry.get() + "&units=metric&appid=" + api_key)
#         api = json.loads(api_request.content)

#         if api.get('cod') != 200:
#             messagebox.showerror("Error", f"City {city_entry.get()} not found!")
#             return

#         # Extract data from the API response
#         y = api['main']
#         current_temprature = y['temp']
#         humidity = y['humidity']
#         tempmin = y['temp_min']
#         tempmax = y['temp_max']

#         x = api['coord']
#         longtitude = x['lon']
#         latitude = x['lat']

#         z = api['sys']
#         country = z['country']
#         citi = api['name']

#         # Update labels with the received info
#         lable_temp.configure(text=current_temprature)
#         lable_humidity.configure(text=humidity)
#         max_temp.configure(text=tempmax)
#         min_temp.configure(text=tempmin)
#         lable_lon.configure(text=longtitude)
#         lable_lat.configure(text=latitude)
#         lable_country.configure(text=country)
#         lable_citi.configure(text=citi)

#     except Exception as e:
#         messagebox.showerror("Error", str(e))



# # Search Bar and Button
# city_nameButton = Button(root, text="Search", command=get_weather)
# city_nameButton.grid(row=1, column=1, padx=5, stick=W+E+N+S)


# # Country Names and Coordinates
# lable_citi = Label(root, text="...", width=0, 
# 				bg='white', font=("bold", 15))
# lable_citi.place(x=10, y=63)

# lable_country = Label(root, text="...", width=0, 
# 					bg='white', font=("bold", 15))
# lable_country.place(x=135, y=63)

# lable_lon = Label(root, text="...", width=0,
# 				bg='white', font=("Helvetica", 15))
# lable_lon.place(x=18, y=95)
# lable_lat = Label(root, text="...", width=0,
# 				bg='white', font=("Helvetica", 15))
# lable_lat.place(x=95, y=95)

# # Current Temperature

# lable_temp = Label(root, text="...", width=0,
# 				font=("Helvetica", 110), fg='black')
# lable_temp.place(x=10, y=220)

# # Other temperature details

# humi = Label(root, text="Humidity: ", width=0, 
# 			 font=("bold", 15))
# humi.place(x=3, y=400)

# lable_humidity = Label(root, text="...", width=0, font=("bold", 15))
# lable_humidity.place(x=107, y=400)


# maxi = Label(root, text="Max. Temp.: ", width=0, 
# 			 font=("bold", 15))
# maxi.place(x=3, y=430)

# max_temp = Label(root, text="...", width=0, 
# 				 font=("bold", 15))
# max_temp.place(x=128, y=430)


# mini = Label(root, text="Min. Temp.: ", width=0, 
# 			 font=("bold", 15))
# mini.place(x=3, y=460)

# min_temp = Label(root, text="...", width=0, 
# 				 font=("bold", 15))
# min_temp.place(x=128, y=460)


# # Note
# note = Label(root, text="All temperatures in degree celsius",
# 			 font=("italic", 10))
# note.place(x=95, y=495)


# root.mainloop()

from tkinter import *
import requests
import json
import datetime
from PIL import ImageTk, Image
from tkinter import messagebox

# Initialize Tkinter root
root = Tk()
root.title("Weather App")
root.geometry("450x700")
root['background'] = "white"

# Load and display background image
bg_image = ImageTk.PhotoImage(Image.open('C:\\Users\\1raas\\OneDrive\\Desktop\\bg.jpg'))
bg_label = Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)  # Fill the entire window

# Overlay image for theme
def update_theme():
    dt = datetime.datetime.now()
    current_hour = int(dt.strftime('%H'))
    if 8 <= current_hour <= 17:
        img = ImageTk.PhotoImage(Image.open('C:\\Users\\1raas\\OneDrive\\Desktop\\sun.png'))
    else:
        img = ImageTk.PhotoImage(Image.open('C:\\Users\\1raas\\OneDrive\\Desktop\\moon.png'))
    theme_panel.configure(image=img)
    theme_panel.image = img

theme_panel = Label(root)
theme_panel.place(x=210, y=200)
update_theme()

# Dates
dt = datetime.datetime.now()
date = Label(root, text=dt.strftime('%A--'), bg='white', font=("bold", 15))
date.place(x=5, y=130)
month = Label(root, text=dt.strftime('%m %B'), bg='white', font=("bold", 15))
month.place(x=100, y=130)

# Time
hour = Label(root, text=dt.strftime('%I : %M %p'), bg='white', font=("bold", 15))
hour.place(x=10, y=160)

# City Search
city_name = StringVar()
city_entry = Entry(root, textvariable=city_name, width=45)
city_entry.grid(row=1, column=0, ipady=10, stick=W+E+N+S)

api_key = "db61e7a02ac693f2ce7de8c9ce65278e"

def get_weather():
    try:
        api_request = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_entry.get()}&units=metric&appid={api_key}")
        api = json.loads(api_request.content)

        if api.get('cod') != 200:
            messagebox.showerror("Error", f"City '{city_entry.get()}' not found!")
            return

        # Extract data from the API response
        y = api['main']
        current_temperature = y['temp']
        humidity = y['humidity']
        tempmin = y['temp_min']
        tempmax = y['temp_max']

        x = api['coord']
        longitude = x['lon']
        latitude = x['lat']

        z = api['sys']
        country = z['country']
        city = api['name']

        # Update labels with the received info
        lable_temp.configure(text=f"{current_temperature}°C")
        lable_humidity.configure(text=f"{humidity}%")
        max_temp.configure(text=f"{tempmax}°C")
        min_temp.configure(text=f"{tempmin}°C")
        lable_lon.configure(text=f"{longitude}")
        lable_lat.configure(text=f"{latitude}")
        lable_country.configure(text=f"{country}")
        lable_city.configure(text=f"{city}")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Request failed: {e}")
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Failed to decode JSON response")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Search Bar and Button
city_nameButton = Button(root, text="Search", command=get_weather)
city_nameButton.grid(row=1, column=1, padx=5, stick=W+E+N+S)

# Weather Information Labels
lable_city = Label(root, text="...", width=0, bg='white', font=("bold", 15))
lable_city.place(x=10, y=63)

lable_country = Label(root, text="...", width=0, bg='white', font=("bold", 15))
lable_country.place(x=135, y=63)

lable_lon = Label(root, text="...", width=0, bg='white', font=("Helvetica", 15))
lable_lon.place(x=18, y=95)
lable_lat = Label(root, text="...", width=0, bg='white', font=("Helvetica", 15))
lable_lat.place(x=95, y=95)

lable_temp = Label(root, text="...", width=0, bg='white', font=("Helvetica", 110), fg='black')
lable_temp.place(x=10, y=220)

# Other temperature details
humi = Label(root, text="Humidity: ", width=0, bg='white', font=("bold", 15))
humi.place(x=3, y=400)

lable_humidity = Label(root, text="...", width=0, bg='white', font=("bold", 15))
lable_humidity.place(x=107, y=400)

maxi = Label(root, text="Max. Temp.: ", width=0, bg='white', font=("bold", 15))
maxi.place(x=3, y=430)

max_temp = Label(root, text="...", width=0, bg='white', font=("bold", 15))
max_temp.place(x=128, y=430)

mini = Label(root, text="Min. Temp.: ", width=0, bg='white', font=("bold", 15))
mini.place(x=3, y=460)

min_temp = Label(root, text="...", width=0, bg='white', font=("bold", 15))
min_temp.place(x=128, y=460)

# Note
note = Label(root, text="All temperatures in degree Celsius", bg='white', font=("italic", 10))
note.place(x=95, y=495)

root.mainloop()

