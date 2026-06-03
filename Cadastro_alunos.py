def calcular_media(lista_alunos):
    soma=0
    for aluno in lista_alunos:
        soma+=aluno["nota"] #isso está certo?
        
        
    return soma/len(lista_alunos)

alunos=[]


while True:
    nome = input("Nome do aluno: ")
    
    try:
        nota = float(input("Nota: "))
        
    except ValueError:
        print("Digite uma nota válida!")
        continue
    
    
    aluno = {
        "nome": nome,  #dicionário
        "nota": nota
    }
    
    alunos.append(aluno)
    
    continuar = input("Deseja continuar? (s/n)")
    
    if continuar == "n":  #pq lower ?
        break
    
    

print("=========    RESULTADO    ============")

for aluno in alunos:
    print(f'{aluno["nome"]} -> {aluno["nota"]}')
    
media = calcular_media(alunos)

print(f"\n A média de da turma: {media}")

print("Aprovados: ")

for aluno in alunos:
    if aluno["nota"]>=7:
        print(aluno["nome"])
        
        
        
        