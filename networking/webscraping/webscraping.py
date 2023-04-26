# Web Scraping
## def - When a program or script pretends to be a browser and retrives web pages, looks at those web pages, extracts information, and then looks at more web pages   
### Python requests.Response Object - https://www.w3schools.com/python/ref_requests_response.asp

#### Project - Write a Python program to test if a given page is found or not on the server.
'''
     1. First, import the necessary modules required for HTTP requests. For example, you can use the "requests" module in Python to send HTTP requests.
     2. Next, define the URL of the page you want to test. You can either hardcode the URL or ask the user to input it.
     3. Use the "requests" module to send a GET request to the URL.
     4. Check the response status code returned by the server. If the status code is 200, then the page is found. Otherwise, it is not found.
     5. Print an appropriate message based on the result. For example, if the page is found, you can print "Page found on the server", and if it is not found, you can print "Page not found on the server".
     Note: You may also want to consider error handling, such as checking if the URL is valid or if there is a network error.
'''

#1. First, import the necessary modules required for HTTP requests.
import requests 

try:
     #2. Next, define the URL of the page you want to test.
     url = 'http://google.com'
     #3. Use the "requests" module to send a GET request to the URL.
     response = requests.get(url, timeout=0.001)
     code = response.status_code
     #4. Check the response status code returned by the server. If the status code is 200, then the page is found. Otherwise, it is not found.
     if code == 200:
          print(f'{code} - page found')
     else:
          print(f'{code} - page not found')
except requests.exceptions.RequestException as e:
     print('An error occured:', e)

#print(response.apparent_encoding) #Returns the apparent encoding (utf-8-this example)
#print(response.content) #Returns the content of the response, in bytes
#print(response.reason)


