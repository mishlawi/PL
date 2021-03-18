"""
Construa um programa que apresente todas as palavras e números do texto fonte,
indicando o número da linha onde se encontram 
(numa segunda versão indique também em que coluna da linha é iniciada a palavra ou o número).
"""

import re

#considerei que uma palavra teria no minimo 2 caracteres e que podia estar misturada com digitos e outros caracteres especiais

def exercise():
	key = re.compile(r'[a-zA-Z]{2,}|\d+')
	n = 0
	f = open("input/random.txt").readlines()
	file = open("input/random.txt").read()
	lista = []
	line = f[n]
	for line in f:
		v = len(line)
		x = re.findall(key,line)
		for parse in x:
			res = re.search(parse,line).span()
			line = line[res[0]+1:]
			print(line)
			lista.append([parse,v-len(line),n])
		n+=1
	print("| Palavra/Numero | Coluna   | Linha   |" )
	print("***************************************")
	for elem in lista:
		print("|",elem[0],(" "*(13-len(elem[0]))),"|",elem[1],(" "*(6-len(str(elem[1])))) ," | ", elem[2],(" "*(5-len(str(elem[2])))) ,"|")
		
exercise()

