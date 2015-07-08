def generateSeries(n):
	if (type(n) != int):
		return 'Not an Integer'
	if (n < 2):
		return 'The number provided must be an integer geater than 1'
	sequence = [0,1]
	if (n == 2):
		return sequence
	for i in range(1, n-1):
		sum = sequence[i] + sequence[i-1]
		sequence.append(sum)
	return sequence





def calculateSum(n):
	pass	

def generateSeriesSum(n, key= None):
	pass