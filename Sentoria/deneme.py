import character_creation
import dice_system
from characthers import main_characther


character_creation.execute()

dice_system.strength_check(main_characther,3)
dice_system.intelligence_check(main_characther,3)
dice_system.dexterity_check(main_characther,3)
