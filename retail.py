# functions demo

retail=[23500,18900,45900,34800,28100,78100,32000,68000]

def iterate():
    print("Listing all laptops")
    for each in retail:
        print(each)
def discount(percent=2,mini=10000,maxi=100000):
    print("Applying the discount of: ",percent,"min ",mini,"maximum: ",maxi)
    for take in range(len(retail)):
        if retail[take]>=mini and retail[take]<maxi:
            retail[take]-=(retail[take]*percent)/100

iterate();
retail.append(98700);retail.append(65100)
retail.append(86090.4);iterate();
discount();iterate();
discount(15,20000,50000);iterate();
discount(mini=70000,maxi=100000,percent=10);iterate();
