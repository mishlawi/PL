# Somador on/off

#    - semáforo está on de início

#    - lê do input

#    - reagir a estímulos:

#           r'[oO][nN]' --> ligar o semáforo

#           r'(o|O)(n|N)'

#           r'[oO][fF]{2}' --> desligar o semáforo

#           r'(o|O)(f|F)(f|F)'

#           r'='  --> escrever o valor acumulado

#           r'\d+' --> acrescentar o valor lido ao acumulado

#           qq outra coisa --> descartar


import ply.lex as lex

import sys



tokens = (

    'ON', 'OFF',

    'PRINT', 'NUM'

)



def t_NUM(t):

    r'\d+'

    if t.lexer.semaforo:

        t.lexer.soma = t.lexer.soma + int(t.value)


def t_ON(t):

    r'[oO][nN]'

    t.lexer.semaforo = True


def t_OFF(t):

    r'[oO][fF]{2}'

    t.lexer.semaforo = False


def t_PRINT(t):

    r'='

    print("soma = ", t.lexer.soma)


# Tracking line numbers

def t_newline(t):

    r'\n+'

    t.lexer.lineno += len(t.value)



t_ignore = " \t"



def t_error(t):

    # print(f"Caráter errado {t.value[0]}")

    t.lexer.skip(1)



lexer = lex.lex()



lexer.soma = 0

lexer.semaforo = True



for linha in sys.stdin:

    lexer.input(linha)

    for tok in lexer:

        print(tok)

