#temp converter C to F

try:
    print("C to F converter: input Celsius")
    c = float(input())
    f = (c*1.8)+32
    print("F is: ",f)
except ValueError:
    print("error in input")

