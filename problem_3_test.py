import problem_3, unittest

class PasswordTest(unittest.TestCase):
	def testUpperCase(self):
		self.assertEqual(problem_3.check_uppercase("ABCD"), 4 , \
			msg = "This test should return 4 for ABCD")
	def testLowerCase(self):
		self.assertEqual(problem_3.check_lowercase("ABCDab"), 2 , \
			msg = "This test should return 2 for ABCDab")

if __name__ == "__main__":
	unittest.main()