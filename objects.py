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
