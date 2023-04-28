'''
Author: RaShunda Williams
Project: Birthday Checker
Description: A simple project that checks the user input against what's in the birthday db.
    -- If the name is there, then print the birthday.
    -- If the name is not there, then ask the user for the birthday to be added.
        - save the new record to the data.json file
IDEAS:
    1. add error handling - DONE 4/27
        - problem: if file doesn't exist, then it throws an error
        - solution: create new file
            -- new problem: error thrown because file is empty
                'raise JSONDecodeError("Expecting value", s, err.value) from None
                json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)'
    2. add birthday validation - check to see if the input is a valid date
    3. print the zodiac sign for the name user inputs
    4. print the horoscope of the day
'''

import json, time

filename = "data.json"

while True:
    try:
        with open(filename,"r") as file:
            content = file.read()
            birthdays = json.loads(content)
            
        #save birthdays to json file
        def saveBirthday(birthdays):
            with open(filename, "w") as file:
                json.dump(birthdays, file)

        while True:
            print('Enter a name: (blank to quit)')
            name = input()
            
            if name == '':
                break 

            if name in birthdays:
                print(birthdays[name] + ' is the birthday of ' + name)
            else:
                print('I do not have birthday information for ' + name)
                
                bday = input('When is their birthday? ')
                birthdays[name] = bday

                saveBirthday(birthdays)

                print('Birthday database updated.')

    except FileNotFoundError:
        # If the file doesn't exist, create a new one
        print('File does not exist. Creating file...')
        open(filename, 'w')
        print(f'{filename} - File created.')
    
    time.sleep(2)  # wait for 1 second before checking again