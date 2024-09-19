from Modelos.Restaurante import Restaurante

pizza_express = Restaurante("pizza express", "Pizzas")
Power_burger = Restaurante("Power burger", "lanches")

Power_burger.receber_avaliacao("Anael", 5)
Power_burger.ativar_desativar_restaurante()
Power_burger.receber_avaliacao("Ayla", 4)

import os
from Modelos.Restaurante import Restaurante

def titulo(texto):
    os.system("cls")
    linha = "-" * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def menu():
    print("1. Cadastrar restaurante.")
    print("2. Listar restaurantes.")
    print("3. Ativar / desativar restaurantes.")
    print("4. Avaliar restaurantes.")
    print("5. Sair do programa.\n")

def voltar_ao_menu():
    input("\nDigite qualquer tecla para voltar ao menu: ")
    main()

def opcao_invalida():
    print("Opção inválida.")
    voltar_ao_menu()

def cadastrar_novo_restaurante():
    titulo("Cadastro de novos restaurantes")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite a categoria de {nome_restaurante}:")
    novo_restaurante = Restaurante(nome_restaurante, categoria)
    print(f"Restaurante {nome_restaurante} cadastrado com sucesso.")
    voltar_ao_menu()

def ativar_desativar_restaurante():
    titulo("Ativar / desativar restaurantes")
    nome_restaurante = input("Digite o nome do restaurante para alternar o seu s=estado: ")
    restaurante_encontrado = False
    for restaurante in Restaurante.restaurantes:
        if nome_restaurante == restaurante._nome:
            restaurante_encontrado = True
            restaurante.ativar_desativar_restaurante()
            print(f"Restaurante {restaurante._nome} {restaurante.ativo} com sucesso.")
    if not restaurante_encontrado:
        print(f"O restaurante {nome_restaurante} não está cadastrado.")
    voltar_ao_menu()

def avaliar_restaurante():
    nome_restaurante = input("Digite o nome do restaurante que deseja avaliar:\n")
    restaurante_encontrado = False
    for restaurante in Restaurante.restaurantes:
        if nome_restaurante == restaurante._nome:
            restaurante_encontrado = True
            cliente = input("Digite seu nome de usuário:\n")
            while True:
                try:
                    nota = float(input("Digite uma nota de 0 a 5: "))
                    if 0 <= nota <= 5:
                        restaurante.receber_avaliacao(cliente, nota)
                        print(f"Restaurante {restaurante._nome} avaliado com sucesso.")
                        break
                    else:
                        print("Valor inválido, tente novamente.")
                except ValueError:
                    print("Digite apenas números.")
    if not restaurante_encontrado:
        print(f"O restaurante {nome_restaurante} não está cadastrado.")
    voltar_ao_menu()

def fim_do_programa():
    titulo("Fim do programa")

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção:"))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            Restaurante.listar_restaurantes()
            voltar_ao_menu()
        elif opcao_escolhida == 3:
            ativar_desativar_restaurante()
        elif opcao_escolhida == 4:
            avaliar_restaurante()
        elif opcao_escolhida == 5:
            fim_do_programa()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    titulo("Sabor express")
    menu()
    escolher_opcao()

if __name__ == "__main__":
    main()
