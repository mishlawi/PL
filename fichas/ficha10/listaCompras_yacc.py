# Lista de compras:
#
# total -> listas --dadas as caracteristicas do input nao adotei esta formulacao
#
# listas -> listas lista  -- nem esta
# 		 |  lista
# 
# lista -> seccoes 

# seccoes -> seccoes seccao
# 		   | seccao
#
# seccao -> 'limpeza' produtos
#			|'frescos'produtos
#			| 'peixe' produtos
#			| 'carne' produtos
#			| 'padaria' produtos
#			| 'etc' produtos
#
#
# produtos -> produtos produto
#           | produto
#
# Produto | num
# 		  | designaçao
#		  | preco
#		  | num
# tendo em conta o seguinte input:
#
# CARNE :
#    - 1 :: Bife :: 10.00 :: 4;
#    - 1 :: Bife :: 10.00 :: 1;
#    - 2 :: Lombo :: 10.00 :: 4;
#    - 2 :: Lombo :: 12.00 :: 1;
#    - 3 :: Figado :: 2.00 :: 1;

# CARNE :
#    - 3 :: Costoleta :: 2.00 :: 1;
#    - 1 :: Bife :: 10.00 :: 7;
#
# PEIXE :
#   - 77 :: Pescada :: 20.00 :: 2;

import ply.yacc as yacc
from listaCompras_lex import tokens
import sys

#production rules:

def p_lista_seccoes(p):
	"lista : seccoes"
	print("Total gasto nas compras:" , p[1], "€")

def p_seccoes(p):
	"seccoes : seccoes seccao"
	p[0] = p[1] + p[2]

def p_seccoes_empty(p):
	"seccoes : "
	p[0] = 0
	
def p_seccao_categoria(p):
	"seccao :  txt ':' produtos"
	p[0] = p[3]


def p_produtos(p):
	"produtos : produtos produto"
	p[0] = p[1] + p[2]

def p_produtos_produto(p):
	"produtos : produto"
	p[0] = p[1]

def p_produto(p):
	"produto : '-' num sep txt sep preco sep num ';'"
	p[0] = p[6] * p[8]

def p_error(p):
    print("erro")
    print(p.type)


parser = yacc.yacc() 

fo = open("../../inputs/listaCompras.txt").read()



parser.parse(fo)