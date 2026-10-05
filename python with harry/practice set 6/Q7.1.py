# Walrus Operator
# Use the walrus operator to read input until the user enters "quit" . Print each  input as it is entered.



while (text := input("enter something: ")) != "quite":
    print(f"you entered {text} .\ntry again....")