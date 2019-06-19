import random
import time
import sys
import re
import functions as func

#displays Cave Pitchblack ascii art
f = open('asciiart.txt', 'r')                                                      
data = f.read()                      # reads asciiart.txt
f.close()               
print (data)    
    
#randomly generates player and enemy stats
class Settings:
    PLAYER_ATTACK = random.randint(5, 10)
    MAX_ENEMY_STRENGTH = 15
    MIN_ENEMY_STRENGTH = 5
    ENEMIES = ['behemoth', 'goblin', 'hellstep', 'orc', 'golem', 'zombie', 'undead mermaid','brinebrute', 'soulcreep','murkmutant']
    ENEMY_PREFIX = ['big', 'giant', 'ugly', 'fat', 'angry', 'vicious', 'murderous', 'vile', 'fat', 'dyslexic', 'terribly anorexic']
    ENEMY_WEAPON = ['sword', 'warhammer', 'charming smile', 'axe', 'hammer', 'club', 'giant bone', 'mace', 'dagger', 'terrible case of body odor', 'shiny gauntlet from a dead city soldier']
    PLAYER_WEAPON = {"sword": 2, "axe": 3, "bow": 2}
    PLAYER_HEAL = 5

#randomly generates enemy type
class Enemy:
    name = (
        random.choice(Settings.ENEMY_PREFIX)
        + " "
        + random.choice(Settings.ENEMIES)
    )
    weapon = random.choice(Settings.ENEMY_WEAPON)
    attack = random.randint(Settings.MIN_ENEMY_STRENGTH, Settings.MAX_ENEMY_STRENGTH)
    health = random.randint(10, 40) 

#uses player input to create a character
class Player:
    

    name = input('What is your name traveller? ')
    
    number = re.compile(r'[1,2,3]+')                                                        #characters allowed
    weapon_choice = input('Choose your weapon: 1. Sword, 2.Battle Axe, 3. Recurve Bow ')    #while loop that executes till the entered character entered is valid
    
    while not number.match(weapon_choice):                                                  #compares the character entered
        print ("Please enter a valid response")                                             #executes if character entered is invalid
        weapon_choice = input('Choose your weapon: 1. Sword, 2. Battle Axe, 3. Recurve Bow ')
    if weapon_choice == '1':
        weapon_bonus = 2
        weapon = "sword"
    elif weapon_choice == "2":
        weapon_bonus = 3
        weapon = "axe"
    elif weapon_choice == "3":
        weapon_bonus = 2
        weapon = "bow"
    else:
        print("You did not choose a weapon, restarting game...")

    attack = Settings.PLAYER_ATTACK + weapon_bonus
    health = 100
    gold = 0
    weapon_bonus = 0