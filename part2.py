Capitals = {}

count = 0
while count == 0:
    person = int(input("Press 1 to add, 2 to change, 3 to delete, 4 to display keys, 5 to display values, or 6 to stop"))
    if person == 1:
        addCountry = input("What country?")
        addCapital = input("What capital")
        Capitals[addCountry] = addCapital
    elif person == 2:
        changeCountry = input("What country do you want to change?")
        changeCapital = input("What capital do you want to change?")
        Capitals[changeCountry] = changeCapital
    elif person == 3:
        delCountry = input("What country do you want to delete?")
        del(Capitals[delCountry])
    elif person == 4:
        print(Capitals.keys())
    elif person ==5:
        print(Capitals.values())
    elif person ==6:
        break
