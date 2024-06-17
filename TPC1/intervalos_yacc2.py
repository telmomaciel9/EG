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

def checkaSentido(p1,p2):
    if parser.ordem:
        if p2<p1:

            parser.success = False
    else:
        if p1<p2:

            parser.success = False

def checkAntigo(p):
    if(parser.antigo != None):
        if parser.ordem:
            if parser.antigo >p:

                parser.success = False
        else:
            if parser.antigo < p:

                parser.success = False


# The set of syntatic rules
def p_sequencia(p):
    "sequencia : sentido intervalos"
    if parser.success == False:
        p[0]=[]
        print("Intervals with wrong format")
    else:
        p[0]= p[2]
    

def p_sentidoA(p):
    "sentido : '+'"
    p[0] = 1
    parser.ordem = 1

def p_sentidoD(p):
    "sentido : '-'"
    p[0] = 0
    parser.ordem = 0

def p_intervalos_intervalo(p):
    "intervalos : intervalo"
    p[0] = [p[1]]

def p_intervalos_intervalos(p):
    "intervalos : intervalos intervalo"
    p[0] = p[1]
    p[0].append(p[2])

def p_intervalo(p):
    "intervalo : '[' NUM ',' NUM ']'"
    checkaSentido(p[2],p[4])
    p[0] = (p[2],p[4])
    checkAntigo(p[2])
    parser.antigo = int(p[4])
    

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
    parser.ordem = 1
    parser.antigo= None
    r = parser.parse(line)
    if parser.success == True:
        print(r)
    