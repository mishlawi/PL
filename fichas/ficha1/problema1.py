import re

fo  = open ('../../inputs/usernames.txt')
lista = []
#^[_]|[\.])\d+[a-zA-Z]{3,}[_]?
key = re.compile(r'^([_]|[.])\d+[a-zA-Z]{3,}[_]?$')

print("O ficheiro usado como input esta na pasta inputs com o nome usernames.txt\n")
lista = [line.rstrip() for line in fo]
for line in lista:
	res = key.search(line)
	if(res):
		print("Válido")
	else:

		print("Invalido")
