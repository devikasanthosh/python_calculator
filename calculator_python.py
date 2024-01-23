
# Python Calculator 

while True:
    print("\n1. Addition\n\n2. Substraction\n\n3.Multiplication\n\n4.Division\n\n5.Exit")
    choice=int(input("\nEnter your choice: "))
    if choice==1:
        num1=float(input("Enter a number: "))
        num2=float(int(input("Enter a number: ")))
        sum=num1+num1
        print("Sum of the numbers: ",sum)
    elif choice==2:
        num1=float(input("Enter a number: "))
        num2=float(int(input("Enter a number: ")))
        sub=num1-num2
        
        print("Difference of the number is: ",sub)
    elif choice==3:
        num1=float(input("Enter a number: "))
        num2=float(int(input("Enter a number: ")))
        mul= num1 * num2
        print("Multiplication of the two number is: ",mul)
    elif choice ==4:
        num1=float(input("Enter a number: "))
        num2=float(int(input("Enter a number: ")))
        div=num1/num2
        print("Division of the numbers is: ",div)
    elif choice==5:
        exit()


        

        