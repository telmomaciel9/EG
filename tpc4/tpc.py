#TPC4: Refazer o exercício Intervalos usando um Interpretador do Lark.
#TPC5: Escrever (em 'papel') uma GA completa (análise semântica + tradução) para o exercício Intervalos Crescentes/Decrescentes

from lark import Lark
from lark.tree import pydot__tree_to_png
from lark import Discard
from lark import Lark,Token,Tree
from lark.visitors import Interpreter

#  + [100,200][3,12]
#  + [-4,-2][1,2][3,5][7,10][12,14][15,19]
#  - [19,15][12,6][-1,-3]
#  - [1000,200][300,12]

class MyInterpreter(Interpreter):
    def __init__(self):
        self.sentido = None # 1 para crescente, -1 para decrescente
        self.last = None
        self.valid = True


    def start(self, tree):
        print("Entrei na Raiz, vou visitar os Elementos")
        if tree.children[0].value == '+':
            self.sentido = 1
        else:
            self.sentido = -1
        r = self.visit(tree.children[1])
        print("Elementos visitados, vou regressar à main()")
        if self.valid:
            print("Lista válida")
        else:
            print("Lista inválida")
        return (r)

    def intervalos(self, tree):
        #print(tree.pretty())
        #print(tree)
        #r = self.visit_children(tree)
        #print(f"visit children : {r}")
        r=0
        for intervalo in tree.children:
          #print(intervalo)
          if (intervalo.data == 'intervalo' and type(intervalo)==Tree):
            #print("Este filho adiciono porque é um intervalo")
            r += self.visit(intervalo)
        return r


    def intervalo(self, tree):
        r = self.visit_children(tree)
        print("intervalo",r)

        if self.sentido == 1:
            if int(r[1]) > int(r[3]):
                self.valid = False
            if self.last != None and int(r[1]) < self.last:
                self.valid = False

        else:
            if int(r[1]) < int(r[3]):
                self.valid = False
            if self.last != None and int(r[1]) > self.last:
                self.valid = False

        self.last = int(r[3])

        return 0
    
    

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

frase = "- [1000,200][300,12]"

p = Lark(grammar) # cria um objeto parser
parse_tree = p.parse(frase)

data = MyInterpreter().visit(parse_tree)
#print(data)