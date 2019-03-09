"""
Author: Matt Tarantino
Description: This application will prompt the user to enter 3 inputs
and evaluate the inputs to return the max in a print statement.
"""

#Requests inputs from user. If an error occurs, a message
#will be returned to the user and the script will exit.
try:
    input1 = input('Please enter the first value: ')
    input2 = input('Please enter the second value: ')
    input3 = input('Please enter the third value: ')
except EOFError:
    print('EOF command given. Quitting...bye!')
    exit()
except:
    print('This input is invalid! Please try again.')
    exit()

if input1.isspace() or input2.isspace() or input3.isspace():
    print('One or more of your inputs contained only spaces. Please try again with valid inputs (letters, numbers, strings)!')
    exit()

#Custom defined function that takes 3 parameters and compares them to return
#the max of the 3 parameters.
def maxOfThree(first, second, third):
    max = first

    if second > first:
        max = second

    if third > max:
        max = third

        #Need to check second against third incase the first if statement did
        #not execute.
        if second > third:
            max = second

    return max

#calls the function and saves the response to a variable called max
#(used in print).
max = maxOfThree(input1, input2, input3)

print('The maximum of ' + input1 + ' ' + input2 + ' ' + input3 + ' is ' + max)
