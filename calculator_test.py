import unittest
from calculator import add, divide, multiply, subtract

class CalculatorTest (unittest.TestCase):

	def testAdd(self):
		self.assertEqual(4, add(2,2))
		self.assertEqual(5, add(2,3))
		self.assertEqual(8.3, add(2.8, 5.5))
		self.assertEqual('ab', add('a', 'b'))
		
	def testDivide(self):
		self.assertEqual(1, divide(2,2))
		self.assertEqual(5, divide(10,2))
		self.assertEqual(3, divide(7.5,2.5))

	def testMultiply(self):
		self.assertEqual(15, multiply(5, 3))
		
	def testSubtract(self):
		self.assertEqual(95, subtract(100, 5))
		
unittest.main()