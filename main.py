from funcoes import *
from time import sleep

while True:
    menu()
    try:
        opc = int(input('Escolha uma opção: '))
    except (ValueError, TypeError):
        print('Entrada inválida. Digite apenas números.')
        continue

    if opc == 0:
        print('Volte sempre!')
        break
    elif opc == 1:
        cadastrar(alunos)
        sleep(1)
    elif opc == 2:
        listar(alunos)
        sleep(1)
    elif opc == 3:
        buscar(alunos)
        sleep(1)
    elif opc == 4:
        remover(alunos)
        sleep(1)
    else:
        print('Entrada inválida! Tente novamente.')
        break