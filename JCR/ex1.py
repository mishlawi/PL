"""


Suponha que ao fim de cada entrevista um Repórter
produz um texto com as perguntas e respostas,
distinguindo umas das outras porque as perguntas começam com 'EU:', no início da linha, e as respostas começam com 'ELE:', também no início da linha.

Nesse contexto, pretende-se desenvolver um FT para processar os questionários que:

simplesmente retire do texto original as tais marcas 'EU:' e 'ELE:', devolvendo todo o resto da entrevista sem qualquer alteração. Melhore o filtro, de modo a tratar as marcas, quer estejam escritas em maiúsculas, quer em minúscul
substituia a marca 'EU' pela palavra 'Entrevistador' e a marca 'ELE' por 'Entrevistado';
substituia a marca 'EU' pelo nome do entrevistador e a marca 'ELE' pelo nome do entrevistado, supondo que no início encontrará as respectivas definições (ordem irrelevante) na forma 'EU=nome.' ou 'ELE=nome.'

"""

import re
fo = open('input/entrevista.txt')
it = [line.rstrip() for line in fo]
def querie1():
	global fo
	key = re.compile(r'^(?i)(ele|eu):')
	global it 
	for line in it:
		re.sub(key,'',line)
		print(line)
	print("************************************\n\n\n")

def querie2():
	global fo
	keyHim = re.compile(r'^(?i)(ele)')
	keyMe = re.compile(r'^(?i)(eu)')
	
	for line in it:
		res1 = keyMe.search(line)
		res2 = keyHim.search(line)
		if res1:
			line= re.sub(keyMe,'Entrevistador',line)
		if res2:
			line =re.sub(keyHim,'Entrevistado',line)
		print(line)
	print("************************************\n\n\n")
	

def querie3():

	global fo
	global it
	print("Indique o nome do entrevistado:")
	entrevistado = input()
	print("Indique o seu nome:")
	entrevistador = input()
	print("-----------------------------------------\n\n\n\n")
	keyHim = re.compile(r'^(?i)(ele)')
	keyMe = re.compile(r'^(?i)(eu)')
	for line in it:
		res1 = keyMe.search(line)
		res2 = keyHim.search(line)
		if res1:
			line= re.sub(keyMe,entrevistador,line)
		if res2:
			line =re.sub(keyHim,entrevistado,line)
		print(line)
	print("************************************\n\n\n")


querie1()
querie2()
querie3()