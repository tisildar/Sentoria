class SharedData:
    def __init__(self, strength, dexterity, intelligince, health,char_name):
        self.__strength = strength
        self.__dexterity = dexterity
        self.__intelligence = intelligince
        self.__current_health = health
        self.__max_health = health
        self.__char_name = char_name

    def get_strength(self):
        return self.__strength   

    def get_dexterity(self):
        return self.__dexterity
    
    def get_intelligence(self):
        return self.__intelligence
    
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
        


