"""


Quando se retiram apontamentos, ou de uma forma geral, se tem de escrever muito depressa, é hábito usar abreviaturas que correspondam a uma ou mais palavras vulgares e longas.

Suponha que criou esse costume e resolveu inserir nos seus textos as ditas abreviaturas (2 ou mais letras) precedidas pelo carácter '\'. Por exemplo: '\qq' (qualquer), ou '\mb' (muito bom), ou ainda '\sse' (se e só se).\

Desenvolva então as seguintes alíneas:

    um FT que lhe devolva o texto original mas com todas as abreviaturas (que definiu à partida) devidamente expandidas;
    melhore o seu filtro de modo a contemplar ainda o tratamento do carácter '/' no fim de uma palavra, representando o sufixo 'mente', e o carácter '~' no início de uma palavra, representando o prefixo 'in'. Uma palavra pode conter ambos os caracteres, um no início e outro no fim (pense na abreviatura da palavra 'infelizmente');
    outra melhoria que poderia introduzir no seu filtro era contemplar a possibilidade de definir abreviaturas dentro do próprio texto, na forma '\def:abrev=termo-expandido;'. Pense como o fazer e nas implicações que tal requisito teria no seu filtro original (alínea proposta para pensar fora da aula).

"""

import re

def querie1():

	print("Insira o path do ficheiro a processar")
	
	try:

		fo = open(input())
		abreviaturas = {}
		print("Insira o nr de abreviaturas:")
		n = (int(input()))
		print("****************************\nDefina-as")
		for x in range(n):
			print("-->Abreviatura")
			word = input()
			print("-->Significado")
			significado = input()
			if word not in abreviaturas:
				abreviaturas.update({word:significado})

	except FileNotFoundError:

		fo = open("input/example.txt")
		abreviaturas = {'bc':'because','expt':'except','opp':'opportunity', 'u':'you', 'crzy':'crazy'}
	
	iterable = [line.rstrip() for line in fo]
	final = []
	for line in iterable:
		aux = line
		for elem in abreviaturas:
			regex = r"\\\b" + elem + r"\b" #key
			key = re.compile(regex)
			res = key.search(aux)
			if res:
				aux = re.sub(regex,abreviaturas[elem],aux)
		final.append(aux)
	for line in final:
		print(line)

querie1()


