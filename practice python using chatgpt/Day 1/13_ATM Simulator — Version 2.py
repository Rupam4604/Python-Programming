# ATM Simulator — Version 2

# Starting balance:

# ₹10,000

# Show this menu repeatedly:

# ===== ATM MENU =====
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit

# The user should be able to perform operations multiple times until they choose 4.

# Requirements

# Check Balance

# Current Balance: ₹10000

# Deposit

# Ask for amount.
# Add it to balance.
# Don't allow 0 or negative deposits.

# Withdraw

# Ask for amount.
# Don't allow 0 or negative amounts.
# Check insufficient balance.
# Deduct the amount if sufficient.

# Exit

# Thank you for using the ATM!

balance = 10000

menu = """ 
===== ATM MENU =====
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
"""
while True:

    print(menu)

    n = int(input("choose option: "))

    if n == 1:
        print(f"Current Balance: {balance}")

    elif n == 2:
        deposite = int(input("Enter deposite amount: "))

        if deposite > 0:
            balance = balance + deposite
            print(f"Current balance: {balance}")
        else:
            print("you entered a invalid input!\npiz try again!")


    elif n == 3:
        withdraw = int(input("Enter withdrawal amount: "))

        if withdraw > 0 and withdraw <= balance:
            balance = balance - withdraw
            print(f"Current balance: {balance}")
        elif withdraw > balance:
            print(f"Insufficient balance!\nCurrent balance: {balance}")
        else:
            print("you entered a invalid input!\npiz try again!")
        

    elif n == 4:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice! Please select 1-4.")
