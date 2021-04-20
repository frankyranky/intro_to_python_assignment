"""
File: guessmynumber.py
----------------------
This program checks if a user's guess of a number matches that guessed by the computer
"""

"""
Franklin Kome Amoo
"""

# import the random module for generating random numbers
import random
# use code below  to generate a random integer between 30 and 50 for example
#print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************

from random import randint  # import randint from the random module

# The first argument to be passed to randint function as the lower limit
minimumLimit = 1

# The second argument to be passed to randint function as the upper limit
maximumLimit = 99

# Generate the random number between 1 and 99, the minimum and maximum integer limits from randint
computerRandomNumber = random.randint(minimumLimit, maximumLimit)

# Ask the user to guess the generated random number between 1 and 99,
# the minimum and maximum integer limits from randint
print("I am thinking of a number between " , minimumLimit, " and ", maximumLimit)
userGuessedNumber = eval(input("Please ENTER your guessed number : "))

# Loop to compare the user's guessed number to the computer generated random number
# Loop to compare the user's guessed number is not zero (0), loop to keep guessing the computer's number
while userGuessedNumber != computerRandomNumber:
        # If the user's guessed number is greater than the computer's
        # random number, display too high message
        if userGuessedNumber > computerRandomNumber :
            print("I am sorry, Your guess is too high\n" )
            # If the user's guessed number is lesser than the computer's
            # random number, display too low message
        elif userGuessedNumber < computerRandomNumber:
            print("Your guess is too low\n")
            # If the user's guessed number is the same as the computer's
            # random number, display guessed right message
        else:
            print( "Your guess is right" )
        # While the user's guessed number is not correct, get user to keep 
        # guessing the computer's random number
        userGuessedNumber = eval(input("\nPlease ENTER your guessed number again : "))
print("Yes, the number is ", userGuessedNumber)
print("\nThat ends the guesses\n")
