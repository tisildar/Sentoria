from characthers import main_characther
import text_manager
import characther_system

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
        characther_system.Barbarian.set_class_to_barbarian(main_characther)
    if choice == '2':
       characther_system.Bard.set_class_to_bard(main_characther)
    if choice == '3':
        characther_system.Cleric.set_class_to_cleric(main_characther)
    if choice == '4':
        characther_system.Druid.set_class_to_druid(main_characther)
    if choice == '5':
        characther_system.Fighter.set_class_to_fighter(main_characther)
    if choice == '6':
        characther_system.Monk.set_class_to_monk(main_characther)
    if choice == '7':
        characther_system.Paladin.set_class_to_paladin(main_characther)
    if choice == '8':
        characther_system.Ranger.set_class_to_ranger(main_characther)
    if choice == '9':
        characther_system.Rouge.set_class_to_rouge(main_characther)
    if choice == '10':
        characther_system.Sorcerer.set_class_to_sorcerer(main_characther)
    if choice == '11':
        characther_system.Warlock.set_class_to_warlock(main_characther)
    if choice == '12':
        characther_system.Wizard.set_class_to_wizard(main_characther)




def execute():
    text_manager.get_text_from_json("CharactherCreation","enterance")
    get_charachter_name()

ask_characther_class()


# Spagetti neydi ? Spagetti emekti. BURAYI ADAM ETMENİN YOLUNU BULMAYI UNUTNMA