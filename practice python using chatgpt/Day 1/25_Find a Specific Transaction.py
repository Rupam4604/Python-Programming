# Find a Specific Transaction

# Now we're going to make your ATM slightly more intelligent.

# Add a new menu option:

# 5. Search Transaction

# The user should be able to enter an amount, for example:

# Enter transaction amount: 2000

# Then search both histories.

# If:

# deposit_history = [2000, 5000, 1000]
# withdraw_history = [500, 200]

# and the user searches:

# 2000

# the program should display:

# Transaction found!
# Type: Deposit
# Amount: 2000

# If the amount isn't found:

# Transaction not found.
# Your challenge

# Create a function:

# def search_transaction(deposit_history, withdraw_history):

# Inside it:

# Ask the user for an amount.
# Check whether the amount exists in deposit_history.
# Check whether it exists in withdraw_history.
# Display the appropriate result.
# 💡 Hint

# Python has a very useful operator:

# if amount in deposit_history:

# For example:

# numbers = [100, 200, 500]

# if 200 in numbers:
#     print("Found")

correct_pin = "4711"
pin_attempts = 0
authenticated = False
running = True


balance = 10000

deposite_count = 0
withdraw_count = 0
total_deposite = 0
total_withdraw = 0

deposit_history = [ ]
withdraw_history = [ ]

menu = """ 
===== ATM MENU =====
1. Check Balance
2. Deposit
3. Withdraw
4. Search Transaction
5. Exit
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


def deposite(balance, total_deposite, deposite_count, deposit_history):
    while True:
        
        deposite_amount = get_positive_integer("Enter the deposite amount: ")

        
        balance = balance + deposite_amount
        print(f"Current balance: {balance}")
        deposite_count += 1
        total_deposite = total_deposite + deposite_amount
        deposit_history.append(deposite_amount)
        return balance, total_deposite, deposite_count, deposit_history




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


def transation_history(deposit_history, withdraw_history):
    
        amount = get_positive_integer("Enter the amount: ")

        if amount in deposit_history and amount in withdraw_history:
            print(f"Transation found!\nType: Deposit & withdraw\nAmount: {amount}")
            
        elif amount in deposit_history:
            print(f"Transation found!\nType: Deposit\nAmount: {amount}")

        elif amount in withdraw_history:
            print(f"Transation found!\nType: Withdraw\nAmount: {amount}")
            
        else:
            print("Transtion Not found!")
        
        





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
                
                n = get_choice("choose option: ", 1, 5)
                
                
                    

                if n == 1:
                    check_balance(balance)
                elif n == 2:               
                    balance, total_deposite, deposite_count, deposit_history = deposite(balance, total_deposite, deposite_count, deposit_history)

                elif n == 3:
                    balance, total_withdraw, withdraw_count, withdraw_history = withdraw(balance, total_withdraw, withdraw_count,withdraw_history)
                elif n == 4:
                    transation_history(deposit_history,withdraw_history)
                
                elif n == 5:
                    print(show_summary(balance,deposite_count,withdraw_count,total_deposite,total_withdraw,deposit_history, withdraw_history))
                   
                    running = False

        
    
    elif pin_attempts == 3:
        print("Incorrect pin!")
        print("Account locked after 3 failed attempts.")
        break
    else:
        print("Incorrect pin!")
        print(f"Attempt remaning: {3 - pin_attempts}")
        print("Try again!")