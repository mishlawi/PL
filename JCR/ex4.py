"""


Os Emails escritos à moda PRH caracterizam-se por terem todas as palavras começadas por letras minúsculas, à exceção dos nomes próprios e siglas.

Desenvolva, então:

    um FT que normalize o texto, capitalizando (escrevendo a letra inicial em maiúsculas) todas as palavras no início de cada frase. Além da primeira palavra do texto, uma frase começa depois de um '.', '?' ou '!', seguido de zero ou mais espaços, eventualmente um ou mais fim-de-linha;
    complete a especificação anterior de modo a que o seu normalizador de emails prh conte também todos os nomes próprios (palavras começadas por maiúsculas) e siglas (palavras formadas só por maiúsculas, uma ou mais) encontradas no texto original.

"""

import re

def exercise():
	capitalize = re.compile(r'^[a-z]|\.\s*[a-z]|\!\s*[a-z]|\?\s*[a-z]|\n\s*[a-z]|\n+[a-z]')

	f = open("input/emailPRH.txt").read()
	final = f
	words = re.findall(capitalize,f)
	print(words)
	for elem in words:
		final =re.sub(elem,elem.upper(),final,1)
	print(final)
exercise()