"""
Num paıs algures, as matriculas seguem os seguintes requisitos:
Uma matrıcula tem 8 dıgitos;•Os 8 dıgitos estao divididos
em 4 partes iguais de 2 dıgitos por um separador que pode ser ’...’, ’-’ ou ’:’;
Cada matrıcula so pode ter uma especie de separador;
Os separadores tem de ter dıgitos antes e depois, nao ha espacos.
P.E.:
22...44...22...11
22-44-22-11
22:44:22:11
"""

import re

key= re.compile(r'((\d{2}(...)){3}|(\d{2}\:){3}|(\d{2}\-){3})\d{2}')
count = 0


print("import from file: (write the correct path\nEx: ../this/is/a/path/for/file")
n = input()

try:

	fo = open(n)

except FileNotFoundError:
	print("*******************************************************")
	print("FICHEIRO INSERIDO INVALIDO -->> SERÁ USADO FICHEIRO DEFAULT")
	print("*******************************************************")
	fo = open('../../inputs/save.txt')


iterable = [line.rstrip() for line in fo]
for elem in iterable:

	result = key.search(elem)

	if result:
		count+=1
		print(elem)
		print("STATUS: Há ", count, "válidos por enquanto\n")

print("Ficheiro inserido continha ", count, "matriculas válidas")

