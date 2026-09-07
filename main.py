#temp converter 
import converters

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
            print("F is: ",converters.ctof(a))
        except ValueError:
            print("error in input")

    elif(x == 2):
        try:
            print("F to C converter: input Farhenheit")
            a = float(input())
            print("C is: ",converters.ftoc(a))
        except ValueError:
            print("error in input")

    elif(x == 3):
        break

    else:
        print("input didn't match anything")

