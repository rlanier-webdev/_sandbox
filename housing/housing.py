#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : rashunda lanier williams
# Created Date: 6/2/23
# version ='1.0'
# ---------------------------------------------------------------------------
""" 
     manually installed dependencies:

     extract the data from the housing list - https://hopeforseniors.files.wordpress.com/2023/05/housing-list-5-12-23.pdf

"""
# ---------------------------------------------------------------------------
# Imports
import requests
import tabula
import csv
import pandas as pd
# ---------------------------------------------------------------------------

# list location
url = "https://hopeforseniors.files.wordpress.com/2023/05/housing-list-5-12-23.pdf"

# download file and save locally
def get_file():
     # requests
     r = requests.get(url, stream=True)

     # --------------------------------------
     print(r.status_code) # status code
     print(r.headers['content-type']) # get content type from header
     print(r.encoding) # encoding
     # --------------------------------------

     file_name = url.split('/')[-1] 

     with open(file_name, 'wb') as pdf:
          for chunk in r.iter_content(chunk_size=1024):
          # writing one chunk at a time to pdf file
               if chunk:
                    pdf.write(chunk)

     print( "%s downloaded!\n"%file_name )

def download_file():
     """   
     download and extract tables within PDF files using tabula
          - supported output_formats are "csv", "json" or "tsv"

     tabula.convert_into() -  convert tables within a PDF document into other formats such as CSV, Excel, or HTML
          - pages="all" - extract tables in all the PDF pages 
     """

     # convert all tables of a PDF file into a single CSV file
     tabula.convert_into(url, "output.csv", output_format="csv", pages="all")

def clean_file():
     '''
     file output.csv
          1. strip information from top of file lines 1-16
          2. clean up table header, line 17
          3. clean up data
               - formatting issues
                    incorrect format:
                    63103 City Parc at Pine	1531 Pine St St. Lois MO (314) 309-2264 Tax Credit 55+	Stdio 2 BR
                         - lines 18-21
                         - lines 23-35

                    
                    correct format:
                    63104,Clinton Peabody,1401 LaSalle,St. Louis,MO,(314) 231-7595,Subsidized,18+,"1,2,3,4,5 BR"


     ''' 
     output_file = 'output.csv'
     new_file = 'new_file.csv'
     
     # initializing temp list and list for column names
     temp = []
     column_names = []

     # read downloaded file
     with open(output_file, 'r') as csv_file:
          reader = csv.reader(csv_file, delimiter=',')

          # Skip the heading
          for _ in range(16):
               next(reader)

          # first row once heading is removed
          temp = next(reader)
          
          # create a new list with first and last, split the second element
          column_names = [temp[0]] + temp[1].split() + [temp[-1]] 
          print(column_names)

     # write to new file
     with open(new_file,'w') as f:
          write = csv.writer(f)
          write.writerow(column_names)

clean_file()