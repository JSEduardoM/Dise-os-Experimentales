"""
Script de Verificación de Normativa para Cultivo de Quinua
==========================================================
Este script analiza el dataset traducido 'quinua_simulada_es.csv' para verificar
si los parámetros agronómicos se encuentran dentro de los rangos aceptables
según normativas técnicas referenciales (ej. NTP 205.062, FAO).

Rangos de Referencia Utilizados:
- pH del Suelo: 6.0 - 8.5 (Rango óptimo para quinua)
- Altitud: 2500 - 4500 m.s.n.m. (Quinua de Altiplano)
- Precipitación: > 100mm (Durante periodo vegetativo crítico, asumiendo datos parciales)
- Calidad de Grano: >= 2.5 (En escala estimada de 1-5 para ser aceptable comercialmente)
"""

import pandas as pd
import numpy as np

# Cargar datos traducidos
try:
    df = pd.read_csv('quinua_simulada_es.csv')
except FileNotFoundError:
    print("Error: No se encontró 'quinua_simulada_es.csv'. Ejecute primero 'traducir_datos.py'.")
    exit()

print("="*80)
print("REPORTE DE CUMPLIMIENTO DE NORMATIVA - CULTIVO DE QUINUA")
print("="*80)

# 1. Definición de Límites
LIMS = {
    'pH_Suelo': {'min': 6.0, 'max': 8.5, 'unidad': 'pH'},
    'Altitud_m': {'min': 2500, 'max': 4500, 'unidad': 'msnm'},
    'Dias_Cosecha': {'min': 100, 'max': 180, 'unidad': 'días'},
}

# 2. Verificación por Variable
reporte_general = []

print(f"\nAnalizando {len(df)} registros totales...\n")

for var, limites in LIMS.items():
    min_val = limites['min']
    max_val = limites['max']
    unidad = limites['unidad']
    
    # Identificar fuera de rango
    fuera_rango = df[(df[var] < min_val) | (df[var] > max_val)]
    num_fuera = len(fuera_rango)
    pct_fuera = (num_fuera / len(df)) * 100
    
    status = "CUMPLE" if num_fuera == 0 else "ALERTA"
    
    print(f"[{status}] Variable {var}:")
    print(f"  - Rango normativo: {min_val} - {max_val} {unidad}")
    print(f"  - Rango observado: {df[var].min()} - {df[var].max()} {unidad}")
    if num_fuera > 0:
        print(f"  - Registros fuera de norma: {num_fuera} ({pct_fuera:.1f}%)")
        print(f"  - Indices (IDs): {fuera_rango['ID_Parcela'].head(5).tolist()} ...")
    else:
        print(f"  - Todos los registros cumplen la normativa.")
    print("-" * 60)

# 3. Análisis de Calidad de Grano (Escala 1-5 asumida)
print(f"[ANÁLISIS] Calidad de Grano:")
calidad_media = df['Calidad_Grano'].mean()
print(f"  - Promedio del lote: {calidad_media:.2f}")
con_calidad_baja = df[df['Calidad_Grano'] < 2.5]
if len(con_calidad_baja) > 0:
    print(f"  - Alerta: {len(con_calidad_baja)} parcelas con calidad baja (< 2.5)")
else:
    print(f"  - Excelente: Todas las parcelas tienen calidad aceptable (>= 2.5)")
print("-" * 60)

# 4. Análisis de Rendimiento
print(f"[ANÁLISIS] Rendimiento (kg/parcela estimada o t/ha):")
rend_promedio = df['Rendimiento_kg'].mean()
print(f"  - Promedio: {rend_promedio:.2f}")
if rend_promedio < 1.0:
    print("  - Nota: Rendimiento bajo promedio.")
elif rend_promedio > 5.0:
    print("  - Nota: Rendimiento muy alto (posible error de datos o condición ideal).")
else:
    print("  - Nota: Rendimiento dentro de rangos normales de producción (1-5 t/ha).")

print("\n" + "="*80)
print("FIN DEL REPORTE")
print("="*80)
