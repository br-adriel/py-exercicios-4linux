cesta = []
precos = {
	"Banana": 3.5,
	"Melancia": 7.5,
	"Morango": 5
}

opcao = 0;
while (opcao != 4):
	print("\nQuitanda:")
	print("1: Ver cesta")
	print("2: Adicionar frutas")
	print("3: Checkout")
	print("4: Sair")
	opcao = int(input("\nDigite a opção desejada: "))

	if opcao == 1:
		print("\nSua cesta:")

		if len(cesta) > 0:
			for fruta in cesta:
				print(fruta)
		else:
			print("Sua cesta está vazia")

	elif opcao == 2:
		print("\nMenu de frutas:")
		print("\nEscolha a fruta desejada:")
		print("1 - Banana");
		print("2 - Melancia")
		print("3 - Morango")
		fruta = int(input("Digite a opção desejada: "))

		if fruta == 1:
			cesta.append("Banana")
			print("Banana adicionada com sucesso!")
		elif fruta == 2:
			cesta.append("Melancia")
			print("Melancia adicionada com sucesso!")
		elif fruta == 3:
			cesta.append("Morango")
			print("Morango adicionada com sucesso!")
		else:
			print("Opção inválida, nenhuma fruta foi adicionada!")
	elif opcao == 3:
		total = 0
		cestaString = "";

		for i in range(len(cesta)):
			total += precos[cesta[i]]

			cestaString += cesta[i]
			if i != len(cesta)-1:
				cestaString += ", "

		print("\nTotal de compras: {}".format(total))
		print("Cesta de compras: {}".format(cestaString))
	elif opcao == 4:
		print("\nSaindo...")
	else:
		print("\nOpção inválida!")


