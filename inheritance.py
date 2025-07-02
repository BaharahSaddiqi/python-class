class Person:
     def __init__(self, name, age):
          self.name=name
          self.age=age
     def introduce(self):
          print(f"my name is {self.name} and i am {self.age} years old")  

class Student(Person):
          def __init__(self, name, age,student_id):
                
                super().__init__(name, age)
                self.student_id=student_id
          def study(self):
              print(f"Student is studing {self.name}")
          def introduce(self):
                super().introduce()  
                print(f"my id is{self.student_id}.")
student1= Student("Anna",20,"123we")  
student1.introduce()
student1.study()            