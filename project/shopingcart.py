class ShopingCart:
    def __init__(self):
        #dic für iteams in shoping card (einkaufvagen)
        self.items={}
    def add_iteams(self,name,price,quantity=1):
            #if iteams war in einkaufwagen mach das noch mehr oder add 
            if name in self.items:
                self.items[name]["quantity"]+=quantity
            else :
                self.items[name]={"price" : price ,"quantity":quantity }

          #remove iteam in einkaufwagen  
    def remove_items(self,name, quantity=1):
     if name in self.items:
        if self.items[name]["quantity"]<=quantity:
            del self.iteams[name]
        else:
            self.iteams[name]["quantity"]-=quantity
         

    def total_preise(self,name,price,quantity=1):
         total_preise=0
         for iteam in self.iteams.values():
             total+=iteam["price"]*iteam["quantity"]
             return total
         
    def show_cart () :
        if not self.items: # type: ignore
            print("your card is impty.") 
        else:
            print ("iteam is in your cart:")
            for name, info, in self.items.items(): # type: ignore
                print(f"{name} - {info[quantity]} x ${info["price"]}") # type: ignore
#object von class 
cart=ShopingCart ()
cart.add_iteams("Apple",0.5,3)
cart.add_iteams("Banana",0.3,5)
#zeigt card sachen 
cart.show_cart()
print ("total prise:" , cart.total_preise() )
cart.remove_items("Apple",2)
cart.show_cart()
print("total prise after removing ", cart.total_preise())