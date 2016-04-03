# -*- encoding: utf-8 -*-

y = int(raw_input("Vnesi številko med 1 in 100:"))

for x in range(1, y):


    if  x % 3 == 0:
        print ("FiZz")
    elif  x % 5 == 0:
        print ("BuZz")
    elif (x % 3) ==0  & (x % 5) == 0:
        print ("FiZzBuZz")
    else:
        print x




