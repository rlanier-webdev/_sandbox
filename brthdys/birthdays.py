"""
AUTHOR: RaShunda Williams
PROJECT: Birthday Checker
DESCRIPTION: A simple project that checks the user input against what's in the file.
            -- If the name is there, then print the birthday.
            -- If the name is not there, then ask the user for the birthday to be added.
                - save the new record to the data.json file

        TO DO:
            - add error handling
                - fixed 042823: if file doesn't exist, then it throws an error
            - change bday to date format
            - validate user input
                - name should only include letters
                - bday should be in date format, valid date
            - print the zodiac sign for the name user inputs
            - print the horoscope of the day
        QUESTIONS:
            - how should duplicates be handled?
            -- if name matches mutliple records...
"""

import json

#from json.decoder import JSONDecodeError

# Initialize filename variable
filename = "data.json"

while True: # keep prompting the user until they quit
    try:
        # Load the initial records from file
        with open(filename,"r") as file:
            records = json.load(file)
    except FileNotFoundError:
        # Create empty list of records if file doesn't exist
        records = []
    
    # Get user input for name
    name = input("Enter a name: (blank to quit)")

    # name is blank, quit
    if name == "":
        break

    # Check if the name exists in the record
    for record in records:
        if record["name"] == name:
            print(f"{name}'s Birthday is: ", record["bday"])
            break
    else:
        # If the name does not exist in the record, get user input for birthday
        bday = input("Enter their birthday: ")

        # generate the record id
        new_id = len(records) + 1

        # create the new record
        new_record = {"id": new_id, "name": name, "bday": bday}

        # add the record
        records.append(new_record)
        
        # write to file
        with open(filename, "w") as file:
            json.dump(records,file,indent = 4)

        # Print the updated record list
        print("New record added.")

# except JSONDecodeError:  # includes json.decoder.JSONDecodeError
#     print("Decoding JSON has failed")
