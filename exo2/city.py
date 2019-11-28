from cities import *
class City:
    def __init__(self, i):
        self.name = None
        self.departement = None
        self.country = None
        self.population = None
        self.mayor = None
        self.capital = None
        self.king = None
        self.hydrat(i)

    def hydrat(self, i):
        for key_name, value_name in i.items():
            if hasattr(self, key_name):
                setattr(self, key_name, value_name)

    def show_location(self):
        print("la ville {} est dans le département {}".format(self.ville,self.dep))

    def change_location(self):
        print("la ville {} est dans le département {}".format(self.ville,self.dep ))

    def show_information(self):
        text = "------------------\n \
        Name: {}\n \
        Departement: {}\n \
        Country : {}\n \
        Population {}\n \
        Mayor: {}\n \
        Capital: {}\n" 

        print(text.format(self.name, self.departement, self.country, self.population, self.mayor, self.capital))