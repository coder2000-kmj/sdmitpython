#platinum class booking chart
chart=""
for row in range(1,5):
    for seat in range(1,9):
        amt=int(input("Tell us amount u have: "))
        if amt>=300:
            print("Ur seat Number: ",row,seat)
            chart+="|"
        else:
            chart+="^"
    chart+="\n"

print(chart)
