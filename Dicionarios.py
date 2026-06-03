
aluno = {
    "nome": "Leina", "idade": 30
}

print(aluno["nome"])

aluno["curso"] = "Sistemas de Informacao"
aluno["cidade"] = "Sao Luis - MA"
aluno["endereco"] = "Rua Dois"


for chave, valor in aluno.items():
    print(f"{chave}: {valor}")


contatos = {
    "guilherme@gmail.com": {"nome":"Guilherme", "telefone":"3233-1547"},
    "leina@gmail.com": {"nome": "Leina", "telefone": "3223-4586"},
    "laissa@gmail.com": {"nome": "Laissa", "telefone": "3226-2563"}
}

'''for chave in contatos:
    print(chave, contatos[chave]) ====== mesma coisa ========  '''
    

for  chave, valor in contatos.items():
    print(f"{chave}: {valor}")