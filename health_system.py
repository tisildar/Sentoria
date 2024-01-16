from Characthers import main_characther
import sys

def gain_life():
    main_characther.increase_max_health()
    main_characther.increase_current_health()

def loose_life(value, characther):
    current_life = characther.get_current_health()
    current_life = current_life - value
    characther.set_current_health(current_life)
    game_over()
    
def heal(value, characther):
    max_health = characther.get_max_health()
    current_health = characther.get_current_health()
    for _ in range(value):
        if current_health<max_health:
            characther.increase_current_health()
            current_health = characther.get_current_health()
        else:
            break

def game_over():
    current_health = main_characther.get_current_health()
    if current_health < 1:
        print("GAME OVER")
        sys.exit()
    else:
        pass 
