class Employee:
    def __init__(self, name , salary):
        self.name=name
        self.salary=salary
        print(f"i am {self.name} and my salary is{self.salary}")

class Developer(Employee):  
  def __init__(self, name, salary, programminglanguage):
     super().__init__(name, salary) 
     self.programminglanguage=programminglanguage 
     print(f" I am learning {self.programminglanguage}")

class Manager(Employee):   
     def __init__(self, name, salary, listofemployee):

        super().__init__(name, salary)
        self.listofemployee=listofemployee
        print(f"iam in the list of {self.listofemployee}")

person1=Developer("Ali",4000,"python")  
person2=Manager("sara",6000,"[d]") 
