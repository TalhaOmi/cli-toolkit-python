#temp converter 

while True:
    print("1: Celsius to Fahrenheit")
    print("2: Fahrenheit to Celsius")
    print("3: Quit")

    try:
        x = int(input())
    except (NameError,ValueError):
        print("error in input")
        continue #it helps to continue the loop as asada type of input checks with the if loop for the next line so different error ends here
    
    if(x == 1):
        try:
            print("C to F converter: input Celsius")
            a = float(input())
            b = (a*1.8)+32
            print("F is: ",b)
        except ValueError:
            print("error in input")

    elif(x == 2):
        try:
            print("F to C converter: input Farhenheit")
            c = float(input())
            d = (c-32)/1.8
            print("C is: ",d)
        except ValueError:
            print("error in input")

    elif(x == 3):
        break

    else:
        print("input didn't match anything")

