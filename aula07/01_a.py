calc = {
	"+": lambda x, y: x + y,
	"-": lambda x, y: x - y,
	"*": lambda x, y: x * y,
	"/": lambda x, y: x / y,
}

def menu():
	print("\n+ -> soma")
	print("- -> subtração")
	print("* -> multiplicacao")
	print("/ -> divisão")
	print("s -> sair")

def main():
	while True:
		try:
			n1 = int(input("Digite o primeiro número: "))		
			n2 = int(input("Digite o segundo número: "))
		except ValueError:
			print("Valor inválido")
		else:
			menu()
			opc = input("\nDigite a operação: ")

			if (opc == "s"):
					exit()
					
			if opc in calc.keys():
				try:
					print("\nResultado:", calc[opc](n1, n2))
				except ZeroDivisionError:
					print("Impossível dividir por zero")
			else:
				print("\nOperação inválida")

if __name__ == '__main__':
	main()
