class Onibus:
	def __init__(self, placa, modelo):
		self.__capacidade_atual = 45
		self.__capacidade_total = 45
		self.__velocidade = 0
		self.__placa = placa
		self.__modelo = modelo

	def get_velocidade(self):
		return self.__velocidade

	def acelerar(self, medida=10):
		self.__velocidade += medida

	def frear(self, medida=10):
		if medida > self.__velocidade:
			self.__velocidade = 0
		else:
			self.__velocidade -= medida

	def embarcar(self):
		if self.__capacidade_atual != 0:
			self.__capacidade_atual-= 1
		else:
			return 'O ônibus está lotado'

	def desembarcar(self):
		if self.__capacidade_atual < self.__capacidade_total:
			self.__capacidade_atual+= 1
		else:
			return 'Não há ninguém no ônibus'
			