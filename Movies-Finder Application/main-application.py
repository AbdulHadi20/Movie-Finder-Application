# start of the program

# importing all the required modules/libraries
from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
from PIL import Image, ImageTk
import requests as rq

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
window.geometry("1440x735")         # sets the size/geometry of the app window
window.resizable(0, 0)             # restricts resizing of the app window

# adding a background image for the application
bg_img = Image.open(os.path.join(filepath, "appbg.jpg"))
bg_img_display = ImageTk.PhotoImage(bg_img)
img_label = tk.Label(window, image = bg_img_display)
img_label.place(relheight = 1, relwidth = 1)

# creating a heading for the application
main_heading = tk.Label(window, font = ('Tahoma', 40, 'bold'), text = "Movie Finder API", fg = '#ffffff', bg = '#000000')
main_heading.pack(side = TOP, pady = 30)

# creating tabs (notebooks)
notebook = ttk.Notebook(window)

# creating frames for each tab
main_menu = tk.Frame(notebook, width = 1440, height = 700)
tv_series_search = tk.Frame(notebook, width = 1440, height = 700)
movie_search = tk.Frame(notebook, width = 1440, height = 700)

# adding the frames to the notebook tabs
notebook.add(main_menu, text = "Main Menu")
notebook.add(tv_series_search, text = "TV Series Search")
notebook.add(movie_search, text = "Movie Search")
notebook.pack(fill = X, expand = 1, anchor = S)

####################################### SEARCHING FOR ANY TV SERIES #################################################

# initailaizing the variables 
show_name = ""
show_origin = ""
show_overview = ""


# creating a heading for the tv series
tv_heading = tk.Label(tv_series_search, font = ('Tahoma', 30, 'bold'), text = "TV SERIES INFO").grid(pady = 5)

# creating a label & entry widget to prompt the user to search for a tv series
tv_entry = tk.StringVar()
tv_search_label = tk.Label(tv_series_search, font = ('Arial', 18, 'bold'), text = "Search for a TV Show = ")
tv_search_label.grid(row = 1, column = 0, pady = 5)

tv_search_entry = tk.Entry(tv_series_search, width = 20, font = ('Arial', 18), textvariable = tv_entry)
tv_search_entry.grid(row = 1, column = 1, pady = 5)

# a function that helps find users the tv series they search for
def search_tvseries():
    query = tv_entry.get() # stores the user's entry

    # url to request the details of the searched show
    url = f"https://api.themoviedb.org/3/search/tv?api_key=50d32784328a030f1f56dfce14a57abf&&query={query}"

    # api fetch data requests 
    request = rq.get(url)       
    data = request.json()
    

    # conditional to check if we get results
    if 'results' in data and isinstance(data['results'], list):
        for show in data['results']:
            show_name = show.get('name', 'Name not available')
            

            print(show_name)

            # result_name = tk.Label(tv_series_search, textvariable = show_name_str)
            # result_name.grid(row = 2, column = 1)
        
        else:
            print("Results list is empty or not present in the data.")

search_tvseries()

# creating buttons
tv_btn = tk.Button(tv_series_search, font = ('Tahoma', 20, 'bold'), text = "Find Series", border = 0, bg = '#000', fg = '#fff', command = search_tvseries)
tv_btn.grid(row = 2, rowspan = 10)


####################################### DISPLAY TRENDING TV SHOWS (BASED ON REGION) #################################################


####################################### SEARCHING FOR ANY MOVIES #################################################

# def search_movies():
#     url = f"https://api.themoviedb.org/3/search/movie?api_key=50d32784328a030f1f56dfce14a57abf"
#     response = requests.get(url)
#     print("\n Movies:", response)

# search_movies()

####################################### DISPLAY TRENDING MOVIES (BASED ON REGION) #################################################

####################################### SHOW WATCH PROVIDERS #################################################



# running the root window (mainloop)
window.mainloop()

# end of program