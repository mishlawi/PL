# calculadora_yacc.py
# 
# Aula 8: 2021-04-20, barata
#
# (5+2) * (3-1)
# 17
# 2-6
#
# Comandos ->  Comandos Comando
#			 | Comando
#
# Comando ->  Ler
#			| Escrever
#			| Despejar
#			| Atribuir
#
# Ler -> '?' id
# Escrever -> '!' exp
# Despejar -> '!!'
# Atribuir -> id = Exp
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

import ply.yacc as yacc
from calc_lex import tokens

def p_Comandos(p):
	"Comandos : Comandos Comando"
	pass

def p_Comandos_single(p):
	"Comandos : Comando"
	pass

def p_Comando(p):
	"""
	Comando : Ler
			| Escrever
			| Despejar
			| Atribuir
	"""
	pass

def p_Exp_add(p):
	" Exp : Exp '+' Termo"
	p[0] = p[1] + p[3]


def p_Exp_sub(p):
	" Exp : Exp '-' Termo"
	p[0] = p[1] - p[3]


def p_Exp_termo(p):
	" Exp : Termo "
	p[0] = p[1]


def p_Termo_mul(p):
	" Termo : Termo '*' Fator"
	p[0] = p[1] * p[3]


def p_Termo_div(p):
	" Termo : Termo '/' Fator"
	if(p[3] != 0):
		p[0] = p[1] / p[3]
	else:
		print("Erro: Divisão por 0, a continuar com 0...")
		p[0] = 0


def p_Termo_fator(p):
	" Termo : Fator"
	p[0] = p[1]


def p_Fator_num(p):
	" Fator : num "
	p[0] = int(p[1])

def p_Fator_id(p):
	" Fator : id "
	p[0] = p.parser.registers.get(p[1])


def p_Fator_group(p):
	" Fator : '(' Exp ')' "
	p[0] = p[2]


def p_Ler(p):
	" Ler : '?' id"
	valor = int(input("Introduza um valor inteiro: "))
	p.parser.registers.update({p[2]: valor})

def p_Escrever(p):
	" Escrever : '!' Exp"
	print(p[2])

def p_Despejar(p):
	" Despejar : '!' '!' "
	print(p.parser.registers)

def p_Atribuir(p):
	" Atribuir : id '=' Exp"
	p.parser.registers.update({p[1]: p[3]})


def p_error(p):
	print('Erro sintático:', p)
	parser.success = False


# build the parser
parser = yacc.yacc()

# my state
parser.registers = {}

# Read line from input and parse it
import sys
for linha in sys.stdin:
	parser.success = True
	result = parser.parse(linha)
	if parser.success:
		print(result)
	else:
		print("Frase inválida... Corrija e tente novamente!")