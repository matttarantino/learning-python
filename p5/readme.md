# P5: String manipulation

Study Severance Chapter 6.

English is a really silly language with many different rules for converting singular to plural.    Your assignment this week will use a simplified set of rules for converting singular to plural.

Read a line of text from the user with input() and convert each word in the line from singular form to plural form using the following heuristics:

-   if the word ends in a 'y' preceded by a vowel (a,e,i,o,u), add 's'; e.g. monkey -> monkeys
-   if the word ends in 'y' not preceded by a vowel, remove the 'y' and add 'ies', e.g. fly -> flies
-   if the word ends in 'o','ch', 's', 'sh', 'x', or 'z' then add 'es'
-   otherwise, just add 's'

For example, if the user enters: 'monkey elephant potato porch fly button fish fox buzz', then the output should be 'monkeys elephants potatoes porches flies buttons fishes foxes buzzes'

Organize your program with a function 'plural(s)' which given a string, returns the plural form of the string using the rules above.  Read the line of input and call plural() on each token in the string and create a new string, appending each token to the new string.   Write your final output with a single print, don't print each word separately.

Hint 1:  Python includes a function called endswith() that might be useful...  

E.g.   'monkey'.endswith('ey) returns True

Hint 2: There are several ways to calls endswith(), either with a single string or a tuple of strings.   We haven't covered tuples yet, but a tuple is like a list except that is defined with parens and the members are immutable.

E.g.    'monkey'.endswith(('ay', 'by', 'cy', 'dy', 'ey')) returns True. 

          In this case, endswith() checks if the string ends with any of the strings.

Hint 3: Slices are very useful when dealing with strings, e.g. 

          'monkey'[-1:] returns the last character of 'monkey' which is 'y'

          'monkey[:-1] returns all but the last character of 'monkey', i.e. 'monke'

Slices work with strings, lists, and tuples.

Hint 4: Experiment with the statement

      " ".join(['hello','world'])

Try it out and see what it does.   This might come in handy.
