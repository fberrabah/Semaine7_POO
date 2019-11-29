from city import City #import City for take def 


paris = City("Paris", 75) #add paris for City with key and value
paris.show_location()#start show_location with info paris

lille = City("Lille", 59)
lille.show_location()

lyon = City("Lyon", 69)
lyon.show_location()

marseille = City("Marseille", 13)
marseille.show_location()


paris = City("Paris", 75000) #add paris for City with new value
paris.change_location() #start paris with change_location()

lille = City("Lille", 59000)
lille.change_location()

lyon = City("Lyon", 69000)
lyon.change_location()

marseille = City("Marseille", 13000)
marseille.change_location()
