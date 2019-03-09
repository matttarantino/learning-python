"""
Author: Matt Tarantino
Description: This application will prompt the user to enter a quiz score and if
the score is valid, it will return a letter grade. If the score is invalid, a
message will be returned to the user. If the score is out of bounds (0 to 100)
then a message will be returned to the user asking them to enter a number between
0 and 100. For example, entering a 90 will return A-. Entering "twenty" will
return "This input is invalid! Please enter a numeric value." Entering 200 will
return "Please enter a score between 0 and 100!"
"""

#promts the user for a quiz score
score = input('Please enter the quiz score: ')

#tries to convert the input into an integer and re-assigns the score variable
#to the value. If the float method throws an exception, then it will be caught
#by the except which will return a message to the user and exit the program,
#stopping any further execution. If the exit is not present, the if statement
#would continue and return another error to the user.
try:
    score = float(score)
except:
    print('This input is invalid! Please enter a numeric value.')
    exit()

#Given everything is okay so far, the score will go through the if/elif/else
#chain. If the score does not match any conditions (outside of 0 to 100) then
#the else statemnt will execure and print a statement to the user asking for a
#value between 0 and 100. This is also done within a try/except so that if anything
#went wrong, a general "try again" message will be returned to the user.
try:
    if 93 <= score <= 100:
        print('A')
    elif 90 <= score < 93:
        print('A-')
    elif 87 <= score < 90:
        print('B+')
    elif 83 <= score < 87:
        print('B')
    elif 80 <= score < 83:
        print('B-')
    elif 70 <= score < 80:
        print('C')
    elif 0 <= score < 70:
        print('F')
    else:
        print('Please enter a score between 0 and 100!')
except:
    print('An error occurred while processing the score. Please try again!')
