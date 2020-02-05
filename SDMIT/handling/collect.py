ctc=[4.5,9.2,5.6,12.5,3.7,1.9,12.3]
try:
    pos = int(input("Tell us position: "))
    tenor = int(input("Tell us how you wish payment to be done: "))
    print((ctc[pos - 1] / tenor) * 100000)
except ValueError as verror:
    print("\nEnter only numeric: ")
    pos = int(input("Tell us position: "))
    tenor = int(input("Tell us how you wish payment to be done: "))
    print((ctc[pos - 1] / tenor) * 100000)
except ZeroDivisionError as zerror:
    tenor = int(input("Tell us payment to be done Not 0: "))
    print((ctc[pos - 1] / tenor) * 100000)
except IndexError as ierror:
    print(ierror,"\nTell the position within",len(ctc))
    pos = int(input("Tell us position: "))
    tenor = int(input("Tell us how you wish payment to be done: "))
    print((ctc[pos - 1] / tenor) * 100000)
except Exception as error:print(error)