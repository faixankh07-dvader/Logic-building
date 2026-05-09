def analyze_transaction(transaction):
    balance = {}

    for t in transaction:
        name, amount = t.split()
        amount = int(amount)

        if name not in balance:
            balance[name] = 0

        balance[name] += amount

    sorted_balance = sorted(balance.items(), key=lambda x: x[1], reverse=True)

    highest = sorted_balance[0] if sorted_balance else None
    lowest = sorted_balance[-1] if sorted_balance else None

    return {"BALANCE": sorted_balance, "highest": highest, "lowest": lowest}


transaction = input("Enter transactions: ").split(", ")
print(analyze_transaction(transaction))
