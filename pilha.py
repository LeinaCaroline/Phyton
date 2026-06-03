pilha = ["prato1","prato2","prato3","prato4","prato5","prato6"]

pilha.append("prato7")
pilha.append("prato8")



while pilha:
    usar = pilha.pop()
    print(f"A pessoa lavou o: {usar}")