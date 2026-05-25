
balance = 10000

while True:
    try:
        print("\n1. Withdraw")
        print("2. Deposit")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "3":
            break

        elif choice == "1":
            amount = int(input("enter withdrawal amount ( or press exit): "))

            if amount <= 0:
               print(" Enter a valid positive amount.")
    
            elif amount > balance:
               print("Insufficient funds")
            else:
               balance -= amount
               print("WITHDRAWAL SUCCESSFUL")
               print("Remaining Balance:", balance)

        elif choice == "2":
            amount = int(input("Enter deposit amount ( or press exit): "))

            if amount <= 0:
                print("Enter a valid positive amount.")

            else:
                balance+=amount
                print("DEPOSIT SUCCESSFULL")
                print("Remaining Balance:", balance)

        else:
            print("Invalid choice")

    except ValueError:
        print("Invalid input! Enter amount. ")

print("Final Balance:", balance)


