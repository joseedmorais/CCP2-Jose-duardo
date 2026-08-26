nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 12:
    print("entrada permitida. Bem-vindo(a), " + nome + "!")

else:
    print("entrada não permitida. Desculpe, " + nome + ". Você precisa ter pelo menos 12 anos para entrar.")