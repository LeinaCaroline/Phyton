usuarios ={
    "leina": "123"
}
    

def fazer_login():
    
    try:
        usuario = input("Digite seu nome de usuario:")
        senha = input("Digite sua senha:")
        
        if usuario in usuarios:
            
            if usuarios[usuario] == senha:
                print("Login bem-sucedido !")
            else:
                print("Senha incorreta !")
        else:
            print("Usuário não encontrado !")
    
    except Exception as erro:
      print(f"Erro : {erro}")
      
      
      
      
fazer_login()
                
    