# Mini ATM

# Now we're going to combine multiple conditions + arithmetic + user choices.

# Write a program that simulates a very simple ATM.

# Start with:

# balance = 10000

# Ask the user:

# 1. Check Balance
# 2. Deposit
# 3. Withdraw

# Then ask them to enter their choice.

# Example 1
# Enter your choice:
# 1. Check Balance
# 2. Deposit
# 3. Withdraw

# Choice: 1
# Current Balance: ₹10000

# Example 2

# Choice: 2
# Enter deposit amount: 2500

# Amount Deposited: ₹2500
# New Balance: ₹12500

# Example 3

# Choice: 3
# Enter withdrawal amount: 3000

# Amount Withdrawn: ₹3000
# Remaining Balance: ₹7000
# Important conditions

# If the user tries to withdraw more than the balance:

# Choice: 3
# Enter withdrawal amount: 15000

# Insufficient Balance!

# If they enter something other than 1, 2, or 3:

# Invalid Choice!

balance = 10000

print("WELCOME!\n1. Check Balance\n2. Deposit\n3. Withdraw")

num = int(input("Enter your choice: "))


if num == 1:
    print(f"Current Balance: {balance}")

elif num == 2:
    deposite = int(input("Enter deposite amount: "))
    print(f"Amount deposited: {deposite}\nNew balance: {balance + deposite}")

elif num == 3:
    withdraw = int(input("Enter withdrawal amount: "))
    if withdraw <= balance:
        print(f"Amount withdrawn: {withdraw}\nNew balance: {balance - withdraw}")
    else:
        print("Insufficient Balance!")

else:
    print("Invalide Choice!")