from lark import Lark
from lark.tree import pydot__tree_to_png

#  + [100,200][3,12]
#  + [-4,-2][1,2][3,5][7,10][12,14][15,19]
#  - [19,15][12,6][-1,-3]
#  - [1000,200][300,12]

grammar = '''
// Regras Sintaticas
start: SENTIDO intervalos
intervalos: intervalo (intervalo)*
intervalo: PE NUMERO VIR NUMERO PD

// Regras Lexicográficas
NUMERO: "-"?"0".."9"+ // [0-9]+
PE:"["
PD:"]"
VIR:","
SENTIDO: "+" | "-"

// Tratamento dos espaços em branco
%import common.WS
%ignore WS
'''

frase = "+ [100,200][3,12]"

p = Lark(grammar) # cria um objeto parser

tree = p.parse(frase)  # retorna uma tree
print(tree)
print(tree.pretty())
pydot__tree_to_png(tree,'lark.png')