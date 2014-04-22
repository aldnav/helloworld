# MACHINE EXERCISE DAY 2: JOSEPHUS GAME USING CIRCULAR LIST
# @author Aldrin A. Navarro

class Soldier(object):	
	def __init__(self, id, next=None, prev=None):
		self.id = id
		self.next = next
		self.prev = prev
	
	def __str__(self):
		return str(self.id)
	
class CircularList(object):
	def __init__(self):
		self.head = self.tail = None
		self.size = 0
	
	def __iter__(self):
		pointer = self.head
		while pointer:
			yield pointer
			pointer = pointer.next
			if pointer is self.head:
				break
	
	def __str__(self):
		if self.size == 0:
			return '[]'
		strBldr = ''
		for i in self:
			soldier = i
			strBldr += '[' + str(soldier.id) + ']'
		return strBldr
	
	def __addFirstsoldier(self, soldier):
		self.head = self.tail = soldier
		self.head.prev = self.tail.next = soldier
	
	def append(self, data):
		soldier = Soldier(data)
		if self.head is None:
			self.__addFirstsoldier(soldier)
		else:
			self.tail.next = soldier
			soldier.prev = self.tail
			self.tail = soldier
		self.tail.next = self.head
		self.head.prev = self.tail
		self.size += 1
	
	def removeHead(self):
		toRemove = self.head
		self.head = self.head.next
		self.head.prev = self.tail
		self.tail.next = self.head
		toRemove.next = None
		toRemove.prev = None
		self.size -= 1
		return toRemove
	
	def removeTail(self):
		toRemove = self.tail
		self.tail = self.tail.prev
		self.tail.next = self.head
		self.head.prev = self.tail
		toRemove.next = None
		toRemove.prev = None
		self.size -=1
		return toRemove
	
	def removeAt(self, data):
		found = False
		for soldiers in self:
			if soldiers.id == data:
				found = True
				toRemove = soldiers
				break
				
		if found:
			prevSoldier = toRemove.prev
			prevSoldier.next = toRemove.next
			toRemove.next.prev = prevSoldier
			toRemove.next = None
			toRemove.prev = None
			self.size -= 1
			return toRemove
		else:
			print 'not found'
			return
	
	def remove(self, data):
		if self.head.id == data:
			self.removeHead()
		elif self.tail.id == data:
			self.removeTail()
		else:
			self.removeAt(data)

def josephus(numOfSoldiers, step):
	print 'SOLDIERS: ', numOfSoldiers
	print 'STEPS: ', step
	if numOfSoldiers <= 0 or step <= 0:
		print 'Invalid params passed'
		return
	
	troop = CircularList()	
	for i in range(1, numOfSoldiers+1):
		troop.append(i)
	
	count = 0
	soldier = troop.head	
	while troop.size > 1:		
		count += 1
		if count == step:
			nextNode = soldier.next			
			troop.remove(soldier.id)			
			count = 0
			soldier = nextNode
		else:		
			soldier = soldier.next
		#~ print troop

	print 'Soldier', soldier, 'survives'
	return
	
if __name__ == '__main__':
	
	#~ ls = CircularList()
	#~ ls.append(1)
	#~ ls.append(2)
	#~ ls.append(3)
	#~ ls.append(4)
	#~ ls.append(5)
	#~ ls.append(6)
	#~ ls.remove(1)
	#~ print ls
	#~ print ls.head, ls.tail
		
	josephus(40, 7)
	josephus(41, 3)
	josephus(5, 2)
	josephus(6, 3)
	josephus(2, 1)
	josephus(0, 0)
	josephus(500, 3)
