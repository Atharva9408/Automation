fNumber=int(input("Enter first number to add: "))
SNumber=int(input("Enter second number to add: "))

option=int(input("Enter 1 for addition & 2 for subtraction: "))

def add():
    ans=fNumber+SNumber
    print("Addition: ", ans)

def subtract():
    ans=fNumber-SNumber
    print("Subtraction: ", ans)

if option==1 :
    add()
elif option==2 :
    subtract()
else:
    print("Enter correct number")