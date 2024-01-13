import random
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
        is_have_proficiency = False

        if characther_class == 'Barbarian':
            is_have_proficiency = True

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

