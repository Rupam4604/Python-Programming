# ATM Security System

# Now we're going to introduce something new: nested loops + authentication.

# Before showing the ATM menu, require a PIN.

# Starting PIN
# 1234

# The user gets 3 attempts to enter the correct PIN.

# Example:

# Enter your PIN: 1111
# Incorrect PIN! Attempts remaining: 2

# Enter your PIN: 2222
# Incorrect PIN! Attempts remaining: 1

# Enter your PIN: 1234
# PIN accepted!

# Then show your ATM menu.

# If all 3 attempts fail:
# Too many incorrect attempts!
# Your account is locked.

# And the program should terminate.

# Important

# Your existing ATM functionality should still work after successful login:

# Check balance
# Deposit
# Withdraw
# Transaction counters
# Transaction summary
# Exit


correct_pin = 4711
pin_attempts = 0
authenticated = False
running = True


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

while pin_attempts < 3 and running:
    pin = int(input(f"Enter your PIN: "))
    pin_attempts += 1
    if correct_pin == pin:
        authenticated = True
    

        while authenticated and running:
        
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
                    running = False
        
                else:
                    print("Invalid choice! Please select 1-4.")

    

    elif pin_attempts == 3:
        print("Account locked")
        break
    else:
        print(f"Attempt remaning: {3 - pin_attempts}")
        print("Try again!")
        
       
    

