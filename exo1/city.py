class City: #new class 
    def __init__(self, ville, dep): #my constructeur with self ville and dep
        self.ville = ville
        self.dep = dep

    def show_location(self): #def show who display ville and dep
        print("la ville {} est dans le département {}".format(self.ville,self.dep))

    def change_location(self): #def change who display ville and new dep 
        print("la ville {} est dans le département {}".format(self.ville,self.dep ))