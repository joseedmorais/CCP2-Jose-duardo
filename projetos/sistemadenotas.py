alunos = []

while True:
    print("===============================")
    print("       SISTEMA DE NOTAS        ")
    print("1 - Cadastrar aluno")
    print("2 - Visualizar alunos")
    print("3 - Sair")
    print("===============================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n====== CADASTRO DE ALUNO ======")

        nome = input("Digite o nome do aluno: ")
        n1 = float(input("Digite a nota 1: "))
        n2 = float(input("Digite a nota 2: "))
        n3 = float(input("Digite a nota 3: "))

        media = (n1 + n2 + n3) / 3
        media = round(media, 2)

        if media >= 7:
            situacao = "Aprovado"
        elif media >= 5:
            situacao = "Recuperação"
        else:
            situacao = "Reprovado"

        aluno = {
            "nome": nome,
            "nota1": n1,
            "nota2": n2,
            "nota3": n3,
            "media": media,
            "situacao": situacao
        }

        alunos.append(aluno)

        print("\nAluno cadastrado com sucesso!")
        print(f"Nome: {nome}")
        print(f"Média: {media}")
        print(f"Situação: {situacao}")

    elif opcao == "2":
        print("\n====== LISTA DE ALUNOS ======")

        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")

        else:
            for aluno in alunos:
                print("-------------------------------")
                print(f"Nome: {aluno['nome']}")
                print(f"Nota 1: {aluno['nota1']}")
                print(f"Nota 2: {aluno['nota2']}")
                print(f"Nota 3: {aluno['nota3']}")
                print(f"Média: {aluno['media']}")
                print(f"Situação: {aluno['situacao']}")
            print("-------------------------------")

    elif opcao == "3":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida!")

