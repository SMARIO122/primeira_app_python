import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]


def exibir_nome_do_programa():
    """Esta função é responsável por exibir o nome estilizado do APP"""
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")



def exibir_opcoes():
    """Esta função é responsável por exibir as opções do APP.

    output:
    Lista as opções do APP.
    """

    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')


def finalizar_app():
    """Esta função é responsável por finalizar o APP"""
    exibir_subtitulo('Finalizando APP')


def voltar_ao_menu_principal():
    """Solicita uma tecla para voltar ao menu principal do APP

    Outputs:
    - Retorna ao menu principal
    """
    input('\nDigite uma tecla para voltar ao menu ')
    main()


def opcao_invalida():
    """ Exibe mensagem de opção inválida e retorna ao menu principal

    Outputs:
    - Retorna ao menu principal"""

    print('Opção inválida!\n')
    voltar_ao_menu_principal()


def exibir_subtitulo (texto):
    """Exibe um subtítulo estilizado na tela

       Inputs:
       - texto: str - O texto do subtítulo
       """


    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    """ Essa função é responsável por cadastrar um novo restaurante

    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    """

    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input('Digite o nome da categoria do restaurante: '.format(nome_do_restaurante))
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()


def listar_restaurantes():
    """ Lista os restaurantes presentes na lista

    Outputs:
    - Exibe a lista de restaurantes na tela
    """
    exibir_subtitulo('Listando restaurantes')

    print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print('{} | {} | {}'.format(nome_restaurante.ljust(20), categoria.ljust(20), ativo))

    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    """ Altera o estado ativo/desativado de um restaurante

    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    """

    exibir_subtitulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante[
                'ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')

    voltar_ao_menu_principal()


def escolher_opcao():
    """ Solicita e executa a opção escolhida pelo usuário

    Outputs:
    - Executa a opção escolhida pelo usuário
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    """Esta função é responsável por iniciar e controlar o fluxo principal do APP"""

    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()









