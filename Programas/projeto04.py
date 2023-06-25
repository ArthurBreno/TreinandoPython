
#Codigo de um estoque de uma bicicletaria, tem as funções de cadastrar uma nova peça, consultar e remover peças, todas armazenadas em um dicionario.

def cadastrar_peca(contador, dicionario_pecas): #função para caddastrar uma nova peça
    while True:  # estrutura de repetição para preenchimento do nome do produto
        nome = input("Nome da peça: ")
        if len(nome) == 0:
            print("O campo nome é obrigatorio, favor preencher.")
        else:
            break
    while True: # estrutura de repetição para preenchimento do fabricante do produto
        fabricante = input("Fabricante da peça: ")
        if len(fabricante) == 0:
            print("O campo Fabricante é obrigatorio é obrigatorio, favor preencher.")
        else:
            break
    while True: # estrutura de repetição para preenchimento do valor do produto
        preco = input("Preço da peça R$ (somente números): ")
        try:
            preco = float(preco)
            break
        except ValueError:
            print("O campo Preço é obrigatorio, e só deve ser preenchido com números (ex: 125.99)")
    lista_temp = list(dicionario_pecas) # lista contendo todos os Ids ja utilizados
    while True:
        contador = contador + 1
        if contador not in lista_temp:  # verificar se o contador atual está presente na lista de Ids
            dicionario_pecas[contador] = {'nome': nome, 'fabricante': fabricante, 'Preço': preco}  # se tiver, encerra o while loop, e adiciona o produto ao dicionario
            break
    print('Peça adicionado com sucesso!')
    return dicionario_pecas


def consultar_peca(dicionario_pecas):
    lista_temp = list(dicionario_pecas)  # construção da lista com os Ids utilizados
    print('1 - Consultar todas as peças, retorna todas as peças cadastradas')
    print('2 - Consultar peças por codigo, retorna a peça referente ao codigo informado')
    print('3 - Consultar peças por fabricante, retorna todas as peças cadastradas com o fabricante informado')
    print('0 - Para retornar ao menu principal')
    while True:  # loop para verificar se é uma resposta valida ou se se encaixa em alguma das opções
        try:
            resp = int(input('Digite sua escolha: '))
            if resp != 1 and resp != 2 and resp != 3 and resp != 0:
                print('Escolha uma das opções acima!')
            else:
                break
        except ValueError:
            print('Digite um número valido!')

    if resp == 1:
        for valor in lista_temp:  # loop para printar dos os produtos cadastrados com seus respectivos IDs
            print('Id: {}'.format(valor))
            print('   Nome: {}'.format(dicionario_pecas[valor]['nome']))
            print('   Fabricante: {}'.format(dicionario_pecas[valor]['fabricante']))
            print('   Preço: R$ {}'.format(dicionario_pecas[valor]['Preço']))
    elif resp == 2:
        checar_resposta = False  # Variavel para verificar se o sistema achou ou não uma peça referente ao codigo digitado
        id_value = 0  # Variavel para armazenar o ID correspondente ao inserido pelo usuario
        while not checar_resposta:
            try:
                resp = int(input('Digite o codigo da peça: '))
                for valor in lista_temp:
                    if resp == valor:
                        id_value = valor
                        checar_resposta = True
                        break
                if not checar_resposta:
                    print('Digite um codigo válido!')
            except ValueError:
                print('Digite um codigo válido!')
        print('o item referente ao codigo informado é: ')  # Printar a peça relativa ao ID digitado
        print('Id: {}'.format(id_value))
        print('   Nome: {}'.format(dicionario_pecas[id_value]['nome']))
        print('   Fabricante: {}'.format(dicionario_pecas[id_value]['fabricante']))
        print('   Preço: {}'.format(dicionario_pecas[id_value]['Preço']))
    elif resp == 3:
        checar_resposta = False
        item_ref_codigo = {}  #dicionario temporario criado para armazenar as peças correspondentes ao fabricante inserido
        while not checar_resposta:
            try:
                resp = input('Digite o fabricante que deseja buscar: ')
                for valor in range(len(lista_temp)):
                    if resp == dicionario_pecas[lista_temp[valor]]['fabricante']:
                        item_ref_codigo.update({lista_temp[valor]: dicionario_pecas[lista_temp[valor]]})  # Adição da peça ao dicionario temporario
                        checar_resposta = True
                if not checar_resposta:
                    print('Não foi encontrado nenhum produto correspondente a esse fabricante.')
            except ValueError:
                print('Digite uma marca válida!')
        print('os itens referente a marca informado é: ')
        lista_temp = list(item_ref_codigo)
        for valor in lista_temp:  # loop para printar o dicionario temporario
            print('Id: {}'.format(valor))
            print('   Nome: {}'.format(item_ref_codigo[valor]['nome']))
            print('   Fabricante: {}'.format(item_ref_codigo[valor]['fabricante']))
            print('   Preço: R$ {}'.format(item_ref_codigo[valor]['Preço']))


def remover_peca(dicionario_pecas):
    lista_temp = list(dicionario_pecas)
    checar_resposta = False
    while not checar_resposta:
        try:
            resp = int(input('Digite o codigo do item que deseja remover: '))
            for valor in range(len(lista_temp)):
                if resp == lista_temp[valor]:
                    del dicionario_pecas[lista_temp[valor]]  # deletar item do dicionario
                    checar_resposta = True
                    break
            if not checar_resposta:
                print('Não foi encontrado nenhum produto correspondente a este codigo.')
        except ValueError:
            print('Digite um codigo valido!')
    print('Peça removida com sucesso!')
    return dicionario_pecas


def main_funccion():  # Função principal
    print('Bem vindo')  # Identificador Pessoal
    print('Bem vindo a bicicletaria')
    print('Oque deseja fazer?')
    dicionario_pecas = {}  # Inicialização do dicionario vazio
    contador = 0
    checar_resposta = False
    while not checar_resposta:
        print('1 - cadastrar nova peça')
        print('2 - Consultar o estoque')
        print('3 - Remover uma peça')
        print('0 - Encerrar o programa')
        while True:  # Loop para verificar se a entrada está correta
            try:
                resp = int(input('Digite sua escolha: '))
                if resp != 1 and resp != 2 and resp != 3 and resp != 0:
                    print('Escolha uma das opções acima!')
                else:
                    break
            except ValueError:
                print('Digite um número valido!')
        if resp == 0:
            checar_resposta = True
        # elif 1 e 3 retornam os dicionarios para ficarem armazenados na função principal, para facilitar export para outros arquivos ou implimentação de interface grafica
        elif resp == 1:
            dicionario_pecas = cadastrar_peca(contador, dicionario_pecas)
        elif resp == 2:
            consultar_peca(dicionario_pecas)
        elif resp == 3:
            dicionario_pecas = remover_peca(dicionario_pecas)


main_funccion()  # Chamado da função principal







