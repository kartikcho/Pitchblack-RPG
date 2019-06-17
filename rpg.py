# -*- coding: utf-8 -*-
"""
Created on Thu Jun 6 11:42:48 2019

@author: Kartik
"""
#importing libraries
import objects as obj
import functions as func


playAgain = "Y"                  #to run the first instance


        
while playAgain == 'Y' or playAgain == 'y':
    func.intro()
    func.instance.score = 0
    obj.Player.gold = 0
    func.instance()
    func.store()
    func.end()
    break
