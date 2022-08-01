def purchase_product(product_type , price ,mobile_brand ,material):
    total_price = 0
    if product_type == "mobile":
        if mobile_brand == "apple":
            discount =10
    
        else:
            discount =5
        total_price = price -price * discount / 100
    else:
        if material == "leather":
            tax =5
        else:
            tax = 2
                
        total_price = price + price * tax/100 
    print("Total price of " +product_type +  " is : " +str(total_price))
    
purchase_product("Mobile",20000,"apple",None)
purchase_product("shoe",800, None,"leather")