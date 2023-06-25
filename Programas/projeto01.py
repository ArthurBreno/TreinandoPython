#Programa com finalidade de calcular o desconto da unidade baseado na quantidade comrpada.

def calcular_desconto(quantidade_produto): #Função para calcular a porcentagem do desconto com base na quantidade
    # Inicio da condicional para evaliar o desconto correto
    if quantidade_produto < 10:
        desconto = 0.00
    elif (quantidade_produto >= 9) and (quantidade_produto <= 99):
        desconto = 0.0
    elif (quantidade_produto >= 100) and (quantidade_produto <= 999):
        desconto = 0.10
    else:
        desconto = 0.15
    # Fim da condicional
    return desconto #a função irá retornar o valor da porcentagem para ser utilizado


print('Bem vindo!')
valorProduto = float(input('Escreva o valor do produto: '))  # receber o valor do produto
quantidadeProduto = int(input('Escreva a quantidade do produto (Somente números): '))  # receber o valor da quantidade do produto
print('-' * 50)  # Divisoria entre o Input e o Output do codigo

# Valor do produto sem desconto, print do desconto garantido com a quantidade adquirida e o valor final do produto após o desconto
print('Valor do produto sem desconto: R$ {:.2f}'.format(valorProduto))
print('desconto garantido com a quantidade: {}%'.format((calcular_desconto(quantidadeProduto)) * 100))
valorProdutoAposDesconto = valorProduto - (calcular_desconto(quantidadeProduto) * valorProduto)
print('Valor final do produto após aplicação do desconto: R$ {:.2f}'.format(valorProdutoAposDesconto))

# Relação entre o valor total com e sem desconto
print('Valor Total sem desconto: R$ {:.2f}'.format(valorProduto * quantidadeProduto))
print('Valor total com desconto: R$ {:.2f}'.format(valorProdutoAposDesconto * quantidadeProduto))




