#funs in strs

'''name=input("Tell us your name: ")
email=input("Tell us your email: ")
word=input("Type Password: ")
org=input("Tell usyour employer: ")
ctc=input("Tell us your salary: ")

print(name.isalpha())
print(word.isalnum())
print(org.isalpha())
print(ctc.isdecimal())

#hold=list(email)
hold=email.split('@')
print(hold)

print("Is your authorised one: ",(hold[1].startswith(org)))

print("Domain check: ",(hold[1].endswith("in")))
'''

domains="network ai ds iot ai agile network ai web testing mobile web"

print(domains.count("java"))
print(domains.index('o'))
domains=domains.replace('ai','ds')
print(domains)

domains=domains.capitalize()
print(domains)

print(domains.lower())
print(domains.upper())
print(domains.find('agile'))

print(len(domains))
print(max(domains))
print(min(domains))

for hai in domains:
    print(hai)
for yet in range(len(domains)):
    print(yet)
