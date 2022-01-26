#task1
#parsing web content using beautifulsoup

import requests
from bs4 import BeautifulSoup
import csv

#enter a link to retrieve web content from   
URL = input("Enter the link to retrieve and parse web content from\n")
try: 
    r = requests.get(URL)
except: #if link is not valid, notify the user through exception handling
    print("Link is not valid")
    
else: #if there is no exception, parse the web content for user 
    soup = BeautifulSoup(r.content, 'html5lib')
    tag=input("Enter a tag to parse by, for example 'a', 'img', 'p'\n")
    print(soup.find(tag))
    
#if there are multiple elements with the same tag, it will output the element which occurs first 
