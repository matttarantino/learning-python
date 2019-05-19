# P10: Writing Regex's

Study chapter 11 of Severance.

Write and submit a script that asks for a filename (to which mbox.txt and mbox-short.txt will be used) and looks for lines of the form

New Revision: 39772

Extract the number from each of the lines using a regular expression and the **findall()** method. Compute the average of the numbers, rounded to a single decimal place, and print out the average and the number of lines used for the computation.

Enter filename: mbox.txt

Average = 38549.8

Number of lines = 1790



Enter filename: mbox-short.txt

Average = 39756.9

Number of lines = 27

You may find https://www.debuggex.com/?flavor=python Links to an external site. to be a helpful resource for writing and testing your regular expression.
