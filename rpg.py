# -*- coding: utf-8 -*-
"""
Created on Thu Jun 6 11:42:48 2019

@author: Kartik
"""

from consolemenu import *
from consolemenu.items import *

import functions as func
# Creating the menu
menu = ConsoleMenu("CAVE PITCHBLACK", "A DnD style roll based RPG")

# A FunctionItem runs a Python function when selected
start_game = FunctionItem("Start Game", func.intro(), ["Starting Game..."])

# A CommandItem runs a console command
leaderboard = MenuItem("View Leaderboards")

# Adding the items to the menu
menu.append_item(start_game)
menu.append_item(leaderboard)

# Show the menu and allow the user to interact
menu.show()

#importing libraries
import objects as obj

playAgain = "Y"                  #to run the first instance


        
while playAgain == 'Y' or playAgain == 'y':
    func.intro()
    func.instance.score = 0
    obj.Player.gold = 0
    func.instance()
    func.store()
    func.end()
    break
