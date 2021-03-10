"""
Um endereco de email e composto por uma lista de strings
separadas por ’.’  antes do @ ao qual se seguem uma nova lista de strings separadas por ’.’. 
Uma string pode ser formada pelos carateres:  [a−z],[A−Z],[0−9] e ’_’

Mail us at hackers@hackerrank.com to chat more. Or you can write to us at interviewstreet@hackerrank.com!
"""


#Seria espectavel receber o input de um ficheiro para o calculo dos valores de N ser relevante
#Nao quis entrar nesse detalhe

import re
key = re.compile(r'(([A−Za-z]|[0-9]|\_)*\.)*([A−Za-z]|[0-9]|\_)+@(([A−Za-z]|[0-9]|\_)*\.)+([A−Za-z]|[0-9]|\_)+')
fo = open ("../../inputs/emails.txt")

def querie():
	global fo	
	global key 
	final=[]
	
	iterable = [line.rstrip() for line in fo]
	N = int(iterable[0])
	if N>=101 or N<1:
		print("erro")
		exit()
	else:
		print("*****************************")
		print("Ficheiro contém", N, "linhas" )
		print("*****************************")
		for elem in iterable:

			final.extend(elem.split(" "))
		
		print(final)
		number  = iterable[0]

		endereco = ''
		for elem in final:
			res = key.search(elem)

			if res:
				endereco = endereco + elem + ';'
		print("Endereços válidos:\n")
		print(endereco)

querie()