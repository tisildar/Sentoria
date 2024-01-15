import random
import Characther_Class
from text_manager_old import General

def strength_check(characther,DC):
        roll = random.randint(1,20)
        bonus = characther.get_strength()

        result = roll + bonus
        General.space()
        if result >= DC:
            print("BAŞARILI")
            check_status = True
        else:
            print("BAŞARISIZ")
            check_status = False
        print(f'Gelen zar = {roll}')
        print(f'Streght bonsunu = {bonus}')
        print(f'Sonuç = {result}')
        print(f'Başarılı olmak için gereken minumum skor = {DC}')
        return check_status
        
def strength_saving_throw(characther,DC):
        roll = random.randint(1,20)
        strength_bonus = characther.get_strength_bonus()
        characther_class = characther.get_characther_class()
        proficiency_bonus = 0
        is_have_proficiency = characther.is_str_prof()

        # if characther_class == 'Barbarian' or characther_class == 'Fighter' or characther_class == 'Monk' or characther_class == 'Ranger':
            #is_have_proficiency = True

        if is_have_proficiency == True:
             proficiency_bonus = 2

        result = roll + strength_bonus + proficiency_bonus
        General.space()
        if result >= DC:
            print("BAŞARILI")
            check_status = True
        else:
            print("BAŞARISIZ")
            check_status = False
        print(f'Gelen zar = {roll}')
        print(f'Streght bonsunu = {strength_bonus}')
        print(f'Proficiency bonsunu = {proficiency_bonus}')
        print(f'Sonuç = {result}')
        print(f'Başarılı olmak için gereken minumum skor = {DC}')
        return check_status

def dexterity_check(characther,DC):
        roll = random.randint(1,20)
        bonus = characther.get_dexterity()

        result = roll + bonus
        General.space()
        if result >= DC:
            print("BAŞARILI")
            check_status = True
        else:
            print("BAŞARISIZ")
            check_status = False
        print(f'Gelen zar = {roll}')
        print(f'Streght bonsunu = {bonus}')
        print(f'Sonuç = {result}')
        print(f'Başarılı olmak için gereken minumum skor = {DC}')
        return check_status
        
def dexterity_saving_throw(characther,DC):
        roll = random.randint(1,20)
        dexterity_bonus = characther.get_dexterity_bonus()
        characther_class = characther.get_characther_class()
        proficiency_bonus = 0
        is_have_proficiency = False

        if characther_class == 'Bard' or characther_class == 'Monk' or characther_class == 'Ranger' or characther_class == 'Rouge':
            is_have_proficiency = True

        if is_have_proficiency == True:
             proficiency_bonus = 2

        result = roll + dexterity_bonus + proficiency_bonus
        General.space()
        if result >= DC:
            print("BAŞARILI")
            check_status = True
        else:
            print("BAŞARISIZ")
            check_status = False
        print(f'Gelen zar = {roll}')
        print(f'Dexterity bonsunu = {dexterity_bonus}')
        print(f'Proficiency bonsunu = {proficiency_bonus}')
        print(f'Sonuç = {result}')
        print(f'Başarılı olmak için gereken minumum skor = {DC}')
        return check_status

def constituion_check(characther,DC):
        roll = random.randint(1,20)
        bonus = characther.get_constituion()

        result = roll + bonus
        General.space()
        if result >= DC:
            print("BAŞARILI")
            check_status = True
        else:
            print("BAŞARISIZ")
            check_status = False
        print(f'Gelen zar = {roll}')
        print(f'Constituion bonsunu = {bonus}')
        print(f'Sonuç = {result}')
        print(f'Başarılı olmak için gereken minumum skor = {DC}')
        return check_status
        
def constituion_saving_throw(characther,DC):
        roll = random.randint(1,20)
        constituion_bonus = characther.get_constituion_bonus()
        characther_class = characther.get_characther_class()
        proficiency_bonus = 0
        is_have_proficiency = False

        if characther_class == 'Barbarian' or characther_class == 'Fighter' or characther_class == 'Sorcerer' or characther_class == 'Warlock':
            is_have_proficiency = True

        if is_have_proficiency == True:
             proficiency_bonus = 2

        result = roll + constituion_bonus + proficiency_bonus
        General.space()
        if result >= DC:
            print("BAŞARILI")
            check_status = True
        else:
            print("BAŞARISIZ")
            check_status = False
        print(f'Gelen zar = {roll}')
        print(f'Constituion bonsunu = {constituion_bonus}')
        print(f'Proficiency bonsunu = {proficiency_bonus}')
        print(f'Sonuç = {result}')
        print(f'Başarılı olmak için gereken minumum skor = {DC}')
        return check_status

