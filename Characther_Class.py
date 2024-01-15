import shared_data

class Characther_Class:
    def __init__(self):
        self.prof = 0
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

    def get_test(self):
        return self.test
    
    def is_str_prof():
        return False
    
    def str_check():
        return 16
    
    def str_savingthrow(self):
        return self.str_check() + self.prof


class Barbarian(Characther_Class):

    def __init__(self):
        self.prof = 2

    def is_str_prof():
        return True
    
    def set_class_to_barbarian(characther):
        Deneme = Characther_Class(test=True)
        characther.set_characther_class('Barbarian')
        x = Deneme.get_test()
        print(x)



    def Rage():
       pass

class Cleric(Characther_Class,):
    Characther_Class(test=False)

    def set_class_to_cleric(characther):
        Deneme = Characther_Class(test=False)
        characther.set_characther_class('Cleric')
        x = Deneme.get_test()
        print(x)

