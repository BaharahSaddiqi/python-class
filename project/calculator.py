class Calculator:

 
   def add(self,firstval,secondval):
       return firstval + secondval
   def sub(self,firstval,secondval):
         return firstval-secondval
   def div(self,firstval,secondval):
        try:
            result = firstval/ secondval
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
            return None
        else:
            return result
        return firstval/secondval
   def multi(self,firstval,secondval):
          return firstval*secondval
       
cal=Calculator()
number1=int(input("enter your first number "))
opration=input("pleas chose the opration(+,-,/,*)")
number2=int(input("enter your second number "))
if opration =="+":
  result= cal.add(number1,number2)
elif opration=="-":
  result= cal.sub(number1,number2)
elif opration=="/":
  result= cal.div(number1,number2)
elif opration == "*":
  result= cal.multi(number1,number2)
print ("result=", result)