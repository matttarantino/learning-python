# P4: Guess a Number using loops and a function

Study Severance Chapter 5 this week.

Some Python functions exist in separate programs called modules that can be brought into any Python script for your use by importing them with an **import **statement. For this program, we will want to generate a random number which we can do using the Python *random* module. It is good form to import all the modules you will use at the beginning of the program so begin this script with the statement

**import ***random*

Within the *random* module is a function for generating a random integer (*randint*). **randint** takes two parameters, the lower bound and the upper bound; and since it is called from the *random* module, its form is

**random.randint**(*lower-bound*, *upper-bound*).

To get a random number between 1 and 100, the statement would look like this:

            number = **random.randint(1, 100)**

Your assignment is to write a script (a program) that implements a "Guess the Number" game. Your script must generate a random number between 1 and 20 and ask the user to guess the number, telling them what numbers the random number falls within. Give the user 6 tries. Running my script, it looks like this:

Hello! What is your name? *Jim*

Well, Jim, I am thinking of a number between 1 and 20.

Take a guess. *5*

Your guess is too low.

Take a guess. *10*

Your guess is too high.

Take a guess. *7*

Your guess is too low.

Take a guess. *8*

Your guess is too low.

Take a guess. *9*

Good job, Jim! You guessed my number in 5 guesses!

If Jim hadn't found the number in 6 tries, the script would say "The number I was thinking of was *__*"

Your solution should include a function that takes two parameters, the number to be guessed and the number that was guessed and returns:

-   0 if the two numbers match 
-   -1 if the number to be guessed is smaller than the number that was guessed
-   1 if the number to be guessed is larger than the number that was guessed

Your program should generate the target random number and then loop until either the user guesses the target or exceeds 6 tries. Each iteration through the loop should collect the user's guess, and then call your function to compare the guess to the target.  Be sure to use a try/except block to insure that your program handles invalid inputs in a user friendly manner.

Be sure to test your program under a variety of conditions, including:

- the user guesses the number in < 6 tries

- the user doesn't guess the number in 6 tries

- the user enters invalid input, e.g. twenty

- the user enters a value < 1 or > 20

Submit your script as a .py file by uploading it to this assignment.  Include a comment at the beginning with your name and the purpose of the program (and include any other comments you wish throughout the program
