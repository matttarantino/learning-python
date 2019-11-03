# P9: Classic Books

Create a Python program that prompts the user for the name of a file with an arbitrary ASCII document, reads the file, and prints a summary of the words in the document.

The summary should include:

-   Total words
-   Total distinct words
-   The top 25 most frequent words and counts (You do NOT need to handle ties.  Just pick the top 25)
-   Character frequency sorted from most frequent to least frequent characters

Test your program on a small file that you can check manually and then download Mark Twain's Adventures of Tom Sawyer from [http://www.gutenberg.org/ebooks/74 (Links to an external site.)](http://www.gutenberg.org/ebooks/74) and verify that your code works on a large input file.

Note: Python's collections module has a really convenient Counter object that is a perfect match for this task, but that would be too easy!   Instead, please use either a dictionary or check out DefaultDict.

Hints:

-   One of the challenges in this task is that prose contains not only words but but also punctuation, e.g. this sentence includes commas, periods, and exclamation marks!   Python's string module includes a translate() function that allows you to translate from one set of characters to another and to eliminate a set of characters.   You can use translate() to remove all punctation characters as follows:
-   In Python 2.7, there is a very straightforward way to remove punctuation from a string:

from string import punctuation

cleanString = dirtyString.translate(None, punctuation)

-   But in Python 3.4, this doesn't work. In 3.4 you still import punctuation from string, but then you set up a punctuation translator: 

from string import punctuation

punc_translator = str.maketrans({key: None for key in punctuation})

cleanString = dirtyString.translate(punc_translator)

-   We also want to collapse upper and lower case characters so "Hello" and "hello" are both included as "hello".   We can use the string.lower() function to accomplish this. e.g. "HeLlO tHeRe".lower() returns "hello there".
-   We've seen in earlier assignments that dictionaries are a convenient way to count items.  We saw that we could handle new dictionary keys by using the default value argument to dict.get(key, default), e.g.

         **d = dict()**

**         d['newKey'] = d.get('newKey',0) + 1**

      Another approach is to use a defaultdict instead of a dict.

        **from collections import defaultdict**

**        dd = defaultdict(int)   # the default value will be an int with value 0**

**        dd['newKey'] += 1**

-   After we've counted all the words and characters, how do we find the most frequent?    Say we have a dictionary, d, with values {'elephant': 3, 'frog': 2, 'hippo': 1, 'lion': 2, 'monkey': 4}.   We can sort the keys with 

          **sorted(d**) returns ['elephant', 'frog', 'hippo', 'lion', 'monkey'], i.e. returns a list of the sorted keys

     To sort the dictionary items we can use 

           **sorted(d.items())** which returns [('elephant', 3), ('frog', 2), ('hippo', 1), ('lion', 2), ('monkey', 4)]

     But that list is sorted by the key, not the value.   We can fix that using another Python function

          **from operator import itemgetter**

**          s = sorted(animals.items(),key=itemgetter(1), reverse=True)**

**     sorted(key=itemgetter(n)) **says to use the nth element as the sort key

     so s == [('monkey', 4), ('elephant', 3), ('lion', 2), ('frog', 2), ('hippo', 1)] which we can use in the next step   

-   The final task is to identify the 25 most frequent words and we don't need to handle ties.   We can easily use Python's slices to implement this.   We used slices with words in the assignment where we converted from singular to plural.  Slices work the same way with lists as with words.  
-   When printing large numbers, it's nice to include commas.    E.g.

          **'{:,}'.format(1000000) ** ==  '1,000,000'
