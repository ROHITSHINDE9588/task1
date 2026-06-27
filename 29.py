balance = 1000000

withdraw_amount = float(input("Enter amount to withdraw: "))

if withdraw_amount <= balance and withdraw_amount > 0:
    balance -= withdraw_amount
    print("Withdrawal successful.")
    print("Remaining Balance:", balance)
elif withdraw_amount <= 0:
    print("Invalid amount entered.")
else:
    print("Insufficient balance.")
