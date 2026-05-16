correct_username = "khan"
correct_password = "7890"

attempt = 3

while attempt > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful")
        break

    else:
        attempt -= 1
        print("Login failed")

        if attempt > 0:
            print("Attempts left:", attempt)
        else:
            print("Account locked. No attempts remaining.")