from bd_Questoes.controler import *

def Menu() -> None:
    CarregarDados()
    while True:
        print('-'*40)
        print(maiorScore())
        print('-'*40)
        print('[1] - Iniciar game:')
        print('[2] - Adicionar questoes')
        print('[3] - Listar estatisticas')
        print('[4] - Sair')

        option = int(input('Escolha: '))
        if option == 1:
            iniciar_Game()
        elif option == 2:
            adicionar_Questoes()
        elif option == 3:
            listar_Dados()
        elif option == 4:
            break
        else:
            print('Opção Invalida')

# Iniciar
Menu()
