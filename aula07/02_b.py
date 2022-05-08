from unittest import TestCase
from unittest import main
from q01_b import fazer_cadastro, fazer_consulta, fazer_exclusao

class testCadastros(TestCase):
	def test_create(self):
		fazer_cadastro('123456789;fulano;18;m;Av das laranjas\n')
		esperado = [
			['123456789', 'fulano', '18', 'm', 'Av das laranjas']
		]
		self.assertEqual(esperado, fazer_consulta('123456789'))

	def test_delete(self):
		fazer_exclusao('123456789')
		self.assertEqual([], fazer_consulta('123456789'))


if __name__ == '__main__':
	main()
