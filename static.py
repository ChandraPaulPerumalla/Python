class shirt:
    discount = 0
    def __init__ (self,price,brand):
        self.price = price
        self.brand = brand
        
    def purchase(self):
        total =self.price - self.price * shirt.discount / 100
        print(  self.brand,"shirt with price",self.price,"is available after discount at",total)
        
        
#print("WE CAN UPDATE THE STATIC VALUE BY USING THE CLASS NAME)
        
        
def enable_discount():
    shirt.discount = 50
    
def disable_discount():
    shirt.discount = 0


        
s1 = shirt(500,"uspolo")
s2 = shirt(1000,"allensollen")
s3 = shirt(1500,"pep_jeans")
s4 = shirt(2000,"ramraj")
      
s1.purchase()
enable_discount()
s2.purchase()
s3.purchase()
disable_discount()
s4.purchase()
    