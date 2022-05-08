from unittest import TestCase
from unittest import main
from q01_a import calc

class testCalculadora(TestCase):
	def test_soma(self):
		n1 = 10
		n2 = 5
		self.assertEqual(15, calc['+'](n1, n2))

	def test_subtracao(self):
		n1 = 10
		n2 = 5
		self.assertEqual(5, calc['-'](n1, n2))

	def test_multiplicacao(self):
		n1 = 10
		n2 = 5
		self.assertEqual(50, calc['*'](n1, n2))

	def test_divisao(self):
		n1 = 10
		n2 = 5
		self.assertEqual(2, calc['/'](n1, n2))

if __name__ == '__main__':
	main()
