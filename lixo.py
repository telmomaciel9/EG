class MyInterpreter2(Interpreter):
    def __init__(self):
        self.sinal = []
        self.amplitudes = []
        self.first = None
        self.last = None
        self.amplitude = None


    def start(self, tree):
        self.sinal = self.visit(tree.children[0])
        self.visit(tree.children[1])

        self.amplitude = abs(self.last - self.first)


    def sentido(self, tree):
        return tree.children[0].value


    def intervalos(self, tree):
        self.visit_children(tree)


    def intervalo(self, tree):
        if self.first == None:
            self.first = int(tree.children[1].value)

        if self.sinal == '+':
            amplitude = int(tree.children[3]) - int(tree.children[1])

        else:
            amplitude = int(tree.children[1]) - int(tree.children[3])

        self.amplitudes.append(amplitude)
        self.last = int(tree.children[3])