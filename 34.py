password = input("Set your mobile password: ")
confirm_password = input("Confirm your mobile password: ")

if password == confirm_password:
    print("Password set successfully.")
else:
    print("Passwords do not match. Try again.")
