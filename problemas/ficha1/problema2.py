"""
Problema 2:
Dada uma lista de linhas em que cada uma deve conter um endereco IP, IPv4 ou IPv6, supostamente valido,
desenvolvaum filtro de texto que identifica o tipo de endereco IP ou acusa um erro.
Os enderecos IPv4 foram os primeiros enderecos a serem usados na Internet e eram constituıdos por 4 bytes.
O formato normal  e ”A.B.C.D”
em que A, B, C e D sao inteiros compreendidos entre 0 e 255 inclusive.
O IPv4 limitava o numero de enderecos a um numero baixo para as necessidades de hoje em dia e assim surgiu o IPv6.Com 128 bits, veio permitir um maior espa ̧co de endere ̧camento.
Os 128 bits dum endereco IPv6 sao representadosem 8 grupos de 16 bits cada um.
Cada grupo e representado por 4 dıgitos hexadecimais e cada grupo  e separado doseguinte por ’:’.  Por exemplo:  ”2001:0db8:0000:0000:0000:ff00:0042:8329”.  Os zeros `a esquerda podem ser omitidos.
Um endereco contendo ”...:0:...”ou ”...:5:...” e identico a ”...:0000:...”ou ”...:0005:....”.
"""


import re

key = re.compile(r'^((([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.){3}([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])|(([0]?[a-f0-9]{4}|[1-9a-f]?[1-9a-f]?[0-9a-f])\:){7}([a-f0-9]{4}|[1-9a-f]?[1-9a-f]?[0-9a-f]))$')
print("introduza o nr de inputs a considerar")
n = int(input())
x=True
conta=0
for i in range(n):
	linha = input()
	res = key.search(linha)
	if not res:
		print("invalido")
	else:
		print("valido")
		conta+=1

print("Total:",conta,"valido(s)")


