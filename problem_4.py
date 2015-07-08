def generateNextValue(n):
	a = len(n)-1
	b = n[a] + n[a-1]
	return b

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
	if (type(n) != list):
		return 'Not a list'
	if len(n) == 0:
		return 'The list is empty'
	for item in n:
		if type(item) != int:
			return 'The list contains a non integer value'
	return sum(n)

def generateSeriesSum(n, filt= None):
	if (type(n) != int):
		return 'Not an Integer'
	if (n < 2):
		return 'The number provided must be an integer geater than 1'
	key = filt
	initial_array = [0,1]
	final_array = []
	if key == None:
		initial_array = generateSeries(n)
		return calculateSum(initial_array)
	if key == 'even':
		while len(final_array) < n:
			temp = generateNextValue(initial_array)
			initial_array.append(temp)
			if temp % 2 == 0:
				final_array.append(temp)
		return calculateSum(final_array)
	if key == 'odd':
		final_array = [1]
		while len(final_array) < n:
			temp = generateNextValue(initial_array)
			initial_array.append(temp)
			if temp % 2 == 1:
				final_array.append(temp)
		return calculateSum(final_array)
	if key != 'odd' and key != 'even':
		return "This function can only be called with 'odd' or 'even'"