ano = int(input("Digite o ano de nascimento: "))

if ano <= 1964:
	print("Geração baby boomer")
elif ano <= 1979:
	print("Geração X")
elif ano <= 1994:
	print("Geração Y")
else:
	print("Geração Z")
