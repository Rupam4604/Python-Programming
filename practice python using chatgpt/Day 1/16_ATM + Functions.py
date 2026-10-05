# ATM + Functions

# You've now written a fairly large procedural program. The next step is functions.

# Instead of putting everything inside one giant loop, create separate functions:

# check_balance()
# deposit()
# withdraw()
# show_summary()

# For example, conceptually:

# def check_balance():
#     # display balance

# Then your menu can call:

# check_balance()
# Your task

# Refactor your existing ATM program so that it has at least these functions:

# def check_balance():
#     ...

# def deposit():
#     ...

# def withdraw():
#     ...

# def show_summary():
#     ...

# Keep:

# 🔐 3-attempt PIN authentication
# 💰 Starting balance ₹10,000
# 💵 Deposit
# 💸 Withdrawal
# 📊 Transaction counters
# 📈 Total deposited/withdrawn
# 🚪 Exit
# ❌ Invalid input handling

# example, think about:

# def deposit(balance):
#     ...
#     return balance

# Then:

# balance = deposit(balance)


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




def check_balance(balance):
    print (f"Current balance: {balance}")


def deposite(balance, total_deposite, deposite_count):
    deposite_amount = int(input("Enter the deposite amount: "))
    if deposite_amount > 0:
        balance = balance + deposite_amount
        print(f"Current balance: {balance}")
        deposite_count += 1
        total_deposite = total_deposite + deposite_amount
    else:
        print("you entered a invalid input!\npiz try again!")
    return balance, total_deposite, deposite_count




def withdraw(balance, total_withdraw, withdraw_count):
    withdraw_amount = int(input("Enter the withdrawal amount: "))
    if withdraw_amount > 0 and withdraw_amount <= balance:
        balance = balance - withdraw_amount
        print(f"Current balance: {balance}")
        withdraw_count += 1
        total_withdraw = total_withdraw + withdraw_amount
    else:
        print("you entered a invalid input!\npiz try again!")
    return balance, total_withdraw, withdraw_count



def show_summary(balance,deposite_count,withdraw_count,total_deposite,total_withdraw ):
    
    return (f"""
            ===== TRANSACTION SUMMARY =====
        
            Final Balance: {balance}
            Deposits Made: {deposite_count}
            Withdrawals Made: {withdraw_count}
            Total Deposited: {total_deposite}
            Total Withdrawn: {total_withdraw}
        
            Thank you for using the ATM!
          """)
        



while pin_attempts < 3 and running:
    pin = int(input(f"Enter your PIN: "))
    pin_attempts += 1
    if correct_pin == pin:
        authenticated = True

        while authenticated and running:
            print(menu)
            n = int(input("choose option: "))

            if n == 1:
                check_balance(balance)
            elif n == 2:               
                balance, total_deposite, deposite_count = deposite(balance, total_deposite, deposite_count)

            elif n == 3:
                balance, total_withdraw, withdraw_count = withdraw(balance, total_withdraw, withdraw_count)
                
            elif n == 4:
                print(show_summary(balance,deposite_count,withdraw_count,total_deposite,total_withdraw))
                running = False

            else:
                print("Invalid choice! Please select 1-4.")
    
        
    
    elif pin_attempts == 3:
        print("Account locked")
        break
    else:
        print(f"Attempt remaning: {3 - pin_attempts}")
        print("Try again!")
        

