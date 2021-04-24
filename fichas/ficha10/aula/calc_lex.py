# cal_lex.py
# 
# Aula 8: 2021-04-20
#
# (5+2) * (3-1)
# 17
# 2-6
#
# Exp ->  Exp '+' Termo
#		| Exp '-' Termo
#		| Termo
#
# Termo ->  Termo '*' Fator
#		  | Termo '/' Fator
#		  | Fator
#
# Fator -> '(' Exp ')'
#		  | num
#		  | id
#


import ply.lex as lex


tokens = ['num','id']
literals = ['(',')','+','-','*','/']


t_num = r'\d+'

t_ignore = "\t\n"

def t_error(t):
	print('Caracter ilegal: ', t.value[0])
	t.lexer.skip(1)

lex = lex.lex()
