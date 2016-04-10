# -*- encoding: utf-8 -*-

print ("Trenutno na voljo:")
print ("mleko, cedevita, solata, lesniki, bonboni") #(kako/ali se lahko printa samo keys iz dictionary?)

izdelki_cene = {"mleko": "1,15",
        "cedevita": "5,56",
        "solata": "7,09",
        "lesniki": "3,45",
        "bonboni": "2,15"
}
def izpisi_ceno():
    for izdelek,cene in izdelki_cene.iteritems():
        izbrani_izdelek = raw_input("Izberi izdelek:")

        if izbrani_izdelek in izdelki_cene:
            cena = izdelki_cene[izbrani_izdelek]
            print "Cena tega izdelka znaša %s €"%(cena)

        else:
            print "Izdelek žal ni na voljo."
if __name__ == "__main__":
    izpisi_ceno()
