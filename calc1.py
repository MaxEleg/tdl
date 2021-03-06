# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables.
# -----------------------------------------------------------------------------

tokens = (
    'NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE','LPAREN','RPAREN',
    'SEMICOLON','OR','AND','EQUAL','COMP_EQ','COMP_LE','COMP_GR',
    'COMP_DIFF','COMP_EQ_LE','COMP_EQ_GR','IF','ELSE','WHILE','COLON')

# Tokens

names = {}

t_PLUS    = r'+'
t_MINUS   = r'-'
t_TIMES   = r'*'
t_DIVIDE  = r'/'
t_LPAREN  = r'('
t_RPAREN  = r')'
t_OR      = r'||'
t_AND    = r'&&'
tNAME    = r'[a-zA-Z][a-zA-Z0-9_]*'
t_SEMICOLON    = r';'
t_COLON      = r':'
t_EQUAL    = r'='
t_COMP_EQ    = r'=='
t_COMP_LE    = r'<'
t_COMP_GR    = r'>'
t_COMP_DIFF    = r'!='
t_COMP_EQ_LE    = r'<='
t_COMP_EQ_GR    = r'>='
t_IF            = r'if'
t_ELSE          = r'else'
t_WHILE         = r'while'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
# Build the lexer
import ply.lex as lex
lex.lex()

# Precedence rules for the arithmetic operators
precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS')
)

def p_bloc(p):
    '''block : block statement
             | statement'''
    length = len(p)
    if length == 3:
        p[0] = (p[1],p[2])
    elif length == 2:
        p[0] = (p[1], 'empty')

    print(p[0])

def p_while_condition(p):
    '''statement : WHILE statement COLON block'''
    if len(p) == 5:
        p[0] = (t_WHILE, p[2], p[4])

    print(p[0])

def p_if_condition(p):
   '''statement : IF statement COLON block
                | IF statement COLON block ELSE COLON block'''
   if len(p) == 5:
       p[0] = (t_IF, p[2], p[4])
   else:
       p[0] = (t_IF, p[2], p[4], t_ELSE, p[7])

   print(p[0])

def p_statement_expr(p):
    '''statement : expression SEMICOLON
                 | expression'''
    length = len(p)
    p[0] = p[1]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''

    if p[2] == '+'  : p[0] = ('+', p[1], p[3])
    elif p[2] == '-': p[0] = ('-', p[1], p[3])
    elif p[2] == '': p[0] = ('', p[1], p[3])
    elif p[2] == '/': p[0] = ('/', p[1], p[3])

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]
def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_name(p):
    'expression : NAME'
    p[0] = p[1]

def p_expression_affect(p):
    '''statement : NAME EQUAL expression SEMICOLON'''
    if p[2] == '=':
        p[0] = ('=',p[3],p[1])

def p_empty(p):
    '''empty :'''
    pass

def p_expression_bool(p):
    '''statement : statement COMP_EQ expression
                 | statement COMP_LE expression
                 | statement COMP_GR expression
                 | statement COMP_DIFF expression
                 | statement COMP_EQ_GR expression
                 | statement COMP_EQ_LE expression'''
    p[0] = (p[2], p[1], p[3])

def p_error(p):
    print("Syntax error at '%s'" % p.value)
def eval(t):
    if type(t) == tuple:
        op=t[0]
        a=t[1]
        b=t[2]
        print(a, b)
        if op == '+':  return eval(a) + eval(b)
        elif op == '-':  return eval(a) - eval(b)
        elif op == '*':  return eval(a) * eval(b)
        elif op == '/': return eval(a) / eval(b)
        elif op == '==': return eval(a) == eval(b)
        elif op == '<': return eval(a) < eval(b)
        elif op == '>': return eval(a) > eval(b)
        elif op == '!=': return eval(a) != eval(b)
        elif op == '<=': return eval(a) <= eval(b)
        elif op == '>=': return eval(a) >= eval(b)
        elif op == 'while':
            while eval(a):
                return eval(b)
        elif op == 'if':
            if eval(a) == True:
                return eval(a)
            else:
                return eval(b)
        elif op == '=':
            names[a] = eval(b)
            return 0

    else:
        return t

def printTree(t):
    if type(t) == tuple:
        print(t[0])
        print("" + t[0])
        print("" + t[1])

import ply.yacc as yacc
yacc.yacc()

while True:
    try:
        s = input('calc > ')   # use input() on Python 3
    except EOFError:
        break
    yacc.parse(s)