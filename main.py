import os
from pyfiglet import figlet_format
from time import sleep
from random import randint
from sys import exit

damage_regulator = 3
money = randint(435, 1025)
turn_count = 0


class Haunter():
    def __init__(self):
        self.name = "Haunter"
        self.type1 = "Ghost"
        self.type2 = "Poison"    
        self.max_hp          = 85    
        self.hp              = 10
        self.attack          = 38
        self.defence         = 38
        self.special_attack  = 55
        self.special_defence = 50
        self.speed           = 50

# print(haunter.hp)
# haunter.hp += 10
# print(haunter.hp)


class Kadabra():
    def __init__(self):
        self.name = "Kadabra"
        self.type1 = "Psychic"

        self.max_hp          = 75    
        self.hp              = 75
        self.attack          = 35
        self.defence         = 35
        self.special_attack  = 60
        self.special_defence = 54
        self.speed           = 55

        self.sleep           = False
        self.confused        = False

def title_banner():
    os.system('clear')
    print('==================================================')
    print(figlet_format("Jaykemon"))
    print('==================================================')

def turn():
    title_banner()

    print('')
    sleep(1)
    print(f'Haunter (HP {haunter.hp}/{haunter.max_hp}) vs Kadabra (HP {kadabra.hp}/{kadabra.max_hp})')
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
    title_banner()
    print('')
    sleep(1)
    print('1 Shadow Ball')
    sleep(1)
    print('2 Shadow Punch')
    sleep(1)
    print('3 Confuse Ray')
    sleep(1)
    print('4 Hypnosis')
    sleep(1)
    print('')
    print('==================================================')
    sleep(1)

    # Todo: do I need return statements for hp, confusion and sleep status'?
    while True:
        move_selected = input('Type a number to select an option: ')
        title_banner()
        if move_selected == '1':
            # Shadow Ball
            sleep(2)
            print('Haunter used Shadow Ball!')
            sleep(1)
            print('It\'s super effective!')
            shadow_ball_base_damage = 80
            shadow_ball_damage = haunter.special_attack - kadabra.special_defence + round((shadow_ball_base_damage/damage_regulator))
            kadabra.hp -= shadow_ball_damage
            sleep(1)
            if kadabra.hp <= 0:
                print(f'Kadabra fainted! You win ${money}!')
                sleep(3)
                exit()
            else:
                print(f'Haunter dealt {shadow_ball_damage} points of damage!')
                sleep(2)
                print(f'Enemy Kadabra\'s HP is now {kadabra.hp}/{kadabra.max_hp}')
            sleep(3)
            kadabra_turn()
            return False
        if move_selected == '2':
            # Shadow Punch
            sleep(2)
            print('Haunter used Shadow Punch!')
            sleep(1)
            print('It\'s super effective!')
            shadow_punch_base_damage = 60
            shadow_punch_damage = haunter.attack - kadabra.defence + round((shadow_punch_base_damage/damage_regulator))
            kadabra.hp -= shadow_punch_damage
            sleep(1)
            if kadabra.hp <= 0:
                print(f'Kadabra fainted! You win ${money}!')
                sleep(3)
                exit()
            else:
                print(f'Haunter dealt {shadow_punch_damage} points of damage!')
                sleep(2)
                print(f'Enemy Kadabra\'s HP is now {kadabra.hp}/{kadabra.max_hp}')
            sleep(3)
            kadabra_turn()
            return False
        if move_selected == '3':
            # Confuse Ray
            sleep(2)
            print('Haunter used Confuse Ray!')
            sleep(1)
            if kadabra.confused == True:
                print('Kadabra is already confused...')
            else:
                print('Enemy Kadabra is confused!')
            sleep(3)
            kadabra_turn()
            return False
        if move_selected == '4':
            # Hypnosis            
            sleep(2)
            print('Haunter used Hypnosis!')
            sleep(1)
            if kadabra.sleep == True:
                print('Kadabra is already asleep...')
            sleep_chance = randint(1, 3)
            if sleep_chance != 1:
                kadabra.sleep = True
                print('Enemy Kadabra fell asleep!')
            else:
                print('Haunter\'s Hypnosis missed!')
            sleep(3)
            kadabra_turn()
            return False
        else:
            sleep(2)
            print('Please only select a choice between 1 and 4...')
            sleep(4)
            fight_choice()
            return False    

def item_choice():
    title_banner()
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
                kadabra_turn()
                False
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
                sleep(4)
                kadabra_turn()
                return False
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

def turn_counter():
    global turn_count
    turn_count += 1
    print(turn_count)
    sleep(3)

def kady_turn():
    tester = input('Count or difference?')
    if tester == 'Count':    
        print(f'Turn number {turn_count}')
    elif tester == 'difference':
        print('update')
        # Assign a variable to reference the current turn_count value
        # Another variable to 
    else:
        print('Wrong choice - try again')
        tester()

# Todo first:
# In kadabra's code, assign a variable to make a reference of the turn_count value when kadabra.confused = True
# When that variable is equal to another variable which is + 2 of the former's value, confused = False
# Same logic with Reflect 
# kady_turn can be deleted as it was a test
# Also delete from while statement at the end of the code

def kadabra_turn():
    sleep(1)
    title_banner()
    print('')
    sleep(3)

    start_turn = 0
    current_turn = start_turn + 1

    if kadabra.sleep == True:
        sleep_chance = randint(1, 3)
        if sleep_chance == 1:
            print('Kadabra woke up!')
            sleep(2)
            kadabra.sleep = False
        else:
            print('Kadabra is fast asleep...')
            sleep(3)
            turn()

    if kadabra.confused == True:
        confusion_chance = randint(1, 2)

    selection = randint(1, 4)
    if selection == 1:
        # Confusion
        print('1')

    elif selection == 2:
        # Psybeam
        print('2')

    elif selection == 3:
        # Reflect
        print('3')

    elif selection == 4:
        # Recover
        print('4')

    # turn()




## GAME ##
switch = 'on'

if switch == 'on':

    haunter = Haunter()
    kadabra = Kadabra()

    # Intro
    title_banner()
    print('')
    print('William wants to battle...')
    sleep(2)
    print('William sent out Kadabra!')
    sleep(2)
    print('Jay sent out Haunter!')
    print('')
    print('==================================================')
    sleep(2)

    while True:
    #     turn()
        turn_counter()
    #    kadabra_turn()
        kady_turn()
    # kadabra_turn()