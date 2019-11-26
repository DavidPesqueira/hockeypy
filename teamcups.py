#!/usr/bin/python3
# -*- coding: utf-8 -*-

from bst import BST
bst = BST()  

def teamcups():
  
    cups = input("See all teams cup count by typing 'Cups'! or Only the winners by typing 'Winners'!\n")
    if cups == "Cups":            
        bst.insert("Montréal Canadiens      24 Cups Holy COW!") 
        bst.insert("Detroit Red Wings       11 Cups!")
        bst.insert("Toronto Maple Leafs     13 Cups Good Job!")
        bst.insert("New Jersey Devils       3 Cups!")
        bst.insert("New York Islanders      4 Cups!")
        bst.insert("New York Rangers        4 Cups!")
        bst.insert("Philadelphia Flyers     2 Cups!")
        bst.insert("Pittsburgh Penguins     5 Cups!")
        bst.insert("Boston Bruins           6 Cups!")
        bst.insert("Buffalo Sabres          0 Cups")
        bst.insert("Ottawa Senators         0 Cups! ")
        bst.insert("Carolina Hurricanes     1 Cup!")
        bst.insert("Florida Panthers        0 Cups.")
        bst.insert("Tampa Bay Lightning     1 Cup.")
        bst.insert("Washington Capitals     1 Cup!")
        bst.insert("Chicago Blackhawks      6 Cups!")
        bst.insert("Nashville Predators     0 Cups.")
        bst.insert("St. Louis Blues         1 Cup.")
        bst.insert("Calgary Flames          1 Cup.")
        bst.insert("Colorado Avalanche      2 Cups!")
        bst.insert("Edmonton Oilers         5 Cups!")
        bst.insert("Vancouver Canucks       0 Cups")
        bst.insert("Anaheim Ducks           1 Cup.")
        bst.insert("Dallas Stars            1 Cup.")
        bst.insert("Los Angeles Kings       2 Cups!")
        bst.insert("San Jose Sharks         0 Cups")
        bst.insert("Columbus Blue Jackets   0 Cups")
        bst.insert("Minnesota Wild          0 Cups.")
        bst.insert("Winnipeg Jets           0 Cups.")
        bst.insert("Arizona Coyotes         0 Cups.")
        bst.insert("Vegas Golden Knights    0 cups.")

        bst.traverseinorder()
        print("Goodbye")      
        
        

    elif cups == "Winners":

        print("These are the real Winners"" \n")
        bst.insert("Montréal Canadiens      24 Cups Holy COW!") 
        bst.insert("Detroit Red Wings       11 Cups!")
        bst.insert("Toronto Maple Leafs     13 Cups Good Job!")
        bst.insert("New Jersey Devils       3 Cups!")
        bst.insert("New York Islanders      4 Cups!")
        bst.insert("New York Rangers        4 Cups!")
        bst.insert("Philadelphia Flyers     2 Cups!")
        bst.insert("Pittsburgh Penguins     5 Cups!")
        bst.insert("Boston Bruins           6 Cups!")
        bst.insert("Buffalo Sabres          0 Cups")
        bst.insert("Ottawa Senators         0 Cups! ")
        bst.insert("Carolina Hurricanes     1 Cup!")
        bst.insert("Florida Panthers        0 Cups.")
        bst.insert("Tampa Bay Lightning     1 Cup.")
        bst.insert("Washington Capitals     1 Cup!")
        bst.insert("Chicago Blackhawks      6 Cups!")
        bst.insert("Nashville Predators     0 Cups.")
        bst.insert("St. Louis Blues         1 Cup.")
        bst.insert("Calgary Flames          1 Cup.")
        bst.insert("Colorado Avalanche      2 Cups!")
        bst.insert("Edmonton Oilers         5 Cups!")
        bst.insert("Vancouver Canucks       0 Cups")
        bst.insert("Anaheim Ducks           1 Cup.")
        bst.insert("Dallas Stars            1 Cup.")
        bst.insert("Los Angeles Kings       2 Cups!")
        bst.insert("San Jose Sharks         0 Cups")
        bst.insert("Columbus Blue Jackets   0 Cups")
        bst.insert("Minnesota Wild          0 Cups.")
        bst.insert("Winnipeg Jets           0 Cups.")
        bst.insert("Arizona Coyotes         0 Cups.")
        bst.insert("Vegas Golden Knights    0 cups.")
        bst.remove("Vegas Golden Knights    0 cups.")
        bst.remove("Winnipeg Jets           0 Cups.")
        bst.remove("Arizona Coyotes         0 Cups.")
        bst.remove("San Jose Sharks         0 Cups")
        bst.remove("Columbus Blue Jackets   0 Cups")
        bst.remove("Vancouver Canucks       0 Cups")
        bst.remove("Nashville Predators     0 Cups.")
        bst.remove("Florida Panthers        0 Cups.")
        bst.remove("Buffalo Sabres          0 Cups")
        bst.remove("Ottawa Senators         0 Cups.")
        bst.remove("Minnesota Wild          0 Cups.")

        bst.traverseinorder()
        print("Goodbye")

    else: 
        print("Goodbye")
