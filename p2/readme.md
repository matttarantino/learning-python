# P2: Convert numeric scores to grades

This week's reading (Chapter 3 in Severance) discusses conditionals, e.g. if-then-else statements, that allow our programs to make different decisions based on different values.   Handling exceptions with try/except was also covered.   Exceptions and try/except are critical concepts in Python.   

Write a script that asks the user for a quiz score and converts that numeric score to a letter grade as follows:

score >= 93: A

90 <= score < 93: A-

87 <= score < 90: B+

83 <= score < 87: B

80 <= score < 83: B-

70 <= score < 80: C

<70: F

Since legal scores generally fall between 0 and 100, your script should reject numbers above 100 or below 0. 

The **input()**, **float()** and **print()** functions are important as are conditionals and **try**/**except**.   Note that **input()** returns a string and not a number so you'll need to convert the value returned to a floating point number before comparing it to other numbers. Calling **float**('twenty') will fail and raise an exception which you can catch and respond appropriately using **try**/**except**.

Be sure to test your program on at least the following test inputs:

100, 93, 92.99, 90, 89.9, 87, 83, 80, 75, 69, eighty, -1, 101

Be sure that your program provides a good user experience on invalid inputs by catching bad input values and warning the user.   

Everything you need to know is covered in the Serverance text, Chapter 3.  Please don't hesitate to reach out to me by email if you have questions or problems getting the code to work properly.
