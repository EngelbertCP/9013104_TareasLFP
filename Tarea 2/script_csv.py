import csv 
  
filename = "data_csv.csv"
  
fields = [] 
rows = [] 
  
# Abrimos el archivo csv 
with open(filename, 'r') as csvfile: 
    # Creamos un objeto para lectura 
    csvreader = csv.reader(csvfile) 
      
    # Extraemos los field names 
    fields = next(csvreader) 
  
    # Extraemos cada fila y las agregamos 
    for row in csvreader: 
        rows.append(row)
  
# Imprimimos las primeras 5 filas 
for row in rows[:5]: 
    print(row)