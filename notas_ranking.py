alunos = []

def cadastrar_aluno():
    nome = input("Digite o nome do aluno")
    try:
        nota = float(input("Nota: "))
    except ValueError:
        print("Nota inválida!")
        return

    alunos.append({
        "nome": nome,
        "nota": nota
    })

    
    def mostrar_ranking():
        
        ranking = sorted(
            alunos,
            key = lambda aluno: aluno["nota"],
            reverse = True
        )
        
        print("======= Ranking dos Alunos =======")
        
        for posição, aluno in enumerate(ranking, start = 1):
            print(f"{posição}º - {aluno["nome"]} - Nota: {aluno["nota"]}")
            
            
while True:
 print("\n1. Cadastrar Aluno")
 print("2. Mostrar Ranking")
 print("3. Sair")
 opcao = input("Escolha uma opção")
 if opcao == "1":
   cadastrar_aluno()
 elif opcao == "2":
    mostrar_ranking()
 elif opcao == "3":
   print("Saindo do programa....")
 break
else:
 print("Opção inválida: Por favor, escolha uma opção válida !") 