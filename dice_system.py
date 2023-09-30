import random
from text_manager_old import General

def strength_check(characther,DC):
        roll = random.randint(1,6)
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
        
def dexterity_check(characther,DC):
    roll = random.randint(1,6)
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
    print(f'Çeviklik bonsunu = {bonus}')
    print(f'Sonuç = {result}')
    print(f'Başarılı olmak için gereken minumum skor = {DC}')
    return check_status

    
def intelligence_check(characther,DC):
    roll = random.randint(1,6)
    bonus = characther.get_intelligence()
    result = roll + bonus
    General.space()
    if result >= DC:
        print("BAŞARILI")
        check_status = True
    else:
        print("BAŞARISIZ")
        check_status = False
    print(f'Gelen zar = {roll}')
    print(f'Zeka bonsunu = {bonus}')
    print(f'Sonuç = {result}')
    print(f'Başarılı olmak için gereken minumum skor = {DC}')
    return check_status
    
    
def luck_check(DC):
    roll = random.randint(1,6)
    General.space()
    print(f'Gelen zar = {roll}')
    result = roll 
    if result >= DC:
        print("BAŞARILI")
        check_status = True
    else:
        print("BAŞARISIZ")
        check_status = False
    print(f'Sonuç = {result}')
    print(f'Başarılı olmak için gereken minumum skor = {DC}')
    return check_status
    
def strenght_passive_check(characther,DC):
    roll = random.randint(1,6)
    bonus = characther.get_strength()
    check_status = False
    result = roll + bonus
    if result >= DC:
        check_status = True
    else:
        check_status = False
    return check_status

def dexterity_passive_check(characther,DC):
    roll = random.randint(1,6)
    bonus = characther.get_dexterity()
    check_status = False
    Result = roll + bonus
    if Result >= DC:
        check_status = True
    else:
        check_status = False
    return check_status

def intelligence_passive_check(characther,DC):
    roll = random.randint(1,6)
    bonus = characther.get_intelligence()
    check_status = False
    result = roll + bonus
    if result >= DC:
        check_status = True
    else:
        check_status = False
    return check_status

def luck_passive_check(DC):
    roll = random.randint(1,6)
    check_status = False
    if roll >= DC:
        check_status = True
    else:
        check_status = False
    return check_status