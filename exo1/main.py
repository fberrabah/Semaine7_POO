from city import City

paris = City("Paris", 75)
paris.show_location()

lille = City("Lille", 59)
lille.show_location()

lyon = City("Lyon", 69)
lyon.show_location()

marseille = City("Marseille", 13)
marseille.show_location()


paris = City("Paris", 75000)
paris.change_location()

lille = City("Lille", 59000)
lille.change_location()

lyon = City("Lyon", 69000)
lyon.change_location()

marseille = City("Marseille", 13000)
marseille.change_location()
