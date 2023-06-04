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
     download and extract tables within PDF files

     tabula.read_pdf() - returns a list of pandas DataFrames (each DataFrame corresponds to a table), passing url directly automatically downloads pdf file
     
     pages="all" - extract tables in all the PDF pages 
     """
     #tables = tabula.read_pdf(url, pages="all")
     #print(tables)
     
     """
     # convert all tables of a PDF file into a single CSV file
     # supported output_formats are "csv", "json" or "tsv"
     """
     tabula.convert_into(url, "output.csv", output_format="csv", pages="all")

def clean_file():
     '''
     file output.csv
          1. strip information from top of file lines 1-16
          2. clean up table header, line 17
               a. if delimeter is not a comma, then covert to comma
          3. clean up data
               - formatting issues
                    incorrect format:
                    63103 City Parc at Pine	1531 Pine St St. Lois MO (314) 309-2264 Tax Credit 55+	Stdio 2 BR
                    
                    correct format:
                    63104,Clinton Peabody,1401 LaSalle,St. Louis,MO,(314) 231-7595,Subsidized,18+,"1,2,3,4,5 BR"
     ''' 
     output_file = 'output.csv'
     # initializing temp list and list for column names
     temp = []
     column_names = []
     
     with open(output_file, 'r') as csv_file:
          # Skip the heading
          for _ in range(0,16):
               next(csv_file)
          
          reader = csv.reader(csv_file, delimiter=',')
          
          for row in reader:
               temp.append(row)
               for field in temp:
                    item = field[1].split() # get the second

                    for x in item:
                         column_names.insert(-1,x)
                    
                    column_names.append(field[-1]) 
                    column_names.insert(0,field[0])
               break # break after the first iteration because you only want the header row
               #rows.append(row)
          #print(column_names)
          print('Column Names:', column_names)
     #print("List of column names : ", column_names[0])

     #print(rows[0:14])
     #delete_headers(output_file)

# skiprows with pandas
def delete_headers(output_file):
     df = pd.read_csv(output_file)
     print(df)

clean_file()