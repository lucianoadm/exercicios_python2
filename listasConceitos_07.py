# nesse programa criaremos uma lista externa que receberá
# uma lista interna com seus elementos alodos em seus
# respectivos índice

inventario = []
resposta = 'C'
while resposta == 'C':
    materiais = [input('Digite o equipamento: '),
                 float(input('Digite o valor: ')),
                 input('Departamento: ')]
    inventario.append(materiais)
    resposta = input('Digite (C) para continuar (S) para sair: ').upper()
for x in inventario:
    print(f'Equipamento....: {x[0]}')
    print(f'Valor..........: {x[1]}')
    print(f'Departamento...: {x[2]}')
    print()
print('\nPrograma Encerrado!')

