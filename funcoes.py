alunos = []
def cadastrar(alunos):
    try:
        nome = str(input('Nome do aluno: '))
        idade = int(input('Idade: '))
        nota = float(input('Nota: '))
    except ValueError:
        print('Dados inválidos.')
        return
    else:
        aluno = {'nome': nome, 'idade': idade, 'nota': nota}
        alunos.append(aluno)
        print('Aluno cadastrado com sucesso!')

def listar(alunos):
    if len(alunos) == 0:
        print('Nenhum aluno cadastrado.')
        return
    print('\nLISTA DE ALUNOS')
    print(f"{'ID':<4}{'NOME':<15}{'IDADE':<12}{'NOTA':<10}")
    print('-' * 40)
    for i, p in enumerate(alunos, start=1):
        print(f"{i:<2}. {p['nome']:<15} {p['idade']:<12} {p['nota']:<10.2f}")
    print('-' * 40)

def buscar(alunos):
    termo = input('Digite um nome ou parte de um nome: ')
    encontrados = []
    for p in alunos:
        if termo.lower() in p['nome'].lower():
            encontrados.append(p)

    if not encontrados:
        print('Aluno não encontrado.')
    else:
        print(f'\nResultados da busca por {termo}: ')
        print(f"{'ID':<4}{'NOME':<15}{'IDADE':<12}{'NOTA':<10}")
        print('-' * 40)

        for i,item in enumerate(encontrados, start=1):
            print(f"{i:<2}. {item['nome']:<15} {item['idade']:<12} {item['nota']:<10.2f}")
            print('-' * 40)

def remover(alunos):
    if not alunos:
        print('Nenhum aluno para remover.')
        return
    listar(alunos)
    try:
        pos = int(input('Digite o ID do aluno que deseja remover: ')) - 1
        if 0 <= pos < len(alunos):
            aluno_removido = alunos.pop(pos)
            print(f"{aluno_removido['nome']} foi removido com sucesso!")
        else:
            print('ID inválido')
    except ValueError:
        print('Entrada inválida. Escreva somente números.')

def menu():
    print('-' * 30)
    print('SISTEMA DE CADASTRO DE ALUNOS')
    print('1 - Cadastrar aluno')
    print('2 - Listar aluno')
    print('3 - Buscar aluno')
    print('4 - Remover aluno')
    print('0 - Sair')
    print('-' * 30)