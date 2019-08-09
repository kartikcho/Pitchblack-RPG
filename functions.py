# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 13:42:48 2019

@author: Kartik
"""
#importing libraries
import random
import time
import sys
import re
import objects as obj


#text output speed
def say(text):
    for char in text:
        print(char, end="")
        time.sleep(0.04)
    print("")
    time.sleep(0.3)

#uses all the stats to start story
def intro():
    say(f"Greetings, {obj.Player.name}.")
    if obj.Player.weapon == "sword":
        say("You have a sword in your hand. Fast and swift.")
    elif obj.Player.weapon == "axe":
        say("You have an axe by your side. Slow, but strong.")
    elif obj.Player.weapon == "bow":
        say("You picked the bow. Silent but deadly.")
    say("You were sent to clear out Cave Pitchblack by the kingdom.")
    say("You reach your destination, the cave dark as the night as you enter.")

#procedurally generates a battle instance
def instance():
    say(f"You have encountered a {obj.Enemy.name} wielding a {obj.Enemy.weapon}.")
    say(f"Its attack is {obj.Enemy.attack} and it has {obj.Enemy.health} health.")
    say(
        f"Your attack would do {obj.Player.attack} damage. You have {obj.Player.health} health left."
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
    while obj.Enemy.health > 0:
        say(f"You attack with your {obj.Player.weapon}.")
        obj.Enemy.health = obj.Enemy.health - obj.Player.attack
        if obj.Enemy.health <= 0:
            say(f"Your attack did {obj.Player.attack} damage. The {obj.Enemy.name} falls.")
            victory()

        say(
            f"Your attack did {obj.Player.attack} damage. The {obj.Enemy.name} now has {obj.Enemy.health} health."
        )

        obj.Player.health = obj.Player.health - obj.Enemy.attack
        say(
            f"The {obj.Enemy.name} attacks back. You take {obj.Enemy.attack} damage. Your health is now {obj.Player.health}."
        )
        if obj.Player.health > 0 and obj.Enemy.health <= 0:
            victory()
        if obj.Player.health <= 0:
            sys.exit("You died. Game Over.")

#generates new enemy strength and stats to increase difficulty and levels up character after fight
def difficulty():
    instance.score = instance.score + 1
    obj.Player.attack = obj.Player.attack + random.randint(1, 3) * instance.score
    obj.Player.health = obj.Player.health + random.randint(1, 3) * instance.score
    obj.Enemy.name = (
        random.choice(obj.Settings.ENEMY_PREFIX)
        + " "
        + random.choice(obj.Settings.ENEMIES)
    )
    obj.Enemy.weapon = random.choice(obj.Settings.ENEMY_WEAPON)
    obj.Enemy.attack = obj.Enemy.attack + random.randint(1, 3) * instance.score
    obj.Enemy.health = random.randint(1, 20) + random.randint(1, 3) * instance.score
    obj.Player.gold = obj.Player.gold + random.randint(5,15) * instance.score

#generates victory and the loot after battle
def victory():
    say(f"You defeated the {obj.Enemy.name}.")
    difficulty()
    say(f"You find some gold while looting and now have {obj.Player.gold} coins.")
    say(f"Your attack goes up to {obj.Player.attack} and your health to {obj.Player.health}")
    if obj.Settings.PLAYER_HEAL > 0:
        say(f"You have {obj.Settings.PLAYER_HEAL} meds left. Use them wisely.")
        say("Would you like to use one? Y/N")

        value = re.compile(r'[y,Y,n,N]+')                                               #characters allowed
        choice = input()                                                                                       
        while not value.match(choice):                                                  #while loop that executes till the entered character entered is valid
            print ("Please enter a valid response")
            choice = input()
        if choice == 'Y' or choice == 'y':                                          #does not work
            obj.Player.health = obj.Player.health + (random.randint(5, 10) * instance.score)
            obj.Settings.PLAYER_HEAL = obj.Settings.PLAYER_HEAL - 1
            say(f"Your health goes up to {obj.Player.health}. You have {obj.Settings.PLAYER_HEAL} meds left.")  
        else:
            say(f"You still have {obj.Settings.PLAYER_HEAL} meds left.")
            
    if obj.Settings.PLAYER_HEAL == 0:
        say("You are out of meds. Good luck.")
    say("Go deeper into the cave? Y/N")
    value = re.compile(r'[y,Y,n,N]+')
    choice = input()
    
    while not value.match(choice):
        print ("Please enter a valid response")
        choice = input()
    
    if choice == 'Y' or  choice == 'y':
        say('You march forward...')
        num = random.randint(1, 10)
        if num < 5:
            store()
            instance()
        else:
            instance()
    if choice == "N" or choice == "n":
        end()
        
#end game if chosen to quit
def end():
    say("You decide to be smart and retreat...")
    say(f"You defeated {instance.score} monsters.")
    say(f"Thank you for playing.")      
    say(f"Made by Kartik Choudhary")                    #Star me on Github lol (kartikch918)
    sys.exit("Exiting game ...")

#merchant uses Player.gold
def store():
    say(f"You see a strange merchant waiting in the shadows with blue flames in his lamp.")
    say(f"\nYou approach him.\n")
    say(f"\n'What are you buying stranger?'\n")
    say(f"You have {obj.Player.gold} coins left.")
    print ("1. Flame Sword       [5 DMG]     --> 100 gold coins")
    print ("2. Enchanted Dagger  [5 DMG]     --> 40 gold coins")
    print ("3. Stealth Bow       [5 DMG]     --> 70 gold coins")
    print ("4. Meds              [1 MED]     --> 20 gold coins")
    print ("5. back")
    print (" ")
    
    merch_number = re.compile(r'[1,2,3,4,5]+')                                                  #characters allowed
    store.choice = input()                                                                #while loop that executes till the entered character entered is valid
    
    
    while not merch_number.match(store.choice):                                                 #compares the character entered
        print ("Please enter a valid response")
        store.choice = input()
    
    if store.choice == '1':
        obj.Player.weapon_bonus = 6
        obj.Player.gold = obj.Player.gold-100
        if obj.Player.gold < 0:
            say("Not enough gold")
            instance()
        else:
            say("Purchased successfully")
            say("He grins as you leave and go forward.")
            instance()
        
    elif store.choice == '2':
        obj.Player.weapon_bonus = 4
        obj.Player.gold = obj.Player.gold-40
        if obj.Player.gold < 0:
            say("Not enough gold")
            instance()
        else:
            say("Purchased successfully")
            say("He grins as you leave and go forward.")
            instance()
        
    elif store.choice == '3':
        obj.Player.weapon_bonus = 5
        obj.Player.gold = obj.Player.gold-70
        if obj.Player.gold < 0:
            say("Not enough gold")
            instance()
        else:
            say("Purchased successfully")
            say("He grins as you leave and go forward.")
            instance()
        
    elif store.choice == '4':
        obj.Settings.PLAYER_HEAL = obj.Settings.PLAYER_HEAL + 1
        obj.Player.gold = obj.Player.gold-20
        if obj.Player.gold < 0:
            say("Not enough gold")
            instance()
        else:
            say("Purchased successfully")
            say("He grins as you leave and go forward.")
            instance()
             
