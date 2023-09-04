import os
from pyfiglet import figlet_format
from time import sleep
from random import randint
from sys import exit

damage_regulator = 3
potion_quantity = 1
randopotion_quantity = 1
money = randint(435, 1025)
confusion_turn_count = 0
disabled_turn_count = 0

class Haunter():
    def __init__(self):
        self.name = "Haunter"
        self.type1 = "Ghost"
        self.type2 = "Poison"    

        self.max_hp          = 85    
        self.hp              = 85
        self.attack          = 38
        self.defence         = 38
        self.special_attack  = 55
        self.special_defence = 50
        self.speed           = 50

        self.disabled        = False
        self.fainted         = False

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
        self.fainted         = False
        self.recoil          = False

def title_banner():
    os.system('clear')
    print('==================================================')
    print(figlet_format("Jaykemon"))
    print('==================================================')

def randomiser():
    global randomise
    randomise = randint(1,3)
    return randomise

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
            print('Only select a choice between 1 and 4...')
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
    print('x Return to Fight | Items | Pokemon | Run screen')
    sleep(1)
    print('')
    print('==================================================')
    sleep(1)

    # Todo: do I need return statements for hp, confusion and sleep status'? Test
    while True:
        global move_selected
        move_selected = input('Type a number between 1 and 4, or type x: ')
        # move_selected = input('Type a number between 1 and 4, or x to select an option: ')
        title_banner()
        if haunter.disabled == True and move_selected == disabled_move:
            sleep(2)
            print('')
            print(f'Haunter\'s {disabled_move} is disabled. Select another choice...')
            sleep(4)
            fight_choice()
            return False 
        else:
            if move_selected == '1':
                # Shadow Ball
                sleep(2)
                print('')
                print('Haunter used Shadow Ball!')
                sleep(1)
                print('It\'s super effective!')
                shadow_ball_base_damage = 80
                shadow_ball_damage = haunter.special_attack - kadabra.special_defence + round((shadow_ball_base_damage/damage_regulator))
                kadabra.hp -= shadow_ball_damage
                sleep(1)
                if kadabra.hp <= 0:
                    kadabra.fainted = True
                    print(f'Kadabra fainted! You win ${money}!')
                    sleep(3)
                    exit()
                else:
                    print(f'Haunter dealt {shadow_ball_damage} points of damage!')
                    sleep(2)
                    print(f'Enemy Kadabra\'s HP is now {kadabra.hp}/{kadabra.max_hp}')
                sleep(3)
                return False
            if move_selected == '2':
                # Shadow Punch
                sleep(2)
                print('')
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
                return False
            if move_selected == '3':
                # Confuse Ray
                sleep(2)
                print('')
                print('Haunter used Confuse Ray!')
                sleep(1)
                if kadabra.confused == True:
                    print('Kadabra is already confused...')
                else:
                    print('Enemy Kadabra is confused!')
                kadabra.confused = True
                sleep(3)
                return False
            if move_selected == '4':
                # Hypnosis            
                sleep(2)
                print('')
                print('Haunter used Hypnosis!')
                sleep(1)
                if kadabra.sleep == True:
                    print('Kadabra is already asleep...')
                else:
                    sleep_chance = randomise
                    if sleep_chance != 1:
                        kadabra.sleep = True
                        print('Enemy Kadabra fell asleep!')
                    else:
                        print('Haunter\'s Hypnosis missed!')
                sleep(3)
                return False
            if move_selected == 'x' or 'X':
                turn()
                return False
            else:
                # Invalid choice
                sleep(2)
                print('Only select a choice between 1 and 4, or x...')
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
    print('x Return to Fight | Items | Pokemon | Run screen')
    sleep(1)
    print('')
    print('==================================================')
    sleep(1)

    while True:
        item_selected = input('Type a number between 1 and 3, or x to select an option: ')
        if item_selected == '1':
            # Potion
            global potion_quantity
            if potion_quantity != 0:
                if haunter.hp == haunter.max_hp:
                    sleep(2)
                    print('Haunter\'s HP is already at max. Select another choice...')
                    sleep(4)
                    item_choice()
                    return False 
                else:
                    start_hp = haunter.hp
                    if haunter.max_hp - haunter.hp <= 20:
                        restored_hp = haunter.max_hp - haunter.hp
                        haunter.hp = haunter.max_hp
                    else:
                        restored_hp = 20
                        haunter.hp += 20
                    sleep(1)
                    print(f'Haunter\'s HP was restored by {restored_hp} points, from {start_hp} to {haunter.hp}')
                    sleep(3)
                    potion_quantity = 0
                    return False
            else:
                sleep(1)
                print('You have ran out of potions. Select another choice...')
                sleep(4)
                item_choice()
                return False
        elif item_selected == '2':
            # Randopotion
            global randopotion_quantity 
            if randopotion_quantity != 0:
                if haunter.hp == haunter.max_hp:
                    sleep(2)
                    print('Haunter\'s HP is already at max. Select another choice...')
                    sleep(4)
                    item_choice()
                    return False
                else:
                    start_hp = haunter.hp
                    potion_power = randint(0, haunter.max_hp - haunter.hp)
                    haunter.hp += potion_power
                    sleep(1)
                    print(f'Haunter\'s HP was restored by {potion_power} points, from {start_hp} to {haunter.hp}')
                    sleep(3)
                    randopotion_quantity = 0
                    return False
            else:
                sleep(1)
                print('You have ran out of randopotions. Select another choice...')
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
        if item_selected == 'x' or 'X':
                turn()
                return False
        else:
            # Invalid choice
            sleep(1)
            print('Only select a choice between 1 and 3, or x...')
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
    print('You can\'t run from a trainer battle! Select another choice...')
    sleep(3)
    turn()

