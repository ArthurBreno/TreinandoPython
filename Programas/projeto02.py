#Codigo referente a uma simples caixa registradora de uma lanchonete, utilizando funções.

#Lista contendo a relação do número, nome do item e preço do item
listaItens = [[100, 'cachorro quente', 9.00],
              [101, 'Cachorro-Quente Duplo', 11.00],
              [102, 'X-Egg', 12.00],
              [103, 'X-Salada', 13.00],
              [104, 'X-Bacon', 14.00],
              [105, 'X-Tudo', 17.00],
              [200, 'Refrigerante Lata', 5.00],
              [201, 'Chá Gelado', 4.00]]

#Função para verificar se o valor inserido corresponde a algum dos valores dos pedidos, utilzando if elif e else
def checar_pedido(valor):
    if valor == 100:
        return True
    elif valor == 101:
        return True
    elif valor == 102:
        return True
    elif valor == 103:
        return True
    elif valor == 104:
        return True
    elif valor == 105:
        return True
    elif valor == 200:
        return True
    elif valor == 201:
        return True
    else:
        return False
def responder_valor(numero):  # função para retornar o preço correspondente ao item escolhido
    for x in range(0, 8):
        if numero == listaItens[x][0]:
            return listaItens[x][2]
def responder_item(numero):  # função para retornar o nome do item correspondente ao item escolhido
    for x in range(0, 8):
        if numero == listaItens[x][0]:
            return listaItens[x][1]


print('Bem vindo')
print('      '+'-' * 10 + 'LISTA DE ITENS' + 10 * '-')  #estrutura para print da tabela dos itens
print('-' * 50)
print('|   Número   |   Item                 |   Preço  |')
print('|     {}    |   {}      |   {}    |'.format(listaItens[0][0], listaItens[0][1], listaItens[0][2]))
print('|     {}    |   {}|   {}   |'.format(listaItens[1][0], listaItens[1][1], listaItens[1][2]))
print('|     {}    |   {}                |   {}   |'.format(listaItens[2][0], listaItens[2][1], listaItens[2][2]))
print('|     {}    |   {}             |   {}   |'.format(listaItens[3][0], listaItens[3][1], listaItens[3][2]))
print('|     {}    |   {}              |   {}   |'.format(listaItens[4][0], listaItens[4][1], listaItens[4][2]))
print('|     {}    |   {}               |   {}   |'.format(listaItens[5][0], listaItens[5][1], listaItens[5][2]))
print('|     {}    |   {}    |   {}    |'.format(listaItens[6][0], listaItens[6][1], listaItens[6][2]))
print('|     {}    |   {}           |   {}    |'.format(listaItens[7][0], listaItens[7][1], listaItens[7][2]))
print('--------------------------------------------------')
valorTotal = 0
while input('Deseja realizar um novo pedido?\nsim - 1\nnão - 0\n') != '0': #while loop para solicitar varios pedidos
    while True: # while loop para adicionar varios itens ao pedido
        numeroPedido = float(input('digite o número para montar o pedido: ')) # armazenar o numero referente ao pedido
        if checar_pedido(numeroPedido): #checar se o número do pedido é valido
            valorTotal = valorTotal + responder_valor(numeroPedido)  #Adicionar o preço do ultimo pedido ao preço total dos pedidos
            print('Você pediu um {}, custando R$ {:.2f}'.format(responder_item(numeroPedido), responder_valor(numeroPedido)))  #Informar o nome e o preço do item solcitado
            if input('Deseja pedir algo a mais?\nsim - 1\nnão - 0\n') == '0':  #condicional para adicionar mais itens ao pedido ou encerrar o pedido
                break
        else:
            print('Por favor escolha um número correspondete a algum item!')
    print('O valor total do pedido foi de: R$ {:.2f}'.format(valorTotal))  #Print do valor total do pedido
print('Volte sempre :)')







