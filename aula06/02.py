class Fila():
	def __init__(self):
		self.__fila = []

	def adicionarPessoa(pessoa):
		if len(self.__fila) > 10:
			return 'A fila está cheia'
		self.__fila.append(pessoa)

	def atender():
		if len(self.__fila) == 0:
			return 'Todos foram atendidos'
		atendido = self.__fila[0]
		del self.__fila[0]
		return atendido

	def darPrioridade():
		nova_fila = []
		for pessoa in self.__fila:
			if pessoa > 65:
				nova_fila.append(pessoa)

		for pessoa in self.__fila:
			if pessoa <= 65:
				nova_fila.append(pessoa)

		self.__fila = nova_fila

	def getFila():
		return self.__fila

