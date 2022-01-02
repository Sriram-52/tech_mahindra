class CustomArray:
  def __init__(self):
    self.a = []
  
  def add_element(self, ele, index):
    self.a.insert(index, ele)
  
  def delete_element(self, ele):
    if len(self.a) == 0:
      print("Your custom array is empty")
    elif ele in self.a:
      self.a.remove(ele)
      print(ele, ' is removed from your custom array')
    else:
      print(ele, ' not element found in your custom array to delete!!!')
  
  def display_array(self):
    if len(self.a) == 0:
      print("Your custom array is empty")
    else:
      print(*self.a)

if __name__ == "__main__":
  custom_array = CustomArray()
  while True:
    print('Enter your choice:')
    print('1. Add element')
    print('2. Delete element')
    print('3. Display')
    print('4. Exit')
    ch = int(input('Enter your choice: '))
    if ch == 1:
      ele, index = list(map(int, input('Enter element and index: ').split()))[:2]
      custom_array.add_element(ele, index)
    elif ch == 2:
      ele = int(input('Enter element to delete: '))
      custom_array.delete_element(ele)
    elif ch == 3:
      custom_array.display_array()
    elif ch == 4:
      break
    else:
      print('You entered wrong choice!!!')
