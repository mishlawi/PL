# abin_lex.py
#
# ()
#(15 () ())
#(40 (20 () ()))
#
#
# T={num, '(',')'}
#
# ABin -> '(' num ABin ABin ')'
#      | '(' ')'

import ply.lex as lex

tokens = ['num'] 	
literals = ['(',')'] #representados em apenas um simbolo 'terminais variaveis'


t_num = r'[+\-]?\d+'

t_ignore = "\t\n"

def t_error(t):
	print('Caracter ilegal: ', t.value[0])
	t.lexer.skip(1)

lex = lex.lex()
