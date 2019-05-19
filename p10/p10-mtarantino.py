"""
Author: Matt Tarantino
Description: This application will prompt the user to enter a file path. The
program will then open and read the file, looking for lines that match the regex
defined below. For each matching line, it will take each match and enter it into
an items array after converting the number to a float. It will then compute the
average and return the average and number of entries in the array to the user.
"""
import re

#custom method that calculates the average by taking an array as an input, and
#divides the sum of the array by the number of items in the array.
def average(items):
    return sum(items) / len(items)

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

items = []

try:
    #reads the file line by line
    for line in file:
        #strips the tailing characters
        line = line.rstrip()

        #applies the regex to the line and returns the matches in an array
        matches = re.findall('^New Revision: ([0-9]+.[0-9]+)', line)

        #if the array contains at least 1 item, loop through the matches and
        #convert the individual item into a float, before adding it to the items
        #array. If an error occurs while this happens, the except will preset
        #an error to the user and exit the program.
        if len(matches) > 0:
            for item in matches:
                number = float(item)
                items.append(number)
except:
    print('Bad data was detected! Please check your file and try again.')
    exit()

#Make sure the program found at least 1 matching line before proceeding.
if len(items) == 0:
    print('The program did not find any matching lines! Please check your file and try again.')
    exit()

#calls the average method and then rounds it to a single decimal place.
average = average(items)
average = round(average, 1)

#returns the info back to the user
print(f'Average = {average}')
print(f'Number of lines = {len(items)}')
