# ATM Transaction Counter

# Let's make the ATM slightly more realistic.

# Modify your current program so that it also tracks:

# 1. Number of deposits

# For example:

# Deposits made: 3
# 2. Number of withdrawals
# Withdrawals made: 2
# 3. Total deposited

# If the user deposits ₹1000, ₹500 and ₹200:

# Total deposited: ₹1700
# 4. Total withdrawn

# If they withdraw ₹500 and ₹1000:

# Total withdrawn: ₹1500
# 5. When the user chooses Exit

# Print a final summary:

# ===== TRANSACTION SUMMARY =====

# Final Balance: ₹9500
# Deposits Made: 3
# Withdrawals Made: 2
# Total Deposited: ₹1700
# Total Withdrawn: ₹1500

# Thank you for using the ATM!

balance = 10000
deposite_count = 0
withdraw_count = 0
total_deposite = 0
total_withdraw = 0

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
            deposite_count += 1
            total_deposite = total_deposite + deposite
        else:
            print("you entered a invalid input!\npiz try again!")


    elif n == 3:
        withdraw = int(input("Enter withdrawal amount: "))

        if withdraw > 0 and withdraw <= balance:
            balance = balance - withdraw
            print(f"Current balance: {balance}")
            withdraw_count += 1
            total_withdraw = total_withdraw + withdraw

        elif withdraw > balance:
            print(f"Insufficient balance!\nCurrent balance: {balance}")
        else:
            print("you entered a invalid input!\npiz try again!")
        

    elif n == 4:
        print(f"""
         ===== TRANSACTION SUMMARY =====

         Final Balance: {balance}
         Deposits Made: {deposite_count}
         Withdrawals Made: {withdraw_count}
         Total Deposited: {total_deposite}
         Total Withdrawn: {total_withdraw}

         Thank you for using the ATM!
         """)
        break

    else:
        print("Invalid choice! Please select 1-4.")


