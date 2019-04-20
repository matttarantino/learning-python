"""
Author: Matt Tarantino
Description: This application will prompt the user to enter a file path. The
program will then open and read the file, looking for lines that begin with a
certain heading. It will then convert the following number to a floating point
number while also adding it to an array. Once done reading the file, it will
compute the average and return it to the user.
"""

#custom method that calculates the average by taking an array as an input, and
#divides the sum of the array by the number of items in the array.
def average(numbers):
    return sum(numbers) / len(numbers)

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

items = []

#reads the file line by line
for line in file:
    #strips the tailing characters
    line = line.rstrip()

    #skips to the next line if the line is not what we are looking for
    if not line.startswith('X-DSPAM-Confidence:'):
        continue

    #gets the remainder of the line after the :
    line = line.split(':')[1]

    #attemps to convert the string into a number, and adds it to the array.
    #if the content is not able to be converted to a float, it will alert the
    #user and exit.
    try:
        number = float(line)
        items.append(number)
    except:
        print('Bad data was detected! Please check your file and try again.')
        exit()

#Make sure the program found at least 1 line before proceeding to math.
if len(items) == 0:
    print('The program did not find any matching lines! Please check your file and try again.')
    exit()

#calls the average method and then rounds it to a length of 4 digits.
output = average(items)
output = round(output, 4)

print(f'Average spam confidence: {output}...')
