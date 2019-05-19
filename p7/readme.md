# P7: Finding unique strings

Study Severance Chapter 8.

Using mbox.txt file, find the lines that start with From: and determine how many unique sender email addresses are included in this file, e.g.

From: cwen@iupui.edu

There are a number of ways to achieve this task but you'll need to identify and parse the appropriate lines and then collect and finally count the unique email addresses. You may want to use a python list or learn about python sets. If you use a list, you should check to see if the email address is already in the list and add it only if it is not already in the list. Alternatively, you can add all email addresses to your list and then identify the number of unique values at the end. Sets are like lists but sets guarantee that all values are unique. Both lists and sets allow you to say len(list) or len(set). Please note that you must implement only one approach, not all three, and you're free to use a completely different approach. Be sure you are including only the email addresses of senders!


Verify that your responds properly with empty files, non-existent files, and files that contain no relevant "From:" lines. You may want to debug your program with mbox-short.txt but verify that it works properly with mbox.txt as well.

Also be sure to keep your try/except blocks small for readability. You may want to use the try:/except:/else: form of the statement.

As always, please let me know if you have any questions about the assignment.
