import os
from pyfiglet import figlet_format
from time import sleep

class Haunter():
    def __init__(self):
        self.name = "Haunter"
        self.type1 = "Ghost"
        self.type2 = "Poison"
        
        hp              = 20
        attack          = 15
        defence         = 18
        special_attack  = 30
        special_defence = 28
        speed           = 30

class Kadabra():
    def __init__(self):
        self.name = "Kadabra"
        self.type1 = "Psychic"
        self.type2 = ""

        hp              = 18
        attack          = 12
        defence         = 10
        special_attack  = 35
        special_defence = 30
        speed           = 28 

def game_title():
    os.system('clear')
    print('==================================================')
    print(figlet_format("Jaykemon"))
    print('==================================================')

def turn():
    print('')
    sleep(1)
    print('1 Fight')
    sleep(1)
    print('2 Item')
    sleep(1)
    print('3 Pokemon')
    sleep(1)
    print('4 Run')
    print('')
    print('==================================================')
    sleep(1)

def turn_choice():
    while True:
        sleep(1)
        main_choice = input('Type a number to select an option: ')
        if main_choice == '1':
            sleep(1)
            print('You chose: Fight')
            fight_choice()
            return False
        elif main_choice == '2':
            sleep(1)
            print('You chose: Item')
            item_choice()
            return False
        elif main_choice == '3':
            sleep(1)
            print('You chose: Pokemon')
            pokemon_choice()
            return False
        elif main_choice == '4':
            sleep(1)
            print('You chose: Run')
            run_choice()
            return False
        else:
            sleep(1)
            print('Please select a choice between 1 and 4')

def core():
    game_title()
    turn()
    turn_choice()

def fight_choice():
    print('Out of the loop')

def item_choice():
    print('Out of the loop')

def pokemon_choice():
    print('Out of the loop')

def run_choice():
    sleep(1)
    print('You can not run from a trainer battle! Select another choice.')
    sleep(3)
    core()





## GAME ##

game_title()

# Intro
print('')
print('William wants to battle...')
sleep(2)
print('William sent out Kadabra!')
sleep(2)
print('Jay sent out Haunter!')
print('')
print('==================================================')
sleep(2)

core()