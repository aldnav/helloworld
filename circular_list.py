class CircularList(object):
	
	#~ CW (linear right) direction set to false by default.
	def __init__(self, list=None, direction=False):
		if list is not None:
			self.list = list
		else:
			self.list = []
		self.direction = direction
			
	def __str__(self):
		return str(self.list)
	
	def append(self, element):
		return self.list.append(element)
		
if __name__ == '__main__':
	#~ warriors = CircularList()
	#~ warriors.append('Octavius')
	#~ print warriors
	
	#~ warriors.append('Julius')
	#~ print warriors
	
	list = range(10)
	print list
	list = [x*x for x in list]
	for x in enumerate(list)
		print x