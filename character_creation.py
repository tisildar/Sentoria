from characthers import main_characther
import dice_system
import text_manager

def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt)
        if user_input in valid_options:
            return user_input
        else:
            text_manager.get_text_from_json("General","wrong_choice")
    

def choose_posstive_ability():
    text_manager.get_text_from_json("CharactherCreation","choose_possitive_ability_options")
    choice = get_valid_input("Seçimin",['1','2','3'])
    
    if choice == '1':
        main_characther.increase_stat('strength')
        text_manager.get_text_from_json("CharactherCreation","choosing_strength_path_text")
            
    elif choice == '2':
        main_characther.increase_stat('dexterity')
        text_manager.get_text_from_json("CharactherCreation","choose_possitive_ability_dexterity_text")
        Roll = dice_system.luck_passive_check(3)
        if Roll == False:
            text_manager.get_text_from_json("CharactherCreation","choosing_dexterity_path_passive_check_fail_text")
        else:
            text_manager.get_text_from_json("CharactherCreation","choosing_dexterity_path_passive_check_success_text")
    else: 
        main_characther.increase_stat('intelligince')
        text_manager.get_text_from_json("CharactherCreation","choosing_intelligince_path_text")
            
def choose_negative_ability():
    strength = main_characther.get_strength()
    dexterity = main_characther.get_dexterity()
    intelligence = main_characther.get_intelligence()
    
    if intelligence == 1:
        text_manager.get_text_from_json("CharactherCreation", "choose_intelligince_negative_ability")
        choice = get_valid_input("Seçimin: ", ['1', '2'])
        if choice == '1':
            main_characther.decrease_stat('strength')
        else:
            main_characther.decrease_stat('dexterity')


    if strength == 1:
        text_manager.get_text_from_json("CharactherCreation", "choose_intelligince_negative_ability")

    if dexterity == 1:
        text_manager.get_text_from_json("CharactherCreation", "choose_intelligince_negative_ability")  
                 


def execute():
    text_manager.get_text_from_json("CharactherCreation","enterance")
    get_charachter_name()
    choose_posstive_ability()
    choose_negative_ability()
    

# Spagetti neydi ? Spagetti emekti. BURAYI ADAM ETMENİN YOLUNU BULMAYI UNUTNMA