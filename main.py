# Uma empresa precisa criar um programa para informar quando um funcionário for se aposentar. Crie um programa que leia a idade # e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. As condições para aposentadoria são:
# • 65 anos para os homens e 62 anos para as mulheres, mais 15 anos de contribuição para mulheres e 20 para homens.


print("Olá, seja bem vindo ao programa de aposentadoria!")

sexoPessoa = input("Você é do genero masculino ou feminino? (M/F): ")

if sexoPessoa == "M" or sexoPessoa == "m":
    idadePessoa = int(input("Qual a sua idade? "))
    tempoContribuicao = int(input("Qual o tempo de contribuição? "))
    if idadePessoa >= 65 and tempoContribuicao >= 20:
        print("Você pode se aposentar!")
    else:
        print("Você não pode se aposentar!")
elif sexoPessoa == "F" or sexoPessoa == "f":
    idadePessoa = int(input("Qual a sua idade? "))
    tempoContribuicao = int(input("Qual o tempo de contribuição? "))
    if idadePessoa >= 62 and tempoContribuicao >= 15:
        print("Você pode se aposentar!")
    else:
        print("Você não pode se aposentar!")

else:
    print("Você não digitou uma opção válida!")