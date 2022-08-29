total_mobile_price = 0
total_shoe_price = 0
def purchase_mobile(price,brand):
    global total_mobile_price
    if brand == "apple":
        discount = 10
    else:
        discount =5
    total_price = price - price * discount/100
        
    print("The total price of mobile is " +str(total_price))
    
def purchase_shoe(price, material):
    global total_shoe_price
    if material == "leather":
        tax = 5
    else:
        tax =2
    total_price = price - price * tax/100
    
    print("The total price of the shoes is: " +str(total_price))
    
def return_shoe():
    print("refund price for shoe is : " , total_shoe_price)
    
def return_mobile():
    print("refund amount of mobile is : " , total_mobile_price)
    
purchase_mobile(20000,"apple")
purchase_shoe(800,"lather")
purchase_mobile(20000,"apple")
return_mobile()
