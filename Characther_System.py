class create_characther:
    def __init__(self,strength,dexterity,constituion,intelligence,wisdom,charisma,health,char_name,char_class):
        self.strength_prof = 0
        self.dexterity_prof = 0
        self.constituion_prof = 0
        self.intelligence_prof = 0
        self.wisdom_prof = 0
        self.charisma_prof = 0
        self.__char_class = char_class
        self.__current_health = health
        self.__max_health = health
        self.__char_name = char_name
        self.__strength = strength
        self.__dexterity = dexterity
        self.__constituion = constituion
        self.__intelligence = intelligence
        self.__wisdom = wisdom
        self.__charisma = charisma   

    def set_characther_class(self,value):
        self.__char_class = value
        return self.__char_class
    
    def get_characther_class(self):
        return self.__char_class
    
    def get_current_health(self):
        return self.__current_health
    
    def set_current_health(self,value):
        self.__current_health = value
        return self.__current_health
    
    def increase_current_health(self):
        self.__current_health += 1
        return self.__current_health
        
    def get_max_health(self):
        return self.__max_health
    
    def set_max_health(self,value):
        return self.__max_health + value
    
    def increase_max_health(self):
        self.__max_health += 1
        return self.__max_health
      
    def get_char_name(self):
        return self.__char_name    
    
    def set_char_name(self):
        self.__char_name = input('Karakterinin ismini yaz: ')
        return self.__char_name
    
    def get_strength_score(self):
        return self.__strength   
    
    def set_strength_score(self,value):
        return self.__strength + value

    def get_strength_bonus(self):
        return  (self.__strength -10) / 2

    def get_strength_savinthrow(self):
        return (self.__strength -10) / 2 + self.strength_prof
    
    def get_dexterity_score(self):
        return self.__dexterity   
    
    def set_dexterity_score(self,value):
        return self.__dexterity + value

    def get_dexterity_bonus(self):
        return  (self.__dexterity -10) / 2

    def get_dexterity_savingthrow(self):
        return (self.__dexterity -10) / 2 + self.dexterity_prof
    
    def get_constituion_score(self):
        return self.__constituion   
    
    def set_constituion_score(self,value):
        return self.__constituion + value

    def get_constituion_bonus(self):
        return  (self.__constituion -10) / 2

    def get_constituion_savingthrow(self):
        return (self.__constituion -10) / 2 + self.constituion_prof
    
    def get_intelligince_score(self):
        return self.__intelligence
    
    def set_intelligence_score(self,value):
        return self.__intelligence + value

    def get_intelligence_bonus(self):
        return  (self.__intelligence -10) / 2

    def get_intelligence_savingthrow(self):
        return (self.__intelligence -10) / 2 + self.intelligence_prof    
    
    def get_wisdom_score(self):
        return self.__wisdom 
    
    def set_wisdom_score(self,value):
        return self.__wisdom + value

    def get_wisdom_bonus(self):
        return  (self.__wisdom -10) / 2

    def get_wisdom_savingthrow(self):
        return (self.__wisdom -10) / 2 + self.wisdom_prof 

    def get_charisma_score(self):
        return self.__charisma 
    
    def set_charisma_score(self,value):
        return self.__charisma + value

    def get_charisma_bonus(self):
        return  (self.__charisma -10) / 2

    def get_charisma_savingthrow(self):
        return (self.__charisma -10) / 2 + self.charisma_prof     

class Barbarian(create_characther):
    
    def set_class_to_barbarian(characther):
        characther.set_characther_class('Barbarian')
        characther.strength_prof = 2
        characther.constituion_prof = 2
        

class Bard(create_characther):
    
    def set_class_to_bard(characther):
        characther.set_characther_class('Bard')
        characther.dexterity_prof = 2
        characther.charisma_prof = 2   

class Cleric(create_characther):

    def set_class_to_cleric(characther):
        characther.set_characther_class('Cleric')
        characther.wisdom_prof = 2
        characther.charisma_prof = 2

class Druid(create_characther):

    def set_class_to_druid(characther):
        characther.set_characther_class('Druid')
        characther.intelligence_prof = 2
        characther.wisdom_prof = 2

class Fighter(create_characther):

    def set_class_to_fighter(characther):
        characther.set_characther_class('Fighter')
        characther.strength_prof = 2
        characther.dexterity_prof = 2

class Monk(create_characther):

    def set_class_to_monk(characther):
        characther.set_characther_class('Monk')
        characther.dexterity_prof = 2
        characther.wisdom_prof = 2

class Paladin(create_characther):

    def set_class_to_paladin(characther):
        characther.set_characther_class('Paladin')
        characther.strength_prof = 2
        characther.charisma_prof = 2

class Ranger(create_characther):

    def set_class_to_ranger(characther):
        characther.set_characther_class('Ranger')
        characther.strength_prof = 2
        characther.dexterity_prof = 2

class Rouge(create_characther):

    def set_class_to_rouge(characther):
        characther.set_characther_class('Rouge')
        characther.dexterity_prof = 2
        characther.intelligence_prof = 2  

class Sorcerer(create_characther):

    def set_class_to_sorcerer(characther):
        characther.set_characther_class('Sorcerer')
        characther.constituion_prof = 2
        characther.charisma_prof = 2

class Warlock(create_characther):

    def set_class_to_warlock(characther):
        characther.set_characther_class('Warlock')
        characther.wisdom_prof = 2
        characther.charisma_prof = 2

class Wizard(create_characther):

    def set_class_to_wizard(characther):
        characther.set_characther_class('Wizard')
        characther.intelligence_prof = 2
        characther.wisdom_prof = 2