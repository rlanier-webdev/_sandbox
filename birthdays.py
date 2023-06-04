import json

file = "data.json"

jsonFile = open(file,"r")
jsonContent = jsonFile.read()
birthdays = json.loads(jsonContent)
    
#save birthdays to json file
def saveBirthday(birthdays):
    jsonString = json.dumps(birthdays)
    jsonFile = open(file, "w")
    jsonFile.write(jsonString)
    jsonFile.close

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('When is their birthday?')
        
        bday = input()
        birthdays[name] = bday

        saveBirthday(birthdays)

        print('Birthday database updated.')

