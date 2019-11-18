#!/usr/bin/python3
# -*- coding: utf-8 -*-
import importlib
import tkinter as tk
from tkinter import *
import requests
import json
from firebaselogin import *
#import webscrape
#import teamcups #Runs BST Easter Egg
from bs4 import BeautifulSoup


'''

Variables to avoid magic numbers

'''
HEIGHT = 380 
WIDTH = 750


'''
The dictionaries below are use to access the NHL api 
that requires the user to enter an ID number rather than
a team name.
'''


ids = ["1", "2", "3", "4", "5" ,"6", "7","8","9","10",
"11", "12", "13", "14", "15" ,"16", "17","18","19","20",
"21", "22", "23", "24", "25" ,"26", "27","28","29","30","52","54"]

teamNames = ["devils", "islanders", "rangers", "flyers", 
"penguins", "bruins","sabers", "canadians","senators",
"leafs", "thrashers", "canes", "panthers","lightning",
"caps","hawks","wings","preds","blues","flames","avs",
"oilers","canucks","Ducks","stars","kings","yotes",
"sharks","jackets","wild","jets","knights"]
name_id_map = {}

for i, name in enumerate(teamNames):
    name_id_map[name] = ids[i]

'''
These are the two windows in the program 
root is the main application and top is the top 
window for the login screen
'''
root = tk.Tk() 
root.title('Get - Hockey')
top = tk.Toplevel() 
top.title('Get - Hockey Login')

'''
The Declarations of functions to be used. I am still working
on Firebase and plan on getting that done for soon. 
'''


def teamInfo(anything): #Team Record

    teamName = entry.get()
    teamId=name_id_map[teamName]
    url = 'https://statsapi.web.nhl.com/api/v1/teams/' + teamId + "?expand=team.stats" #Grabbing from the NHL API
    response = requests.get(url)    
    packages_json = response.json()
    packages_str = json.dumps(packages_json, indent=2, sort_keys=True)

    gamesPlayed=(json.loads(packages_str)['teams'][0]['teamStats'][0]['splits'][0]['stat']['gamesPlayed'])
    teamPoints =(json.loads(packages_str)['teams'][0]['teamStats'][0]['splits'][0]['stat']['pts'])
    wins =(json.loads(packages_str)['teams'][0]['teamStats'][0]['splits'][0]['stat']['wins'])
    losses =(json.loads(packages_str)['teams'][0]['teamStats'][0]['splits'][0]['stat']['losses'])

    label['text']=  teamPoints, "Points,", gamesPlayed, "GP,", wins, "W's,", losses, "L's"
    

def webscrape():
    data = requests.get('https://www.hockey-reference.com/leagues/NHL_2020_standings.html')
    soup = BeautifulSoup(data.text, 'html.parser') # Load data into bs4
    standings = soup.find('table',{'id': 'standings'})
    tbody = standings.find('tbody')

    for tr in tbody.find_all('tr'):
        place = tr.find_all('td')[0].text.strip()
        record = tr.find_all('td')[1].text.strip()
        print(place, record)

        label['text']= place, record

'''
Firebase Begin Def's 
'''

def user_login():
    
    try:
        email =  email_entry.get()
        passwd = passwd_entry.get()
        user = auth.sign_in_with_email_and_password(email, passwd) #To Sign in
        auth.get_account_info(user['idToken'])
           
        top.destroy() 
        root.deiconify()
    except requests.exceptions.HTTPError as e:
        error_json = e.args[1]
        print (error_json)
        error = json.loads(error_json)['error']
        print(error) 

def user_register():
    
    try:
        email =  email_entry.get()
        passwd = passwd_entry.get()
        user = auth.create_user_with_email_and_password(email, passwd) #To Create User
        auth.get_account_info(user['idToken'])
           
        top.destroy() 
        root.deiconify()
    except requests.exceptions.HTTPError as e:
        error_json = e.args[1]
        print (error_json)
        error = json.loads(error_json)['error']
        print(error) 



def exitProgram():
    top.destroy() 
    root.destroy()
    sys.exit() 

def command3():
    top.destroy() #Removes the toplevel window
    root.destroy() #Removes the hidden root window
    sys.exit() #Ends the script

'''
This is the design code for the login screen
There is something about tkinter that I havn't figured 
out yet why I can't use the same HEIGHT and WIDTH
from earlier that I use on my root window, It shows
up way off if I do, so I needed to declare it's own 
dimensions and create new lables and background image code,
rather than just using the same for top and root.
'''
topWidth = 400
topHeight = 400
canvasLogin = tk.Canvas(top, height=topHeight, width=topWidth)
canvasLogin.pack()
background_image2=tk.PhotoImage(file='hockey.png')
backround_label2 = tk.Label(top, image=background_image2)
backround_label2.place(relwidth=1, relheight=1)



canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image=tk.PhotoImage(file='hockey.png')
backround_label = tk.Label(root, image=background_image)
backround_label.place(relwidth=1, relheight=1)
frame = tk.Frame(root, bg='white', bd=5)
frame.place(relx=0.5, rely=0.1,relwidth=0.75, relheight=0.1, anchor='n')

'''
There are a couple different methods of placing items in tkinter
grid and using place. In my orginal app that I used to upgrade I also
used this method of place where you set the coordinates using
relx, rely, relwidth and relheight to postion things.
'''



'''
This is the code to get the email and password
'''
email_entry = tk.Entry(top, font=20) #I'm defining email twice...I'm just confused on how to make this work
email_entry.place(relx=.55,relwidth=0.45, relheight=.1) 
label=tk.Label(top)
label.place(relx=.01,relwidth=0.3, relheight=.08,)
label['text'] = 'Enter Email: '

passwd_entry = tk.Entry(top, font=20) #Password entry
passwd_entry.place(relx=.55, rely=.08,relwidth=0.45, relheight=.1)
label=tk.Label(top)
label.place(relx=.01,relwidth=0.3, rely=.09, relheight=.08)
label['text'] = 'Enter Password: '


login = Button(top, text="Login", font=40, command=lambda:user_login()) #Login button
login.place(relx=.55, rely=.2,relwidth=0.45, relheight=.12)

register = Button(top, text="Register", font=40, command=lambda:user_register()) #Cancel button
register.place(relx=.01, rely=.21,relwidth=0.5, relheight=.12)

register = Button(top, text="Forgot Password", font=40, command=lambda:command3()) #Cancel button
register.place(relx=.01, rely=.8,relwidth=0.45, relheight=.1)

cancel= Button(top, text="Exit", font=40, command=lambda:exitProgram()) #Cancel button
cancel.place(relx=.01, rely=.9,relwidth=0.45, relheight=.1)

'''
These are the buttons and entries for the main program
Team info and I am not totally sure how I plan to use the web scraping. I would
like live scores but I might just need to redirect that to a website that has them 
and use the scraper for something else
'''

button = tk.Button(frame, text='Team Info', font=40, bd=5, command=lambda: teamInfo(entry.get())) 
button.place(relx=0.8, relwidth=0.2, relheight=1)

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.78, relheight=1)

lower_frame =tk.Frame(root, bg='white', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

lower_frame2 =tk.Frame(root, bg='white', bd=10)
lower_frame2.place(relx=0.125, rely=0.9, relwidth=0.25, relheight=0.1, anchor='w')

button = tk.Button(lower_frame2, text='Live Scores', font=40, command=lambda: webscrape()) 
button.place(relx=.1, relwidth=.8, relheight=1)


'''
These open and close the windows
and contain the main program loop
'''


if __name__ == "__main__":
    root.withdraw() #This hides the main window, it's still present it just can't be seen or interacted with
    root.mainloop()
