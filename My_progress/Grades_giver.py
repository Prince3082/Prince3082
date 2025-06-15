# Write a Python program that takes a student's marks (0–100) and prints their grade
marks = float(input("Enter your marks here :"))

if marks <= 60 :
    print("F")
elif marks <= 69 :
    print("D")
elif marks <= 79 :
    print("C")
elif marks <= 89 :
    print("B")
else :
    print("A")
