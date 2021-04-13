# aula6: 2021-04-06, jcr

#

# Somador on/off com condições de contexto

#    - semáforo está on de início

#    - lê do input

#    - reagir a estímulos:

#           r'[oO][nN]' --> ligar o semáforo

#           r'(o|O)(n|N)'

#           r'[oO][fF]{2}' --> desligar o semáforo

#           r'(o|O)(f|F)(f|F)'

#           r'='  --> escrever o valor acumulado

#           r'\d+' --> acrescentar o valor lido ao acumulado se semáforo ligado

#           qq outra coisa --> descartar

import ply.lex as lex

import sys


# Context Conditions declaration

states = (

    ('off', 'inclusive'),

)


# Token declarations

tokens = (

    'ON', 'OFF',

    'PRINT', 'NUM'

)


# Rules for initial state

def t_NUM(t):

    r'\d+'

    t.lexer.soma = t.lexer.soma + int(t.value)


def t_ON(t):

    r'[oO][nN]'

    t.lexer.skip(len(t.value))


def t_OFF(t):

    r'[oO][fF]{2}'

    t.lexer.begin('off')


def t_PRINT(t):

    r'='

    print("soma = ", t.lexer.soma)


# Tracking line numbers

def t_newline(t):

    r'\n+'

    t.lexer.lineno += len(t.value)


# Characters to be ignored

t_ignore = " \t"


# Errors

def t_error(t):

    print("Caráter ilegal: ", t.value[0])

    t.lexer.skip(1)


# Rules for off state

def t_off_ON(t):

    r'[oO][nN]'

    t.lexer.begin('INITIAL')


def t_off_NUMBER(t):

    r'\d+'

    t.lexer.skip(len(t.value))


# build the lexer

lexer = lex.lex()


# My state

lexer.soma = 0


# reading input

for linha in sys.stdin:

    lexer.input(linha)

    for tok in lexer:

        pass