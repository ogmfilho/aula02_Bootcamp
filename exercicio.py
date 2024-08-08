# 2) Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# 4) Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# 5) Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# 7) Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário
# 13) Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14) Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# 19)Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20)Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# # teste = True
# print(f"teste {5+2}     {7+4}")

# 1- Solicita ao usuário a entrada de uma lista de 4 números
try:
    numero_1 = int(input("Insira o 1o número inteiro: "))
    numero_2 = int(input("Insira o 2o número inteiro: "))
    numero_3 = int(input("Insira o 3o número inteiro: "))
    numero_4 = int(input("Insira o 4o número inteiro: "))
except ValueError:
    print("Insira um número inteiro válido")
# except:
#     print (Exception)
else:
    lista = [numero_1, numero_2, numero_3, numero_4]
    print(lista)

# 2- Converte as strings em inteiros
# 3- Adiciona os inteiros a uma lista