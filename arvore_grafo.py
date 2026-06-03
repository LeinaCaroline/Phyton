class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

raiz = No(10)
raiz.esquerda = No(5)
raiz.direita = No(15)

def pre_ordem(no):
    if no is not None:
        print(no.valor,end=" ") #visita a raiz
        pre_ordem(no.esquerda) #visita o no a esquerda
        pre_ordem(no.direita) #visita o no a direita
        
        
        
pre_ordem(raiz)