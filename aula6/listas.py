from lark import Discard
from lark import Lark,Token,Tree
from lark.tree import pydot__tree_to_png
from lark.visitors import Interpreter

class MyInterpreter(Interpreter):
    def __init__(self):
        self.comprimento = 0
        self.soma = 0
        self.isOn = False


    def start(self, tree):
        print("Entrei na Raiz, vou visitar os Elementos")
        r = self.visit(tree.children[1])
        print("Elementos visitados, vou regressar à main()")
        return (self.comprimento, r)

    def elementos(self, tree):
        #print(tree.pretty())
        #print(tree)
        #r = self.visit_children(tree)
        #print(f"visit children : {r}")
        r=0
        for elemento in tree.children:
          print(elemento)
          if (elemento.data == 'elemento' and type(elemento)==Tree):
            print("Este filho adiciono porque é 1 Elemento")
            r += self.visit(elemento)
        return r


    def elemento(self, tree):
        r = self.visit_children(tree)
        print("elemento",r)
        if(r[0].type=='NUMERO' and self.isOn):
            self.comprimento += 1
            return int(r[0])
        if (r[0].lower() == 'agora'):
            self.isOn = True
        if (r[0].lower() == 'fim'):
            self.isOn = False
        return 0

    def vir(self, tree):
      pass


## Primeiro precisamos da GIC
grammar = '''
start: PE elementos PD
elementos : elemento (vir elemento)*
vir : VIR
elemento : NUMERO | PALAVRA |ASPAS
NUMERO:"0".."9"+
ASPAS: ESCAPED_STRING
PALAVRA:("A".."Z"|"a".."z")+
PE:"["
PD:"]"
VIR:","

%import common.WS
%import common.ESCAPED_STRING
%ignore WS
'''

#frase = "[a,1,2,3,a,4]"
#frase = "[10,pala,1,2,3,a,4,outra,\"A\"]"
frase = "[10,pala,1,2,3,agora,1,2,3,4,5,fim,2,2,2,2,2,agora,2,2,2,fim,a,4,outra,\"A\"]"
p = Lark(grammar)
parse_tree = p.parse(frase)

data = MyInterpreter().visit(parse_tree)
print("Número de números ",data[0]," Somatório: ",data[1])