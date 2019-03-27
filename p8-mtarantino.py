"""
Author: Matt Tarantino
Description: This application will prompt the user to enter a file path. The
program will then open and read the file, looking for lines that begin with
From:. It will then parse the email address out of the line and add it to a
dictionary with a count of 1. For each repeat, it will increment the count.
After all lines have been checked, and all emails added to the dictionary the
program will iterate through the dictionary and find the sender with the highest
number of sent emails, and return that information to the user.
"""
import re

#custom method that uses re to regex the email. If the email does
#not match the regex, false is returned.
def valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

#prompts the user for the filename, with error handling.
try:
    file_name = input('Enter the file name (include path if file is outside directory): ')
except EOFError:
    print('EOF command given. Quitting...bye!')
    exit()
except:
    print('This input is invalid! Please try again.')
    exit()

#attemps to the open the file, with exception handling if the program
#cannot find the file or another error occurs.
try:
    file = open(file_name)
except FileNotFoundError:
    print('File cannot be opened:', file_name)
    exit()
except:
    print('An error occurred opening this file! Please try again.')
    exit()

#creates a new dictionary
sender_counts = dict()

#reads the file line by line
for line in file:
    #strips the tailing characters
    line = line.rstrip()

    #skips to the next line if the line is not what we are looking for
    if not line.startswith('From:'): continue

    #if the content is not able to be parsed, it will alert the
    #user and exit.
    try:
        #gets the remainder of the line after the : In this case its the email address.
        email = line.split(': ')[1]

        #if the parsed email is not valid, then raise an error. This error will
        #be caught by the except and a message will be returned the user.
        if not valid_email(email):
            raise Exception('Malformed email detected!')

        #adds the parsed email to the dictionary and increments the count.
        #If the email is not already in the dictionary, then this method will
        #add it with a value of 0, and increment. If it already exists, it will
        #only increment.
        sender_counts[email] = sender_counts.get(email, 0) + 1
    except:
        print('Bad data was detected! Please check your file and try again.')
        exit()

#Make sure the program found at least 1 line before proceeding.
if len(sender_counts) == 0:
    print('The program did not find any email addresses! Please check your file and try again.')
    exit()

max_sender = ""
max_count = 0

#goes through the dictionary item by item
for key in sender_counts :
    #if the value is greater than the highest items so far, then rewrite the variables
    if sender_counts[key] > max_count :
        max_sender = key
        max_count = sender_counts[key]

print(f'The email with the most sent messages is {max_sender} with {max_count} emails.')
