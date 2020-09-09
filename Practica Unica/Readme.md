# SimpleSQL - Ayuda

SimpleSQL es una aplicaci�n para consola desarrollada en Python que soporta comandos de SQL. No todos. Los que soporta est�n descrito abajo.
No posee un manejador de Base de Datos sino que permite cargar archivos a memoria y sobre ellos realizar consultas, selects, max, min, conteo de registros y un reporte.

# Cargar

Sint�xis: Cargar <archivo1.json>, <archivo2.json>, ...

Abre cada uno de los archivos listados, deben ir separados por comas, verifica que el archivo exista, de lo contrario intenta cargar el siguiente, hasta terminar con la lista de archivos. Al cargar cada archivo emite  un mensaje en consola de que el archivo fue cargado. El formato de los archivos es .JSON y la estructura debe ser esta:
[  
    {  
        "nombre": "registro 1",  
  "edad": 45,  
  "activo": true,  
  "promedio": 56.456  
  },  
  {  
        "nombre": "registro 2",  
  "edad": 35,  
  "activo": false,  
  "promedio": 45.896  
  }  
]


## Seleccionar

Sint�xis: Seleccionar <*>/<atributo> 

Permite seleccionar los registros cargados a memoria listando cada atributo o con un * para mostrar todos los atributos.

## Maximo

Sint�xis: Maximo <edad> / <promedio>

Despliega el mayor  valor del atributo seleccionado de entre todos los registros cargados a memoria.

## Minimo

Sint�xis: Minimo <edad> / <promedio>

Despliega el valor menor del atributo seleccionado de entre todos los registros cargados a memoria.

## Suma

Sint�xis: Suma <edad>/<promedio>

Realiza la suma de los valores del atributo elegido para todos los registros cargados a memoria.

## Cuenta

Sint�xis: Cuenta 

Realiza un conteo de cu�ntos registros fueron cargados a memoria y despliega ese valor.

## Reportar

Sint�xis: Reportar <N>

Crea un reporte HTML y lo abre en el explorador con el n�mero N de registros indicados en el comando.


# Manual T�cnico


Diagr�ma de Flujo del Programa

```mermaid
graph LR
A[Inicio] -- Ingresa Comando --> B((Circle))
A --> C(Round Rect)
B --> D{Rhombus}
C --> D
```