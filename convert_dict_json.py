import json

# create a Variable of Python dictionary
data = {
    'name': 'Tom Cruise', 
    'age': 60, 
    'city': 'New York'
    }

# convert dict to JSON
json_data = json.dumps(data, indent=5)

# print the Converted JSON object
print(json_data)