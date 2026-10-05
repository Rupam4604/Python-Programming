# Transaction History

# Now we're going to introduce something important for real-world Python:

# Lists

# Your ATM currently stores only totals:

# total_deposite
# total_withdraw

# But suppose the user does:

# Deposit 2000
# Withdraw 500
# Deposit 1000
# Withdraw 300

# The ATM knows the totals, but it doesn't know the individual transaction history.

# Your task

# Create two lists:

# deposit_history = []
# withdraw_history = []

# Then, whenever a successful deposit happens, add the amount to:

# deposit_history

# For example:

# Deposit 2000
# Deposit 1000
# Deposit 500

# should produce:

# [2000, 1000, 500]

# Similarly:

# Withdraw 500
# Withdraw 300

# should produce:

# [500, 300]
# 💡 Hint

# Python lists have a method:

# list_name.append(value)

# So inside your successful deposit section, you'll need something like:

# deposit_history.append(________)
# Important challenge

# Your current function is:

# def deposite(balance, total_deposite, deposite_count):

# Think carefully:

# How will the function access deposit_history?

# Don't immediately use global.

# We've already learned to pass state into functions and return updated state.

# 🎯 Your task

# Modify your deposit system so that successful deposits are recorded in a list.

# Then modify the summary to display the deposit history.

# For example:

# ===== TRANSACTION SUMMARY =====

# Final Balance: 12200

# Deposits Made: 2
# Withdrawals Made: 1

# Total Deposited: 3000
# Total Withdrawn: 800

# Deposit History: [2000, 1000]
# Withdraw History: [800]


correct_pin = "4711"
pin_attempts = 0
authenticated = False
running = True


balance = 10000

deposite_count = 0
withdraw_count = 0
total_deposite = 0
total_withdraw = 0

deposite_history = [ ]
withdraw_history = [ ]

menu = """ 
===== ATM MENU =====
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
"""


def get_pin(prompt):
    while True:
        
        pin = input(prompt)
        if len(pin) != 4:
            print("Invalid input! Enter your 4 digit pin only..")
            continue
        if pin.isdigit() == False:
            print("Inavalid input! Enter digits only..")
            continue
        return pin
    




def get_positive_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number == 0:
                print("Invalid input! Number shoud not be  0")
                continue
            if number < 0:
                print("Invalid input! Number shoud be greater than 0")
                continue
            return number

        except ValueError:
             print("Invalid input! Please enter number only")




def get_choice(prompt,minimum,maximum):
    while True:
        try:
            n = int(input(prompt))
            
            if minimum > n or n >maximum:
                print(f"Invalid choice! Choose between {minimum} to {maximum}")
                continue
            return n
        except ValueError:
            print("Invalid input! Please enter numbers only.")






def check_balance(balance):
    print (f"Current balance: {balance}")


def deposite(balance, total_deposite, deposite_count, deposite_history):
    while True:
        
        deposite_amount = get_positive_integer("Enter the deposite amount: ")

        
        balance = balance + deposite_amount
        print(f"Current balance: {balance}")
        deposite_count += 1
        total_deposite = total_deposite + deposite_amount
        deposite_history.append(deposite_amount)
        return balance, total_deposite, deposite_count, deposite_history




def withdraw(balance, total_withdraw, withdraw_count, withdraw_history):
    while True:
        
        withdraw_amount = get_positive_integer("Enter the withdrawal amount: ")
            
        if  withdraw_amount > balance:
            print("Invalid amount! Amount must be  lower than balance")
            continue

        
        balance = balance - withdraw_amount
        print(f"Current balance: {balance}")
        withdraw_count += 1
        total_withdraw = total_withdraw + withdraw_amount
        withdraw_history.append(withdraw_amount)
        return balance, total_withdraw, withdraw_count, withdraw_history



def show_summary(balance,deposite_count,withdraw_count,total_deposite,total_withdraw, deposite_history, withdraw_history ):
    
    return (f"""
            ===== TRANSACTION SUMMARY =====
        
            Final Balance: {balance}
            Deposits Made: {deposite_count}
            Withdrawals Made: {withdraw_count}
            Total Deposited: {total_deposite}
            Total Withdrawn: {total_withdraw}
            Deposit History: {deposite_history}
            Withdraw History: {withdraw_history}
        
            Thank you for using the ATM!
          """)






while pin_attempts < 3 and running:
    
    pin = get_pin("Enter your PIN: ")
        
    
    
        

    pin_attempts += 1
    if correct_pin == pin:
            print("Login successful!")
            authenticated = True

            while authenticated and running:
                print(menu)
                
                n = get_choice("choose option: ", 1, 4)
                
                
                    

                if n == 1:
                    check_balance(balance)
                elif n == 2:               
                    balance, total_deposite, deposite_count, deposite_history = deposite(balance, total_deposite, deposite_count, deposite_history)

                elif n == 3:
                    balance, total_withdraw, withdraw_count, withdraw_history = withdraw(balance, total_withdraw, withdraw_count,withdraw_history)
                
                elif n == 4:
                    print(show_summary(balance,deposite_count,withdraw_count,total_deposite,total_withdraw,deposite_history, withdraw_history))
                   
                    running = False

        
    
    elif pin_attempts == 3:
        print("Incorrect pin!")
        print("Account locked after 3 failed attempts.")
        break
    else:
        print("Incorrect pin!")
        print(f"Attempt remaning: {3 - pin_attempts}")
        print("Try again!")

