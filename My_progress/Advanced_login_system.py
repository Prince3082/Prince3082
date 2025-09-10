
def login_system(correct_username, correct_password):
    username = input("\033[33m Please enter your username here: \033[0m")
    password = input("\033[34m Now enter your password: \033[0m")

    if username == correct_username and password == correct_password:
        print("\033[32mPermission Granted, Please wait...\033[0m")
        return "success"

    elif username == correct_username and password != correct_password:
        print('\033[31mWrong Password!!\033[0m')
        return "wrong_password"

    elif username != correct_username and password == correct_password:
        print("\033[31mIncorrect Username!!\033[0m")
        return "wrong_username"

    elif username != correct_username and password != correct_password:
        print('\033[31mBoth Username and Password are incorrect!\033[0m')
        return "wrong_username"


pass_Username = "Prince3082"
pass_key = "Follow Prince"

login_result = login_system(pass_Username, pass_key)

if login_result == "wrong_password":
    reset_password = input("\033[33mEnter your new password: \033[0m")
    pass_key = reset_password

    print("\n\033[35mNow, please re-login to begin\033[0m\n")
    login_system(pass_Username, pass_key)

elif login_result == "wrong_username":
    print("\033[31mAccess denied. Cannot reset password for unknown user.\033[0m")