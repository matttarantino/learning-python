"""
Author: Matt Tarantino
Description: This application will prompt the user to enter a string containing
multiple words, each with a space inbetween. This program will then take each
word and determine the plural version of each word using a list of heuristics.
The program will then return the user a sentence with the plural version of each
word seperated with a space.
"""

#custom method that returns the plural version of the input based on a few
#rules defined below
def plural(string):
    #if the string ends with y but is not preceded by a vowel, remove the y
    #and add ies to the string. The reason I did not duplicate the "s" logic within
    #the y check is because with this logic, words ending with y preceded by a vowel
    #will fail the first two conditions, and be picked up by the third condition
    #which adds an "s" to anything that does not match previous conditions anyway.
    if string.endswith('y') and not string[:-1].endswith(('a', 'e', 'i', 'o', 'u')):
        #remove the y and add 'ies' to the string
        return string[:-1] + 'ies'
    #if the word ends in 'o','ch', 's', 'sh', 'x', or 'z' then add 'es'. This is done
    #using a tuple
    elif string.endswith(('o', 'ch', 's', 'sh', 'x', 'z')):
        return string + 'es'
    else:
        return string + 's'

try:
    string = input('> ')
except EOFError:
    print('EOF command given. Quitting...bye!')
    exit()
except:
    print('This input is invalid! Please try again.')
    exit()

output = []

#takes the string and splits the string into individual words
words = string.split()

#loops through the words and assigns each word to a variable called word
for word in words:
    #appends the plurarilized version of the word to the array output
    output.append(plural(word))

#prints the output array using the join method putting a space in between each
#item in the array
print(" ".join(output))
