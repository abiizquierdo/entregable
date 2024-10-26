import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_venta=np.genfromtxt('documentoVentas.csv', delimiter=',', dtype=None, encoding ='utf-8', skip_header=1)
print(data_venta)

precios= data_venta['f3']
cantidades = data_venta['f4']

print("precios:", precios)
print("cantidades :", cantidades)

ingresos=precios*cantidades
total_ingresos=np.sum(ingresos)
print("Ingreso Total:", total_ingresos)


precio_promedio=np.mean(precios)
print("precio promedio:", precio_promedio)

df=pd.read_csv('documentoVentas.csv')
print(df)

estadisticas=df.describe()
print("Estadisticas Descritivas :\ n", estadisticas)

productos_caros = df[df['precios'] > 200]
print("Productos con precios mayor a 200")
print(productos_caros)

ventas_categoria= df['categoria'].value_counts()
print('cantidad de ventas x categoria')
print(ventas_categoria)
