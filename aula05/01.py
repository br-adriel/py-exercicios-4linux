vogais = 0

with open('letra_faroeste_caboclo.txt', 'r') as arquivo:
	letra_musica = arquivo.readlines()

for linha in letra_musica:
	for letra in linha:
		if letra in 'aeiou':
			vogais += 1

print(f"Número de vogais em faroeste caboclo: {vogais}")
