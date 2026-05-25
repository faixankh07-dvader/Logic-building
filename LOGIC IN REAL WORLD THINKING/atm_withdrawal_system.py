
balance = 10000

while True:
    try:
        user = input("enter withdrawal amount ( or press exit): ")

        if user.lower() == "exit":
           break
    
        amount = int(user)
    
        if amount > balance:
            print("Insufficient funds")
        else:
            balance -= amount
            print("Remaining Balance:", balance)
    
    except ValueError:
        print("Invalid input! must be positive")

print("Final Balance:", balance)


