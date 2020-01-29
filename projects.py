#list operations: [], all types of data

running=["ruby","node","kotlin","swift","java","spring","angular"]
#insert
running.insert(1,"selenium")
running.insert(15,"Deep learning")
running.append("sdn")
print(running)

#read
print("Top 5 priority: ",running[:5])
print("Recent addded projects are: \n",running[5:])
print("Average priority: \n",running[3:7])

#update
running[4]="ERP"
#search and update:
print(running)
for sin in range(len(running)):
    if running[sin].startswith('s') or running[sin].startswith('k'):
        running[sin]="Rest Web service"

print(running)

# deletion
del running[2]
running.pop()#running.pop(index)
running.remove("Rest Web service")
print(running)
running.sort()
print("After sort: \n",running)
running.reverse()
print("REverse: \n",running)
