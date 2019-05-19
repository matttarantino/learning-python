"""
Author: Matt Tarantino
Description: This application will prompt the user for their name, and then
ask the user to guess a number between the defined range. If the user does not
guess the correct number in the allowed guesses, it will return them the number.
If the user does guess the number before they hit the maximum number of allowed
guesses, then the program will let them know and return how many gueseses it took.
"""

import random

#define the constants
RANGE_MIN = 1
RANGE_MAX = 20
ALLOWED_GUESSES = 6

#calculate the random number between the range
number = random.randint(RANGE_MIN, RANGE_MAX)

#this is a custom function that will return either 0, 1, or -1 depending on the
#inputs.
def calculateGuess(number, guess):
    if number == guess:
        return 0
    elif number < guess:
        return -1
    elif number > guess:
        return 1


try:
    name = input('Hello! What is your name? ')
except EOFError:
    print('EOF command given. Quitting...bye!')
    exit()
except:
    print('This input is invalid! Please try again.')
    exit()

print(f'Well, {name}, I am thinking of a number between {RANGE_MIN} and {RANGE_MAX}.')

#set a variable to the constant as we will be reducing the variable, but dont
#want to touch the constant.
guesses = ALLOWED_GUESSES

#will continue until guesses is zero.
while guesses > 0:
    try:
        guess = input('Take a guess: ')
        #converts the inputs to a float and will catch for errors.
        guess = float(guess)
    except EOFError:
        print('EOF command given. Quitting...bye!')
        exit()
    except:
        print('This input is invalid! Please try again.')
        #does not take a guess away until they enter a valid input. we have to
        #do this because we cannot continue this iteration of the while loop
        #until a valid input is entered.
        continue

    #calls the custom function defined above and stores the result to a variable
    result = calculateGuess(number, guess)

    if guess > RANGE_MAX or guess < RANGE_MIN:
        print('You guessed outside the range. Please try again.')
    elif result == 0:
        #calculates how many guesses it took them to complete
        attemps = ALLOWED_GUESSES - guesses + 1

        print(f'Good job, {name}! You guessed my number in {attemps} guesses!')

        #exits the loop if they correctly guessed the number
        break
    elif result == -1:
        print('Your guess is too high.')
    elif result == 1:
        print('Your guess is too low.')

    #reduces the guesses variable by one so the while loop doesn't run forever
    guesses = guesses - 1

#if the while loop reaches 0 and finishes, then we will inform the user that
#they did not correctly guess in the alloted number of guesses and return the
#random number
if guesses == 0:
    print(f'The number I was thinking of was {number}')
