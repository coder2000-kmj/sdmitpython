# onsite opportunity for Infosys US, UK

offer=15
while offer<=24:
    exp=int(input("Tell us experience u have: "))
    pro=input("Tell us which project u haved worked recently: ")
    if exp>=1 and exp<=4 and pro == "Java Server Stack" or pro=="Automation":
        print("Onsite oppotunity to Washington DC,US of ",offer)
        offer+=1
    elif exp>=5  and exp<=8 and pro == "JavaScript" or pro=="DataScience" or pro=="ERP":
        print("Onsite to Manchester, UK of ",offer);offer+=1
    else:
        print("Ur service required to India")
