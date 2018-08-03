# docket_alarm_test
Test of employment for Docket Alarm

Test Questions
1. Basic Programming Test:

a. List the libraries or framework you have used creating a python web crawler. In 200 words or
less, describe the working flow.

Libraries/Frameworks: requests, urllib, BeautifulSoup, Parsel, Scrapy, Selenium, lxml, MechanicalSoup, mechanize, aiohttp, html5lib, MarkupSafe, xhtml2pdf, Bleach, sanitize, fake-useragent, cssutils.

I will investigate the target source of the scraping first. For instance, if the target we need to scrape is a website I will analyze the website structure and try to understand how it is organized. Then I will look for possible scraping traps and hurdles, namely anti-scraping mechanisms and IP restrictions. The info that we want to gather is the main asset, so I need to be sure that is accessible to us, first of all. Then I will put together a small scraping prototype to test my assumptions and later on start building the main scraper itself.

b. Explain difference between python list and tuple.

While a list is mutable, a tuple is immutable. Tuples are heterogeneous data structures, while lists are homogeneous sequences. Tuples have structure, lists have order.

c. Write a program that prints numbers from 1 to 1000 on each line. But for numbers that are
multiples of 7 print "Docket" instead of the number. For multiples of 6 print "Alarm" instead
of the number. For numbers that are multiples of both 6 and 7 print "Docket Alarm".
d. Explain what a Python generator is. Modify the answer to part “c” to utilize a generator.

2. Basic Internet Programming: Write a program that prints the IP address of the computer that it
is being run on. If the computer is not connected to the internet, it should print "not connected"

3. Single Scraper (one Virginia case)

a. Write a scraper which can download and parse the page here
b. The program should output the Appellant name, Appellee name, CAV record number, and
date received. The format should be in JSON and saved to a filename q3.json. The exact
format of the JSON file is not important.

4. Batch Scraper (multiple Virginia cases)

a. Build on top of the previous answer to create a program that downloads 50 cases
sequentially. Note the form of the URL, to scan through caseids 23800 to 23850.
b. Output the result into a JSON format into a file named q4.json. The JSON format should be a
list, where each list item is in the same form of the JSON object you created in question 3.

5. Form Submission (Maryland)

a. Create a program that downloads the page located here and saves it to the file q5-1.html.
b. Then have the program click the checkbox, and select continue, download the resulting case
search page and save it into a file named q5-2.html

6. Advanced Scraper

a. You should have received the HTML files q6-1.html, q6-2.html, and q6-3.html
b. Open each HTML file in a web browser. After scrolling down, you should see an “Actions”
table, with headings “Viewed” and “Date”, among several others.
c. Create a program that opens each file and creates a corresponding file called q6-1.json, q6-
2.json, and q6-3.json, respectively.
d. Each JSON file should be a list of dictionaries, where each entry corresponds to the values in
the table. So for example, the first entry in q6-1.html should be:
 [{
"Viewed" : "",
"Date": "11/05/2004",
"Action Text": "EXHIBITS DESTROYED",
"Disposition": "Not Applicable",
"Image: "",
 }, ...]
If there are HTML links in any of the tables, add the link to the structure in a way that makes
sense to you.
