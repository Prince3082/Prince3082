#  Clean Up a User Message

Original_message = input("Enter your messege here :")

total_lenth = len(Original_message)

Finding_double_space = Original_message.find("  ")


if Finding_double_space != -1 :

    print(f"Doulble space found in your messege: {Finding_double_space}")


    Clear_messege = Original_message.replace("  "," ")


    print("\033[92m Your message has cleaned successfully!\033[0m")

    print(f"Your Original messege: \'{Original_message}\'")

    print(f" Cleared messege: \'{Clear_messege}\'")


    Cleared_leght = len(Clear_messege)


    print(f"Original messege lenght : {total_lenth} cherecters ")

    print(f"Cleared messege lenght {Cleared_leght} cherecters ")
else :
    print("\033[92mThere is no doulble spacing between any word, your messege is already cleaned.\033[0m")
    print(f"Original messege : {Original_message}")
    print(f"Original message lenth has {total_lenth} characters")



