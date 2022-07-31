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