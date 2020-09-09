# Proyecto: Práctica Única
# Laboratorio de Lenguajes Formales 2S2020
# USAC
# Tutor: Javier Alberto Cabrera
# Engelbert Cárdenas Palacios - Carné: 009013104

import json
import webbrowser
import os

# Bienvenida
print("Conectado a SimpleSQL")

# Ciclo principal
carga = False;
# Inicializa diccionario
#with open('Practica1.json') as file:
#    data = json.load(file)
dataList = []

while True:

    # lee comando
    comando = input("Escriba comando SimpleSQL> ")
    palabras_comando = list(map(str, comando.strip().split()))
    # print(palabras_comando)

    # Considerando palabras_comando como parámetro iterable

    if isinstance(palabras_comando, (list, tuple, set)):
        # print("Línea ingresada, {} is a {}. Tiene los {} elementos.".format(palabras_comando, type(palabras_comando).__name__,len(palabras_comando)))
        for item in palabras_comando:
            # print("The {} contiene '{}' y su lóngitud es {}.".format(type(palabras_comando).__name__, item, len(item)))

            # Para la primer palabra de la línea ingresada

            # Select
            if item.lower() == "select":
                #print("SimpleSQL Select")
                # with open('Practica1.json') as file:
                # data = json.load(file)
                nombresi = False
                edadsi = False
                activosi = False
                promediosi = False
                if not carga:
                    print("No ha cargado datos para consultar")
                else:
                    for item in palabras_comando:
                        campo = item.replace(',', '')
                        if campo.lower() == 'nombre': nombresi = True
                        if campo.lower() == 'edad': edadsi = True
                        if campo.lower() == 'activo': activosi = True
                        if campo.lower() == 'promedio': promediosi = True
                        if campo.lower() == '*':
                            nombresi = True
                            edadsi = True
                            activosi = True
                            promediosi = True
                    for i in dataList:
                        for j in i:
                        #if item.lower() == i[k]:
                        # print('sublista:', i[k])
                            if nombresi: print('nombre: ', j['nombre'])
                            if edadsi: print('edad: ', j['edad'])
                            if activosi: print('activo: ', j['activo'])
                            if promediosi: print('promedio: ', j['promedio'])
                        # print('Nombre:', i['nombre'])
                        #if item.lower() == 'edad':
                        #    for i in dataList:
                        #        for j in i:
                        #            print('edad: ', j['edad'])

            # Cargar
            if item.lower() == "cargar":
                # print("SimpleSQL Cargar")
                carga = True
                for item in palabras_comando:
                    if item.lower() != "cargar":
                        if os.path.exists(item.replace(',', '')):
                            with open(item.replace(',', '')) as file:
                                data = json.load(file)
                                dataList.append(data)
                                # Lista registros cargados
                                #for i in data:
                                #    print('Nombre:', i['nombre'])
                                print ('Comando Carga ejecutado.')
                        else: print("Archivo no existe: ", item.replace(',', ''))
                #print(data)
                #print(dataList)
                break

            # Suma
            if item.lower() == "suma":
                edades = 0
                promedios = 0
                #print("SimpleSQL Suma")
                if not carga:
                    print("No ha cargado datos para consultar")
                else:
                    for item in palabras_comando:
                        for i in dataList:
                            if item.lower() == "edad":
                                k = 0
                                for j in i:
                                    #print('Edad:', i[0]['edad'])
                                    edades = edades + i[k]['edad']
                                    k = k + 1
                                    #print('Suma Edades:', edades)
                        for i in dataList:
                            if item.lower() == "promedio":
                                k = 0
                                for j in i:
                                    promedios = promedios + i[k]['promedio']
                                    k = k + 1
                    if edades !=0: print('Suma Edades:', edades)
                    if promedios !=0: print('Suma Promedios:', promedios)

            # Cuenta
            if item.lower() == "cuenta":
                registros = 0
                #print("SimpleSQL Cuenta")
                if not carga:
                    print("No ha cargado datos para consultar")
                else:
                    for i in dataList:
                        for j in i:
                            registros = registros + 1
                    print('Número de Registros:', registros)

            # Maximo
            if item.lower() == "maximo":
                maximo = 0
                # print("SimpleSQL Maximo")
                if not carga:
                    print("No ha cargado datos para consultar")
                else:
                    for item in palabras_comando:
                        for i in dataList:
                            if item.lower() == "edad":
                                k = 0
                                for j in i:
                                    if i[k]['edad'] > maximo: maximo = i[k]['edad']
                                    k = k + 1
                                    # print('Suma Maximo:', maximo)
                        for i in dataList:
                            if item.lower() == "promedio":
                                k = 0
                                for j in i:
                                    if i[k]['promedio'] > maximo: maximo = i[k]['promedio']
                                    k = k + 1
                    if maximo != 0: print('Maximo:', maximo)

            # Minimo
            if item.lower() == "minimo":
                minimo = 0
                # print("SimpleSQL Minimo")
                if not carga:
                    print("No ha cargado datos para consultar")
                else:
                    for item in palabras_comando:
                        for i in dataList:
                            if item.lower() == "edad":
                                k = 0
                                minimo = i[k]['edad']
                                for j in i:
                                    if i[k]['edad'] < minimo: minimo = i[k]['edad']
                                    k = k + 1
                                    # print('Suma Maximo:', maximo)
                        for i in dataList:
                            if item.lower() == "promedio":
                                k = 0
                                minimo = i[k]['promedio']
                                for j in i:
                                    if i[k]['promedio'] < minimo: minimo = i[k]['promedio']
                                    k = k + 1
                    if minimo != 0: print('Minimo:', minimo)

            # Reportar
            if item.lower() == "reportar":
                N = 0
                for item in palabras_comando:
                    if item.lower() != "reportar":
                        N = int(item.lower())
                    #print("N: ", N)
                #if os.path.exists('reporte.html'):
                #    os.remove('reporte.html')
                #else: print("No se puedo borrar, modo append.")
                #f = open('reporte.html', 'w')

                TABLE = '''
                <!DOCTYPE html>
                <html>
                    <head>
                    </head>
                    <body>
                        <table>
                            <tr>
                                <th>Nombre</th>
                                <th>Edad</th>
                                <th>Activo</th>
                                <th>Promedio</th>
                            </tr>
                %s
                        </table>
                    </body>
                </html>
                '''
                ROW = ' ' * 16 + "<tr><td>%s</td><td>%d</td><td>%e</td><td>%f</td></tr>"
                row_list = []
                reporte = ""
                if N != 0:
                    numregrep = 0
                    for i in dataList:
                        k = 0
                        for j in i:
                            #print("k: ",k)
                            #print("numregrep: ", numregrep)
                            if numregrep < N:
                                row_list = row_list + [ROW % (i[k]['nombre'],i[k]['edad'],i[k]['activo'],i[k]['promedio'])]
                                k = k+1
                                numregrep = numregrep + 1
                                reporte = TABLE % '\n'.join(row_list)

                    if os.path.exists('reporte.html'):
                        os.remove('reporte.html')
                    else: print("No se puedo borrar, modo append.")
                    f = open('reporte.html', 'w')
                    f.write(reporte)
                    f.close()
                    webbrowser.open_new_tab('reporte.html')
# Fin del código.