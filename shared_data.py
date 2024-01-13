class SharedData:
    def __init__(self, strength, dexterity,constituion, intelligince, wisdom, charisma, health,char_name,char_class):
        self.__strength = strength
        self.__dexterity = dexterity
        self.__constituion = constituion
        self.__intelligence = intelligince
        self.__wisdom = wisdom
        self.__charisma = charisma        
        self.__current_health = health
        self.__max_health = health
        self.__char_name = char_name
        self.__char_class = char_class

    def get_strength(self):
        return self.__strength   

    def get_dexterity(self):
        return self.__dexterity
    
    def get_constituion(self):
        return self.__constituion
    
    def get_intelligence(self):
        return self.__intelligence
    
    def get_wisdom(self):
        return self.__wisdom
    
    def get_charisma(self):
        return self.__charisma
    
    def get_strength_bonus(self):
        current_strength = self.__strength
        strength_bonus = (current_strength-10)/2
        return strength_bonus
    
    def get_dexterity_bonus(self):
        current_dexterity = self.__dexterity
        dexterity_bonus = (current_dexterity-10)/2
        return dexterity_bonus
    
    def get_constituion_bonus(self):
        current_constituion = self.__constituion
        constituion_bonus = (current_constituion-10)/2
        return constituion_bonus
    
    def get_intelligence_bonus(self):
        current_intelligence = self.__intelligence
        intelligence_bonus = (current_intelligence-10)/2
        return intelligence_bonus
    
    def get_wisdom_bonus(self):
        current_wisdom = self.__wisdom
        wisdom_bonus = (current_wisdom-10)/2
        return wisdom_bonus
    
    def get_charisma_bonus(self):
        current_charisma = self.__charisma
        charisma_bonus = (current_charisma-10)/2
        return charisma_bonus
    
    def get_current_health(self):
        return self.__current_health
    
    def increase_current_health(self):
        self.__current_health += 1
        return self.__current_health
    
    def set_current_health(self,value):
        self.__current_health = value
        return self.__current_health
    
    def get_max_health(self):
        return self.__max_health
    
    def increase_max_health(self):
        self.__max_health += 1
        return self.__max_health

    def get_char_name(self):
        return self.__char_name    
    
    def set_char_name(self):
        self.__char_name = input('Karakterinin ismini yaz: ')
        return self.__char_name
    
    def set_characther_class(self,value):
        self.__char_class = value
        return self.__char_class
    
    def get_characther_class(self):
        return self.__char_class
    
    def increase_stat(self,type):

        if type == 'strength':
            self.__strength += 1
            return self.__strength
        
        elif type == 'dexterity':
            self.__dexterity += 1
            return self.__dexterity
        
        elif type == 'intelligince':
            self.__intelligence += 1
            return self.__intelligence
        else:
            raise Exception("Yanlış stat tipi girdiniz")
            
    def decrease_stat(self,type):

        if type == 'strength':
            self.__strength -= 1
            return self.__strength
        
        elif type == 'dexterity':
            self.__dexterity -= 1
            return self.__dexterity
        
        elif type == 'intelligence':
            self.__intelligence -= 1
            return self.__intelligence
        else:
            raise Exception("Yanlış stat tipi girdiniz")
        


