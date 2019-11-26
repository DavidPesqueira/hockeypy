#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def webscrape():
    #get data 
    data = requests.get('https://www.hockey-reference.com/leagues/NHL_2020_standings.html')

    # Load data into bs4
    soup = BeautifulSoup(data.text, 'html.parser')

    standings = soup.find('table',{'id': 'standings'})
    tbody = standings.find('tbody')

    for tr in tbody.find_all('tr'):
        place = tr.find_all('td')[0].text.strip()
        record = tr.find_all('td')[1].text.strip()

    
        print("\nTeam name: "+ place+  "\nRecord: "+ record)
  