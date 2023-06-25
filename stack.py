class Stack:
  def __init__():
    self.stack = []
    
  def push(self,element):
    self.stack.append(element)
    
  def pop(self):
    if not self.isEmpty():
      self.stack.pop()
    else:
      print("Underflow")
      
  def peek(self):
    if not self.isEmpty():
      return self.stack[-1]
    else:
      print("Stack is Empty")
      
  def isEmpty(self):
    return len(self.stack) == 0
