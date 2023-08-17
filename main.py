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

game_title()

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
sleep(2)

main_choice = input('Type a number to select an option: ')
if main_choice == '1':
    print('You chose: Fight')
    # move_choice()
elif main_choice == '2':
    print('You chose: Item')
    # item_choice()
elif main_choice == '3':
    print('You chose: Pokemon')
    # pokemon_choice()
elif main_choice == '4':
    print('You chose: Run')
    # run_choice()