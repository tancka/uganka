# -*- encoding: utf-8 -*-
resitev = 5
 # print (resitev)

while True:

    ugibaj = int(raw_input("Ugibaj številko:")) #int ne rabis

    if ugibaj == resitev:
        print ("Bravoooooooooooo! ;)")
        break
    elif ugibaj < resitev:
        print ("Ups, prava številka je še višja!:0")

    else:
        print ("Ajoj, prava številka je nižja! :/")

