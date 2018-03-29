

'''
Hero who is allergic to apples.

'''

class Hero(object):
    
    def __init__(self, name):

        self.name = name
        self.health = 100
        print "Present hero name : ", self.name
        print "Present health status : ", self.health
        

    def allergic_apples(self, fruit=None, query_params=False):
        
        print "Fruit : ", fruit
        if query_params:
           print "query_params is True"             
        else:
           print "query_params is False"             

        if fruit == "apple":
            self.health-=10
            print "health decreased : ", self.health
        else:
            self.health+=10
            print "health increased : ", self.health



hero_obj = Hero("Omkar")
hero_obj.allergic_apples("orange", True)
