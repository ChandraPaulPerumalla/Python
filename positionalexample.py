def display1(flight_number , seating_capacity):
    print("flight_number:",flight_number)
    print("seating_capacity:",seating_capacity)
    
print("code-1: positional arguments")
display1("FN200",300)



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