def intelligince_check(characther,DC):
        roll = random.randint(1,20)
        bonus = characther.get_intelligince()

        result = roll + bonus
        General.space()
        if result >= DC:
            print("BAŞARILI")
            check_status = True
        else:
            print("BAŞARISIZ")
            check_status = False
        print(f'Gelen zar = {roll}')
        print(f'Intelligince bonsunu = {bonus}')
        print(f'Sonuç = {result}')
        print(f'Başarılı olmak için gereken minumum skor = {DC}')
        return check_status
        
def intelligince_saving_throw(characther,DC):
        roll = random.randint(1,20)
        intelligince_bonus = characther.get_intelligince_bonus()
        characther_class = characther.get_characther_class()
        proficiency_bonus = 0
        is_have_proficiency = False

        if characther_class == 'Druid' or characther_class == 'Rogue'or characther_class == 'Wizard':
            is_have_proficiency = True

        if is_have_proficiency == True:
             proficiency_bonus = 2

        result = roll + intelligince_bonus + proficiency_bonus
        General.space()
        if result >= DC:
            print("BAŞARILI")
            check_status = True
        else:
            print("BAŞARISIZ")
            check_status = False
        print(f'Gelen zar = {roll}')
        print(f'Intelligince bonsunu = {intelligince_bonus}')
        print(f'Proficiency bonsunu = {proficiency_bonus}')
        print(f'Sonuç = {result}')
        print(f'Başarılı olmak için gereken minumum skor = {DC}')
        return check_status

def wisdom_check(characther,DC):
        roll = random.randint(1,20)
        bonus = characther.get_wisdom()

        result = roll + bonus
        General.space()
        if result >= DC:
            print("BAŞARILI")
            check_status = True
        else:
            print("BAŞARISIZ")
            check_status = False
        print(f'Gelen zar = {roll}')
        print(f'Wisdom bonsunu = {bonus}')
        print(f'Sonuç = {result}')
        print(f'Başarılı olmak için gereken minumum skor = {DC}')
        return check_status
        
def wisdom_saving_throw(characther,DC):
        roll = random.randint(1,20)
        wisdom_bonus = characther.get_wisdom_bonus()
        characther_class = characther.get_characther_class()
        proficiency_bonus = 0
        is_have_proficiency = False

        if characther_class == 'Cleric' or characther_class == 'Druid' or characther_class == 'Paladin' or characther_class == 'Wizard':
            is_have_proficiency = True

        if is_have_proficiency == True:
             proficiency_bonus = 2

        result = roll + wisdom_bonus + proficiency_bonus
        General.space()
        if result >= DC:
            print("BAŞARILI")
            check_status = True
        else:
            print("BAŞARISIZ")
            check_status = False
        print(f'Gelen zar = {roll}')
        print(f'Wisdom bonsunu = {wisdom_bonus}')
        print(f'Proficiency bonsunu = {proficiency_bonus}')
        print(f'Sonuç = {result}')
        print(f'Başarılı olmak için gereken minumum skor = {DC}')
        return check_status

def charisma_check(characther,DC):
        roll = random.randint(1,20)
        bonus = characther.get_charisma()

        result = roll + bonus
        General.space()
        if result >= DC:
            print("BAŞARILI")
            check_status = True
        else:
            print("BAŞARISIZ")
            check_status = False
        print(f'Gelen zar = {roll}')
        print(f'Charisma bonsunu = {bonus}')
        print(f'Sonuç = {result}')
        print(f'Başarılı olmak için gereken minumum skor = {DC}')
        return check_status
        
def charisma_saving_throw(characther,DC):
        roll = random.randint(1,20)
        charisma_bonus = characther.get_charisma_bonus()
        characther_class = characther.get_characther_class()
        proficiency_bonus = 0
        is_have_proficiency = False

        if characther_class == 'Bard' or characther_class == 'Cleric' or characther_class =='Paladin' or characther_class == 'Sorcerer' or characther_class == 'Warlock':
            is_have_proficiency = True

        if is_have_proficiency == True:
             proficiency_bonus = 2

        result = roll + charisma_bonus + proficiency_bonus
        General.space()
        if result >= DC:
            print("BAŞARILI")
            check_status = True
        else:
            print("BAŞARISIZ")
            check_status = False
        print(f'Gelen zar = {roll}')
        print(f'Charisma bonsunu = {charisma_bonus}')
        print(f'Proficiency bonsunu = {proficiency_bonus}')
        print(f'Sonuç = {result}')
        print(f'Başarılı olmak için gereken minumum skor = {DC}')
        return check_status