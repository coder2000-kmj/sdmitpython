ctc=[4.5,9.2,5.6,12.5,3.7,1.9,12.3]
pos,tenor=0,0
def find():
    try:
        pos = int(input("Tell us position: "))
        tenor = int(input("Tell us how you wish payment to be done: "))
        print((ctc[pos - 1] / tenor) * 100000)
    except Exception as e:raise e;

#function call recursivly
try:
    find()
except ValueError as ve:
    try:print("Enter only numeric");find()
    except IndexError as ie:
        try:print("Index should be <",len(ctc));find()
        except ZeroDivisionError as ze:
            try:print("tenor shouldn't 0");find()
            except Exception as e:print(e)
except IndexError as ie:
    try:print("Index should be <",len(ctc));find()
    except ZeroDivisionError as ze:
        print("tenor shouldn't 0");find()