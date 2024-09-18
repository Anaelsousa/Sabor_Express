import os

restaurantes = [{"nome":"Pizza bar", "categoria":"pizzas", "ativo":False}, {"nome":"Burger King", "categoria":"lanches", "ativo":True}, {"nome":"Power burger", "categoria":"lanches", "ativo":False}]

def exibir_nome_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print("1. Cadastrar restaurantes")
    print("2. Listar restaurantes")
    print("3. Ativar / desativar restaurantes")
    print("4. Sair\n")

def exibir_subtitulo(texto):
    os.system("cls")
    linha = "-" * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu():
    input("\nDigite qualquer tecla para voltar ao menu: ")
    main()

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite a categoria de {nome_restaurante}:")
    novo_restaurante = {"nome":nome_restaurante, "categoria":categoria, "ativo":False}
    restaurantes.append(novo_restaurante)
    print(f"Restaurante {novo_restaurante["nome"]} cadastrado com sucesso.")
    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo("Lista dos restaurantes cadastrados")
    print("Nome do restaurante".ljust(25), "Categoria".ljust(23), "Estatos")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativado" if restaurante["ativo"] else "desativado"
        print(f" - {nome_restaurante.ljust(22)}, {categoria.ljust(22)}, {ativo}")
    voltar_ao_menu()

def ativar_desativar_restaurante():
    exibir_subtitulo("Ativar / desativar restaurantes")
    nome_restaurante = input("Digite o nome do restaurante para alternar o seu s=estado: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            print(f"Restaurante {restaurante["nome"]} {"ativado" if restaurante["ativo"] else "desativado"} com sucesso.")
    if not restaurante_encontrado:
        print(f"O restaurante {nome_restaurante} não está cadastrado.")
    voltar_ao_menu()

def fim_do_programa():
    exibir_subtitulo("Fim do programa")

def opcao_invalida():
    print("Opção inválida.")
    voltar_ao_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção:"))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            ativar_desativar_restaurante()
        elif opcao_escolhida == 4:
            fim_do_programa()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    os.system("cls")
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()

