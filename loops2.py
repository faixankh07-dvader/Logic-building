num = input("Enter a number: ")
print("Reversed:", num[::-1])  # print(text[::-1]) moves backward through the string


n = int(input("enter: "))
reverse = 0

while n > 0:
    digits = n % 10
    reverse = reverse * 10 + digits
    n = n // 10

print("Reversed number:", reverse)
