import shared_data
import dice_system

main_characther = shared_data.SharedData(strength=0,dexterity=0, constituion=0,intelligince=0, wisdom= 0, charisma=0, health=3,char_name='',char_class='Bard')
enemy = shared_data.SharedData(strength=0,dexterity=0, constituion=0,intelligince=0, wisdom= 0, charisma=0, health=3,char_name='',char_class='')

dice_system.dexterity_saving_throw(main_characther,15)