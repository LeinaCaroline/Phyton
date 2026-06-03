'''
numeros = [1,2,3,4,5]

numeros.append(6)#adiciona
numeros.remove(3)

print(numeros[0])
'''

#Exercício: crie uma lista de tarefas e faça um programa que adicione, remova e mostre as tarefas.
tarefas = ["lavar louças","lavar roupas","fazer bolo","passear","supermercado","compar vertido"]

tarefas.append("manicure")
tarefas.remove("lavar roupas")
tarefas.remove("passear")

for i in range(len(tarefas)):
    print(f"Posicao {i}: {tarefas[i]}")

'''print(f"Posicao {3}: {tarefas[3]}")'''
    
    
    
    
letras = list("python")
print(letras)