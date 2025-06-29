class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduct(self):    
        print(f"my name is {self.name} i am {self.age}years old")


person1=Person("ali",30)    
person1.introduct()