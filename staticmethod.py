class car:
    __discount =10
    def __init__ (self,company,cost):
        self.company = company
        self.cost = cost
        
    def purchase(self):
        total = self.cost - self.cost * car.__discount / 100
        print(self.company,"car with price",self.cost,"is available after discount at",total)
        
        
        
    @staticmethod
    def enable_discount():
        car.set_discount(10)
        
    @staticmethod
    def disable_discount():
        car.set_discount(0)
        
    @staticmethod
    def get_discount():
        return car.__discount
    @staticmethod
    def set_discount(discount):
        car.__discount = discount
        
car1 = car("ford mustang",25000000)
car2 = car("ferrary" , 5000000)
car3 = car("bently" ,10000000)


car.disable_discount()
car3.purchase()

car.enable_discount()
car1.purchase()
car2.purchase()