# # Number Guessing Game

# # Now we're moving from individual logic problems → a small interactive program.

# # Create a number guessing game.

# # Requirements

# # The computer secretly chooses a number between 1 and 100.

# # The user gets 7 attempts to guess it.

# # After every guess:

# # If guess is too high → "Too High!"
# # If guess is too low → "Too Low!"
# # If correct → "🎉 Correct!" and stop the game.
# # If all 7 attempts are used → reveal the secret number.

# # Also keep track of the number of attempts.

# Rules

# Use:

# random
# while loop
# if / elif / else
# counter variable
# break

# 💡 First hint:

# You'll need:

# import random

# Then look into:

# random.randint(1, 100)

import random

secret_num = random.randint(1, 50)

attempt = 1
won = False

while attempt <= 7:
    guess = int(input(f"Guess the secrect number {attempt}: "))
    
    if guess == secret_num:
        print("excellent!")
        won = True
        break
        
    elif guess < secret_num:
        print("Too Low!")
    elif guess > secret_num:
        print("Too High!")
    attempt += 1
   

if  won :
    print(f"You won in {attempt} attempts!")
else:
    print(f"Game Over! The number was {secret_num}")