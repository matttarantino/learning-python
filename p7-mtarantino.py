"""
Author: Matt Tarantino
Description: This application will prompt the user to enter a file path. The
program will then open and read the file, looking for lines that begin with
From:. It will then parse the email address out of the line and add it to a
set. Sets are unique so repetitive lines will be ignored in the set. After all
lines have been checked, the program will calculate the length of the set and
return the unique number of senders to the user.
"""
import re

#custom method that uses re to regex the email. If the email does
#not match the regex, false is returned.
def valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

#prompts the user for the filename, with error handling.
try:
    string = input('Enter the file name (include path if file is outside directory): ')
except EOFError:
    print('EOF command given. Quitting...bye!')
    exit()
except:
    print('This input is invalid! Please try again.')
    exit()

#attemps to the open the file, with exception handling if the program
#cannot find the file or another error occurs.
try:
    file = open(string)
except FileNotFoundError:
    print('File cannot be opened:', string)
    exit()
except:
    print('An error occurred opening this file! Please try again.')
    exit()

#creates a new unique set
items = set()

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
        line = line.split(': ')[1]

        #if the parsed email is not valid, then raise an error. This error will
        #be caught by the except and a message will be returned the user.
        if not valid_email(line):
            raise Exception('Malformed email detected!')

        #adds the parsed line to the set. Items already in the set will be ignored.
        items.add(line)
    except:
        print('Bad data was detected! Please check your file and try again.')
        exit()

#Make sure the program found at least 1 line before proceeding.
if len(items) == 0:
    print('The program did not find any matching lines! Please check your file and try again.')
    exit()

#gets the length of the set and stores it to an output variable for easier printing
output = len(items)

print(f'There are {output} unique senders in this file.')
