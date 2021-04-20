"""
File: khansole_academy.py
-------------------------
Khansole Academy is a program that teaches users how to add by asking users to input answers for the addition of two
randomly generating integers between 10 and 99 inclusive. The program returns feedback based on the User's answers.

"""

"""
Franklin Kome Amoo
"""

# import the random module for generating random numbers
import random

# use code below  to generate a random integer between 30 and 50 for example
#print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************

# import randint from the random module for use in 
#from random import randint  

# The first argument to be passed to randint function as the lower limit
lowerLimit = 30

# The second argument to be passed to randint function as the upper limit
upperLimit = 50

# The first random number generated for the addition process
firstRandomNumber = random.randint(lowerLimit, upperLimit)

# The second random number generated for the addition process
secondRandomNumber = random.randint(lowerLimit, upperLimit)

# Display the two random numbers generated for the addition process
print("I am thinking of the numbers " , firstRandomNumber, " and ", secondRandomNumber )
#print(random.randint(firstRandomNumber, secondRandomNumber))

# Assign the sum of the two random numbers generated for the addition process to variable computer result
computerResult = firstRandomNumber + secondRandomNumber

# Ask user to tell the sum of the two random numbers
print("What is ", firstRandomNumber , " + ", secondRandomNumber , "?")
userResult = eval(input("Your answer, please? : "))

# Initialise counter for the user's correctly determined answers for the sum for the addition of the numbers
correctAnswers = 0
inCorrectAnswers = 0 

while correctAnswers <= 2 :
    if userResult == computerResult:
        correctAnswers += 1 
        print("Correct. You have " , correctAnswers, " correct answers in a row")

        # The first random number generated for the addition process
        firstRandomNumber = random.randint(lowerLimit, upperLimit)

        # The second random number generated for the addition process
        secondRandomNumber = random.randint(lowerLimit, upperLimit)
        
        # Display the two random numbers generated for the addition process
        print("I am thinking of the numbers " , firstRandomNumber, " and ", secondRandomNumber )
        #print(random.randint(firstRandomNumber, secondRandomNumber))

        # Assign the sum of the two random numbers generated for the addition process to variable computer result
        computerResult = firstRandomNumber + secondRandomNumber

        # Ask user to tell the answer sum of the two random numbers
        print("What is ", firstRandomNumber , " + ", secondRandomNumber , "?")
        userResult = eval(input("Your answer please? : "))
    else:
        print( "Incorrect, the expected answer is ", computerResult )
        inCorrectAnswers += 1 
        print( "You have ", inCorrectAnswers, " incorrect answers now " )

        # The first random number generated for the addition process
        firstRandomNumber = random.randint(lowerLimit, upperLimit)

        # The second random number generated for the addition process
        secondRandomNumber = random.randint(lowerLimit, upperLimit)
        
        # Display the two random numbers generated for the addition process
        print("I am thinking of the numbers " , firstRandomNumber, " and ", secondRandomNumber )
        #print(random.randint(firstRandomNumber, secondRandomNumber))

        # Assign the sum of the two random numbers generated for the addition process to variable computer result
        computerResult = firstRandomNumber + secondRandomNumber

        # Ask user to tell the sum of the two random numbers
        print("What is ", firstRandomNumber , " + ", secondRandomNumber , "?")
        userResult = eval(input("Your answer please? : "))
print("\nWell done. You have completed the exercise with ", correctAnswers, " correct answers")

print("\nThat ends it\n")
