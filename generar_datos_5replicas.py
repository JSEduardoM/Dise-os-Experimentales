"""
Generador de Datos para DBCA con 5 Réplicas y 60 Unidades Experimentales
Diseño: 2 Variedades × 3 Fertilizantes × 2 Riegos = 12 Tratamientos
Con 5 réplicas = 60 unidades experimentales
Distribuidas en 3 bloques (20 parcelas por bloque)
"""

import pandas as pd
import numpy as np

# Configurar semilla para reproducibilidad
np.random.seed(42)

# ============================================================================
# DEFINICIÓN DEL DISEÑO EXPERIMENTAL
# ============================================================================

# Factores
variedades = ['A', 'B']  # 2 niveles
fertilizantes = ['None', 'Low', 'High']  # 3 niveles
riegos = ['Low', 'High']  # 2 niveles
bloques = ['Bloque1', 'Bloque2', 'Bloque3']  # 3 bloques

# Total de tratamientos: 2 × 3 × 2 = 12
# Réplicas por tratamiento: 5
# Total de unidades experimentales: 12 × 5 = 60

# ============================================================================
# GENERACIÓN DE DATOS
# ============================================================================

data = []
plot_id = 1

# Características de cada bloque (diferencias ambientales)
caracteristicas_bloques = {
    'Bloque1': {'altitud': 3800, 'precipitacion': 120, 'ph': 6.8},
    'Bloque2': {'altitud': 3900, 'precipitacion': 90, 'ph': 6.7},
    'Bloque3': {'altitud': 4000, 'precipitacion': 150, 'ph': 6.9}
}

# Generar datos para cada bloque
for bloque in bloques:
    # Características del bloque
    alt_base = caracteristicas_bloques[bloque]['altitud']
    precip_base = caracteristicas_bloques[bloque]['precipitacion']
    ph_base = caracteristicas_bloques[bloque]['ph']
    
    # Efecto del bloque en el rendimiento
    efecto_bloque = {'Bloque1': 0.0, 'Bloque2': 0.1, 'Bloque3': -0.05}[bloque]
    
    # Generar todas las combinaciones de tratamientos
    for variedad in variedades:
        for fertilizante in fertilizantes:
            for riego in riegos:
                # Calcular rendimiento base según tratamiento
                rendimiento_base = 1.5  # kg base
                
                # Efecto de variedad
                if variedad == 'B':
                    rendimiento_base += 0.05
                
                # Efecto de fertilizante
                if fertilizante == 'Low':
                    rendimiento_base += 0.15
                elif fertilizante == 'High':
                    rendimiento_base += 0.35
                
                # Efecto de riego
                if riego == 'High':
                    rendimiento_base += 0.25
                
                # Interacciones
                if variedad == 'A' and fertilizante == 'High':
                    rendimiento_base += 0.1
                if fertilizante == 'High' and riego == 'High':
                    rendimiento_base += 0.15
                
                # Generar 5 réplicas para este tratamiento en este bloque
                # Pero distribuir equitativamente: cada tratamiento aparece ~1.67 veces por bloque
                # Para 60 parcelas en 3 bloques = 20 parcelas/bloque
                # 12 tratamientos, entonces algunos tratamientos tendrán 2 réplicas en un bloque
                # y otros 1 réplica, para balancear
                
                # Estrategia: asignar réplicas de forma balanceada
                # Bloque 1: réplicas 1 y 2 de algunos tratamientos
                # Bloque 2: réplicas 3 y 4 de algunos tratamientos  
                # Bloque 3: réplica 5 de todos los tratamientos
                
                # Para simplificar: cada tratamiento tiene al menos 1 réplica por bloque
                # y algunas tienen 2 réplicas en ciertos bloques
                
                # Determinar número de réplicas en este bloque para este tratamiento
                if bloque == 'Bloque1':
                    num_replicas = 2
                elif bloque == 'Bloque2':
                    num_replicas = 2
                else:  # Bloque3
                    num_replicas = 1
                
                for rep in range(1, num_replicas + 1):
                    # Variación aleatoria
                    variacion = np.random.normal(0, 0.15)
                    
                    # Rendimiento final
                    rendimiento = rendimiento_base + efecto_bloque + variacion
                    rendimiento = max(0.5, rendimiento)  # Mínimo realista
                    
                    # Otras variables
                    altitud = alt_base + np.random.normal(0, 10)
                    precipitacion = precip_base + np.random.normal(0, 10)
                    ph = ph_base + np.random.normal(0, 0.15)
                    densidad = np.random.choice([150, 200, 250])
                    dias_cosecha = int(np.random.normal(122, 4))
                    calidad = max(1.0, min(5.0, np.random.normal(3.2, 0.8)))
                    
                    # Crear registro
                    data.append({
                        'PlotID': f'P{plot_id:03d}',
                        'Bloque': bloque,
                        'Replicacion': rep,
                        'Variedad': variedad,
                        'Fertilizante': fertilizante,
                        'Riego': riego,
                        'Densidad_plants_m2': densidad,
                        'Altitud_m': round(altitud, 1),
                        'Precipitacion_mm': round(precipitacion, 1),
                        'pH_Suelo': round(ph, 2),
                        'Rendimiento_kg': round(rendimiento, 3),
                        'Dias_cosecha': dias_cosecha,
                        'Calidad_grano': round(calidad, 2)
                    })
                    
                    plot_id += 1

# Crear DataFrame
df = pd.DataFrame(data)

# Verificar que tenemos 60 observaciones
print(f"Total de observaciones generadas: {len(df)}")
print(f"\nDistribución por bloque:")
print(df['Bloque'].value_counts().sort_index())
print(f"\nDistribución por tratamiento:")
df['Tratamiento'] = df['Variedad'] + '_' + df['Fertilizante'] + '_' + df['Riego']
print(df['Tratamiento'].value_counts().sort_index())

# Guardar datos
df.to_csv('quinua_5replicas.csv', index=False)
print(f"\n✓ Datos guardados en: quinua_5replicas.csv")
print(f"\nPrimeras filas:")
print(df.head(10))
print(f"\nEstadísticas del rendimiento:")
print(df['Rendimiento_kg'].describe())
