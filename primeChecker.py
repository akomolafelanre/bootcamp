
class PrimeChecker(object):
	"""docstring for PrimeChecker"""
	def __init__(self, number = None):
	  super(PrimeChecker, self).__init__()
	  self.number = 0
	  if number != None:
	  	self.number = number
	  	if type(number) == str:
	  		self.number = 0
	  		if len(number) > 0:
	  			self.number = int(number)
		
	def is_prime(self):
		number = self.number
		if number <= 0 or number == 1:
			return False
		if number == 2:
			return True
		if number % 2 == 0:
			return False
		a = ((number + 1)/2) + 1
		for i in range(2,a):
			if number % i == 0:
				return False
		return True
		
nb = PrimeChecker('')
print nb.is_prime()