# -*- encoding: utf-8 -*-
class Kontakti:
    def __init__(self, first_name, last_name, email, phone, address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
    def to_string(self):
        return Kontakti.to_string(self)

while True:
    dodaj = raw_input("Do you want to add a new contact? yes/no" )
    belezka = Kontakti(first_name ="", last_name="", email="", phone="", address="")

    if dodaj == "yes":
        Kontakti(first_name= raw_input("Enter first name:"),
        last_name= raw_input("Enter last name:"),
        email= raw_input("Enter email:"),
        phone= raw_input("Enter phone number:"),
        address= raw_input("Enter home address:"))
    if dodaj == "no":
        print ("Check your contact list below:")
        break

belezka = Kontakti(first_name="Name", last_name="", email ="",phone ="", address="")
print belezka

#print moram naštudirat...mi je zmanjkalo časa :)










