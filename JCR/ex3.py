import re

"""
Construa um Filtro de Texto que adicione todos os números dum texto e que, no final, imprima a sua soma (no ficheiro de saída não deve aparecer nenhum caracter do texto de entrada).

Evolua o seu processador no sentido de:

    Escrever a soma sempre que encontre o carácter '=';
    Só comece a somar quando detectar o carácter '+' e deixe de somar quando este carácter voltar a aparecer.

"""

def exercicio():
	key = re.compile('\d+|\=|\+')

	f = open("input/somador.txt").read()

	res = re.findall(key,f)
	tof = False
	aux = []
	for elem in res:
		if not tof:
			if re.match(r'\+',elem):
				tof = True
		else:
			if tof:
				if re.match(r'\+',elem):
					tof = False
				if re.search(r'\d+',elem):
					aux.append(int(elem))
				if re.search(r'\=',elem):
					print(sum(aux))
				
	





exercicio()




