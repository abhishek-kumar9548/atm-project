balance = 20000
print("-----------ATM----------")
print("1. Check balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input("Enter your choice :"))

match choice:
    case 1:
        print("Your balance is Rs",balance)

    case 2:
        amount = int(input("Enter deposit amount :"))
        balance = balance + amount
        print ("Deposit successful")
        print ("New balance : Rs" ,balance)

    case 3:
        amount = int(input("Enter withdraw amount :"))
        if amount <= balance:
            balance = balance - amount
            print ("withdraw successful")
            print("Remanining balance: Rs",balance)
        else:
            print("Insufficient balance")
    case 4:
        print("Thank you for using ATM")

    case _:
        print("Invalid choice")                      