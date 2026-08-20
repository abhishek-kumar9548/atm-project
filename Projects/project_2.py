balance = 5000
userpin = 123456
attempts = 3

while attempts > 0:
    enterpin = int(input("Enter your pin: "))

    if userpin == enterpin:
        print("PIN verified successfully!")
        
        while True:
            print("\n------------ATM-------------")
            print("1. check balance")
            print("2. deposit money")
            print("3. withdraw money")
            print("4. exit")

            choice = int(input("choice an option :"))

            if choice == 1:
                print("your balance is : ₹", balance)

            elif choice == 2:
                amount = int(input("Enter your amount deposit :"))
                balance = balance + amount
                print("money deposit successfully")
                print("new money : ₹", balance)

            elif choice == 3:
                amount = int(input("Enter your withdraw amount :"))
                if amount <= balance:
                    balance = balance - amount
                    print("withdraw successfully")
                    print("remaning balance ₹", balance)
                else:
                    print("insufficient balance")

            elif choice == 4:
                print("Thank you for using ATM")
                break

            else:
                print("invalid option")
        
        # Exit the outer PIN loop once the user finishes their ATM session
        break

    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect PIN. You have {attempts} attempt(s) remaining.\n")
        else:
            print("Incorrect PIN. Your card has been blocked due to 3 failed attempts.")