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
window.resizable(1, 1)             # allows resizing of the app window

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
main_menu = tk.Frame(notebook, width = 1440, height = 750)
tv_series_search = tk.Frame(notebook, width = 1440, height = 750)
movie_search = tk.Frame(notebook, width = 1440, height = 750)

# adding the frames to the notebook tabs
notebook.add(tv_series_search, text = "TV Series Search")
notebook.add(movie_search, text = "Movie Search")

####################################### SEARCHING FOR ANY TV SERIES #################################################

# creating a heading for the tv series
tv_heading = tk.Label(tv_series_search, font = ('Tahoma', 16, 'bold'), text = "TV SERIES INFO").pack(pady = 5, side = TOP)

# creating a label & entry widget to prompt the user to search for a tv series
tv_entry = tk.StringVar()
tv_search_label = tk.Label(tv_series_search, font = ('Arial', 12, 'bold'), text = "Search for a TV Show = ")
tv_search_label.pack(pady = 10)

tv_search_entry = tk.Entry(tv_series_search, width = 20, font = ('Arial', 12), textvariable = tv_entry)
tv_search_entry.pack(pady = 10)

# a function that helps find users the tv series they search for
def search_tvseries():
    query = tv_entry.get() # stores the user's entry

    # url to request the details of the searched show
    url = f"https://api.themoviedb.org/3/search/tv?api_key=50d32784328a030f1f56dfce14a57abf&&query={query}"

    # api fetch data requests 
    request = rq.get(url)       
    data = request.json()

    # checking if data is available
    if request.status_code == 200:
        # conditional to check if we get results
        if 'results' in data and isinstance(data['results'], list):
            for show in data['results']:

                show_name = show.get('name', 'Name not available') # fetching the show name
                show_name_ans = show_name # storing the show name in a variable
                
                # label to display the name
                result_name = tk.Label(tv_series_search, text = f"Show Name: {show_name_ans}", font = ('Arial', 10))
                result_name.pack(padx = 5, pady = 5)
                
                show_origin = show.get('origin_country', 'Country not available') # fetching the show countr
                show_origin_ans = show_origin # storing the show country in a variable
                
                # label to display the origin
                result_origin = tk.Label(tv_series_search, text = f"Origin: {show_origin_ans}", font = ('Arial', 10))
                result_origin.pack(padx = 5, pady = 5)
                
                show_overview = show.get('overview', 'Country not available') # fetching the show overview
                show_overview_ans = show_overview # storing the show overview in a variable
                
                # label to display the overview
                result_overview = tk.Label(tv_series_search, text = f"Overview: {show_overview_ans}", font = ('Arial', 10), width = 80, wraplength = 500)
                result_overview.pack(padx = 5, pady = 5)
                
                show_voteavg = show.get('vote_average', 'Vote Average Not Found')
                show_voteavg_ans = show_voteavg
                
                # label to display the votes
                result_voteavg = tk.Label(tv_series_search, text = f"Overview: {show_voteavg_ans}", font = ('Arial', 10))
                result_voteavg.pack(padx = 5, pady = 5)
                
        else:
            print("Results list is empty or not present in the data.")

    else:
        print("Error")

search_tvseries()

# creating buttons
tv_btn = tk.Button(tv_series_search, font = ('Tahoma', 20, 'bold'), text = "Find Series", border = 0, bg = '#000', fg = '#fff', command = search_tvseries)
tv_btn.pack(padx = 10, pady = 10, anchor = S)

####################################### SEARCHING FOR ANY MOVIES #################################################

# creating a heading for the movies
movie_heading = tk.Label(movie_search, font = ('Tahoma', 16, 'bold'), text = "Movies INFO").pack(pady = 5, side = TOP)

# creating a label & entry widget to prompt the user to search for a tv series
movie_entry = tk.StringVar()
movie_search_label = tk.Label(movie_search, font = ('Arial', 12, 'bold'), text = "Search for a Movie = ")
movie_search_label.pack(pady = 10)

movie_search_entry = tk.Entry(movie_search, width = 20, font = ('Arial', 12), textvariable = movie_entry)
movie_search_entry.pack(pady = 10)

# creating a function to find the movie
def search_movie():
    query = movie_entry.get()

    # url to request the details of the searched show
    url = f"https://api.themoviedb.org/3/search/movie?api_key=50d32784328a030f1f56dfce14a57abf&&query={query}"

    # api fetch data requests 
    request = rq.get(url)       
    data = request.json()

    # checking if data is available
    if request.status_code == 200:
        # conditional to check if we get results
        if 'results' in data and isinstance(data['results'], list):
            for show in data['results']:

                show_name = show.get('name', 'Name not available') # fetching the show name
                show_name_ans = show_name # storing the show name in a variable
                
                # label to display the name
                result_name = tk.Label(movie_search, text = f"Show Name: {show_name_ans}", font = ('Arial', 10))
                result_name.pack(padx = 5, pady = 5)
                
                show_origin = show.get('origin_country', 'Country not available') # fetching the show countr
                show_origin_ans = show_origin # storing the show country in a variable
                
                # label to display the origin
                result_origin = tk.Label(movie_search, text = f"Origin: {show_origin_ans}", font = ('Arial', 10))
                result_origin.pack(padx = 5, pady = 5)
                
                show_overview = show.get('overview', 'Country not available') # fetching the show overview
                show_overview_ans = show_overview # storing the show overview in a variable
                
                # label to display the overview
                result_overview = tk.Label(movie_search, text = f"Overview: {show_overview_ans}", font = ('Arial', 10), width = 80, wraplength = 500)
                result_overview.pack(padx = 5, pady = 5)
                
                show_voteavg = show.get('vote_average', 'Vote Average Not Found')
                show_voteavg_ans = show_voteavg
                
                # label to display the votes
                result_voteavg = tk.Label(movie_search, text = f"Overview: {show_voteavg_ans}", font = ('Arial', 10))
                result_voteavg.pack(padx = 5, pady = 5)

        else:
            print("Results list is empty or not present in the data.")

    else:
        print("Error")

search_movie()

# creating buttons
movie_btn = tk.Button(movie_search, font = ('Tahoma', 20, 'bold'), text = "Find Series", border = 0, bg = '#000', fg = '#fff', command = search_movie)
movie_btn.pack(padx = 10, pady = 10, anchor = S)

####################################### MAIN MENU #################################################

# displaying the tabs
def display_tabs():
    notebook.pack(fill = X, expand = 1)

# creating a button to display tabs
displaytabs_btn = tk.Button(window, font = ('Tahoma', 14, 'bold'), text = "Click to Start", command = display_tabs, bg = '#fff', fg = '#000', border = 5)
displaytabs_btn.pack(pady = 10)

# running the root window (mainloop)
window.mainloop()

# end of program