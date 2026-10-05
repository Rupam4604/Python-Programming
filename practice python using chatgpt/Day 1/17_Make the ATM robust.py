# Your current program works when the user behaves correctly.

# But what happens if someone enters:

# Enter your PIN: hello

# Your program crashes because of:

# pin = int(input(...))

# Or:

# choose option: abc

# Or:

# Enter the deposit amount: xyz

# Again, the program crashes.

# A real program should handle these situations.

# So our next Python lesson is try / except.

# Your next challenge — Problem 17

# Modify only the PIN input first.

# Currently:

# pin = int(input("Enter your PIN: "))

# Your goal is:

# Enter your PIN: abc
# Invalid input! Please enter numbers only.

# Enter your PIN: 1234
# Try again!

# Enter your PIN: 4711
# Login successful!
# Hint

# Python gives you:

# try:
#     # code that might cause an error
# except:
#     # what to do if an error occurs

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
    while True:
        try:
            deposite_amount = int(input("Enter the deposite amount: "))

        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue            
        
        if deposite_amount <= 0:
            print("Invalid amount! Amount must be greater than 0.")
            continue

        
        balance = balance + deposite_amount
        print(f"Current balance: {balance}")
        deposite_count += 1
        total_deposite = total_deposite + deposite_amount
        return balance, total_deposite, deposite_count




def withdraw(balance, total_withdraw, withdraw_count):
    while True:
        try:
            withdraw_amount = int(input("Enter the withdrawal amount: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue
      

        if withdraw_amount <= 0 :
            print("Invalid amount! Amount must be greater than 0")
            continue
            
        if  withdraw_amount > balance:
            print("Invalid amount! Amount must be  lower than balance")
            continue

        
        balance = balance - withdraw_amount
        print(f"Current balance: {balance}")
        withdraw_count += 1
        total_withdraw = total_withdraw + withdraw_amount
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
    try:
        pin = int(input("Enter your PIN: "))
        
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    pin_attempts += 1
    if correct_pin == pin:
            print("Login successful!")
            authenticated = True

            while authenticated and running:
                print(menu)
                try:
                    n = int(input("choose option: "))
                except ValueError:
                    print("Invalid input! Please enter numbers only.")
                    continue

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
        