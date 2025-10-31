import pandas as pd
from funciones import triangulo, rectangulo, circulo

dataFile = pandas.read_csv("figuras.csv")

print("Procesando figuras ... \n")

areas = []
perimetros = []

for index, row in dataFile.iterrows():
	print(f"Fila {index}: FIGURA={row['FIGURA']}, Medida1={row['MEDIDA1']}, Medida2={row['MEDIDA2']}")
