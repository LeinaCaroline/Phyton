class televisao:
    
    def __init__(self, pcanal, min, max): #Método construtor
        self.canal = pcanal
        self.cmin = min
        self.cmax = max
        
    def muda_canal_para_baixo(self):
        self.canal+=1
        
        
    def muda_canal_para_cima(self):   #Métodos da classe
        self.canal+=1
    
    #Objeto1
    tv1 = televisao(2, 2, 10)
    print(f"Canal sintonizado: ", tv1.canal)
    
    print("Mudando canal para cima: ")
    for x in range(1,20):
        muda_canal_para_cima
        print("canal sintonizado: ", tv1.canal)
        
    #Objeto2
    tv2 = televisao(10,2,20)
    print("canal sintonizado:", tv2.canal)
    
    print("Mudando canal para baixo: ")
    for x in range(1,20):
        muda_canal_para_baixo
        print("canal sintonizado: ", tv2.canal)
            
    