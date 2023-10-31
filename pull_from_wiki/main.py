import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

def clean_data(text):
     # Remove text within square brackets
     text = re.sub(r'\[.*\]', '', text)

     # Remove any double quotes and commas from the text
     text = text.replace('"', '').replace(',', '')

     return text


def expand_first_row(original_data, num_rows_to_insert):
     # Generate the new rows with modifications
     new_rows = []
     for i in range(1, num_rows_to_insert + 1):
          year = 1889 + i - 1
          new_row = [str(i), str(year), 'W', 'L']  # Adjusted column indices
          new_rows.append(new_row)

     # Insert the new rows at the beginning of the data
     original_data[0:0] = new_rows


def scrape_and_process_table_data(url, table_index_to_scrape):
     # Send an HTTP GET request to the URL
     response = requests.get(url)

     if response.status_code == 200:
          # Parse the HTML content of the page
          soup = BeautifulSoup(response.text, 'html.parser')

          # Find all tables on the page
          all_tables = soup.find_all('table')

          if table_index_to_scrape < len(all_tables):
               table_to_scrape = all_tables[table_index_to_scrape]

               if table_to_scrape:
                    data = []  # Create a list to store table data
                    header_processed = False

                    # Extract table data (<td> elements)
                    for row in table_to_scrape.find_all("tr"):
                         cells = row.find_all(["td", "th"])
                         row_data = [cell.get_text().strip() for cell in cells]

                         # Check if there are at least 5 columns in the row (header has 5 columns)
                         if len(row_data) >= 5:
                              if not header_processed:
                                   data.append(row_data)  # Add the header as-is
                                   header_processed = True
                              else:
                                   data.append([row_data[i] for i in [0, 1, 3, 5, 6]])  # Select the desired columns
                         else:
                              print(f"Skipping row with insufficient columns: {row_data}")

                    # Replace the existing data with the expanded data
                    expand_first_row(data, 12)

                    # Create a Pandas DataFrame from the extracted data
                    df = pd.DataFrame(data)

                    # Export the DataFrame to a CSV file
                    df.to_csv("wiki_table_data.csv", index=False)

                    print("Data exported to 'wiki_table_data.csv")
               else:
                    print("Table not found on the page.")
          else:
               print("Table index specified is out of range.")
     else:
          print("Failed to retrieve the web page. Status code:", response.status_code)


# Example usage:
url = "https://en.wikipedia.org/wiki/Baltimore_City_College_football"  # Replace with your target URL
table_index = 5  # Replace with the index of the table you want to scrape
scrape_and_process_table_data(url, table_index)
