class mobile:
    def __init__(self,brand,price):
        print("Inside Constructor")
        self.brand = brand
        self.price = price
    def purchase(self):
        print("Purchasing a mobile")
        print("This mobile has brand",self.brand, "and price",self.price)
        
        
print("Mobile-1")
mob1=mobile("Apple",20000)
mob1.purchase()


print("Mobile-2")
mob2=mobile("Samsung" , 10000)
mob2.purchase()