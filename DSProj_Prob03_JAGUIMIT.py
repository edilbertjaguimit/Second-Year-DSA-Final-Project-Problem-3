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
    if self.head == None:
      self.head = Node(operand)
    else:
      newNode = Node(operand)
      newNode.next = self.head
      self.head = newNode

  # REMOVE AT FIRST
  def pop(self):
    if self.head == None:
      print("List is Empty or cannot Fulfill the Operation.")
    else:
      current = self.head.data
      self.head = self.head.next
      return current

  # INFIX TO POSTFIX CONVERSION
  def convertInfixToPostfix(self, infix):
    preOperator = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    result = ''
    ctr = 0
    i = 0
    while i < len(infix):
      j = 0
      while j < len(operators):
        if infix[i] != operators[j]:
          if 'a' <= infix[i] <= 'z' or 'A' <= infix[i] <= 'Z' or '0' <= infix[i] <= '9':
            result += infix[i] + ' '
            break
        else:
          if infix[i] == '(':
            self.push(infix[i])
          elif infix[i] == ')':
            while not self.empty() and self.peek() != '(':
              result += str(self.pop()) + ' '
            self.pop()
          else:
            ctr += 1
            while not self.empty() and self.peek() != '(' and preOperator[infix[i]] <= preOperator[self.peek()]:
              result += str(self.pop()) + ' '
            self.push(infix[i])
        j += 1
      i += 1    
    # DISPLAY THE EXPRESSION AND EVALUATION RESULT
    if ctr != 0:
      while not self.empty():
        result += str(self.pop()) + ' '
      self.prefix(result)
      print("Postfix :", result)
      self.evaluation(result)
      print()
    else:
      print("Invalid Operator")

  def prefix(self, pref):
    pre = pref.split()
    index = len(pre)-1
    print("Prefix :", end=' ')
    while index >= 0:
      print(pre[index], end=' ')
      index -= 1
    print()
    
  # EVALUATION OF THE EXPRESSION
  def evaluation(self, evaluate):
    eval = evaluate.split()
    flag = True
    i = 0
    while i < len(eval):
      j = 0
      while j < len(operators):
        if eval[i] == operators[j]:
          val1 = self.pop()
          val2 = self.pop()
          result = 0
          if eval[i] == '-':
            result = float(val2) - float(val1)
          elif eval[i] == '*':
            result = float(val2) * float(val1)
          elif eval[i] == '^':
            result = float(val2)**float(val1)
          elif eval[i] == '/':
            result = float(val2) / float(val1)
          elif eval[i] == '+':
            result = float(val2) + float(val1)
          self.push(result)
        elif '0' <= eval[i] <= '9':
          self.push(eval[i])
          break
        else:
          flag = False
        j += 1
      i += 1
      
    if flag:
      print("Invalid Operator")
    else:
      temp = self.head
      print("Evaluation :", end=' ')
      while temp:
        print(temp.data)
        temp = temp.next
      
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
    i = 0
    while i < len(infix):
      j = 0
      while j < len(operators):
        if infix[i] == operators[j]:
          ctrOperator += 1
          break
        if 'a' <= infix[i] <= 'z' or 'A' <= infix[i] <= 'Z' or '0' <= infix[i] <= '9':
          ctrOperand += 1
          break
        j += 1
      i += 1
        
    if infix[0] == 'x' or infix[0] == 'X':
      print("Program Terminated.")
      break
    else:
      if ctrOperand != ctrOperator:
        if ('a' <= infix[0] <= 'z' or 'A' <= infix[0] <= 'Z' or '0' <= infix[0] <= '9') and ('a' <= infix[-1] <= 'z' or 'A' <= infix[-1] <= 'Z' or '0' <= infix[-1] <= '9') or (infix[0] == '(' or infix[-1] == ')'):
          llstack.convertInfixToPostfix(infix)
        else:
          print("Invalid.")
      else:
        print("Invalid Declaration.")
    print()
      
  except:
    pass
