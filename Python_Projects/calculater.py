"""
Simple Calculator
-----------------
This program takes two numbers as input and calculates:
- Sum
- Difference
- Product
- Division (if second number is not zero)
"""

def main():
    # Take input from user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calculate results
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2

    # Handle division carefully
    if num2 != 0:
        division_result = num1 / num2
    else:
        division_result = "Not defined (division by zero)"

    # Display results
    print("\n----- Calculation Results -----")
    print(f"Sum: {sum_result}")
    print(f"Difference: {difference_result}")
    print(f"Product: {product_result}")
    print(f"Division: {division_result}")
    print("-------------------------------")


# Run the program
if __name__ == "__main__":
    main()
