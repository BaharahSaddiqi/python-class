class Animal:
     def speak(self):
         pass
class Dog(Animal):
     def speak(self):
        print("Woffff")
class Cat(Animal):
  def speak(self):
        print("MIAUUUU")

    
class Cow(Animal):  
   def speak(self):
        
        print("Mahhhhhh")

animals=[Dog(), Cat(),Cow()]
for i in animals:
    i.speak()




