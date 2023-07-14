# Reverse Polish Notation

# https://www.youtube.com/watch?v=qN8LPIcY6K4&ab_channel=BackToBackSWE
# https://www.geeksforgeeks.org/stack-data-structure/
# https://www.geeksforgeeks.org/stack-in-python/

'''
     - single space bewteen each operand and operators
     - should split the operands into new list instead of operators

     Read from left to right
     When requirements are fulfilled, execute operation

          for example: 3 4 + 2 * = 14
          3 4 +
          7 2 *
          14

     Notes:
     - Only the last 2 numbers matter when we execute an operation
          -- last in first out
     - this is a stack problem
          example: 3 4 + 2 * 1 +

          Steps
               push operands
               when we see operation
               pop 2 items
               evaluate
               push back onto stack
               ///
               If the operand is a digit, the function pushes the value of the digit onto the stack. 
               If the token is an operator, the function pops the top two items off the stack, evaluates the expression, and pushes the result back onto the stack.

          Errors
          Traceback (most recent call last):
          File "c:\Users\rlani\_dev\_sandbox\rpn\main.py", line 59, in <module>
          evaluate_expression(expression)
          File "c:\Users\rlani\_dev\_sandbox\rpn\main.py", line 52, in evaluate_expression
          op1 = stack.pop()
                    ^^^^^^^^^^^
          IndexError: pop from empty list
'''

def evaluate_expression(expression):
     array = expression.split()
     #print(array)
     
     stack = [] # this is your stack
     #operators = ['+','-','*','/']
     # loop through the list and push operands to stack
     
     # If the token is an operator, the function pops the top two items off the stack, evaluates the expression, and pushes the result back onto the stack.
     for item in array:
          # If the operand is a digit, push the operand onto the stack. 
          if item.isnumeric():
               stack.append(item)
               print(item)
          else:
               op2 = stack.pop()
               op1 = stack.pop()
               #result = op1, item, op2
               
               print(op1)    
     #print(operands)

expression = '8 2 3 - +'
evaluate_expression(expression)

