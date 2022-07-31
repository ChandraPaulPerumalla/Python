def change_number(num):
    num = 10
    
def change_list(num_list):
    num_list.append(20)
    
print("---------------output--------------------")


num_value =10
print("************effect of pass by value**************")
print("num_value before function call :",num_value)
change_number(num_value)
print("num_value after function call:",num_value)
print("_______________----------------_____________________")


value_list=[5,10,15]
print("*******************effect of pass by referance***************")
print("value_list before function call :" ,value_list)
change_list(value_list)
print("val_list after function call :",value_list)



def display1(flight_number , seating_capacity):
    print("flight_number:",flight_number)
    print("seating_capacity:",seating_capacity)
    
print("code-1: positional arguments")
display1("FN200",300)

#display1(300,"FN200")



def display2(flight_number,seating_capacity):
    print("Flight_number:",flight_number)
    print("Seatig_capacity:",seating_capacity)
    
print("code-2: Keyword argument")
display2(seating_capacity=250 ,flight_number = "FN300")







def display3(flight_number,flight_make="Boeing",seating_capacity=150):
    print("Flight Number:",flight_number)
    print("flight make:" ,flight_make)
    print("seating capacity",seating_capacity)
    
print("code-3: default arguments")    
display3("FN400" , "Eagle")




wt_limit = 30
def baggage_check(baggage_wt):
    extra_baggage_charge=0
    if not(baggage_wt >=0 and baggage_wt <= wt_limit):
        extra_baggage = baggage_wt-wt_limit
        extra_baggage_charge = extra_baggage*100
    return extra_baggage_charge

def update_baggage_limit(new_wt_limit):
    wt_limit=new_wt_limit
    print("This airline now allows baggage limit till",wt_limit,"kgs")
    
    
print ("This airline allows baggage limit till " , wt_limit,"kgs")
print("pay the extra baggage change of ",baggage_check(35),"rupees")
update_baggage_limit(45)
print("pay the extra baggage charge of ",baggage_check(35),"rupees")
    



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



pancard_number ="AABGT6715H"
print("length of the PAN card number :",len(pancard_number))



name1 = "pan"
name2= "card"
name = name1 + name2
print(name)



print("Iterating the string using range()")
for index in range(0,len(pancard_number)):
    print(pancard_number[index])


print("searching for char in string")
if "A" in pancard_number:
    print("It is there")
else:
    print("not there")
    


