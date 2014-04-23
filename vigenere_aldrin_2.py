import cProfile

class Vigenere(object):
	__alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890 '
	__keyword = 'excalibur'
	__plain_text = 'now is the time for all good men to come to the aid of their fellow man'
	__unwanted_chars = '`~!@#$%^&*()_+-={}|[]\\|;\'\"<>?,./'

	def __init__(self):
		self.alphabet = self.__alphabet

	def encrypt(self, key, message):
		self.__check_duplicates(key)
		self.__check_valid_input(key)
		self.__check_valid_input(message)
		message = message.lower()
		key = key.lower()
		print 'PASSWORD : ', key
		print '   MESSAGE : ', message
		self.mixed_alphabet = self.__construct_mixed_alphabet(key)
		self.table = self.__construct_table(self.mixed_alphabet)
		count = 0
		max_count = len(key) - 1
		cypher = ''
		for char in message:
			cypher += self.table[ key[count] ][ self.alphabet.index(char) ]
			if count < max_count:
				count += 1
			else:
				count = 0
		print '      CYPHER : ', cypher
		print
		return cypher

	def decrypt(self, key, message):
		self.__check_duplicates(key)
		self.__check_valid_input(key)
		self.__check_valid_input(message)
		message = message.lower()
		key = key.lower()
		print 'PASSWORD : ', key
		print '   MESSAGE : ', message
		self.mixed_alphabet = self.__construct_mixed_alphabet(key)
		self.table = self.__construct_table(self.mixed_alphabet)
		count = 0
		max_count = len(key) - 1
		cypher = ''
		for char in message:
			index = self.table[key[count]].index(char)
			cypher += self.alphabet[index]
			if count < max_count:
				count += 1
			else:
				count = 0
		print '      CYPHER : ', cypher
		return cypher

	def __check_valid_input(self, input):
		exist = False
		for char in input:
			for unwanted in self.__unwanted_chars:
				if char == unwanted:
					exist = True
			if exist is True:
				raise Exception('Only alphanumeric characters are allowed.')

	def __check_duplicates(self, key):
		count = 0
		for char in key:
			for unit in key:
				if char == unit:
					count += 1
			count = 0
			if count > 1:
				raise Exception('Password/Key cannot contain duplicate characters')

	def __construct_mixed_alphabet(self, key):
		string = self.alphabet.translate(None, key)
		string = key + string
		count = 0
		flag = 5
		max_passes = flag - 1
		passes = 0
		mixed = ''
		mixed_length = 0
		alphabet_length = len(self.alphabet)

		while mixed_length < alphabet_length and passes <= max_passes:
			for char in string:
				if count % flag == passes:
					mixed += char
					mixed_length += 1
				count += 1
			passes += 1
			count = 0
		return mixed

	def __construct_table(self, alphabet):
		r = c = 0
		dim = len(alphabet)
		mat = {}
		for i in xrange(dim):
			row = ''
			mat[self.__alphabet[r]] = alphabet[c:]+alphabet[:c]
			r += 1
			c = r % dim
		return mat

if __name__ == '__main__':
	krypto = Vigenere()

	message = 'now is the time for all good men to come to the aid of their fellow man'
	password = 'excalibur'

	cProfile.run("encrypted = krypto.encrypt(password, message)")
	cProfile.run("decrypted = krypto.decrypt(password, encrypted)")

	print encrypted
	print decrypted
