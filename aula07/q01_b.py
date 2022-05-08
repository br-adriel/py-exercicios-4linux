import csv

def fazer_cadastro(item):
	try:
		with open('cadastros.csv', 'a') as arquivo:
			arquivo.write(item)

		print('\nCadastro realizado com sucesso!')
	except Exception:
		print('Um erro ocorreu')


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

		fazer_cadastro(linhaCadastro)

		opcao = 0
		while opcao not in [1, 2]:
			print('\nDeseja cadastrar novamente?')
			print('[1] SIM\t[2] NÃO')
			try :
				opcao = int(input('>> '))
			except ValueError:
				print('Valor inválido')


def fazer_consulta(termo):
	resultado = []
	try :
		with open('cadastros.csv', 'r') as arquivo:
			dados = csv.reader(arquivo, delimiter=';')
			for linha in dados:
				for dado in linha:
					if termo.lower() in dado.lower():
						resultado.append(linha)
						break
	except Exception:
		print('Um erro ocorreu')
		resultado = []
	finally:
		return resultado;


def consulta():
	termo = input('\nDigite o termo de busca: ')

	print('\nPesquisando...')

	resultado = fazer_consulta(termo)
	
	print(f'\n{len(resultado)} resultados encontrado(s)')
	for item in resultado:
		print('-' * 50)
		print(f'CPF: {item[0]}')
		print(f'Nome: {item[1]}')
		print(f'idade: {item[2]}')
		print(f'Sexo: {item[3]}')
		print(f'Endereço: {item[4]}')


def fazer_exclusao(cpf):
	with open('cadastros.csv', 'r') as arquivo:
		try:
			conteudo = csv.reader(arquivo, delimiter=';')
		except Exception:
			print('Um erro ocorreu')
		else:
			novo_conteudo = []
			for linha in conteudo:
				if cpf != linha[0]:
					novo_conteudo.append(linha)

			try:
				with open('cadastros.csv', 'w') as arquivo2:
					gravador = csv.writer(arquivo2, delimiter=';')

					for linha in novo_conteudo:
						gravador.writerow(linha)
			except Exception:
				print('Um erro ocorreu')		


def excluir():
	cpf = input('\nDigite o CPF do registro que deseja exlcuir: ')

	certeza = 'a'
	while certeza not in ['1', '2']:
		print(f'\nTem certeza que deseja excluir o registro com CPF {cpf}?')
		print('[1] SIM \t [2] NÃO')
		certeza = input('>> ')

	if certeza == '1':
		print('\nExcluindo...')
		fazer_exclusao(cpf)
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
