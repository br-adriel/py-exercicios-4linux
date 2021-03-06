import csv

def cadastro():
	opcao = 1
	while opcao == 1:
		print('\nNovo cadastro')
		cpf = input('Digite seu CPF: ')
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


def consulta():
	resultado = []

	termo = input('\nDigite o termo de busca: ')

	print('\nPesquisando...')
	with open('cadastros.csv', 'r') as arquivo:
		dados = csv.reader(arquivo, delimiter=';')
		for linha in dados:
			for dado in linha:
				if termo.lower() in dado.lower():
					resultado.append(linha)
					break

	print(f'\n{len(resultado)} resultados encontrado(s)')
	for item in resultado:
		print('-' * 50)
		print(f'CPF: {item[0]}')
		print(f'Nome: {item[1]}')
		print(f'idade: {item[2]}')
		print(f'Sexo: {item[3]}')
		print(f'Endereço: {item[4]}')


def excluir():
	cpf = input('\nDigite o CPF do registro que deseja exlcuir: ')

	certeza = 'a'
	while certeza not in ['1', '2']:
		print(f'\nTem certeza que deseja excluir o registro com CPF {cpf}?')
		print('[1] SIM \t [2] NÃO')
		certeza = input('>> ')

	if certeza == '1':
		print('\nExcluindo...')

		with open('cadastros.csv', 'r') as arquivo:
			conteudo = csv.reader(arquivo, delimiter=';')
		
			novo_conteudo = []
			for linha in conteudo:
				if cpf != linha[0]:
					novo_conteudo.append(linha)

		with open('cadastros.csv', 'w') as arquivo2:
			gravador = csv.writer(arquivo2, delimiter=';')

			for linha in novo_conteudo:
				gravador.writerow(linha)

		print('\nRegistro exlcuido com sucesso')


def main():
	menu = {
		'1': cadastro,
		'2': consulta,
		'3': excluir
	}

	opcao = 'a'
	while opcao != '0':
		print('\nMENU PRINCIPAL')
		print('1 - Cadastrar dados')
		print('2 - Consultar registro')
		print('3 - Excluir registro')
		print('0 - Sair')
		opcao = input('>> ')

		if opcao in menu:
			menu[opcao]()


if __name__ == '__main__':
	main()
