"""
Author: Matt Tarantino
Description: This application will prompt the user to enter a file path. The
program will then open and read the file. For each line in the file, it will
strip whitespace characters, remove punctuation, and lowercase all letters. It
will then split the line into words. For each word, it will add the word to a
dictionary, and increment the count. It will also increment a total word counter.
It will then split each word into characters and add each character into a
dictionary. The program will finally report a summary including total word count,
total distinct words, top 25 most used words, and the count of each character used
from most to least.
"""
import re
#imports the necessary helpers for default dictionaries and sorting
from collections import defaultdict
from operator import itemgetter

#custom method that formats the input to include commas in the proper places
def format(number):
    return '{:,}'.format(number)

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
    file = open(file_name, encoding="utf-8")
except FileNotFoundError:
    print('File cannot be opened:', file_name)
    exit()
except:
    print('An error occurred opening this file! Please try again.')
    exit()

#inits the word dictionary, word counter, and letter dictionary. It also sets
#up the regex we will use against the line.
word_dictionary = defaultdict(int)
word_count = 0
letters_dictionary = defaultdict(int)
regex = re.compile('([^\s\w]|[0-9_])')

#iterates through each line in the file
for line in file:
    line = line.rstrip()

    #if the content is not able to be parsed, it will alert the
    #user and exit.
    try:
        #performs the regex on the line
        line = regex.sub('', line)
        line = line.lower()
        words = line.split()
        for word in words:
            print(word)
            #adds the word to the word dictionary
            word_dictionary[word] += 1
            word_count = word_count + 1
            for letter in word:
                print(letter)
                #adds each letter in the word to the letter dictionary
                letters_dictionary[letter] += 1
    except:
        print('Bad data was detected! Please check your file and try again.')
        exit()

#Make sure the program found at least 1 word before proceeding.
if len(word_dictionary) == 0:
    print('The program did not find any words in the file! Please check your file and try again.')
    exit()

#begins printing the summary
print('----------------')
print(f'The are {word_count} total words.')

#gets the length of the words dictionary
distinct_words = len(word_dictionary.items())

print(f'The are {distinct_words} distinct words.')

#sorts the words dictionary by the value, and reverses it so the top words are
#at the end. Then uses a slice to get the last 25 items.
sorted_words = sorted(word_dictionary.items(),key=itemgetter(1), reverse=True)
top_words = sorted_words[:25]

#prints the top 25 words by iterating through the list and printing the key and
#formatted value.
print('The top 25 most used words are:')
for key, value in top_words:
    print(f'{key} => {format(value)}')

#sorts the letters dictionary by the value, and reverses it so the top letters are
#at the end.
letters = sorted(letters_dictionary.items(),key=itemgetter(1), reverse=True)

#prints the top letters by iterating through the list and printing the key and
#formatted value. This prints all letters in descending order.
print('The top most used letters are:')
for key, value in letters:
    print(f'{key} => {format(value)}')
print('----------------')
