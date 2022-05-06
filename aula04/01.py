import random
import time

def main():
	jogadores = ['Ana', 'Beatriz', 'Caio', 'Dante', 'Eliana', 
				'Fábio', 'Gertrudes', 'Horácio', 'Iara', 'João']
	cadeiras = len(jogadores)-1

	print('Jogadores:')
	for j in jogadores:
		print(j)

	while cadeiras > 0:
		print(f'Restam {len(jogadores)} jogadores e {cadeiras} cadeiras')
		time.sleep(2)
		print('\nA música está tocando...')
		time.sleep(1)
		print('Os participantes estão circulando...')
		time.sleep(3)
		print('A música vai parar em 3, ', end='')
		time.sleep(1)
		print('2, ', end='')
		time.sleep(1)
		print('1!')
		time.sleep(1)

		random.shuffle(jogadores)
		quem_saiu = jogadores.pop()
		cadeiras = len(jogadores)-1

		print(f'\n{quem_saiu} não conseguiu sentar!')
	print(f'\n{jogadores[0]} ganhou!!!')


if __name__ == '__main__':
	main()
