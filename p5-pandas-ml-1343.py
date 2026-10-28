import numpy as np
import pandas as pd
# Daniel Nieves NC=1343
## datos de matriz
datos_alumno=[
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
# poner nombre de los alumnos
# y almacenar la tabla en variable df dataframe
print("--- Datos apartir de una matriz 4 x 3 ---")
df=pd.DataFrame(datos_alumno,columns=['ci','marcas','paquete'])
print (df)
# datos a partir de un diccionario
print("--- datos a partir de un diccionario ---")
alumno_diccionario={
    "nombre":["Daniel","Yahir","Alexia","Iris","Anais","Caleb"],
    "califa":[60,90,100,100,90,80],
    "edad":[16,16,17,17,16,15]
}

estudiantes = pd.DataFrame(alumno_diccionario)
print(estudiantes)

print("Daniel Nieves NC=1343")