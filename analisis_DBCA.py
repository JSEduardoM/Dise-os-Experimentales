"""
Análisis de Diseño en Bloques Completamente al Azar (DBCA) para datos de Quinua
Autor: Análisis Experimental
Fecha: 2025-12-10
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import warnings
warnings.filterwarnings('ignore')

# Configuración de visualización
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# ============================================================================
# 1. CARGA Y PREPARACIÓN DE DATOS
# ============================================================================

print("="*80)
print("ANÁLISIS DE DISEÑO EN BLOQUES COMPLETAMENTE AL AZAR (DBCA)")
print("Dataset: Quinua Simulada")
print("="*80)

# Cargar datos procesados (español)
try:
    df = pd.read_csv('quinua_simulada_es.csv')
except FileNotFoundError:
    print("Advertencia: No se encontró 'quinua_simulada_es.csv', intentando cargar original.")
    df = pd.read_csv('quinua_simulada.csv')

# Asegurar tipos de datos para evitar errores por mezcla de str/float
cols_cat = ['Bloque', 'Variedad', 'Fertilizante', 'Riego']
for col in cols_cat:
    df[col] = df[col].astype(str)

print("\n1. ESTRUCTURA DE LOS DATOS")
print("-"*80)
print(f"Total de observaciones: {len(df)}")
print(f"\nPrimeras filas:")
print(df.head(10))

print(f"\nDistribución de observaciones por Bloque:")
print(df['Bloque'].value_counts().sort_index())

print(f"\nCaracterísticas de cada Bloque:")
print(df.groupby('Bloque')[['Altitud_m', 'Precipitacion_mm', 'pH_Suelo']].mean())

# ============================================================================
# 2. ANÁLISIS DBCA - EFECTO DE VARIEDAD (CONTROLANDO POR BLOQUES)
# ============================================================================

print("\n\n2. ANÁLISIS DBCA: EFECTO DE VARIEDAD EN RENDIMIENTO")
print("="*80)

# Estadísticas descriptivas por variedad y bloque
print("\nRendimiento medio por Variedad y Bloque:")
tabla_var_bloque = df.pivot_table(values='Rendimiento_kg', 
                                   index='Variedad', 
                                   columns='Bloque', 
                                   aggfunc='mean')
print(tabla_var_bloque)

# Modelo DBCA - Variedad con efecto de Bloque
modelo_var_dbca = ols('Rendimiento_kg ~ C(Bloque) + C(Variedad)', data=df).fit()
anova_var_dbca = anova_lm(modelo_var_dbca, typ=2)

print("\nTabla ANOVA - DBCA (Variedad):")
print(anova_var_dbca)

# (Sección de comparación eliminada para enfoque exclusivo en DBCA)

# ============================================================================
# 3. ANÁLISIS DBCA - EFECTO DE FERTILIZANTE (CONTROLANDO POR BLOQUES)
# ============================================================================

print("\n\n3. ANÁLISIS DBCA: EFECTO DE FERTILIZANTE EN RENDIMIENTO")
print("="*80)

# Estadísticas descriptivas
print("\nRendimiento medio por Fertilizante y Bloque:")
tabla_fert_bloque = df.pivot_table(values='Rendimiento_kg', 
                                    index='Fertilizante', 
                                    columns='Bloque', 
                                    aggfunc='mean')
print(tabla_fert_bloque)

# Modelo DBCA
modelo_fert_dbca = ols('Rendimiento_kg ~ C(Bloque) + C(Fertilizante)', data=df).fit()
anova_fert_dbca = anova_lm(modelo_fert_dbca, typ=2)

print("\nTabla ANOVA - DBCA (Fertilizante):")
print(anova_fert_dbca)

# Prueba de Tukey
tukey_fert = pairwise_tukeyhsd(endog=df['Rendimiento_kg'], 
                                groups=df['Fertilizante'], 
                                alpha=0.05)
print("\nPrueba de Tukey (Comparaciones múltiples - Fertilizante):")
print(tukey_fert)

# ============================================================================
# 4. ANÁLISIS DBCA - EFECTO DE RIEGO (CONTROLANDO POR BLOQUES)
# ============================================================================

print("\n\n4. ANÁLISIS DBCA: EFECTO DE RIEGO EN RENDIMIENTO")
print("="*80)

# Estadísticas descriptivas
print("\nRendimiento medio por Riego y Bloque:")
tabla_riego_bloque = df.pivot_table(values='Rendimiento_kg', 
                                     index='Riego', 
                                     columns='Bloque', 
                                     aggfunc='mean')
print(tabla_riego_bloque)

# Modelo DBCA
modelo_riego_dbca = ols('Rendimiento_kg ~ C(Bloque) + C(Riego)', data=df).fit()
anova_riego_dbca = anova_lm(modelo_riego_dbca, typ=2)

print("\nTabla ANOVA - DBCA (Riego):")
print(anova_riego_dbca)

# Prueba de Tukey
tukey_riego = pairwise_tukeyhsd(endog=df['Rendimiento_kg'], 
                                 groups=df['Riego'], 
                                 alpha=0.05)
print("\nPrueba de Tukey (Comparaciones múltiples - Riego):")
print(tukey_riego)

# ============================================================================
# 5. ANÁLISIS DBCA - MODELO FACTORIAL COMPLETO
# ============================================================================

print("\n\n5. ANÁLISIS DBCA: MODELO FACTORIAL COMPLETO")
print("="*80)

# Modelo factorial con bloques
modelo_factorial_dbca = ols('''Rendimiento_kg ~ C(Bloque) + 
                                C(Variedad) * C(Fertilizante) * C(Riego)''', 
                            data=df).fit()
anova_factorial_dbca = anova_lm(modelo_factorial_dbca, typ=2)

print("\nTabla ANOVA - DBCA Factorial:")
print(anova_factorial_dbca)

print("\nResumen del modelo:")
print(modelo_factorial_dbca.summary())

# ============================================================================
# 6. EVALUACIÓN DEL EFECTO DE BLOQUES
# ============================================================================

print("\n\n6. EVALUACIÓN DEL EFECTO DE BLOQUES")
print("="*80)

# Estadísticas por bloque
print("\nEstadísticas de Rendimiento por Bloque:")
print(df.groupby('Bloque')['Rendimiento_kg'].describe())

# Visualizar diferencias entre bloques
print("\nCaracterísticas ambientales por Bloque:")
caracteristicas_bloques = df.groupby('Bloque')[['Altitud_m', 'Precipitacion_mm', 
                                                  'pH_Suelo', 'Rendimiento_kg']].mean()
print(caracteristicas_bloques)

# Test de significancia del efecto de bloques
p_valor_bloques = anova_factorial_dbca.loc['C(Bloque)', 'PR(>F)']
print(f"\nSignificancia del efecto de Bloques:")
print(f"  p-valor: {p_valor_bloques:.4f}")
print(f"  Conclusión: {'Bloques tienen efecto significativo (p < 0.05)' if p_valor_bloques < 0.05 else 'Bloques NO tienen efecto significativo (p > 0.05)'}")

# ============================================================================
# 7. VERIFICACIÓN DE SUPUESTOS
# ============================================================================

print("\n\n7. VERIFICACIÓN DE SUPUESTOS DEL ANOVA")
print("="*80)

# Residuos
residuos = modelo_factorial_dbca.resid
valores_ajustados = modelo_factorial_dbca.fittedvalues

# Test de normalidad (Shapiro-Wilk)
stat_shapiro, p_shapiro = stats.shapiro(residuos)
print(f"\nTest de Normalidad (Shapiro-Wilk):")
print(f"  Estadístico: {stat_shapiro:.4f}")
print(f"  p-valor: {p_shapiro:.4f}")
print(f"  Conclusión: {'Residuos normales (p > 0.05)' if p_shapiro > 0.05 else 'Residuos NO normales (p < 0.05)'}")

# Test de homogeneidad de varianzas (Levene)
df['Tratamiento'] = df['Variedad'] + '_' + df['Fertilizante'] + '_' + df['Riego']
grupos = [df[df['Tratamiento'] == t]['Rendimiento_kg'].values 
          for t in df['Tratamiento'].unique()]
stat_levene, p_levene = stats.levene(*grupos)
print(f"\nTest de Homogeneidad de Varianzas (Levene):")
print(f"  Estadístico: {stat_levene:.4f}")
print(f"  p-valor: {p_levene:.4f}")
print(f"  Conclusión: {'Varianzas homogéneas (p > 0.05)' if p_levene > 0.05 else 'Varianzas NO homogéneas (p < 0.05)'}")

# Test de aditividad (Tukey)
# Verificar si hay interacción Bloque × Tratamiento
modelo_aditividad = ols('Rendimiento_kg ~ C(Bloque) * C(Tratamiento)', data=df).fit()
anova_aditividad = anova_lm(modelo_aditividad, typ=2)
p_interaccion = anova_aditividad.loc['C(Bloque):C(Tratamiento)', 'PR(>F)']
print(f"\nTest de Aditividad (Interacción Bloque × Tratamiento):")
print(f"  p-valor: {p_interaccion:.4f}")
print(f"  Conclusión: {'Modelo aditivo apropiado (p > 0.05)' if p_interaccion > 0.05 else 'Posible falta de aditividad (p < 0.05)'}")

# ============================================================================
# 8. VISUALIZACIONES
# ============================================================================

print("\n\n8. GENERANDO VISUALIZACIONES...")
print("-"*80)

# Crear figura con múltiples subplots
fig = plt.figure(figsize=(18, 14))

# 8.1 Rendimiento por Bloque
ax1 = plt.subplot(3, 4, 1)
df.boxplot(column='Rendimiento_kg', by='Bloque', ax=ax1)
plt.title('Rendimiento por Bloque')
plt.suptitle('')
plt.xlabel('Bloque')
plt.ylabel('Rendimiento (kg)')

# 8.2 Rendimiento por Variedad (con bloques)
ax2 = plt.subplot(3, 4, 2)
for bloque in df['Bloque'].unique():
    data_bloque = df[df['Bloque'] == bloque]
    medias = data_bloque.groupby('Variedad')['Rendimiento_kg'].mean()
    plt.plot(medias.index, medias.values, marker='o', label=bloque, linewidth=2)
plt.title('Rendimiento por Variedad (por Bloque)')
plt.xlabel('Variedad')
plt.ylabel('Rendimiento medio (kg)')
plt.legend(title='Bloque')
plt.grid(True, alpha=0.3)

# 8.3 Rendimiento por Fertilizante (con bloques)
ax3 = plt.subplot(3, 4, 3)
for bloque in df['Bloque'].unique():
    data_bloque = df[df['Bloque'] == bloque]
    medias = data_bloque.groupby('Fertilizante')['Rendimiento_kg'].mean()
    plt.plot(medias.index, medias.values, marker='o', label=bloque, linewidth=2)
plt.title('Rendimiento por Fertilizante (por Bloque)')
plt.xlabel('Fertilizante')
plt.ylabel('Rendimiento medio (kg)')
plt.legend(title='Bloque')
plt.grid(True, alpha=0.3)

# 8.4 Rendimiento por Riego (con bloques)
ax4 = plt.subplot(3, 4, 4)
for bloque in df['Bloque'].unique():
    data_bloque = df[df['Bloque'] == bloque]
    medias = data_bloque.groupby('Riego')['Rendimiento_kg'].mean()
    plt.plot(medias.index, medias.values, marker='o', label=bloque, linewidth=2)
plt.title('Rendimiento por Riego (por Bloque)')
plt.xlabel('Riego')
plt.ylabel('Rendimiento medio (kg)')
plt.legend(title='Bloque')
plt.grid(True, alpha=0.3)

# 8.5 Heatmap: Variedad × Bloque
ax5 = plt.subplot(3, 4, 5)
pivot_var = df.pivot_table(values='Rendimiento_kg', index='Variedad', 
                            columns='Bloque', aggfunc='mean')
sns.heatmap(pivot_var, annot=True, fmt='.3f', cmap='YlOrRd', ax=ax5)
plt.title('Heatmap: Variedad × Bloque')

# 8.6 Heatmap: Fertilizante × Bloque
ax6 = plt.subplot(3, 4, 6)
pivot_fert = df.pivot_table(values='Rendimiento_kg', index='Fertilizante', 
                             columns='Bloque', aggfunc='mean')
sns.heatmap(pivot_fert, annot=True, fmt='.3f', cmap='YlGnBu', ax=ax6)
plt.title('Heatmap: Fertilizante × Bloque')

# 8.7 Heatmap: Riego × Bloque
ax7 = plt.subplot(3, 4, 7)
pivot_riego = df.pivot_table(values='Rendimiento_kg', index='Riego', 
                              columns='Bloque', aggfunc='mean')
sns.heatmap(pivot_riego, annot=True, fmt='.3f', cmap='PuBuGn', ax=ax7)
plt.title('Heatmap: Riego × Bloque')

# 8.8 Interacción Variedad × Fertilizante
ax8 = plt.subplot(3, 4, 8)
medias_vf = df.groupby(['Variedad', 'Fertilizante'])['Rendimiento_kg'].mean().unstack()
medias_vf.plot(ax=ax8, marker='o', linewidth=2)
plt.title('Interacción Variedad × Fertilizante')
plt.xlabel('Variedad')
plt.ylabel('Rendimiento medio (kg)')
plt.legend(title='Fertilizante')
plt.grid(True, alpha=0.3)

# 8.9 Q-Q Plot
ax9 = plt.subplot(3, 4, 9)
stats.probplot(residuos, dist="norm", plot=ax9)
plt.title('Q-Q Plot (Normalidad)')
plt.grid(True, alpha=0.3)

# 8.10 Residuos vs Valores Ajustados
ax10 = plt.subplot(3, 4, 10)
plt.scatter(valores_ajustados, residuos, alpha=0.6)
plt.axhline(y=0, color='r', linestyle='--', linewidth=2)
plt.title('Residuos vs Valores Ajustados')
plt.xlabel('Valores Ajustados')
plt.ylabel('Residuos')
plt.grid(True, alpha=0.3)

# 8.11 Residuos por Bloque
ax11 = plt.subplot(3, 4, 11)
df_residuos = pd.DataFrame({'Bloque': df['Bloque'], 'Residuos': residuos})
df_residuos.boxplot(column='Residuos', by='Bloque', ax=ax11)
plt.title('Residuos por Bloque')
plt.suptitle('')
plt.xlabel('Bloque')
plt.ylabel('Residuos')

# 8.12 Histograma de residuos
ax12 = plt.subplot(3, 4, 12)
plt.hist(residuos, bins=20, edgecolor='black', alpha=0.7)
plt.title('Histograma de Residuos')
plt.xlabel('Residuos')
plt.ylabel('Frecuencia')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('DBCA_analisis_quinua.png', dpi=300, bbox_inches='tight')
print("✓ Gráficos guardados en: DBCA_analisis_quinua.png")

# ============================================================================
# 9. RESUMEN DE RESULTADOS
# ============================================================================

print("\n\n9. RESUMEN DE RESULTADOS - DBCA")
print("="*80)

print("\nEfecto de Bloques:")
print(f"  p-valor: {anova_factorial_dbca.loc['C(Bloque)', 'PR(>F)']:.4f}")
print(f"  Suma de cuadrados: {anova_factorial_dbca.loc['C(Bloque)', 'sum_sq']:.4f}")

print("\nEfectos principales (p-valores):")
print(f"  - Variedad: p = {anova_factorial_dbca.loc['C(Variedad)', 'PR(>F)']:.4f}")
print(f"  - Fertilizante: p = {anova_factorial_dbca.loc['C(Fertilizante)', 'PR(>F)']:.4f}")
print(f"  - Riego: p = {anova_factorial_dbca.loc['C(Riego)', 'PR(>F)']:.4f}")

print("\nInteracciones (p-valores):")
print(f"  - Variedad × Fertilizante: p = {anova_factorial_dbca.loc['C(Variedad):C(Fertilizante)', 'PR(>F)']:.4f}")
print(f"  - Variedad × Riego: p = {anova_factorial_dbca.loc['C(Variedad):C(Riego)', 'PR(>F)']:.4f}")
print(f"  - Fertilizante × Riego: p = {anova_factorial_dbca.loc['C(Fertilizante):C(Riego)', 'PR(>F)']:.4f}")
print(f"  - Variedad × Fertilizante × Riego: p = {anova_factorial_dbca.loc['C(Variedad):C(Fertilizante):C(Riego)', 'PR(>F)']:.4f}")

print("\nBondad de ajuste:")
print(f"  R² del modelo: {modelo_factorial_dbca.rsquared:.4f}")
print(f"  R² ajustado: {modelo_factorial_dbca.rsquared_adj:.4f}")

print("\n" + "="*80)
print("ANÁLISIS COMPLETADO")
print("="*80)

plt.show()
