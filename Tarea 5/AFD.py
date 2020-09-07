import re

regexint = r"([0-9]+)"
regexstr = r"([a-zA-Z]+)"
regexuscore = r"([_]+)"

cadena = '__servidor1' #incorrecta
cadena2 = '3servidor' #incorrecta


def AFP(entrada):
    estado=0

    for i in range(len(entrada)):
        #print(entrada[i])
        if estado == 0:
            match = re.match(regexuscore, entrada[i])
            if match != None:
                estado = 1
            else:
                match = re.match(regexstr, entrada[i])
                if match != None:
                    estado = 2
                else:
                    print("Error: cadena incorrecta")
                    return
        elif estado == 1:
            match = re.match(regexuscore, entrada[i])
            if match != None:
                estado = 1
            else:
                match = re.match(regexstr, entrada[i])
                if match != None:
                    estado = 3
                else:
                    print("Error: cadena incorrecta")
                    return
        elif estado == 2:
            match = re.match(regexstr, entrada[i])
            if match != None:
                estado = 2
            else:
                match = re.match(regexint, entrada[i])
                if match != None:
                    estado = 4
                else:
                    print("Error: cadena incorrecta")
                    return
        elif estado == 3:
            match = re.match(regexint, entrada[i])
            if match !=  None:
                estado = 4
            else:
                print("Error: cadena incorrecta")
                return
    print("Cadena aceptada")

AFP(cadena)
AFP(cadena2)