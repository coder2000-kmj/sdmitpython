#calculator
one,two=0,0
try:
    one=float(input("First data"))
    two=float(input("Second data"))
except ValueError as verror:
    print(verror,"\nEnter only numeric data")
    one = float(input("First data"))
    two = float(input("Second data"))
finally:
    option = input("operation to do...")
    if option == "+":print(one + two)
    elif option == "-":print(one - two)
    elif option == "*":print(one * two)
    elif option == "/":print(one / two)
    print("Calculation done")