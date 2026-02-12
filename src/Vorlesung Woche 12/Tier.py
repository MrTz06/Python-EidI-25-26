class Tier(object):
    #Konstruktor
    def __init__(self, alter):
        self.jahre = alter
        self.name = None

    #getter und setter Methoden
    def get_alter(self):
        return self.jahre
    def get_name(self):
        return self.name
    def set_alter(self, neues_alter=None):
        self.jahre = neues_alter
    def set_name(self, neuer_name=""):
        self.name = neuer_name



    def __str__(self):
        return "Tier:"+str(self.name)+":"+str(self.jahre)

