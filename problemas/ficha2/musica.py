import re


"""
provincia// zona geografica//nome da cancao// musico // ficheiro de audio//duracao em minutos e segundos
"""

#ordem alfabetica
#top 10

fo = open('../../inputs/arqson.txt')
iterable = [line.rstrip() for line in fo]


def querie1():
	count = 0
	result = []
	rascunho = []
	global iterable
	keyAlentejo = re.compile(r'^(Alentejo)') #r'^(Alentejo)'
	
	for elem in iterable:
		res = keyAlentejo.search(elem)
		if res:
			aux = elem.split("::")
			count+=1
			rascunho.append(aux[2])
	
	[result.append(song) for song in rascunho if song not in result]
	result.sort()
	
	print("                  LISTA DE MUSICAS - (nao repetidas)")
	
	for elem in result:
		print (elem)
	print("****************************************************")
	print("Numero total de musicas (c/ as repetidas) associadas ao Alentejo:")
	print(count)
	print("----------------------------------------------------")

	return result


# sorted (iterável, key= oq for , reverse (opcional))
def querie2():
	global iterable
	
	rascunho = {}
	for elem in iterable:
		aux = elem.split("::")
		if aux[1] in rascunho:
			x = rascunho[aux[1]]
			x+=1
			rascunho[aux[1]]=x
		else:
			rascunho.update({aux[1]:1})
	regioesAux = sorted(rascunho.items(), key = lambda x : x[1], reverse = True)
	regioes = {k : v for k, v in regioesAux}
	print("TOP 10")
	n=1

	for elem in list(regioes)[0:10]:
		print(n,elem,":",regioes[elem])
		n+=1


def querie3():
	global iterable
	rascunho = []
	mp3 = []
	key = re.compile(r'\.mp3:')

	for elem in iterable:
		res = key.search(elem)
		if res:
			musica = elem.split("::")[2]
			rascunho.append(musica)
	print("\n***********************************")
	print("LISTA DE MUSICAS DISPONIVEIS EM MP3 (S/ REPETIÇÕES")
	
	[mp3.append(x) for x in rascunho if x not in mp3]
	for music in mp3:
		print(music)
	print("TOTAL S/ REMOVER REPETIDAS:", len(rascunho))
	print("TOTAL C/ REMOÇÃO DE REPETIDAS:", len(mp3))


def querie4():
	global iterable
	nome = []
	holykey = re.compile(r'(J|j)esus')


	for elem in iterable:
		musica = elem.split("::")[2]
		res = holykey.search(musica)

		if res:
			
			nome.append(musica)
	print("\n***********************************")
	print("LISTA DE MUSICAS COM O NOME JESUS (S/ REPETIÇÕES)")
	for music in nome:
		print(music)
	print("------------------------------------")
	print("TOTAL:",len(nome))
	print("***********************************")


	





querie1()
querie2()
querie3()
querie4()

