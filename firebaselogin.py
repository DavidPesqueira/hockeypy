#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pyrebase
from flask import *
import requests
app = Flask(__name__)

'''
Remove api key before commit
'''
config = {
    "apiKey": "",
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



