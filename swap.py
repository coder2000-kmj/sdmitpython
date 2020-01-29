#swap bike price
r15=int(input("Tell us bike price of Honda R15: "))
fz=int(input("Tell us bike price of Yamaha FZS: "))

'''#using temp
temp=r15;r15=fz;fz=temp
print("Price of R15: ",r15,"Price of Yamaha FZS:",fz)

#using + and -
r15+=fz;fz=r15-fz;r15-=fz

#using * /
r15*=fz;fz=r15/fz;r15/=fz
'''

#using ^
r15^=fz;fz^=r15;r15^=fz

print("Price of R15: ",r15,"Price of Yamaha FZS:",fz)
