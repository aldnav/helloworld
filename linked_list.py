#~ Singly linked list implementation
class SLinkedList(object):
	
	class Node(object):
		def __init__(self, element):
			self.element = element
			self.next = None
		
		def __str__(self):
			return str(self.element)		
	
	def __init__(self, element = None):
		if element is None:
			self.head = None
			self.tail = None
			self.size = 0
		else:
			self.head = SLinkedList.Node(element)
			self.tail = self.head
			self.size = 1
	
	def __iter__(self):
		pointer = self.head
		while pointer:
			yield pointer.element
			pointer = pointer.next
	
	def __str__(self):
		if self.size == 0:
			return '[]'
		strBldr = ''
		for i in self:
			strBldr += '[' + i + ']->'
		strBldr += 'NULL'
		return strBldr
	
	''' Adds an element at the beginning of list'''
	def addFirst(self, element):
		element = SLinkedList.Node(element)
		element.next = self.head
		self.head = element
		self.size += 1
	
	''' Adds an element at the end of the list'''
	def addLast(self, element):
		element = SLinkedList.Node(element)
		element.next = None
		self.tail.next = element
		self.tail = element
		self.size += 1
	
	''' Removes an element at the beginning of list '''
	def removeFirst(self):
		try:
			temp = self.head
			self.head = self.head.next
			temp.next = None
			self.size -= 1
			return temp
		except:
			print 'RemoveElementError: Empty list. Cannot remove first element.'
			raise