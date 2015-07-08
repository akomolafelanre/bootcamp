import unittest, problem_4

class TestFunWithFibonacci(unittest.TestCase):
	
	def testGNextValue_CheckCorrectResult(self):
		result = problem_4.generateNextValue([0,1,1])
		self.assertEqual(result, 2,  \
			msg = "This should return an empty list")

	def testGNextValue_CheckCorrectResult2(self):
		result = problem_4.generateNextValue([0,1,1,2,3])
		self.assertEqual(result, 5,  \
			msg = "This should return an empty list")

	def testGSeries_NotInteger(self):
		result = problem_4.generateSeries("A")
		self.assertEqual(result, 'Not an Integer',  \
			msg = "This should return an empty list")

	def testGSeries_NotLessThanOne(self):
		result = problem_4.generateSeries(0)
		self.assertEqual(result, 'The number provided must be an integer geater than 1',  \
			msg = "This should return an error string since 0 is less than 1")

	def testGSeries_NotLessThanOne2(self):
		result = problem_4.generateSeries(-1)
		self.assertEqual(result, 'The number provided must be an integer geater than 1',  \
			msg = "This should return an error string since -1 is less than 1")

	def testGSeries_CheckCorrectResult(self):
		result = problem_4.generateSeries(3)
		self.assertEqual(result, [0,1,1],  \
			msg = "This should generate the list [0,1,1] ")

	def testGSeries_CheckCorrectResult2(self):
		result = problem_4.generateSeries(5)
		self.assertEqual(result, [0,1,1,2,3],  \
			msg = "This should generate the list [0,1,1] ")

	def testSum_IsList(self):
		result = problem_4.calculateSum(1)
		self.assertEqual(result, 'Not a list',  \
			msg = "This should return the sum of the list")

	def testSum_IsList2(self):
		result = problem_4.calculateSum('aded')
		self.assertEqual(result, 'Not a list',  \
			msg = "This should return the sum of the list")

	def testSum_IsList3(self):
		result = problem_4.calculateSum([0,1,2])
		self.assertEqual(result, 3,  \
			msg = "This should return the sum of the list")

	def testSum_IsListOfDigits(self):
		result = problem_4.calculateSum(["D", 3, 4])
		self.assertEqual(result, 'The list contains a non integer value',  \
			msg = "This should return -1 since D is not a number and cant be summed")

	def testSum_IsNotEmptyList(self):
		result = problem_4.calculateSum([])
		self.assertEqual(result, 'The list is empty',  \
			msg = "This should return 'The list is empty' ")

	def testSum_IsResultCorrect(self):
		result = problem_4.calculateSum([3, 4])
		self.assertEqual(result, 7,  \
			msg = "This should return the sum of [3,4] as 7 ")

	def testSum_IsResultCorrect2(self):
		result = problem_4.calculateSum([3, 4, 5, 1])
		self.assertEqual(result, 13,  \
			msg = "This should return the sum of [3, 4, 5, 1] as 13 ")

	def testGSeriesSum_IsInputCorrect(self):
		result = problem_4.generateSeriesSum("A")
		self.assertEqual(result, 'Not an Integer',  \
			msg = "This should return that the input is not an integer value")

	def testGSeriesSum_IsInputCorrect2(self):
		result = problem_4.generateSeriesSum([1,2])
		self.assertEqual(result, 'Not an Integer',  \
			msg = "This should return that the input is not an integer value")

	def testGSeriesSum_IsResultCorrect(self):
		result = problem_4.generateSeriesSum(3)
		self.assertEqual(result, 2,  \
			msg = "This should return the sum of fibonacci sequence with three elements as 2")

	def testGSeriesSum_IsResultCorrect2(self):
		result = problem_4.generateSeriesSum(1)
		self.assertEqual(result, 'The number provided must be an integer geater than 1',  \
			msg = "This should return an error string since a fibbonnacci sequence must have at least 2 elements")

	def testGSeriesSum_IsResultCorrect3(self):
		result = problem_4.generateSeriesSum(4, 'even')
		self.assertEqual(result, 188,  \
			msg = "This should return the sum of even numbers in a fibonacci sequence with 5 elements as 2")

	def testGSeriesSum_IsResultCorrect4(self):
		result = problem_4.generateSeriesSum(3, 'even')
		self.assertEqual(result, 44,  \
			msg = "This should return the sum of even numbers in a fibonacci sequence with 3 elements as 0")

	def testGSeriesSum_IsResultCorrect5(self):
		result = problem_4.generateSeriesSum(4, 'odd')
		self.assertEqual(result, 10,  \
			msg = "This should return the sum of odd numbers in a fibonacci sequence with 5 elements as 5")

	def testGSeriesSum_IsResultCorrect6(self):
		result = problem_4.generateSeriesSum(2, 'odd')
		self.assertEqual(result, 2,  \
			msg = "This should return the sum of odd numbers in a fibonacci sequence with 2 elements as 1")

	def testGSeriesSum_IsResultCorrect7(self):
		result = problem_4.generateSeriesSum(5, 'all')
		self.assertEqual(result, "This function can only be called with 'odd' or 'even'",  \
			msg = "This should return that function is called with a wrong parameter")

	def testGSeriesSum_IsResultCorrect8(self):
		result = problem_4.generateSeriesSum(1, 'all')
		self.assertEqual(result, 'The number provided must be an integer geater than 1',  \
			msg = "This should return that function is called with a wrong parameter")


if __name__ == "__main__":
	unittest.main()