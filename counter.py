for ticket in range(1,30+1):
    if ticket<=10 or ticket==15 or ticket==17 or ticket==19 or ticket==22:
        print(ticket,"already booked in online");continue
    else:
        amt=int(input("Bring the amount: "))
        if amt >= 150:
            print("U can enjoy the Sampoornesh babu film @ ",ticket)
        else:
            print("U r very unlucky")
