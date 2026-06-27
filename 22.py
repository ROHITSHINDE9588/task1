username = input("Enter username: ")
password = input("Enter password: ")

correct_username = "Rohit"
correct_password = "12345"

if username == correct_username and password == correct_password:
    print("Login successful!")
elif username == correct_username and password != correct_password:
    print("Incorrect password.")
elif username != correct_username and password == correct_password:
    print("Incorrect username.")
else:
    print("Login failed. Both username and password are incorrect.")
