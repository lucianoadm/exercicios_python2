# criando múltiplas listas para melhorar o código
# cada elemento terá uma lista específica
# lista do tipo inventário
material = []
valor_unit = []
cod = []
setor = []
resposta = 'C'
while resposta == 'C':
    material.append(input('Digite o material: '))
    valor_unit.append(float(input('Digite o valor unitário: ')))
    cod.append((int(input('Digite o código do material: '))))
    setor.append(input('Digite o setor do produto: '))
    resposta = input('Digita \'s\' para sair \'c\' para continuar: ').upper()

for x in range(len(material)):
    print(f'\nEquipamento....: {x+1}')
    print(f'Material.........: {material[x]}')
    print(f'Valor............: {valor_unit[x]}')
    print(f'Código...........: {cod[x]}')
    print(f'Setor............: {setor[x]}')

