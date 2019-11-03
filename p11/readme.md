# P11: Browsing the Web

Python makes it easy to access websites programmatically which can be very useful for applications such as web crawling or interacting with web sites from a Python program. See chapter 12 of the Severance text.  

Your assignment is to write a Python script that is able to read an arbitrary URL provided by the user and count the number of unique web links on that page. For this purpose,  you may assume that a web link can be identified with a regular expression that recognizes http and https references, e.g.:

-   [http://my.favorite.url (Links to an external site.)](http://my.favorite.url/)
-   [HTTP://MY.FAVORITE_URL.ORG (Links to an external site.)](http://my.favorite_url.org/)
-   [https://123.456.788.111/foo.txtLinks to an external site.](https://123.456.788.111/foo.txt)
-   [HTTPS://foo.bar (Links to an external site.)](https://foo.bar/)

You should ***NOT*** include local file references in your distinct count, e.g. 

-   /news/guitar-great-carlos-alomar-technology-offers-new-opportunities-todays-musicians
-   /events/innovation-expo-2016
-   /events/alumni-weekend-2016

URLs occur in a variety of contexts in some sites including:

<meta content="[http://www.google.com (Links to an external site.)](http://www.stevens.edu/)/" >

<link href="http://www.google.com/" />

<a href="[http://www.google.com/maps (Links to an external site.)](http://www.stevens.edu/mystevens)" </a>

<source  srcset="http://www.google.com/sites/stevens_edu/files/styles/home_feature_persona_250x172/public/Elizabeth-Pascetta.jpg?itok=pptNNoVG">

<img src="[http://www.stevens.edu/sites/stevens_edu/files/styles/home_feature_persona_80x80/public/Elizabeth-Pascetta.jpg?itok=_ut8qP45 (Links to an external site.)](http://www.stevens.edu/sites/stevens_edu/files/styles/home_feature_persona_80x80/public/Elizabeth-Pascetta.jpg?itok=_ut8qP45)"

<section  data-background-options='{"source":{"0px": "http://www.stevens.edu/sites/stevens_edu/files/styles/hompage_statistics_500x400/public/15-013_Stevens_0238_8.jpg?itok=vFz_2dzY"

For this assignment, you may assume that a URL begins with double quote followed by "http"  and ends with a double quote. This won't catch unusual cases like

meta name="generator" content="Drupal 7 (http://drupal.org)" />

but don't worry about that case.  (Don't forget that HTTP and http are equivalent).

You may also assume that the arguments to the URL should be included in the URL when counting distinct values.  E.g.  

"[http://www.google.com/mapss (Links to an external site.)](http://www.stevens.edu/mystevens)?login=jrr"  and "[http://www.google.com/maps (Links to an external site.)](http://www.stevens.edu/mystevens)?login=rcohen2"  should be counted as two distinct URLs.   You do NOT need to strip the arguments from the end of the URL when detecting duplicates

The purpose of this assignment is for you to understand how to interact with web sites from Python and to get more experience with regular expressions.  I don't expect you to you write the ultimate regular expression for detecting valid URLs.

How many distinct http/https references do you find on [www.google.com? (Links to an external site.)](http://www.stevens.edu/)  How about www.mtv.com?  (Beware, website change frequently so don't be surprised if your answer changes over time.)

HINTS:

-   There are a number of Python packages for parsing web pages but for this assignment, please use the urllib and regular expression packages to implement your solution.
-   The request module in urllib is of great value here.
-   You may need to specify 'http://www.google.com' rather than 'www.google.com' in your urllib.request() call.
-   Some websites require Secure Socket Layer certificates.  If you encounter one of these (such as [www.stevens.edu (Links to an external site.)](http://www.stevens.edu/)), try a different website.
