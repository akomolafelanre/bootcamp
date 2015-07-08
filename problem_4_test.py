import unittest, problem_4

class TestFunWithFibonacci(unittest.TestCase):
	
	def testGSeries_NotInteger(self):
		self.assertEqual(problem_4.generateSeries("A"), -1,  \
			msg = "This should return that the value is not an integer")
		self.assertEqual(problem_4.generateSeries("]"), -1,  \
			msg = "This should return that the value is not an integer")

	def testGSeries_NotLessThanOne(self):
		self.assertEqual(problem_4.generateSeries(0), -1,  \
			msg = "This should return -1 since 0 is less than 1")

	def testGSeries_CheckCorrectResult(self):
		self.assertEqual(problem_4.generateSeries(3), [0,1,1],  \
			msg = "This should generate the list [0,1,1] ")
		self.assertEqual(problem_4.generateSeries(5), [0,1,1,2,3],  \
			msg = "This should generate the list [0,1,1,2,3] ")

	def testSum_IsList(self):
		self.assertEqual(problem_4.calculateSum(0), -1,  \
			msg = "This should return -1 since 0 is not a list")
		self.assertEqual(problem_4.calculateSum([0,1,2]), 3,  \
			msg = "This should return the length of the list")

	def testSum_IsListOfDigits(self):
		self.assertEqual(problem_4.calculateSum(["D", 3, 4]), -1,  \
			msg = "This should return -1 since D is not a number and cant be summed")
		self.assertEqual(problem_4.calculateSum([0,1,2]), 3,  \
			msg = "This should return the length of the list")

	def testSum_IsResultCorrect(self):
		self.assertEqual(problem_4.calculateSum([3, 4]), 7,  \
			msg = "This should return the sum of [3,4] as 7 ")

	def testSum_IsResultCorrect(self):
		self.assertEqual(problem_4.calculateSum([3, 4]), 7,  \
			msg = "This should return the sum of [3,4] as 7 ")

if __name__ == "__main__":
	unittest.main()