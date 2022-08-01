def purchase_mobile(price,brand):
    if brand == "apple":
        discount = 10
    else:
        discount =5
    total_price = price - price * discount/100
        
    print("The total price of mobile is " +str(total_price))
    
    
    
def purchase_shoe(price,material):
    if material == "leather":
        tax = 5
    else:
        tax =2
    total_price = price - price * tax/100
    
    print("The total price of the shoes is: " +str(total_price))
    
purchase_mobile(20000,"apple")
purchase_shoe(800,"lather")