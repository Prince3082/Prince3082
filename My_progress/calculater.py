num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2

if num2 != 0:
    division_result = num1 / num2
else :
    division_result = ("not defined")

print("Sum is:",sum_result)
print("Difference is:",difference_result)
print("product is:",product_result)
print("division is:",division_result)