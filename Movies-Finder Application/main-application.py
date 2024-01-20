# start of the program

# importing all the required modules/libraries
from tkinter import *
import tkinter as tk
import os
from PIL import Image, ImageTk
import requests
import json

# url of the api website
url = "https://api.themoviedb.org/3/movie/157336?api_key=50d32784328a030f1f56dfce14a57abf"

# API KEY displaying
APIKEY = "50d32784328a030f1f56dfce14a57abf"

# creating a variable, for storing the file path
filepath = os.path.dirname(os.path.realpath(__file__))

####################################### APPLICATION GUI SETUP #################################################

# initializng the root window
window = tk.Tk()

# setting up the dimensions, size, resizing etc. 
window.title("MOVIE FINDER API")         # sets the title of the window 
window.geometry("1020x555")         # sets the size/geometry of the app window
window.resizable(0, 0)             # restricts resizing of the app window


####################################### API BACKEND SETUP #################################################


def search_tvseries():
    url = f"https://api.themoviedb.org/3/search/tv?api_key=50d32784328a030f1f56dfce14a57abf"
    response = requests.get(url)
    print(response)

    data = response.json()
    print(data)

search_tvseries()

def search_movies():
    url = f"https://api.themoviedb.org/3/search/movie?api_key=50d32784328a030f1f56dfce14a57abf"
    response = requests.get(url)
    print("\n Movies:", response)

search_movies()

###################################### END OF BACKEND STUFF ###############################################

# running the root window (mainloop)
window.mainloop()

# end of program