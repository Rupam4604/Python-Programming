# Reusable Validation System

# Now we're going to make your ATM code more professional.

# Currently you have:

# def get_integer(prompt):

# This accepts any integer, including negative numbers.

# But different situations have different rules:

# PIN → exactly 4 digits
# Menu → only 1–4
# Deposit → greater than 0
# Withdrawal → greater than 0 and ≤ balance

# Instead of putting these rules everywhere, we're going to create a more reusable function.

# Your task

# Create:

# def get_positive_integer(prompt):

# It should:

# Ask the user for input.
# Convert it to int.
# If the user enters text like abc, show:
# "Invalid input! Please enter numbers only."
# If the number is 0 or negative, show:
# "Invalid input! Please enter a positive number."
# Keep asking until a valid positive integer is entered.
# Return the number.
# Example behavior
# Enter amount: abc
# Invalid input! Please enter numbers only.
# Enter amount: -500
# Invalid input! Please enter a positive number.
# Enter amount: 0
# Invalid input! Please enter a positive number.
# Enter amount: 2000

# Then:

# amount = get_positive_integer("Enter amount: ")
# print(amount)

# should produce:

# 2000
# 💡 Hint

# You already know almost everything needed.

# Think:

# def get_positive_integer(prompt):
#     while True:
#         try:
#             number = int(input(prompt))

#             # What condition should check whether
#             # number is invalid?

#             # If valid:
#             # return number

#         except ValueError:
#             # What should happen here?


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




# def get_integer(prompt):
#     while True:
#         try:
#             number = int(input(prompt))
#             return number
#         except ValueError:
#             print("Invalid input! Please enter number only")


def check_balance(balance):
    print (f"Current balance: {balance}")


def deposite(balance, total_deposite, deposite_count):
    while True:
        
        deposite_amount = get_positive_integer("Enter the deposite amount: ")

        
        balance = balance + deposite_amount
        print(f"Current balance: {balance}")
        deposite_count += 1
        total_deposite = total_deposite + deposite_amount
        return balance, total_deposite, deposite_count




def withdraw(balance, total_withdraw, withdraw_count):
    while True:
        
        withdraw_amount = get_positive_integer("Enter the withdrawal amount: ")
            
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
    
    pin = get_positive_integer("Enter your PIN: ")
        
    
    
        

    pin_attempts += 1
    if correct_pin == pin:
            print("Login successful!")
            authenticated = True

            while authenticated and running:
                print(menu)
                
                n = get_positive_integer("choose option: ")
                
                
                    

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
        