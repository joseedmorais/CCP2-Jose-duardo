alunos = []

while True:
    print("===============================")
    print("       Sistema de notas        ")
    print("1-Cadastrar aluno")
    print("2-Visualizar alunos")
    print("3-Sair")
    opcao = input("Escolha uma opção: ")
    print("===============================")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        n1 = float(input("Digite a nota 1: "))
        n2 = float(input("Digite a nota 2: "))
        media = (n1 + n2) / 2

        if media >= 7:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado"

        aluno = {
            "nome": nome,
            "nota1": n1,
            "nota2": n2,
            "media": media,
            "situacao": situacao,
        }
        alunos.append(aluno)

    elif opcao == "2":
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            print("================================")
            print("       Lista de alunos         ")

            for aluno in alunos:
                print(f"Nome: {aluno['nome']}")
                print(f"Nota 1: {aluno['nota1']}")
                print(f"Nota 2: {aluno['nota2']}")
                print(f"Média: {aluno['media']}")
                print(f"Situação: {aluno['situacao']}")
                print("================================")

    elif opcao == "3":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida.")
    