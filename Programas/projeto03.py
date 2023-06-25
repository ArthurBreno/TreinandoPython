#Codigo de um sistema para calculo go custo do frete de cargas tendo base os valores de dimenções, peso e destino.

def dimensoes_objeto():
    while True:
        lista_valores = [0.0, 0.0, 0.0]  # Lista de valores (altura, largura e comprimento) e lista dors nomes para os prints
        lista_nomes = ['altura', 'largura', 'comprimento']
        for x in range(len(lista_nomes)):  # for loop par preencher os valores de altura, largura e comprimento
            while True:  # loop para verificar se o valor numerico é valido, e se o valor é um valor numerico
                try:
                    lista_valores[x] = float(input('Qual a {} do objeto (cm) (somente numeros): '.format(lista_nomes[x])))
                    if lista_valores[x] > 0:
                        break
                    else:
                        print('Valor precisa ser maior que zero!')
                except ValueError:
                    print('Informe um valor numerico, motivo: {}'.format(ValueError))
        volume = lista_valores[0] * lista_valores[1] * lista_valores[2]  # Calculo do volume do item
        if volume < 1000.0:  # Elif para relacionar o valor do volume ao custo do envio ou se o valor exede o limite de tamanho
            res_dimensao = 10.0
            break
        elif 1000.0 <= volume < 10000.0:
            res_dimensao = 20.0
            break
        elif 10000.0 <= volume < 30000.0:
            res_dimensao = 30.0
            break
        elif 30000.0 <= volume < 100000.0:
            res_dimensao = 50.0
            break
        else:
            print('O volume do objeto é: {:.1f} cm3. oque execede o limite máximo de tamanho, por favor Insira novamente os valores.'.format(volume))
    print('O volume do objeto é: {:.1f}'.format(volume))
    return res_dimensao


def peso_objeto():
    while True:
        while True:  # Loop para verificar se valor inserido é numerico, ou se é um valor numerico valido
            try:
                peso = float(input('Qual o peso do objeto (kg) (somente numeros): '))
                if peso > 0:
                    break
                else:
                    print('Valor precisa ser maior que zero!')
            except ValueError:
                print('Informe um valor numerico, motivo: {}'.format(ValueError))
        if peso < 0.1:  # Elif para relacionar o peso ao multiplicador, ou se o valor exedeu o limite máximo de peso
            res_peso = 1
            break
        elif 0.1 <= peso < 1:
            res_peso = 1.5
            break
        elif 1 <= peso < 10:
            res_peso = 2
            break
        elif 10 <= peso < 30:
            res_peso = 3
            break
        else:
            print('O valor execedeu o limite máximo de peso, por favor Insira novamente o valor.')
    return res_peso


def rota_objeto():
    lista_destinos = [['RS', 1],   # Lista contendo a relação entre a sigla das rotas e o multiplicador
                      ['SR', 1],
                      ['BS', 1.2],
                      ['SB', 1.2],
                      ['BR', 1.5],
                      ['RB', 1.5]]
    print('        ------Rotas Disponiveis -------  ')  # print para exebição da sigla das rotas com o nome comleto delas
    print('| Sigla |            Rota               |')
    print('|  RS   |  Rio de Janeiro até São Paulo |')
    print('|  SR   |  São Paulo até Rio de Janeiro |')
    print('|  BS   |  Brasília até São Paulo       |')
    print('|  SB   |  São Paulo até Brasília       |')
    print('|  BR   |  Brasília até Rio de Janeiro  |')
    print('|  RB   |  Rio de Janeiro até Brasília  |')
    multiplicador = 0
    checar_resposta = False
    while not checar_resposta:
        resposta = input('Escolha qual a rota através da sigla: ').upper()  # verificar se o valor inserido é uma das siglas
        for x in range(len(lista_destinos)):
            if lista_destinos[x][0] == resposta:  # verificar se a sigla presente na lista é igual a resposta dada pelo usuario
                multiplicador = lista_destinos[x][1]  # armazena o valor do multiplicador para retorno
                checar_resposta = True
                break
        if not checar_resposta:
            print('Insira uma sigla correspondente a uma das opções!')
    return multiplicador


print('Bem vindo Arthur Breno Rocha Mariano, RU: 4386712')  # Identificador Pessoal
print('Bem vindo a nossa compania logistica!')
print('Para podermos calcular o preço do seu pedido iremos pedir algumas informações ok?')
valor_volume = float(dimensoes_objeto())         # chamar as funções e armazenar seus valores em variaveis para o calculo final
fator_multiplicador_peso = float(peso_objeto())
fator_multiplicador_rota = float(rota_objeto())
valor_final = float(valor_volume * fator_multiplicador_peso * fator_multiplicador_rota)
print('Total a pagar(R$): {:.2f} (volume = {:.0f} * peso = {:.1f} * rota = {:.1f})'      # print do resultado final
      .format(valor_final, valor_volume, fator_multiplicador_peso, fator_multiplicador_rota))
