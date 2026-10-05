# Build get_choice()

# Now we're going one step further.

# Your menu currently does:

# n = get_positive_integer("choose option: ")

# if n == 1:
#     ...
# elif n == 2:
#     ...
# elif n == 3:
#     ...
# elif n == 4:
#     ...
# else:
#     print("Invalid choice! Please select 1-4.")

# Instead, let's create a function specifically for menu choices:

# def get_choice(prompt, minimum, maximum):

# It should:

# Accept only integers.
# Reject invalid text.
# Reject numbers below minimum.
# Reject numbers above maximum.
# Return a valid choice.
# Example
# choice = get_choice("Choose option: ", 1, 4)

# Then:

# Choose option: abc
# Invalid input!

# Choose option: 8
# Invalid choice! Enter a number between 1 and 4.

# Choose option: 2
# 💡 Hint

# You already know almost everything:

# def get_choice(prompt, minimum, maximum):
#     while True:
#         try:
#             number = int(input(prompt))

#             if __________________:
#                 print("Invalid choice!")
#                 continue

#             return number

#         except ValueError:
#             print("Invalid input! Please enter numbers only.")

# Your job is to figure out the condition.

# Think:

# When should the number be rejected if it must be between minimum and maximum?






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





# def get_integer(prompt):
#     while True:
#         try:
#             number = int(input(prompt))
#             return number
#         except ValueError:
#             print("Invalid input! Please enter number only")


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
                
                n = get_choice("choose option: ", 1, 4)
                
                
                    

                if n == 1:
                    check_balance(balance)
                elif n == 2:               
                    balance, total_deposite, deposite_count = deposite(balance, total_deposite, deposite_count)

                elif n == 3:
                    balance, total_withdraw, withdraw_count = withdraw(balance, total_withdraw, withdraw_count)
                
                elif n == 4:
                    print(show_summary(balance,deposite_count,withdraw_count,total_deposite,total_withdraw))
                    running = False

        
    
    elif pin_attempts == 3:
        print("Account locked")
        break
    else:
            print(f"Attempt remaning: {3 - pin_attempts}")
            print("Try again!")
        