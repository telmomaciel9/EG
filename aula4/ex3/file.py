#TURMA A
#ana (12, 13, 15, 12, 13, 15, 14);
#joao (9,7,3,6,9);
#xico (12,16).

#TURMA B
#ana (12, 13, 15, 12, 13, 15, 14);
#joao (9,7,3,6,9,12);
#xico (12,16).

from lark import Lark,Transformer,Discard
from lark.tree import pydot__tree_to_png

grammar = '''
start: turmas
turmas: (turma ".")+
turma: "TURMA" ID alunos+ 
alunos: aluno ( ";" aluno)* 
aluno: NAME "(" notas ")"
notas: NUMBER ("," NUMBER)*

ID: /[A-Z]+/
NAME: /[a-zA-Z_]\w*/

%import common.NUMBER
%import common.WS
%ignore WS

'''

frase= '''

TURMA A
ana (12, 13, 15, 12, 13, 15, 14);
joao (9,7,3,6,9);
xico (12,16).

TURMA B
ana (12, 13, 15, 12, 13, 15, 14);
joao (9,7,3,6,9,12);
xico (12,16).

'''

p = Lark(grammar) # cria um objeto parser

tree = p.parse(frase)  # retorna uma tree

print(tree.pretty())

class TransformerIntervalos(Transformer):
    def __init__(self):
        self.nalunos=0
        self.medias={}
        self.idturma = ""
        self.dicnotas = {}
        self.nomealuno = ""

    def start(self, elementos):
        #print("start", elementos)
        return elementos, self.nalunos, self.medias, self.dicnotas
    
    def turmas(self,turmas):
        print("turmas",turmas)
        return turmas

    def turma(self,turma):
        print("turma",turma)
        return turma
    
    def alunos(self,alunos):
        print("alunos",alunos)
        return alunos

    def aluno(self,aluno):
        print("aluno",aluno)
        self.medias[f"{self.idturma}_{aluno[0]}"]= sum(aluno[1]) / len(aluno[1])
        self.nalunos+=1
        return aluno
  
    def notas(self,notas):
        print("notas",notas)
        return notas

    def NUMBER (self,numero):
        if int(numero) in self.dicnotas:
            self.dicnotas[int(numero)].add(self.nomealuno)
        else:
            self.dicnotas[int(numero)] = set()
        print("NUM",numero)
        return int(numero)

    def ID(self,id):
        self.idturma = id.value
        print("ID",id)
        return id.value
    
    def NAME(self,name):
        self.nomealuno = name.value
        print("NAME",name)
        return name.value
    
    

data, nalunos, medias, dicnotas = TransformerIntervalos().transform(tree)
print(f"Número de alunos : {nalunos}\nMédias: {medias}\nNotas: {dicnotas}")