# ------------------------------------------------------------
# TPC1 : Intervalos (definição sintática)
#  + [100,200][3,12]
#  + [-4,-2][1,2][3,5][7,10][12,14][15,19]
#  - [19,15][12,6][-1,-3]
#  - [1000,200][300,12]
# ------------------------------------------------------------
import sys
import ply.yacc as yacc
from intervalos_lex import tokens


def teste_sequencia(sentido, intervalo):
    last = None
    if (sentido=='+'):
        for a,b in intervalo:
            if a>=b or (last!=None and last >= a):
                parser.success = False
                return "Intervalo inválido"
            last = b
        return intervalo
    if (sentido=='-'):
        for a,b in intervalo:
            if a<=b or (last!=None and last <= a):
                parser.success = False
                return "Intervalo inválido"
            last = b
        return intervalo

# The set of syntatic rules
def p_sequencia(p):
    "sequencia : sentido intervalos"
    print(teste_sequencia(p[1],p[2]))

def p_sentidoA(p):
    "sentido : '+'"
    p[0] = p[1]

def p_sentidoD(p):
    "sentido : '-'"
    p[0] = p[1]

def p_intervalos_intervalo(p):
    "intervalos : intervalo"
    p[0] = [p[1]]

def p_intervalos_intervalos(p):
    "intervalos : intervalos intervalo"
    p[0] = p[1]
    p[0].append(p[2])

def p_intervalo(p):
    "intervalo : '[' NUM ',' NUM ']'"
    p[0] = (p[2],p[4])

# Syntatic Error handling rule
def p_error(p):
    print('Syntax error: ', p)
    parser.success = False

# Build the parser
parser = yacc.yacc()

# Start parsing the input text
for line in sys.stdin:
    parser.success = True
    parser.flag = True
    parser.last = 0
    parser.parse(line)
