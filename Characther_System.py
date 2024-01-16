import shared_data

class Characther_Class:
    def __init__(self,strength,dexterity,constituion,intelligince,wisdom,charisma,health,char_name,char_class):
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
        self.__intelligence = intelligince
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

    def get_strength_savingthrow(self):
        return ((self.__strength -10) / 2) + self.strength_prof
    
    def get_dexterity_score(self):
        return self.__dexterity   
    
    def set_dexterity_score(self,value):
        return self.__dexterity + value

    def get_dexterity_bonus(self):
        return  (self.__dexterity -10) / 2

    def get_dexterity_savingthrow(self):
        return ((self.__dexterity -10) / 2) + self.dexterity_prof
    
class Barbarian(Characther_Class):

    def __init__(self):
        self.strength_prof = 2
    
    def set_class_to_barbarian(characther):
        characther.set_characther_class('Barbarian')

    def Rage():
       pass

class Cleric(Characther_Class,):
    Characther_Class(test=False)

    def set_class_to_cleric(characther):
        Deneme = Characther_Class(test=False)
        characther.set_characther_class('Cleric')
        x = Deneme.get_test()
        print(x)

