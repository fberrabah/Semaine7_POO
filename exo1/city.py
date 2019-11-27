class City:
    def __init__(self, ville, dep):
        self.ville = ville
        self.dep = dep

    def show_location(self):
        print("la ville {} est dans le département {}".format(self.ville,self.dep))

    def change_location(self):
        print("la ville {} est dans le département {}".format(self.ville,self.dep ))