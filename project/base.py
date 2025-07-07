from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    def __init__(self,accunt_holder,currency):
     self.accunt_holder= accunt_holder
     self.currency = currency
    
    def authorize_payment(self):
      pass

    def process_payment(self):
       pass






class CreditCardpayment(PaymentMethod):
    def __init__(self, accunt_holder, currency,card_number):
       super().__init__(accunt_holder, currency)
       self.card_number=card_number
   
    

    def authorize_payment(self):
     print(f"[CreditCardpayment] CreditCard is belong to{self.accunt_holder} and your card number is{self.card_number}")


    def process_payment(self):
       
     print(f"[CreditCardpayment]The currency is {self.currency}")





class Paypal(PaymentMethod):
    def __init__(self, accunt_holder, currency,email):
        super().__init__(accunt_holder, currency)



        self.email=email
    def authorize_payment(self):
     print(f"[Paypal] Paypal is belong to{self.accunt_holder} and your card number is{self.email}") 

    def process_payment(self):
       
     print(f"[Paypal] Paypal  currency is{self.currency}")







class Crypto(PaymentMethod):
     def __init__(self, accunt_holder, currency,wallet_adress):
          super().__init__(accunt_holder, currency)
          self.wallet_adress=wallet_adress



     def authorize_payment(self):
      print(f"[Crypto] this accunt is belong to {self.accunt_holder} die adresse ist {self.wallet_adress}")

     def process_payment(self):
       
       print(f"[Crypto] the acuunt currency is {self.currency}")







      #Polymorphism

if __name__=="__main__":
      payments=[CreditCardpayment("Bahar" ,"USD","345_6755_654"),
               Paypal("Fardin","EUR","fardin23@gmail.com"),
               Crypto("Umair","BT","3e5rt6tz")]
      
      for payment in payments:
           payment.authorize_payment()
           payment.process_payment()
           print("______________")