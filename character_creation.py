from Characthers import main_characther
import dice_system
import text_manager
import Characther_System

def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt)
        if user_input in valid_options:
            return user_input
        else:
            text_manager.get_text_from_json("General","wrong_choice")
    
def get_charachter_name():
    while True:
        text_manager.get_text_from_json("General","space")
        char_Name = main_characther.set_char_name()
        if char_Name.isalpha():
            text_manager.get_text_from_json("CharactherCreation","choose_possitive_ability_text")
            break
        else:
            text_manager.get_text_from_json("General","wrong_name")

def ask_characther_class():
    text_manager.get_text_from_json("CharactherCreation","choose_class_text")
    text_manager.get_text_from_json("CharactherCreation","choose_class_options")
    choice = get_valid_input("Seçimin = ",['1','2','3','4','5','6','7','8','9','10','11','12'])
    
    if choice == '1':
        Characther_System.Barbarian.set_class_to_barbarian(main_characther)
    if choice == '2':
        main_characther.set_char_class('Bard')
    if choice == '3':
        Characther_System.Cleric.set_class_to_cleric(main_characther)
    if choice == '4':
        main_characther.set_char_class('Druid')
    if choice == '5':
        main_characther.set_char_class('Fighter')
    if choice == '6':
        main_characther.set_char_class('Monk')
    if choice == '7':
        main_characther.set_char_class('Paladin')
    if choice == '8':
        main_characther.set_char_class('Ranger')
    if choice == '9':
        main_characther.set_char_class('Rogue')
    if choice == '10':
        main_characther.set_char_class('Sorcerer')
    if choice == '11':
        main_characther.set_char_class('Warlock')
    if choice == '12':
        main_characther.set_char_class('Wizard')




def execute():
    text_manager.get_text_from_json("CharactherCreation","enterance")
    get_charachter_name()

ask_characther_class()
dice_system.strength_saving_throw(main_characther,12)

# Spagetti neydi ? Spagetti emekti. BURAYI ADAM ETMENİN YOLUNU BULMAYI UNUTNMA