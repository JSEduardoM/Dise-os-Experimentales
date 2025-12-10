import pandas as pd
import numpy as np

# Cargar datos originales
df = pd.read_csv('quinua_simulada.csv')

# Diccionarios de traducción
mapa_columnas = {
    'PlotID': 'ID_Parcela',
    'Bloque': 'Bloque',
    'Replicacion': 'Replicacion',
    'Variedad': 'Variedad',
    'Fertilizante': 'Fertilizante',
    'Riego': 'Riego',
    'Densidad_plants_m2': 'Densidad_Plantas_m2',
    'Altitud_m': 'Altitud_m',
    'Lluvia_mm': 'Precipitacion_mm',
    'Soil_pH': 'pH_Suelo',
    'Rendimiento_kg': 'Rendimiento_kg',
    'Dias_cosecha': 'Dias_Cosecha',
    'Calidad_grano': 'Calidad_Grano'
}

mapa_fertilizante = {
    'None': 'Ninguno',
    'Low': 'Bajo',
    'High': 'Alto'
}

mapa_riego = {
    'Low': 'Bajo',
    'High': 'Alto'
}

# Aplicar traducciones
df_es = df.rename(columns=mapa_columnas)
df_es['Fertilizante'] = df_es['Fertilizante'].map(mapa_fertilizante).fillna(df_es['Fertilizante'])
df_es['Riego'] = df_es['Riego'].map(mapa_riego).fillna(df_es['Riego'])

# Guardar nuevo archivo
output_path = 'quinua_simulada_es.csv'
df_es.to_csv(output_path, index=False, encoding='utf-8')

print(f"Archivo traducido guardado en: {output_path}")
print("\nPrimeras filas del dataset traducido:")
print(df_es.head())
