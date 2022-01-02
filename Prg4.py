class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Queue:
	def __init__(self):
		self.head = None
	
	def insert(self, data):
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
		else:
			last = self.head
			while last.next:
				last = last.next

			last.next = new_node
		print('String', data, 'inserted successfully')
	
	def delete(self):
		if self.head is None:
			print("Queue is empty!!!")
			return
		
		head = self.head
		self.head = head.next
		
		print('String', head.data, 'deleted from the queue')
		head = None
	
	def display(self):
		last = self.head
		if last is None:
			print('Queue is empty!!!')
		else:
			while last:
				print(last.data, end=' ')
				last = last.next
			print()
	

if __name__ == "__main__":
	queue = Queue()
	while True:
		print('Enter your choice:')
		print('1. Insert')
		print('2. Delete')
		print('3. Display')
		print('4. Exit')
		ch = int(input('Enter your choice: '))
		if ch == 1:
			ele = input('Enter element to push: ')
			queue.insert(ele)
		elif ch == 2:
			queue.delete()
		elif ch == 3:
			queue.display()
		elif ch == 4:
			break
		else:
			print('You entered wrong choice!!!')