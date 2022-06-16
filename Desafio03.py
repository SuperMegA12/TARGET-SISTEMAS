import json


ler_json = open('dados.json')

data = json.load(ler_json)

array = []
for dict_ in data:
    valor = dict_['valor']
    array.append(valor)

array_semO = []
for i in array:
    if i > 0.0:
        array_semO.append(i)


maior_valor = max(array_semO)
menor_valor = min(array_semO)

media = sum(array_semO)/len(array_semO)

print(f'O maior faturamento em um dia foi {maior_valor:.2f}R$ e o menor foi {menor_valor:.2f}R$')

cont = 0
for valores in array_semO:
    if valores > media:
        cont+=1

print(f'Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {cont}')