lista_contatos = [] #lista que vai armazenar os contatos
id_global = 5471923

def cadastrar_contato(id) : #função pra cadastrar os contatos
    print(f'Id do contato {id_global} ')
    nome = input('Digite o nome do contato: ').upper()
    atividade = input('Digite o atividade do contato: ').upper()
    telefone = input('Digite o telefone do contato: ')
    contato = {'id': id, 'nome': nome, 'atividade': atividade, 'telefone': telefone}
    lista_contatos.append(contato.copy()) #copia o dicionario pra lista

def consultar_contato () : #consultar os contatos
   while True:
       print('\n1 - Consultar todos os contatos.')
       print('2 - consultar contato por id.')
       print('3 - consultar contato(s) por atividade.')
       print('4 - retornar')
       opcao = int(input('>>: '))
       if opcao == 1 : #consulta tudo
           for contato in lista_contatos :
               print(f'Id : {contato["id"]}')
               print(f'Nome: {contato["nome"]}')
               print(f'Atividade: {contato["atividade"]}')
               print(f'Telefone: {contato["telefone"]}')
               print('-' * 30)
       elif opcao == 2 : #consulta por id
            id_busca = int(input('Digite o id do contato: '))
            for contato in lista_contatos :
                if contato["id"] == id_busca :
                  print(f'Id : {contato["id"]}')
                  print(f'Nome: {contato["nome"]}')
                  print(f'Atividade: {contato["atividade"]}')
                  print(f'Telefone: {contato["telefone"]}')
                  print('-' * 30)
       elif opcao == 3 : #consulta por atividade
           atividade = (input('Digite atividade do contato: ')).upper()
           for contato in lista_contatos :
               if contato["atividade"] == atividade :
                  print(f'Id : {contato["id"]}')
                  print(f'Nome: {contato["nome"]}')
                  print(f'Atividade: {contato["atividade"]}')
                  print(f'Telefone: {contato["telefone"]}')
                  print('-' * 30)
       elif opcao == 4 :
           return

       else:
           print('opção invalida!')

def remover_contato () : #remove o contato
    while True:
        id_busca = int(input('Buscar id do contato: '))
        for contato in lista_contatos :
            if contato["id"] == id_busca :
                lista_contatos.remove(contato)
                print('contato removido com sucesso!')
                return
        print('id invalido')

print('Bem vindo ao Gerenciamento de contatos do Gustavo Amaral!!')
print('-' * 60)
print('-' * 20 + 'Menu principal' + '-' * 26)
print('-' * 60)
print('Escolha a opção desejada:')
while True:

    print('1 - Cadastrar contato')
    print('2 - consultar contato')
    print('3 - remover contato')
    print('4 - sair')

    opcao = int(input('>>: '))
    if opcao == 1 :
        print('-' * 60)
        print('-' * 20 + 'cadastrar contato' + '-' * 26)
        print('-' * 60)
        cadastrar_contato(id_global)
        id_global += 1
    elif opcao == 2 :
        print('-' * 60)
        print('-' * 20 + 'consultar contato' + '-' * 26)
        print('-' * 60)
        consultar_contato()
    elif opcao == 3 :
        print('-' * 60)
        print('-' * 20 + 'Remover contato' + '-' * 26)
        print('-' * 60)
        remover_contato()
    elif opcao == 4 :
        break
    else:
        print('opçao invalida!')










