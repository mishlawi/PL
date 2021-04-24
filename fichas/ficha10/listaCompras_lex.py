import ply.lex as lex

tokens = ['txt', 'preco', 'num','sep']
literals = [';','-',':',',']


#t_codigo = r'([a-zA-Z]+)?\d+' dava problemas (?)

t_txt = r'[A-Za-z]+'

t_sep = r'::'

def t_preco (t):
	r'\d+\.\d+'
	t.value = float(t.value)
	return t

def t_num(t):
	r'\d+'
	t.value = int(t.value)
	return t

#t_ignore only checks literal chars, regex wont work
t_ignore = ' \t\n'

def t_error(t):
	print('Caracter ilegal: ', t.value)
	t.lexer.skip(1)

lexer = lex.lex()