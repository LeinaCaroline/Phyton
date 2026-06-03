estoque = {}  #estoque = Dicionario ???

def adicionar_produto():

    nome = input("Produto: ")
    
    try:
        quantidade = int(input("Quantidade: "))  #está certo ?  chave e valor ? 
    except ValueError:
        print("Digite um número válido! ")
        return
    
    estoque[nome] = quantidade  
    print("Produto adicionado !\n")
    
    
def remover_produto():
    nome = input("Produto: ")
    
    if nome not in estoque:
        print("Produto não encontrado !")
        return
    
    try:
        quantidade = int(input("Quantidade para remover: "))
    except ValueError:
        print("Digite um número válido !")
        return
    
    if quantidade > estoque[nome]:  
        print("Quantidade insuficiente !")
        
    else:
        estoque[nome] -= quantidade
        print("remoção realizada !")
        

def listar_estoque():
    print("========= ESTOQUE =========")
    
    for nome, quantidade in estoque.items():
        print(f"{nome}: {quantidade}")
            
  
  
  
while True:
    print("\n1- Adicionar \n2- Remover \n3- Listar \n 4- Sair")
    
    opcao = int(input("\nEscolha:"))
           
    if opcao == 1:
            adicionar_produto()
    elif opcao == 2:
            remover_produto()
    elif opcao == 3:
            listar_estoque()
    elif opcao == 4:
            break
    else:
     print("Opção inválida !")