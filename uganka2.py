# -*- encoding: utf-8 -*-
resitev = 5
ugibaj = 0
 # print (resitev)

while resitev != int(ugibaj):

    ugibaj = int(raw_input("Izvoli, ugibaj številko:"))

    if ugibaj == resitev:
        print ("Bravoooooooooooo! ;)")
    elif ugibaj < resitev:
        print ("Ups, prava številka je še višja!:0")
    else:
        print ("Ajoj, prava številka je nižja! :/")