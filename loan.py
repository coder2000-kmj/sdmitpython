#loan
ctc=float(input("Tell us ur annual salary: "))
years=int(input("Tell us how many years u filing IT: "))
if ctc>=3.5 and ctc<5.0 and years>=3:
    print("We offer PL of 2LACKS")
elif ctc>=5.0 and ctc<7.5 and years>=4:
    print("We offer BL of 4LACKS")
elif ctc>=7.5 and years>=6:
    print("We offer HL of 6LACKS")
else:
    print("We can't offer any loan")
