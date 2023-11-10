# POSTFIX EVALUATION
# 
# Sample Output 1:
# Postfix : 100 200 + 2 / 5 * 7 +
# Result : 757
# 
# Sample Output 2:
# Postfix: 2 3 1 * + 9 -
# Result : -4
# 
# Author: Edilbert Crist P. Jaguimit
operators = ['+', '-', '*', '/', '^']
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

  # EVALUATE THE POSTFIX EXPRESSION
  def eval(self, postf):
  
    for post in postf:
      if post in operators:
        val1 = llstack.pop()
        val2 = llstack.pop()
        result = 0
        if post == '-':
          result = int(val2) - int(val1)
        elif post == '*':
          result = int(val2) * int(val1)
        elif post == '^':
          result = int(val2) ** int(val1)
        elif post == '/':
          result = float(int(val2) / int(val1))
        elif post == '+':
          result = int(val2) + int(val1)
        llstack.push(result)
      elif post.isdigit():
        llstack.push(post)
      else:
        print("Invalid Operator")

  # DISPLAY THE RESULT
  def traverse(self):
    if self.head is None:
      pass
    else:
      temp = self.head
      list = ''
      while temp:
        list += ' ' + str(temp.data)
        temp = temp.next
      print("Result :", list)


# COMMAND AREA
while True:
  llstack = LinkedStack()
  # This try and except will prevent the error when you accidentally clicked the enter key if the user input is empty.
  try:
    postfix = list(input("Postfix : ").split())
    ctrOperator = 0
    ctrOperand = 0
    for i in postfix:
      if i in operators:
        ctrOperator += 1
      if i.isdigit():
        ctrOperand += 1
    if postfix[0] == 'x' or postfix[0] == 'X':
      break
    else:
      if ctrOperand != ctrOperator:
        if (postfix[0].isdigit() and postfix[1].isdigit()):
          if postfix[-1].isdigit() or (postfix[0] != '(' and postfix[-1] != ')'):
            llstack.eval(postfix)
        else:
          print("Invalid Declaration.")
      else:
          print("Invalid Declaration.")
      llstack.traverse()
    print()
  except:
    pass
