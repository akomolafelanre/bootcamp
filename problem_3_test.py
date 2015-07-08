import problem_3, unittest

class PasswordTest(unittest.TestCase):
	def testUpperCase(self):
		self.assertEqual(problem_3.check_upper("ABCD"), 4 , \
			msg = "This test should return 4 for ABCD")

if __name__ = "__main__":
	unittest.main()