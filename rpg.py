# -*- coding: utf-8 -*-
"""
Created on Thu Jun 6 11:42:48 2019

@author: Kartik
"""

from consolemenu import *
from consolemenu.items import *

# Creating the menu
menu = ConsoleMenu("CAVE PITCHBLACK", "A DnD style roll based RPG")

# A FunctionItem runs a Python function when selected
start_game = FunctionItem("Start Game", func.intro(), ["Starting Game..."])

# A CommandItem runs a console command
leaderboard = MenuItem("View Leaderboards")

# Adding the items to the menu
menu.append_item(function_item)
menu.append_item(command_item)
menu.append_item(submenu_item)

# Show the menu and allow the user to interact
menu.show()

#importing libraries
import functions as func
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
