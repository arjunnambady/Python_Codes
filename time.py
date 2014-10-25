''' Program to parse HTML data'''
''' Retrives current time in India from the webpage '''
''' Just for studying HTML parsing using the modules,
    not a good nethod to get time '''
    
# Import the required modules
# The urllib and BeautifulSoup are used for  HTML parsing 

import urllib2
from bs4 import BeautifulSoup

# The url that need to be fetched

url = 'http://www.worldtimeserver.com/current_time_in_IN.aspx/'

# The url is opened and the response is stored to a variable
# Print the info to get details about the page

response = urllib2.urlopen(url)
info = response.info()

# Read the data and close the link

big_data = response.read()
response.close()

# Make a BeautifulSoup instance

process_data = BeautifulSoup(big_data)

# Strip out the time and date from the HTML data

time =  process_data.find(class_ = 'font7')

time =str(data)
print data[37:45]

date = process_data.find(class_ = 'font6')

date = str(date)
print date[47:63]

