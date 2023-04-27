"""
Project Title: Web Scraping Top Headlines from a News Website

Project Description: In this project, you will learn how to scrape the top headlines from a news website using Python. You will use the Beautiful Soup library to extract the headlines from the HTML source code of the news website. You will then store the headlines in a CSV file.

Project Steps:

1. Import the required libraries:
     - requests (to send HTTP requests to the website)
     - BeautifulSoup (to parse the HTML source code)
2. Send an HTTP request to the news website using the requests library.
     - Make sure to check the response code to ensure that the request was successful.
3. Parse the HTML source code using the BeautifulSoup library.
     - Use the html.parser parser to parse the HTML source code. 
4. Identify the HTML tags and attributes that contain the headlines.
     - Inspect the HTML source code of the news website to identify the tags and attributes that contain the headlines.
5. Use the find_all() method of the BeautifulSoup object to extract the headlines.
     - Pass the tag and attribute information as parameters to the find_all() method.
6. Store the headlines in a CSV file.
     - Use the csv module to create and write the headlines to a CSV file.
7. Test the script by running it and verifying that the headlines are correctly extracted and stored in the CSV file. """

import requests
from bs4 import BeautifulSoup 


try:

     url = 'http://techcrunch.com'

     response = requests.get(url, timeout=0.10)
     code = response.status_code

     if code == 200:
          print(f'{code} - page found')

          data = BeautifulSoup(response.text, 'html.parser')
          # for link in data.find_all('a'):
          #      print(link.get('href'))
          for headline in data.select('article.post-block:nth-child(3) > header:nth-child(1) > h2:nth-child(2)'):
               print(headline)
               
     else:
          print(f'{code} - page not found')

except requests.exceptions.RequestException as e:
     print('An error occured:', e)