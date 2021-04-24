"""


Um número misto é constituído por uma parte inteira e uma fração própria (numerador é inferior ao denominador). Exemplos: 5 3/4, 1 2/3, 100 27/35.

Especifique um processador em lex que responda às seguintes alíneas:

    Sempre que apanhar um número constituído por parte inteira e parte decimal converte-o num número misto. Exemplos dos números a converter: +356.32, -47.989, 3.731;
    Sempre que apanhar uma fração, verifica se esta é imprópria e, em caso afirmativo, converte-a para um número misto. Exemplos de frações impróprias: 10/3, -15/2, +35/25;
    Sempre que apanhar um número misto em que a fração é imprópria assinala o erro e apesenta a forma correta do número em causa;
    Em todas as situações a fração do número misto a ser apresentado deverá estar sempre na sua forma mais reduzida.

"""
import sys
import ply.lex as lex
import re
import math


tokens = ('INT','INTDEC','FRACTION','MISTO')


#track numero inteiro com parte decimal
def t_INTDEC(t):
	r'(\+|\-)?[0-9]+\.[0-9]+'
	signal = ''
	if t.value[0]=='+':
		signal= t.value[0]
	nr = t.value[::-1].find('.')

	decimal = float(t.value) % 1
	inteiro = int(float(t.value) - decimal)
	fraction = signal+ str(int(inteiro)) + ' ' + str(int(decimal*(10**nr))) + '/' + str(10**(nr))  
	t.value = fraction
	return t


#track numero fracionario
def t_FRACTION(t):
	r'(\+|\-)?[0-9]+\/[0-9]+'
	signal = ''
	if t.value[0]=='+':
		signal= t.value[0]
	baixo = int(re.split(r'\/',t.value)[1])
	cima = int(re.split(r'\/',t.value)[0])	
	if baixo<cima:
		val = cima//baixo
		frac = cima-val*baixo
		t.value= signal + (str(val)+' '+str(frac)+'/'+str(baixo))
	return t

#track numero misto
def t_MISTO(t):
	r'(\+|\-)?[0-9]+(\ {1,2})[0-9]+\/[0-9]+'
	signal = ''
	if t.value[0]=='+':
		signal= t.value[0]
	baixo = int(re.split(r'\/',t.value)[1])
	cima = int(re.split(r' ',re.split(r'\/',t.value)[0])[1])
	ant = int(re.split(r' ',re.split(r'\/',t.value)[0])[0])
	if baixo<cima:
		print("Número MISTO com fracao impropria")
		val = cima//baixo
		frac = cima-val*baixo
		ant += val
		t.value=signal +(str(ant)+' '+str(frac)+'/'+str(baixo))
	return t


#define ignore
t_ignore = '\n'

def t_SPACES(t):
	r'\t'
	pass

#define error
def t_error(t):
	print('caracter errado',t.value[0])
	t.lexer.skip(1)

lexer = lex.lex()


for linha in sys.stdin:
	lexer.input(linha)
	for tok in lexer:
		print(tok.type, ":" , tok.value)
