# -*- coding: utf-8 -*-
# desarollo de aanalizardor lexico

import ply.lex as lex  # inportacion de librerias necesarias
import re

resultado_lexema = []

tokens = [
    # inicio y final
    #'TAGINICIO', 'TAG_FINAL',

    'IDENTIFICADOR', 'ENTERO', 'ASIGNAR', 'SUMA', 'RESTA', 'MULT', 'DIV', 'POTENCIA', 'MODULO',
    'MINUSMINUS', 'PLUSPLUS','PUNTOYCOMA','PUNTO','COMA','DECIMAL', 'INICIOBLOQUE',
    #'VARIABLE',
    'COMENTARIO', 'SIGNOCOMENTARIO',
    # Condiones
    'SI', 'SINO', 'EN',
    # Ciclos
    'MIENTRAS', 'PARA', 'CADENA',
    # logica
    'AND', 'OR', 'NOT', 'MENORQUE', 'MENORIGUAL', 'MAYORQUE', 'MAYORIGUAL', 'IGUAL', 'DISTINTO',
    # Symbolos
    'PARIZQ', 'PARDER', 'CORIZQ', 'CORDER', 'LLAIZQ', 'LLADER', 'RETURN', 'VOID', 'DEFINIR', 'GLOBAL', 'INTENTAR', 'EXCEPCION' 
]

# Reglas de Expresiones Regualres para token de Contexto simple
#t_PUNTO = r'[+,-]?[[0-9]*[.]]?[0-9]+'
#[+,-]?[[0-9]*[.]]?[0-9]+t__COMA = r'\,'
t_PUNTOYCOMA = r';'
t_SUMA = r'\+'
t_RESTA = r'-'
t_MINUSMINUS = r'\-\-'
#t_PUNTO = r'\.'
t_MULT = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'
t_POTENCIA = r'(\*{2} | \^)'
t_ASIGNAR = r'='
# Expresiones
t_AND = r'\&\&'
t_OR = r'\|{2}'
t_NOT = r'\!'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'{'
t_LLADER = r'}'

def t_GLOBAL(t):
    r'global'
    return t

def t_INICIOBLOQUE(t):
    r':'
    return t

def t_INTENTAR(t):
    r'try'
    return t

def t_EXCEPCION(t):
    r'except'
    return t

def t_DEFINIR(t):
    r'def'
    return t

def t_DECIMAL(t):
    r'([0-9][.]]?[0-9]+)'
    return t

def t_SINO(t):
    r'else'
    return t


def t_SI(t):
    r'if'
    return t

def t_EN(t):
    r'in'
    return t


def t_RETURN(t):
    r'return'
    return t


def t_VOID(t):
    r'void'
    return t


def t_MIENTRAS(t):
    r'while'
    return t


def t_PARA(t):
    r'for'
    return t


def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    return t


def t_CADENA(t):
    r'[\"]+(\w+ \ *\w*\d* \ *)[\"]+'
    return t


def t_SIGNOCOMENTARIO(t):
    r'\#'
    return t

def t_COMENTARIO(t):
    r'[\#][a-z0-9A-Z ]+'

def t_PLUSPLUS(t):
    r'\+\+'
    return t


def t_MENORIGUAL(t):
    r'<='
    return t


def t_MAYORIGUAL(t):
    r'>='
    return t


def t_IGUAL(t):
    r'=='
    return t


def t_MAYORDER(t):
    r'<<'
    return t


def t_MAYORIZQ(t):
    r'>>'
    return t


def t_DISTINTO(t):
    r'!='
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'


def t_error(t):
    global resultado_lexema
    estado = "** Token no valido en la Linea {:4} Valor {:4}".format(str(t.lineno), str(t.value)
                                                                      )
    resultado_lexema.append(estado)
    t.lexer.skip(1)


# Prueba de ingreso

def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)
    while True:
        tok = analizador.token()
        if not tok:
            break
        # print("lexema de "+tok.type+" valor "+tok.value+" linea "tok.lineno)
        estado = "Linea {:4} Tipo {:4} Valor {:4}".format(
            str(tok.lineno), str(tok.type), str(tok.value))
        resultado_lexema.append(estado)

    return resultado_lexema


# abrir archivo
analizador = lex.lex()
path = "doragon.py"

try:
    archivo = open(path, 'r')
except:
    print("el archivo no se encontro")
    quit()

text = ""
for linea in archivo:
    text += linea
prueba(text)
print('\nBienvenido al analizador lexico de python\n')
print('Analizando el archivo "doragon.py"\n\n')
print('\n'.join(list(map(''.join, resultado_lexema)))) #AL IMPRIMIR LOS DATOS, ESTO LO ORDENA DE MANERA ESTRUCTURADA
