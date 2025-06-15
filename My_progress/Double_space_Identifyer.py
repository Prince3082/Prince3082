# Write a Python program to find the first occurrence of double spaces in a sentence entered by the user.
# lets make it as you are making an discription
description = input("Description:\t")
print(description.find("  "))
position = description.find("  ")

if position != -1:
    print(f"Double space found at index {position}.")
else:
    print("No double space found!")
   