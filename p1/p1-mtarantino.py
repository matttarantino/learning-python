"""
Author: Matt Tarantino
Description: This application will prompt the user to enter their first name
and last name, and will then return that information to them within a sentence:
Hello Matt Tarantino
"""

#creates a first_name variable equal to an input method that will ask the user a
#question. The response from the input method will be stored to the
#first_name variable to be used later.
first_name = input('What is your first name: ')

#creates another variable called last_name and is equal to an input method that
#will ask the user a second question. The response from the input method will be
#stored to the last_name variable to be used later.
last_name = input('What is your last name: ')

#Prints the variables along with some hardcoded strings including Hello, and a
#string containing a space between the first_name and last_name variables. Also
#contains a try/except to catch any error with printing the concatenated string.
try:
    print('Hello ' + first_name + ' ' + last_name)
except:
    print('An error occurred. Please try again!')
