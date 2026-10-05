# Transaction records

# Instead of storing:

# deposit_history = [2000, 5000, 1000]

# we'll make your ATM store information like:

# Transaction 1
# Type: Deposit
# Amount: 2000

# Transaction 2
# Type: Withdraw
# Amount: 500


correct_pin = "4711"
pin_attempts = 0
authenticated = False
running = True



balance = 10000

deposite_count = 0
withdraw_count = 0
total_deposite = 0
total_withdraw = 0

transation_count = 1

deposit_history = {  }
withdraw_history = {  }

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


def deposite(balance, total_deposite, deposite_count, deposit_history, transation_count):
    while True:
        
        deposite_amount = get_positive_integer("Enter the deposite amount: ")

        
        balance = balance + deposite_amount
        print(f"Current balance: {balance}")
        deposite_count += 1
        total_deposite = total_deposite + deposite_amount
        deposit_history[transation_count] = {"Type" : "Deposite","Amount": deposite_amount,"Balance": balance}
        transation_count += 1
        return balance, total_deposite, deposite_count, deposit_history, transation_count




def withdraw(balance, total_withdraw, withdraw_count, withdraw_history, transation_count):
    while True:
        
        withdraw_amount = get_positive_integer("Enter the withdrawal amount: ")
            
        if  withdraw_amount > balance:
            print("Invalid amount! Amount must be  lower than balance")
            continue

        
        balance = balance - withdraw_amount
        print(f"Current balance: {balance}")
        withdraw_count += 1
        total_withdraw = total_withdraw + withdraw_amount
        withdraw_history[transation_count] = {"Type" : "Withdraw", "Amount" : withdraw_amount, "Balance": balance}
        transation_count += 1
        return balance, total_withdraw, withdraw_count, withdraw_history, transation_count


def transation_history(deposit_history, withdraw_history):
        found = False
    
        amount = get_positive_integer("Enter the amount: ")
        for transtion_no,transtion in deposit_history.items():

            if amount == transtion["Amount"] :
                print(f"Transation found!\nTranstion no: {transtion_no}\nType:{transtion['Type']}\nAmount: {transtion['Amount']}\nBalance: {transtion['Balance']}")
                found = True
                

                
        for transtion_no,transtion in withdraw_history.items():
            if amount == transtion["Amount"] :
                print(f"Transation found!\nTranstion no: {transtion_no}\nType:{transtion['Type']}\nAmount: {transtion['Amount']}\nBalance: {transtion['Balance']}")
                found = True
                

        if found == False:
            print("Transtion not found!")



def total_transtion_history(deposit_history, withdraw_history):
    every_transtion_history = deposit_history|withdraw_history
    history = ""
    for transtion_no,transtion in sorted(every_transtion_history.items()):
        history += f"Transtion no: {transtion_no}\nType:{transtion['Type']}\nAmount: {transtion['Amount']}\nBalance: {transtion['Balance']}\n\n"

                
    return history            
            



def show_summary(balance,deposite_count,withdraw_count,total_deposite,total_withdraw, deposit_history, withdraw_history ):
   
    
    return (f"""
            ===== TRANSACTION SUMMARY =====
        
Final Balance: {balance}
Deposits Made: {deposite_count}
Withdrawals Made: {withdraw_count}
Total Deposited: {total_deposite}
Total Withdrawn: {total_withdraw}
Total Transtion: {deposite_count + withdraw_count}
All transations:\n{total_transtion_history(deposit_history, withdraw_history)}

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
                    balance, total_deposite, deposite_count, deposit_history, transation_count = deposite(balance, total_deposite, deposite_count, deposit_history, transation_count)

                elif n == 3:
                    balance, total_withdraw, withdraw_count, withdraw_history, transation_count = withdraw(balance, total_withdraw, withdraw_count,withdraw_history, transation_count)
                elif n == 4:
                    transation_history(deposit_history,withdraw_history)
                
                elif n == 5:
                    print(show_summary(balance,deposite_count,withdraw_count,total_deposite,total_withdraw, deposit_history, withdraw_history))
                   
                    running = False

        
    
    elif pin_attempts == 3:
        print("Incorrect pin!")
        print("Account locked after 3 failed attempts.")
        break
    else:
        print("Incorrect pin!")
        print(f"Attempt remaning: {3 - pin_attempts}")
        print("Try again!")