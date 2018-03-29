

'''
Inheritance demo
'''

class Character(object):
    
    def __init__(self, name):
        self.name = name
        self.health = 100

  

class ArmyMajor(Character):
    
    def __init__(self, name):

        # super(CallingClassName, TypeofCallingClass).__init__(VariablesOfBaseClass)
        super(ArmyMajor, self).__init__(name)


a_obj = ArmyMajor("Omkar")
print a_obj.name
