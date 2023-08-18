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
    game_title()

    print('')
    sleep(1)
    print('Haunter (HP 20/20) vs Kadabra (HP 18/18)')
    print('')
    sleep(1)
    print('1 Fight')
    sleep(1)
    print('2 Item')
    sleep(1)
    print('3 Pokemon')
    sleep(1)
    print('4 Run')
    sleep(1)
    print('')
    print('==================================================')
    sleep(1)

    while True:
        sleep(1)
        main_choice = input('Type a number to select an option: ')
        if main_choice == '1':
            sleep(1)
            print('You chose: Fight')
            sleep(3)
            fight_choice()
            return False
        elif main_choice == '2':
            sleep(1)
            print('You chose: Item')
            sleep(3)
            item_choice()
            return False
        elif main_choice == '3':
            sleep(1)
            print('You chose: Pokemon')
            sleep(3)
            pokemon_choice()
            return False
        elif main_choice == '4':
            sleep(1)
            print('You chose: Run')
            sleep(3)
            run_choice()
            return False
        else:
            sleep(1)
            print('Please only select a choice between 1 and 4...')
            sleep(3)
            turn()

def fight_choice():
    print('Update me!')

def item_choice():
    game_title()
    sleep(1)
    print('')
    print('Items')
    print('')
    sleep(1)
    print('1 Potion')
    sleep(1)
    print('2 Randopotion')
    sleep(1)
    print('3 Pokeball')
    sleep(1)
    print('')
    print('==================================================')
    sleep(1)

    while True:
        item_selected = input('Type a number to select an option: ')
        if item_selected == '1':
            print(2)
            # Todo: make a Haunter instance
            # Haunter HP + 20
            # If HP > max: max
            # Print 'Haunter's HP is now x'
        elif item_selected == '2':
            print(2)
            # Restore health by randint between 0 and (max health - current health)
        elif item_selected == '3':
            sleep(1)
            print('You can\'t catch another trainer\'s Pokemon! Select another item...')
            sleep(4)
            item_choice()
            return False
        else:
            sleep(1)
            print('Please only select a choice between 1 and 3...')
            sleep(4)
            item_choice()
            return False
            

def pokemon_choice():
    sleep(1)
    print('You currently have no other Pokemon in your party. Select another choice...')
    sleep(4)
    turn()

def run_choice():
    sleep(1)
    print('You can not run from a trainer battle! Select another choice...')
    sleep(3)
    turn()





## GAME ##

# Intro
game_title()
print('')
print('William wants to battle...')
sleep(2)
print('William sent out Kadabra!')
sleep(2)
print('Jay sent out Haunter!')
print('')
print('==================================================')
sleep(2)

# Turn
turn()
