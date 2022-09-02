num = int(input("Enter a number : "))
first_digit = num // 100
middle_digit = num // 10 - first_digit * 10
print(middle_digit)