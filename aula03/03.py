def menuPrincipal():
	print("\nQuitanda:")
	print("1: Ver cesta")
	print("2: Adicionar frutas")
	print("3: Checkout")
	print("4: Sair")
	return int(input("\nDigite a opção desejada: "))


def listarCesta(cesta=[]):
	print("\nSua cesta:")
	if len(cesta) > 0:
		for fruta in cesta:
			print(fruta)
	else:
		print("Sua cesta está vazia")


def adicionarFruta(cesta, fruta):
	cesta.append(fruta)
	print(f"{fruta} adicionada com sucesso!")


def menuFrutas():
	print("\nMenu de frutas:")
	print("\nEscolha a fruta desejada:")
	print("1 - Banana");
	print("2 - Melancia")
	print("3 - Morango")
	return int(input("Digite a opção desejada: "))


def mostrarTotal(cesta, precos):
	total = 0
	cestaString = "";

	for i in range(len(cesta)):
		total += precos[cesta[i]]

		cestaString += cesta[i]
		if i != len(cesta)-1:
			cestaString += ", "

	print("\nTotal de compras: R$ {:.2f}".format(total))
	print("Cesta de compras: {}".format(cestaString))


def main():
	cesta = []
	precos = {
		"Banana": 3.5,
		"Melancia": 7.5,
		"Morango": 5
	}

	opcao = 0;

	while (opcao != 4):
		opcao = menuPrincipal()

		if opcao == 1:
			listarCesta(cesta)
		elif opcao == 2:
			fruta = menuFrutas()

			if fruta == 1:
				adicionarFruta(cesta, "Banana")
			elif fruta == 2:
				adicionarFruta(cesta, "Melancia")
			elif fruta == 3:
				adicionarFruta(cesta, "Morango")
			else:
				print("Opção inválida, nenhuma fruta foi adicionada!")
		elif opcao == 3:
			mostrarTotal(cesta, precos)
		elif opcao == 4:
			print("\nSaindo...")
		else:
			print("\nOpção inválida!")


if __name__ == '__main__':
	main()
