from abc import ABC, abstractmethod

class Veiculo(ABC):
    
    @classmethod
    @abstractmethod
    def mover(cls):
        pass
    
    @classmethod
    @abstractmethod
    def ligar(cls):
        pass
    
    
    class Carro(Veiculo):
        def mover(self):
            print("O carro esta se movendo")
            
        def ligar(self):
            print("O carro esta ligado")
            
    class Bicicleta(Veiculo):
        def mover(self):
            print("A bicicleta esta se movendo")
            
        
        def ligar(self):
            print("Nao eh possivel ligar uma bicicleta")
            
    
    #testando as implementacoes
    carro = Carro()
    bicicleta = Bicicleta()
    
    print(carro.mover())
    print(carro.ligar())
    
    print(bicicleta.mover())
    print(bicicleta.ligar())