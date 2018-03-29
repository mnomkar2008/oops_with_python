
'''
Overriding example
'''


class Baseclass(object):
    
    def __init__(self):
        self.x = 30



class Iseclass(Baseclass):
    def __init__(self):
        self.y = 90


#obj = Iseclass()
obj = Baseclass()
print "x value : ", obj.x
