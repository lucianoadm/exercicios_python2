# criando uma lista que recebe elementos e valores
# posteriormente mostre qual o maior e menor valor
# e o total de todos os equipamentos
materiais = []
resposta = 'C'
while resposta == 'C':
    equipamentos = [input('Digite o equipamento: '),
                   float(input('Digite o valor:'))]
    materiais.append(equipamentos)
    resposta = input('Digite \'C\'para continuar \'S\' para sair: ').upper()
valores = []
for elemento in materiais:
    valores.append(elemento[1])
if len (valores) > 0:
    print(f'Equipamento mais caro.....: {max(valores)}')
    print(f'Equipamento mais barato...: {min(valores)}')
    print(f'Total de equipamentos.....: {sum(valores)}')

