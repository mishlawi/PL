import sys
import ply.lex as lex



#tokenizer para uma maquina de calular
# input: (3-1)*5+8/3
# out : PA NUM SUB NUM PF MUL NUM ADD NUM DIV NUM


tokens = ('PA','PF', 'ADD', 'SUB', 'MUL' , 'DIV', 'NUM')


t_PA = r'\('
t_PF = r'\)'
t_ADD =r'\+'
t_SUB =r'-'
t_MUL =r'\*'
t_DIV = r'\/'

def t_NUM(t):
	r'\d+'
	t.value = int(t.value)
	return t

#tracking line numbers
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

#caracteres a serem ignorados
t_ignore = " \t"

#erros:
def t_error(t):
	print('caracter errado',t.value[0])
	t.lexer.skip(1)

#lexer
lexer = lex.lex()

#input reader
for linha in sys.stdin:
	lexer.input(linha)
	for tok in lexer:
		print(tok)
