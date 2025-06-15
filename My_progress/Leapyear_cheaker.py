# Write a Python program to check whether a year entered by the user is a leap year or not.
a = float(input("Enter the year: "))
if (a % 4 == 0 and a % 100 != 0 ) or (a % 400 == 0):
    print("Its a leap year")
else :
    print("Its not a leap year")
