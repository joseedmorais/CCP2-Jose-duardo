produtos = []

while True:
    print("===============================")
    print("       SISTEMA DE PRODUTOS      ")
    print("1 - Cadastrar produto")
    print("2 - Visualizar produtos")
    print("3 - Finalizar compra")
    print("4 - sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n====== CADASTRO DE PRODUTO ======")

        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade do produto: "))

        produto = {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }

        produtos.append(produto)
        print("\nProduto cadastrado com sucesso!")

    elif opcao == "2":
        if len(produtos) == 0:
            print("\nNenhum produto cadastrado.")   
        else:
            print("====== LISTA DE PRODUTOS ======")
            for produto in produtos:
                print("-------------------------------")
                print(f"Nome: {produto['nome']}")
                print(f"Preço: R${produto['preco']:.2f}")
                print(f"Quantidade: {produto['quantidade']}")
                print("-------------------------------")
    elif opcao == "3":
        if len(produtos) == 0:
            print("\nNenhum produto cadastrado.")
        else:
            total = 0
            print("====== FINALIZAR COMPRA ======")
            for produto in produtos:
                subtotal = produto['preco'] * produto['quantidade']
                total += subtotal
                print("-------------------------------")
                print(f"Nome: {produto['nome']}")
                print(f"Preço: R${produto['preco']:.2f}")
                print(f"Quantidade: {produto['quantidade']}")
                print(f"Subtotal: R${subtotal:.2f}")
                print("-------------------------------")
            print(f"Total da compra: R${total:.2f}")
    elif opcao == "4":
        print("Saindo do sistema...")
        break
    