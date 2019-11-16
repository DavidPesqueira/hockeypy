#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pyrebase
from flask import *
import requests
app = Flask(__name__)

config = {

    "authDomain": "hockeypy.firebaseapp.com",
    "databaseURL": "https://hockeypy.firebaseio.com",
    "projectId": "hockeypy",
    "storageBucket": "hockeypy.appspot.com",
    "messagingSenderId": "516953468161",
    "appId": "1:516953468161:web:85e81eea16fe8eb774ff00",
    "measurementId": "G-F64QVYNWE5"

}

Firebase = pyrebase.initialize_app(config)

auth = Firebase.auth()

@app.route('/', methods=['GET', 'POST'])

#Firebase = pyrebase.initialize_app(config)

#auth = Firebase.auth()

#email = input('email\n') #Get Email

#password = input('Password\n') #input Password


#user = auth.create_user_with_email_and_password(email, password) #To Create User

#user = auth.sign_in_with_email_and_password(email, password) #To Sign in

#auth.send_email_verification(user['idToken']) #You signed in

#auth.send_password_reset_email #Email reset

#auth.get_account_info(user['idToken'])

def loginFirebase():
    if request.method == 'POST':
        email = request.form['name']
        password = request.form['pass']
        auth.sign_in_with_email_and_password(email, password)
        return "Login Successfull"
if __name__ == '__main__':
    app.run()