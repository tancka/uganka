# -*- encoding: utf-8 -*-

dna = raw_input("Prosim vnesite dna osumljenca: ")


print("Barva las:")
crna = dna.find("CCAGCAATCGC")
#print dna.find("CCAGCAATCGC")
rjava = dna.find("GCCAGTGCCG")
#print dna.find("GCCAGTGCCG")
korencek = dna.find("TTAGCTATCGC")
#print dna.find("TTAGCTATCGC")

if crna > -1 :
    print("črna")
if rjava > -1 :
    print("rjava")
if korencek > -1 :
    print("korenček")

print("Oblika obraza:")
kvadraten = dna.find("GCCACGG")
#print dna.find("GCCACGG")
okrogel = dna.find("ACCACAA")
#print dna.find("ACCACAA")
ovalen = dna.find("AGGCCTCA")
#print dna.find("AGGCCTCA")

if kvadraten > -1 :
    print("kvadraten")
if okrogel > -1 :
    print("okrogel")
if ovalen > -1 :
    print("ovalen")


print("Barva oči:")
modra = dna.find("TTGTGGTGGC")
#print dna.find("TTGTGGTGGC")
zelena = dna.find("GGGAGGTGGC")
#print dna.find("GGGAGGTGGC")
rjava = dna.find("AAGTAGTGAC")
#print dna.find("AAGTAGTGAC")

if modra > -1 :
    print("modra")
if zelena > -1 :
    print("zelena")
if rjava > -1 :
    print("rjava")


print("Spol:")
moski = dna.find("TGCAGGAACTTC")
#print dna.find("TGCAGGAACTTC")
zenska = dna.find("TGAAGGACCTTC")
#print dna.find("TGAAGGACCTTC")

if moski > -1 :
    print("moški")
if zenska > -1 :
    print("ženska")

print("Rasa:")
belec = dna.find("AAAACCTCA")
#print dna.find("AAAACCTCA")
crnec= dna.find("CGACTACAG")
#print dna.find("CGACTACAG")
azijec = dna.find("CGCGGGCCG")
#print dna.find("CGCGGGCCG")

if belec > -1 :
    print("belec")
if crnec > -1 :
    print("crnec")
if azijec > -1 :
    print("azijec")


