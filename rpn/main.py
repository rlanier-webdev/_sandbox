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
               If an operator, the function pops the top two items off the stack, evaluates the expression, and pushes the result back onto the stack.
'''

def evaluate_expression(expression):
     arr = expression.split()

     stack = [] # this is your stack
     
     # loop through the list and push operands to stack
     for item in arr:
          # If the operand is a digit, push the operand onto the stack. 
          if item.isnumeric():
               stack.append(int(item))
          else:
               #If an operator, the function pops the top two items off the stack, evaluates the expression, and pushes the result back onto the stack.
               op2 = stack.pop()
               op1 = stack.pop()

               if item == '+':
                    stack.append(op1 + op2)
               elif item == '-':
                    stack.append(op1 - op2)
               elif item == '*':
                    stack.append(op1 * op2)
               elif item == '/':
                    stack.append(op1 / op2)

     return stack.pop()

expression = '8 2 3 - +'
print(evaluate_expression(expression))