def kadabra_sleep_checker():
    title_banner()
    print('')
    sleep(1)
    print('Enemy Kadabra\'s turn...')
    sleep(1)

    if kadabra.sleep == True:
        sleep_chance = randomise
        if sleep_chance == 1:
            print('Kadabra woke up!')
            sleep(2)
            kadabra.sleep = False
        else:
            sleep(1)
            print('Kadabra is fast asleep...')
            sleep(3)

def kadabra_confusion():
    kadabra.recoil = False
    if kadabra.confused == True:
        global confusion_turn_count
        confusion_turn_count += 1
    if confusion_turn_count == 3:
        kadabra.confused = False
        confusion_turn_count = 0
        print('Kadabra snapped out of its confusion!')
        sleep(3)
    if kadabra.confused == True:
        print('Kadabra is confused...')
        sleep(2)
        recoil_chance = randomise
        if recoil_chance == 1:
            kadabra.recoil = True
            print('Kadabra hurt itself in it\'s confusion!')
            kadabra.hp -= round(kadabra.max_hp * (randint(20, 30)/100))
            if kadabra.hp <= 0:
                print(f'Kadabra fainted! You win ${money}!')
                sleep(3)
                exit()
            else:
                sleep(2)
                print(f'Enemy Kadabra\'s HP is now {kadabra.hp}/{kadabra.max_hp}')
                sleep(3)

def kadabra_move():
    kadabra_move_selected = randint(1, 4)
    if kadabra_move_selected == 1:
        # Confusion
        sleep(2)
        print('')
        print('Kadabra used Confusion!')
        sleep(1)
        print('It\'s super effective!')
        confusion_base_damage = 50
        confusion_damage = kadabra.special_attack - haunter.special_defence + round((confusion_base_damage/damage_regulator))
        haunter.hp -= confusion_damage
        sleep(1)
        if haunter.hp <= 0:
            print(f'Haunter fainted! You lose...')
            sleep(3)
            exit()
        else:
            print(f'Kadabra dealt {confusion_damage} points of damage!')
            sleep(2)
            print(f'Haunter\'s HP is now {haunter.hp}/{haunter.max_hp}')
        sleep(3)

    elif kadabra_move_selected == 2:
        # Psybeam
        sleep(2)
        print('')
        print('Kadabra used Psybeam!')
        sleep(1)
        print('It\'s super effective!')
        psybeam_base_damage = 60
        psybeam_damage = kadabra.special_attack - haunter.special_defence + round((psybeam_base_damage/damage_regulator))
        haunter.hp -= psybeam_damage
        sleep(1)
        if haunter.hp <= 0:
            print(f'Haunter fainted! You lose...')
            sleep(3)
            exit()
        else:
            print(f'Kadabra dealt {psybeam_damage} points of damage!')
            sleep(2)
            print(f'Haunter\'s HP is now {haunter.hp}/{haunter.max_hp}')
        sleep(3)

    elif kadabra_move_selected == 3:
        # Disable
        if haunter.disabled == False:
            sleep(2)
            print('')
            print('Kadabra used Disable!')
            sleep(1)
            global disabled_move
            global disabled_move_name
            disabled_move = move_selected

            haunter_moves = {
            '1': 'Shadow Ball',
            '2': 'Shadow Punch',
            '3': 'Confuse Ray',
            '4': 'Hypnosis'
            }

            disabled_move_name = haunter_moves.get(disabled_move)
            print(f'Haunter\'s {disabled_move_name} has been disabled!')
            haunter.disabled = True
            sleep(3)
        else:
            kadabra_move()

    elif kadabra_move_selected == 4:
        # Recover
        if kadabra.hp == kadabra.max_hp:
            kadabra_move()
        else:
            sleep(2)
            print('')
            print('Kadabra used Recover!')
            sleep(1)
            kadabra_start_hp = kadabra.hp
            kadabra.hp += round((0.5 * kadabra.max_hp))
            if kadabra.hp > kadabra.max_hp:
                kadabra.hp = kadabra.max_hp
            restored_hp = kadabra.hp - kadabra_start_hp
            sleep(1)
            print(f'Kadabra\'s HP was restored by {restored_hp} points, from {kadabra_start_hp} to {kadabra.hp}')
            sleep(3)

def disable_turns():
    if haunter.disabled == True:
        global disabled_turn_count
        disabled_turn_count += 1
        if disabled_turn_count == 3:
            print('')
            print(f'Haunter\'s {disabled_move_name} is no longer disabled!')
            sleep(3)
            disabled_turn_count = 0
            haunter.disabled = False

# =====================================================
# ================= Game loop =========================
# =====================================================

haunter = Haunter()
kadabra = Kadabra()

title_banner()
print('')
print('Sabrina wants to battle...')
sleep(2)
print('Sabrina sent out Kadabra!')
sleep(2)
print('Ash sent out Haunter!')
print('')
print('==================================================')
sleep(2)

while True:
    randomiser()
    turn()
    randomiser()
    kadabra_sleep_checker()
    if kadabra.sleep == False:
        randomiser()
        kadabra_confusion()
        if kadabra.recoil == True:
            pass
        else: kadabra_move()
    disable_turns()