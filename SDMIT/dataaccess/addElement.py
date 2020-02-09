#import pymysql
from pymysql import *

person=input("Tell us your name: ")
skill=input("Tell us what you knew: ")
exp=int(input("Tell us Experience: "))
pay=int(input("TEll us Payment: "))

con=connect("localhost","root","","python")
qry="""insert into lancer(name,skill,exp,pay) values('%s','%s',%d,%d)"""%(person,skill,exp,pay)
carry=con.cursor()
carry.execute(qry)
print("Data has inserted")
con.close()
