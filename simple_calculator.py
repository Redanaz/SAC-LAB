def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b!=0:
        return a/b
    else:
        return "Error! Division by zero."
while True:
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice=int(input("Enter which operation do you want:"))
    if choice!=5:
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        if choice==1:
            print("Addition:",add(a,b))
        elif choice==2:
            print("Subtraction:",subtract(a,b))
        elif choice==3:
            print("Multiplication:",multiply(a,b))
        elif choice==4:
            print("Division:",divide(a,b))
        else:
            print("Invalid choice. Enter again")
    else:
        print("Exiting")
        break

