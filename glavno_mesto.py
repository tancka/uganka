# -*- encoding: utf-8 -*-
print ("Ugani glavno mesto")
drzave_mesta = {"Slovenije": "Ljubljana",
        "Hrvaške": "Zagreb",
        "Italije": "Rim",
        "Nemčije": "Berlin",
        "Avstrije": "Dunaj",
        "Rusije":"Moskva",
        "Albanije":"Tirana",
        "Grčije": "Atene",}


def ugani_mesto():

    for drzava, mesto in drzave_mesta.iteritems():
        ugibaj = raw_input("Katero je glavno mesto " + (drzava)+ "?")
        if ugibaj == mesto:
            print ("Odgovor je pravilen")
        elif ugibaj != mesto:
            print ("Odgovor je napačen")

if __name__ == "__main__":
    ugani_mesto()

#stevec
