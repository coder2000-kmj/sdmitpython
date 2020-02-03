trans=[]

def show(index=0):
    if index<len(trans):
        print(trans[index])
        index+=1;show(index)
    else:
        return
'''trans.append('credit')
trans.append('debit')
trans.append('debit')
trans.append('debit')
trans.append('credit')
show()
'''
