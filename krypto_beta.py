from collections import OrderedDict

class Vigenere(object):
	__alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	#~ __keyword = 'xoarhythmzy'
	__keyword = 'excalibur'
	
	def __init__(self, **kwargs):
		if 'alphabet' not in kwargs:			
			self.alphabet = self.__alphabet.lower()
		else:	
			self.alphabet = kwargs['alphabet'].lower()
		print '>>',self.alphabet
		if 'keyword' in kwargs:
			self.keyword = kwargs['keyword'].lower()		
		self.matrix = self.generateMatrix()
	
	def generateMatrix(self):
		r = c = 0
		dim = len(self.alphabet)
		mat = {}
		row = []

		for symbol in self.alphabet:
			for symbol in self.alphabet:
				row.append(self.alphabet[c])
				c += 1
				if c >= dim:
					c = 0
			mat[row[0]] = row
			row = []
			r += 1
			c = r % dim
			
		return mat
	
	def printMatrix(self):
		sorted =  self.matrix.items()
		sorted.sort()
		for k, v in sorted:
			print k, v
	
	def encrypt(self, keyword=__keyword, ):
		pass
			
if __name__ == '__main__':
	krypt = Vigenere()
	krypt.printMatrix()