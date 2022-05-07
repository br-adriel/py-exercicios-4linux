import csv

def main():
	opcao = 1
	while opcao == 1:
		print('\nNovo cadastro')
		cpf = input('Digite seu cpf: ')
		nome = input('Digite seu nome: ')
		idade = input('Digite sua idade: ')
		sexo = input('Digite seu sexo: ')
		endereco = input('Digite seu endereço: ')

		linhaCadastro = f'{cpf};{nome};{idade};{sexo};{endereco}\n'

		with open('cadastros.csv', 'a') as arquivo:
			arquivo.write(linhaCadastro)

		print('\nCadastro realizado com sucesso!')

		opcao = 0
		while opcao not in [1, 2]:
			print('\nDeseja cadastrar novamente?')
			print('[1] SIM\t[2] NÃO')
			opcao = int(input('>> '))


if __name__ == '__main__':
	main()
