# Build a Real Input-Safe ATM

# Now we're going to make your ATM much more robust.

# There is one remaining problem:

# Your PIN input, menu input, deposit input, and withdrawal input are protected against text, but we're still using int() directly in several places.

# For example, your program should never crash if someone enters:

# ₹1000
# 1.5
# hello
# abc123
# -500
# 0
# Your next task

# Create a small reusable function:

# def get_integer(prompt):
#     ...

# It should:

# Ask the user for input.
# Convert it to an integer.

# If conversion fails, print:

# Invalid input! Please enter numbers only.
# Ask again.
# Return the valid integer.
# Expected behavior
# Enter amount: abc
# Invalid input! Please enter numbers only.

# Enter amount: xyz
# Invalid input! Please enter numbers only.

# Enter amount: 2500

# The function should finally return:

# 2500
# 💡 Hint

# You already know almost everything:

# def get_integer(prompt):

#     while True:
#         try:
#             number = int(input(prompt))
#             return number

#         except ValueError:
#             print("Invalid input! Please enter numbers only.")

# Try writing it yourself first.

# Then we'll replace repeated code like:

# try:
#     n = int(input("choose option: "))
# except ValueError:
#     ...

# with:

# n = get_integer("choose option: ")


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





def get_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid input! Please enter number only")


def check_balance(balance):
    print (f"Current balance: {balance}")


def deposite(balance, total_deposite, deposite_count):
    while True:
        
        deposite_amount = get_integer("Enter the deposite amount: ")

                    
        
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
        
        withdraw_amount = get_integer("Enter the withdrawal amount: ")
        
      

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
    
    pin = get_integer("Enter your PIN: ")
        
    
    
        

    pin_attempts += 1
    if correct_pin == pin:
            print("Login successful!")
            authenticated = True

            while authenticated and running:
                print(menu)
                
                n = get_integer("choose option: ")
                
                
                    

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
        