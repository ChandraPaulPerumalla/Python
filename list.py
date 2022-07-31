list_of_airlines=["AL1","AL2","AL3"]

print("Iterating the list using range()")
for index in range(0,len(list_of_airlines)):
    print(list_of_airlines[index])
    
    
print("Iterating the list using keyword in ")
for airline in  list_of_airlines:
    print(airline)



list_of_airlines=["AL1","AL2","AL3"]

airline = "AL3"
if airline in list_of_airlines:
    print("Airline founs")
else:
    print("Airline not found")


list_of_airlines =["AL1","AL2","AL3","AL4","AL5",]
sub_list = list_of_airlines[0:4]
print(sub_list)



alist=[1,1,5,100,-20,-20,6,0,0]
i=0
for i in range(len(alist)-1):
    if(alist[i] == alist[i+1]):
        print(alist)