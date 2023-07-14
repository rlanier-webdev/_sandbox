# Reverse Polish Notation
'''
     - single space bewteen each operand and operators
'''

def function(string):
     array = string.split()
     #print(array)

     operators = ["+","-"]
     new_list = []

     for x in array:
          if x in operators:
               new_list.append(x)

     print(new_list)

function('8 1 3 - +')