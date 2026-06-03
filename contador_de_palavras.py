def analisar_frase(frase):
    palavras = frase.lower().split()
    conjunto_palavras = set(palavras)
    
    print(f"\n Total de palavras: {len(palavras)}")
    print("\n Palavras únicas: ")
    
    for palavra in conjunto_palavras:
        print(palavra)
        
    print(f"\n Quantidade de palavras únicas: {len(conjunto_palavras)}")
    
    
    
texto = input("Digite deu texto aqui: ")
analisar_frase(texto)