# P8: Counting unique items

Study Severance Chapter 9.

Write a program that reads the mbox.txt file from the previous assignment and counts the total number of email messages sent by each user.  Your program should print the email address and the number of emails sent for the email address that sent the most emails.

Hints:

-   You can identify senders by looking for lines that start with "From: <senderEmail>".  
-   Store the sender's email and the total number of emails sent in a dict().    
-   Dictionaries raise a KeyError exception if you specify a key that is not found in the dictionary, but dict.get(key,default=None) can be used to simplify your code. E.g. 

      d = dict()

      #  d['unknown key']  raises a KeyError exception

      d.get('unknown key', 0) # adds 'unknown key' to dictionary d with value 0

      d.get(key, 0) += 1  # adds key to the dictionary with value 0 if key is not already in the dictionary and then adds 1

                                    # or increments the value if key is already in the dictionary

-   You can track the max emails and sender either as you read the file or wait until the entire file has been read and then find the max after reading the file.
