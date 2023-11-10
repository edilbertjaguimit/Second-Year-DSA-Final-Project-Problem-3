# Input an infix expression. Convert the expression into prefix and postfix. Also, evaluate the given
# expression. Display the equivalent prefix, postfix, and also the result after the evaluation. Repeat
# the operation as often as possible. Be able to check the validity of the input.

# SAMPLE

# INPUT 
#   Infix : a + b * ( c ^ d - e ) ^ ( f + g * h ) - i
# OUTPUT
#   Result in Prefix :
#   Result in Postfix : 
#   Evaluated : 

#========================================================================#

# INFIX TO POSTFIX CONVERSION

# Sample Output 1:
# Infix : a + b * ( c ^ d - e ) ^ ( f + g * h ) - i
# Result in Postfix : a b c d ^ e - f g h * + ^ * + i -
# 
# Sample Output 2:
# Infix: m * n + ( p - q ) + r
# Result in Postfix : m n * p q - + r +
# 
# Author: Edilbert Crist P. Jaguimit

operators = ['+', '-', '*', '/', '^', '(', ')']

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedStack:
  def __init__(self):
    self.head = None

  # ADD AT FIRST
  def push(self, operand):
    if self.head is None:
      self.head = Node(operand)
    else:
      newNode = Node(operand)
      newNode.next = self.head
      self.head = newNode

  # REMOVE AT FIRST
  def pop(self):
    if self.head is None:
      print("List is Empty or cannot Fulfill the Operation.")
    else:
      current = self.head.data
      self.head = self.head.next
      return current
      
  # INFIX TO POSTFIX CONVERSION
  def convertInfixToPostfix(self, infixed):
    preOperator = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '^' : 3}
    result = ''
    ctr = 0
    for inf in infixed:
      if inf not in operators:
        if inf.isdigit() or inf.isalpha():
          result += inf + ' '
      else:
        if inf == '(':
          self.push(inf)
        elif inf == ')':
          while not self.empty() and self.peek() != '(':
            result += str(llstack.pop()) + ' '
          self.pop() 
        else:
          ctr += 1
          while not self.empty() and self.peek() != '(' and preOperator[inf] <= preOperator[self.peek()]:
            result += str(self.pop()) + ' '
          self.push(inf)
    # DISPLAY THE RESULT
    if ctr != 0 :
      print("Result in Postfix :", end=' ')    
      while not self.empty():
        result += str(self.pop()) + ' '
      print(result, end='')
      print()
    else:
      print("Invalid Operator")

      
  # Return the element on Top
  def peek(self):
    return self.head.data

  # Return an Empty Stack
  def empty(self):
    return self.head == None
  

# COMMAND AREA
while True:
  llstack = LinkedStack()
  # This try and except will prevent the error when you accidentally clicked the enter key if the user input is empty.
  try:
    infix = list(input("Infix : ").split())
    ctrOperator = 0
    ctrOperand = 0
    for i in infix:
      if i in operators:
        ctrOperator += 1
      if i.isdigit() or i.isalpha():
        ctrOperand += 1
    if infix[0] == 'x' or infix[0] == 'X':
      break
    else:
      if ctrOperand != ctrOperator:
        if (infix[0].isdigit() or infix[0].isalpha()) and (infix[-1].isdigit() or infix[-1].isalpha()) or (infix[0] == '(' and infix[-1] == ')'):
          llstack.convertInfixToPostfix(infix)
        else:
          print("Invalid Declaration.")
      else:
        print("Invalid Declaration.")
      print()
  except:
    pass
