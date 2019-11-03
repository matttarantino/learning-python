# P6: Slicing & Dicing files

Severence's chapters 6 and 7 are needed for this assignment.

Download [www.py4inf.com/code/mbox.txt (Links to an external site.)](http://www.py4inf.com/code/mbox.txt) and [www.py4inf.com/code/mbox-short.txt (Links to an external site.)](http://www.py4inf.com/code/mbox-short.txt) to your working Python directory. Each of these files contain email messages from a variety of persons and institutions.

Do what in my version of Severence is Exercise 7.2.

"Write a program to prompt for a file name, and then read through the file and look for lines of the form:

X-DSPAM-Confidence: **0.8475**

"When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart the line to extract the floating point number on the line. Count these lines and compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence" rounded to four decimal places.      

 Enter the file name: mbox.txt

 Average spam confidence: 0.8941....

       Enter the file name: mbox-short.txt

       Average spam confidence: 0.7507....

 "Test your file on the mbox.txt and mbox-short.txt files."

Be sure to use **try** and **except** when querying the user for file names.  

Your code should handle bad data values, e.g. what happens if the input file is corrupted, e.g. 

X-DSPAM-Result: Innocent\
X-DSPAM-Processed: Sat Jan 5 09:14:16 2008\
X-DSPAM-Confidence: BAD value\
X-DSPAM-Probability: BAD value\
X-DSPAM-Confidence: BAD\
X-DSPAM-Probability: BAD

Also, be sure that you test your program to be sure that it works properly with empty files or non-existent files, e.g. the user types in the wrong file name.  Beware evil professors who might run test cases that might cause a divide by zero error.

Hint:  Python has a number of useful functions that apply to strings including

str.find(str, beg=0  end=len(string))
