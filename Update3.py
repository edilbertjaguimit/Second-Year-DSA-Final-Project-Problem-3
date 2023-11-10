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
  def convertInfixToPostfix(self, infix):
    preOperator = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    result = ''
    ctr = 0
    i = 0
    while i < len(infix):
      j = 0
      while j < len(operators):
        if infix[i] != operators[j]:
          if infix[i].isdigit() or infix[i].isalpha():
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
    # DISPLAY THE POSTFIX EVALUATION RESULT
    if ctr != 0:
      while not self.empty():
        result += str(self.pop()) + ' '
      print("Postfix :", result)
      self.prefix(result)
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
    print("\n")
    
  # EVALUATE OF THE EXPRESSION
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
            result = int(val2) - int(val1)
          elif eval[i] == '*':
            result = int(val2) * int(val1)
          elif eval[i] == '^':
            result = int(val2)**int(val1)
          elif eval[i] == '/':
            result = float(int(val2) / int(val1))
          elif eval[i] == '+':
            result = int(val2) + int(val1)
          self.push(result)
        elif eval[i].isdigit():
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
          # llstack.postfixResult()
        else:
          print("Invalid Declaration.")
      else:
        print("Invalid Declaration.")
    print()
      
  except:
    pass
