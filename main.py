import os
from pyfiglet import figlet_format
from time import sleep
from random import randint

class Haunter():
    def __init__(self):
        self.name = "Haunter"
        self.type1 = "Ghost"
        self.type2 = "Poison"    
        self.max_hp          = 40    
        self.hp              = 10
        self.attack          = 15
        self.defence         = 18
        self.special_attack  = 30
        self.special_defence = 28
        self.speed           = 30

# print(haunter.hp)
# haunter.hp += 10
# print(haunter.hp)


class Kadabra():
    def __init__(self):
        self.name = "Kadabra"
        self.type1 = "Psychic"

        self.max_hp          = 35    
        self.hp              = 35
        self.attack          = 12
        self.defence         = 15
        self.special_attack  = 35
        self.special_defence = 30
        self.speed           = 34 

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
        turn_choice = input('Type a number to select an option: ')
        if turn_choice == '1':
            sleep(1)
            print('You chose: Fight')
            sleep(3)
            fight_choice()
            return False
        elif turn_choice == '2':
            sleep(1)
            print('You chose: Item')
            sleep(3)
            item_choice()
            return False
        elif turn_choice == '3':
            sleep(1)
            print('You chose: Pokemon')
            sleep(3)
            pokemon_choice()
            return False
        elif turn_choice == '4':
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

# Todo: end turn after potion or randopotion. Maybe through returning false then running a function to determine Kadabra's move?
    while True:
        item_selected = input('Type a number to select an option: ')
        if item_selected == '1':
            # Potion
            if potion_quantity != 0:
                start_hp = haunter.hp
                haunter.hp + 20
                if haunter.hp > haunter.max_hp:
                    haunter.hp = haunter.max_hp
                if start_hp < 20:
                    restored_hp = 20
                else:
                    restored_hp = haunter.max_hp - start_hp
                sleep(1)
                print(f'Haunter\'s HP was restored by {restored_hp} points, from {start_hp} to {haunter.max_hp}')
                potion_quantity = 0
                sleep(4)
            else:
                sleep(1)
                print('You have ran out of potions. Please select another choice...')
                sleep(4)
                item_choice()
                return False
        elif item_selected == '2':
            # Randopotion
            if randopotion_quantity != 0:
                start_hp = haunter.hp
                potion_power = randint(0, haunter.max_hp - haunter.hp)
                sleep(1)
                print(f'Haunter\'s HP was restored by {potion_power} points, from {start_hp} to {start_hp + potion_power}')
                randopotion_quantity = 0
                sleep(5)
            else:
                sleep(1)
                print('You have ran out of randopotions. Please select another choice...')
                sleep(4)
                item_choice()
                return False
        elif item_selected == '3':
            # Pokeball
            sleep(1)
            print('You can\'t catch another trainer\'s Pokemon! Select another item...')
            sleep(4)
            item_choice()
            return False
        else:
            # Invalid choice number
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
switch = 'on'

if switch == 'on':

    haunter = Haunter()
    Kadabra = Kadabra()

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
