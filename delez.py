# -*- encoding: utf-8 -*-

# x = število mladih
# y = vsi prebivalci

def delez(x, y):
    result =int((x / y)*100)
    return result

def main():
    print ("Vrednost deleža mladih:")
    print delez(30,120.0),("%")

if __name__ == "__main__":
    main()

#x, y -raw_input?

