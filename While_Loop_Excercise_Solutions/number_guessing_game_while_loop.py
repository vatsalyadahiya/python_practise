#14. Create a number guessing game: 
#• Generate a random number (1–10) 
#• Keep asking user until they guess correctly

import random
secret_number = random.randrange(1, 11)
n = int(input("Number guessing game (1-10): "))

while n != secret_number:
    print("Incorrect guess, guess again!")
    n = int(input("Number guessing game (1-10): "))

print("Number guessed correctly!")