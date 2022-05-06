calc = {
	"+": lambda x, y: x + y,
	"-": lambda x, y: x - y,
	"*": lambda x, y: x * y,
	"/": lambda x, y: x / y
}

def main():
	n1 = int(input("Digite o primeiro número: "))		
	n2 = int(input("Digite o segundo número: "))

	print("\n+ -> soma")
	print("- -> subtração")
	print("* -> multiplicacao")
	print("/ -> divisão")
	
	opc = (input("\nDigite a operação: "))
	if opc in calc.keys():
		print("\nResultado:", calc[opc](n1, n2))
	else:
		print("\nOperação inválida")

if __name__ == '__main__':
	main()
