"""
Author: Matt Tarantino
Description: This application will prompt the user to enter a URL, with validation
to ensure they enter a url that starts with http:// or https://. It will then
request the URL and get back the HTML contents. It will then use regex to parse
out the href links. For each link, it will decode, lower the URL (incase it was capital),
and add it to a set to ensure uniqueness. At the end of the program, it will return
the unique number of links it was able to parse from the URL.
"""
#import required libraries
import urllib.request, urllib.parse, urllib.error
import re
import ssl

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#ask the user for a URL and lowercase the input incase its capital, with error handling
try:
    url = input('Enter a URL (Be sure to include http(s)://): ')
    url = url.lower()
except EOFError:
    print('EOF command given. Quitting...bye!')
    exit()
except:
    print('This input is invalid! Please try again.')
    exit()

#if the user did not enter a properly formatted URL, then throw an error.
if not (url.startswith('http://') or url.startswith('https://')):
    print('This URL is invalid! Please make sure it starts with http(s):// and try again.')
    exit()

#ueses the urllib library to make the http request and get the contents of the URL
try:
    #makes the request and stores it in an html variable.
    html = urllib.request.urlopen(url, context=ctx).read()
except:
    print('An error occurred while opening this URL! Please check the URL, website, or internet connection and try again.')
    exit()

#gets all the links by applying the regex to the html contents
links = re.findall(b'"(http[s]?://.*?)"', html)

#creates a new unique set
items = set()

#Make sure the program found at least 1 link before proceeding.
if len(links) == 0:
    print("The program did not find any links! Please check your URL and try again.")
    exit()

#loops through the links
for link in links:
    #decodes the link
    link = link.decode()
    #lowercase any links found on the page
    link = link.lower()
    #adds the parsed link to the set. Items already in the set will be ignored.
    items.add(link)

#gets the length of the set and stores it to an output variable for easier printing
output = len(items)

print(f'There are {output} unique links parsed from your URL.')
