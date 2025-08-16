# Simple Calculator Program
print("welcome to the simple calculator program")
cal =True
while cal:
    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        choice = input("1.add 2.subtract 3.multiply 4.divide : ")

        if choice == "1":
            print(n1+n2)
        elif choice == "2":
            print(n1-n2)
        elif choice == "3":
            print(n1*n2)
        elif choice == "4":
            print(n1/n2)
        else:
            print("Invalid choice please try again")
       
    
    except ValueError:
        print("Invalid input")

    continue_choice = input("Do you want to continue? (yes/no): ") 
    if continue_choice == "yes":
        continue
    elif continue_choice == "no":
        break
    elif continue_choice !="yes" and continue_choice !="no":
      print("Invalid input please try again") 
    continue
print("Thank you for using the calculator!")

    