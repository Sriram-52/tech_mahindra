class Stack:
  def __init__(self, size):
    self.stk = []
    self.size = size
  
  def push(self, data):
    if len(self.stk) == self.size:
      print("Stack Overflow!!!")
    else:
      self.stk.append(data)
  
  def pop(self):
    if len(self.stk) == 0:
      print("Stack underflow!!!")
    else:
      self.stk.pop()
  
  def peek(self):
    if len(self.stk) == 0:
      return -1
    else:
      return self.stk[len(self.stk) - 1]
  
  def display(self):
    if len(self.stk) == 0:
      print('Stack is empty')
    else:
      print('->'.join(list(map(str, reversed(self.stk)))))

if __name__ == "__main__":
  max_size = int(input('Enter max size of the stack: '))
  stk = Stack(max_size)
  while True:
    print('Enter your choice:')
    print('1. Push')
    print('2. Pop')
    print('3. Peek')
    print('4. Display')
    print('5. Exit')
    ch = int(input('Enter your choice: '))
    if ch == 1:
      ele = int(input('Enter element to push: '))
      stk.push(ele)
    elif ch == 2:
      stk.pop()
    elif ch == 3:
      print('Peek of the stack is', stk.peek())
    elif ch == 4:
      stk.display()
    elif ch == 5:
      break
    else:
      print('You entered wrong choice!!!')
