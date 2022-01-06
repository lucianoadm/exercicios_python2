lista = []
resposta = 'C'
while resposta != 'S':
    dados = input('\nDigite o produto: ')
    quantidade = int(input('Digite a quantidade: '))
    valor = float(input(f'Digite o valor unitário: '))
    cod = int(input('Digite o código do produto: '))
    resposta = input('Digite \'s\' para sair  \'c\' para continuar: ').upper()
    lista.append([dados, quantidade, valor, cod])
soma = 0
cont = 0
for i in lista:
    cont += 1
    print(f'\nproduto.......: {i[0]}')
    print(f'quantidade    : {i[1]}')
    subtotal = i[1] * i[2]
    print(f'Subtotal......: {round(subtotal,2)}\n')
    soma += subtotal
print(f'Total gasto...: {round(soma,2)}')
