import ply.lex as lex

import sys



#Exercício Nº 6: Palavras, números e número de linha

#Construa um programa em Lex que apresente todas as palavras e números do texto fonte, indicando o número da linha onde se encontram (numa segunda versão indique também em que coluna da linha é iniciada a palavra ou o número).


tokens = (
	'NUMBER',
	'WORD'
	)

t_NUMBER = r'[0-9]+'
t_WORD = r'[A-Za-z]+'


#track nr linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#track coluna 
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

#ignore
def t_tab(t):
	r'\t+'
	pass

t_ignore = " "


def t_error(t):
	print("ERROR:   this is the invalid char: ", t.value[0])
	t.lexer.skip(1)


lexer = lex.lex()




print("Indique o nome do ficheiro a fazer parse:")
ficheiro = input()
ficheiro = open(ficheiro).readlines()

for elem in ficheiro:
	lexer.input(elem)
	for tok in lexer:
		print(tok.type, ":" , tok.value, " linha" , tok.lineno, "coluna" , tok.lexpos)


