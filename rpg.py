# -*- coding: utf-8 -*-
"""
Created on Thu Jun 6 11:42:48 2019

@author: Kartik
"""


from consolemenu import *
from consolemenu.items import *

# Create the menu
menu = ConsoleMenu("CAVE PITCHBLACK", "A DnD style roll based RPG")

# Create some items

# MenuItem is the base class for all items, it doesn't do anything when selected
menu_item = MenuItem("Menu Item")

# A FunctionItem runs a Python function when selected
function_item = FunctionItem("Call a Python function", func.intro(), ["Starting Game..."])

# A CommandItem runs a console command
command_item = CommandItem("Run a console command",  "touch hello.txt")

# A SelectionMenu constructs a menu from a list of strings
selection_menu = SelectionMenu(["item1", "item2", "item3"])

# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

# Once we're done creating them, we just add the items to the menu
menu.append_item(menu_item)
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
