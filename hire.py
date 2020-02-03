# function returns
resources={"Koushal":"pyhton","Preetham":"java","Veena":"javascript"}
print(len(resources))
def recruit():
    name=input("Tell us name: ")
    skill=input("Tell waht you knew: ")
    if skill == "python" or skill == "java" or skill == "javascript":
        resources[name]=skill;print("Dlithe recruited you")
    else:
        print("Update your skillset")
def report():
    for hai in resources.items():
        print(hai)
def filter(skill="python"):
    people=[]
    for yet in resources.keys():
        if resources[yet]==skill:
            people.append(yet)
    return people;
report()
for people in range(1,int(input("How many u wish to interview: "))+1):
    recruit()
print(filter("javascript"))
