
total_price = 0
count = 0
highest = 0

while True:
    try:
        user_input = input("Enter item price (or type 'exit' to stop): ")
    
        if user_input.lower() == "exit":
          break
    
        price = float(user_input)
    

        total_price += price
        count += 1

        if price > highest:
           highest = price

    except ValueError:
       print("Invalid input! Please enter item price.")

print("Total Bill:", total_price)
print("Items Purchased:", count)
print("Most Expensive Item:", highest)