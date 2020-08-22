import json

with open('data_json.json') as file:
    data = json.load(file)
    for cliente in data['clientes']:
        print('Nombre:', cliente['nombre'])
        print('Apellido:', cliente['apellido'])
        print('Edad:', cliente['edad'])
        print('Monto:', cliente['monto'])
        print('')