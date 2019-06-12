# -*- coding: utf-8 -*-
"""
Created on Thu Jun 6 11:42:48 2019

@author: Kartik
"""
#importing libraries
import random
import time
import sys
import re

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


f = open('asciiart2.txt', 'r')   #read file to display logo
asciiart = f.read()
playAgain = "Y"                  #to run the first instance



#text output speed
def say(text):
    for char in text:
        print(char, end="")
        time.sleep(0.04)
    print("")
    time.sleep(0.3)

#uses all the stats to start story
def intro():
    print (asciiart)            #display logo
    print ()
    print ()
    say(f"Greetings, {Player.name}.")
    if Player.weapon == "sword":
        say("You have a sword in your hand.")
    elif Player.weapon == "axe":
        say("You have an axe by your side. Slow, but strong.")
    elif Player.weapon == "bow":
        say("You picked the bow. Silent but deadly.")
    say("You were sent to clear out the Pitchblack cave by the kingdom.")
    say("You reach your destination, the cave dark as the night as you enter.")

#procedurally generates a battle instance
def instance():
    say(f"You have encountered a {Enemy.name} wielding a {Enemy.weapon}.")
    say(f"Its attack is {Enemy.attack} and it has {Enemy.health} health.")
    say(
        f"Your attack would do {Player.attack} damage. You have {Player.health} health left."
    )
    say(f"You choose to:")
    say(f"1. Attack, 2. Run")
    
    number = re.compile(r'[1,2]+')                                                  #characters allowed
    choice = input()                                                                #while loop that executes till the entered character entered is valid
    
    while not number.match(choice):                                                 #compares the character entered
        print ("Please enter a valid response")
        choice = input()
    if choice == '1':
        battle()
    elif choice == '2':
        end()
        
#simulates the fight
def battle():
    while Enemy.health > 0:
        say(f"You attack the {Enemy.name} with your {Player.weapon}.")
        Enemy.health = Enemy.health - Player.attack
        if Enemy.health <= 0:
            say(f"Your attack did {Player.attack} damage. The {Enemy.name} falls.")
            victory()

        say(
            f"Your attack did {Player.attack} damage. The {Enemy.name} now has {Enemy.health} health."
        )

        Player.health = Player.health - Enemy.attack
        say(
            f"The {Enemy.name} attacks back. You take {Enemy.attack} damage. Your health is now {Player.health}."
        )
        if Player.health > 0 and Enemy.health <= 0:
            victory()
        if Player.health <= 0:
            sys.exit("You died. Game Over.")

#generates new enemy strength and stats to increase difficulty and levels up character after fight
def difficulty():
    instance.score = instance.score + 1
    Player.attack = Player.attack + random.randint(1, 3) * instance.score
    Player.health = Player.health + random.randint(1, 3) * instance.score
    Enemy.name = (
        random.choice(Settings.ENEMY_PREFIX)
        + " "
        + random.choice(Settings.ENEMIES)
    )
    Enemy.weapon = random.choice(Settings.ENEMY_WEAPON)
    Enemy.attack = Enemy.attack + random.randint(1, 3) * instance.score
    Enemy.health = random.randint(1, 20) + random.randint(1, 3) * instance.score
    Player.gold = Player.gold + random.randint(5,15) * instance.score

#generates victory and the loot after battle
def victory():
    say(f"You defeated the {Enemy.name}.")
    difficulty()
    say(f"You find some gold while looting and now have {Player.gold}")
    say(f"Your attack goes up to {Player.attack} and your health to {Player.health}")
    if Settings.PLAYER_HEAL > 0:
        say(f"You have {Settings.PLAYER_HEAL} meds left. Use them wisely.")
        say("Would you like to use one? Y/N")

    value = re.compile(r'[y,Y,n,N]+')                                               #characters allowed
    choice = input()                                                                                       
    while not value.match(choice):                                                  #while loop that executes till the entered character entered is valid
        print ("Please enter a valid response")
        choice = input()
        if choice == 'Y' or choice == 'y':
            Player.health = Player.health + (random.randint(5, 10) * instance.score)
            Settings.PLAYER_HEAL = Settings.PLAYER_HEAL - 1
            say(f"Your health goes up to {Player.health}. You have {Settings.PLAYER_HEAL} meds left.")
        else:
            say(f"You still have {Settings.PLAYER_HEAL} meds left.")
            
    if Settings.PLAYER_HEAL == 0:
        say("You are out of meds. Good luck.")
    store()    
    say("Go deeper into the cave? Y/N")
    value = re.compile(r'[y,Y,n,N]+')
    choice = input()
    
    while not value.match(choice):
        print ("Please enter a valid response")
        choice = input()
    
    if choice == 'Y' or  choice == 'y':
        say('You march forward...')
        instance()
    if choice == "N" or choice == "n":
        end()
        
#end game if chosen to quit
def end():
    say("You decide to be smart and retreat...")
    say(f"You defeated {instance.score} monsters.")
    say(f"Thank you for playing.")
    sys.exit("Exiting game ...")

#merchant uses Player.gold
def store():
    say(f"You see a strange merchant waiting in the shadows with blue flames in his lamp")
    say(f"\n'What are you buying stranger?'\n")
    say(f"You have {Player.gold} coins left.")
    print ("1. Flame Sword       [5 DMG]     --> 100 gold coins")
    print ("2. Enchanted Dagger  [5 DMG]     --> 40 gold coins")
    print ("3. Stealth Bow       [5 DMG]     --> 70 gold coins")
    print ("4. Meds              [1 MED]     --> 20 gold coins")
    print ("5. back")
    print (" ")
    
    store.choice = input()
    
    if store.choice == '1':
        Player.weapon_bonus = 6
        instance()
        
    elif store.choice == '2':
        Player.weapon_bonus = 4
        instance()
        
    elif store.choice == '3':
        Player.weapon_bonus = 5
        instance()
        
    elif store.choice == '4':
        Settings.PLAYER_HEAL = Settings.PLAYER_HEAL + 1
        instance()
             
        
while playAgain == 'Y' or playAgain == 'y':
    intro()
    instance.score = 0
    Player.gold = 0
    instance()
    end()
    break
