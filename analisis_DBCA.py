"""
Análisis de Diseño en Bloques Completamente al Azar (DBCA) para datos de Quinua
Diseño Optimizado: 5 Réplicas, 60 Unidades Experimentales
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
print("Dataset: Quinua con 5 Réplicas (60 Unidades Experimentales)")
print("="*80)

# Cargar datos (priorizar archivo de 5 réplicas)
try:
    df = pd.read_csv('quinua_5replicas.csv')
    print("\n✓ Datos cargados: quinua_5replicas.csv (5 réplicas, 60 UE)")
except FileNotFoundError:
    try:
        df = pd.read_csv('quinua_simulada_es.csv')
        print("\n✓ Datos cargados: quinua_simulada_es.csv")
    except FileNotFoundError:
        df = pd.read_csv('quinua_simulada.csv')
        print("\n✓ Datos cargados: quinua_simulada.csv")

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
# 8. BOXPLOTS DETALLADOS
# ============================================================================

print("\n\n8. GENERANDO BOXPLOTS DETALLADOS...")
print("-"*80)

# Crear figura para boxplots
fig_boxplots = plt.figure(figsize=(20, 16))

# Función auxiliar para agregar medias a boxplots
def add_means_to_boxplot(ax, data, positions):
    """Agrega puntos de media a un boxplot"""
    means = [np.mean(d) for d in data]
    ax.plot(positions, means, 'D', color='red', markersize=8, 
            markeredgecolor='darkred', markeredgewidth=1.5, 
            label='Media', zorder=3)

# 8.1 Boxplot: Rendimiento por Bloque
ax1 = plt.subplot(3, 4, 1)
bloques_orden = sorted(df['Bloque'].unique())
data_bloques = [df[df['Bloque'] == b]['Rendimiento_kg'].values for b in bloques_orden]
bp1 = ax1.boxplot(data_bloques, labels=bloques_orden, patch_artist=True)
for patch in bp1['boxes']:
    patch.set_facecolor('lightblue')
    patch.set_alpha(0.7)
add_means_to_boxplot(ax1, data_bloques, range(1, len(bloques_orden)+1))
ax1.set_title('Rendimiento por Bloque', fontsize=12, fontweight='bold')
ax1.set_xlabel('Bloque')
ax1.set_ylabel('Rendimiento (kg)')
ax1.grid(True, alpha=0.3)
ax1.legend()

# 8.2 Boxplot: Rendimiento por Variedad
ax2 = plt.subplot(3, 4, 2)
variedades_orden = sorted(df['Variedad'].unique())
data_variedades = [df[df['Variedad'] == v]['Rendimiento_kg'].values for v in variedades_orden]
bp2 = ax2.boxplot(data_variedades, labels=variedades_orden, patch_artist=True)
for patch in bp2['boxes']:
    patch.set_facecolor('lightgreen')
    patch.set_alpha(0.7)
add_means_to_boxplot(ax2, data_variedades, range(1, len(variedades_orden)+1))
ax2.set_title('Rendimiento por Variedad', fontsize=12, fontweight='bold')
ax2.set_xlabel('Variedad')
ax2.set_ylabel('Rendimiento (kg)')
ax2.grid(True, alpha=0.3)
ax2.legend()

# 8.3 Boxplot: Rendimiento por Fertilizante
ax3 = plt.subplot(3, 4, 3)
fertilizantes_orden = sorted(df['Fertilizante'].unique())
data_fertilizantes = [df[df['Fertilizante'] == f]['Rendimiento_kg'].values for f in fertilizantes_orden]
bp3 = ax3.boxplot(data_fertilizantes, labels=fertilizantes_orden, patch_artist=True)
for patch in bp3['boxes']:
    patch.set_facecolor('lightyellow')
    patch.set_alpha(0.7)
add_means_to_boxplot(ax3, data_fertilizantes, range(1, len(fertilizantes_orden)+1))
ax3.set_title('Rendimiento por Fertilizante', fontsize=12, fontweight='bold')
ax3.set_xlabel('Fertilizante')
ax3.set_ylabel('Rendimiento (kg)')
ax3.grid(True, alpha=0.3)
ax3.legend()

# 8.4 Boxplot: Rendimiento por Riego
ax4 = plt.subplot(3, 4, 4)
riegos_orden = sorted(df['Riego'].unique())
data_riegos = [df[df['Riego'] == r]['Rendimiento_kg'].values for r in riegos_orden]
bp4 = ax4.boxplot(data_riegos, labels=riegos_orden, patch_artist=True)
for patch in bp4['boxes']:
    patch.set_facecolor('lightcoral')
    patch.set_alpha(0.7)
add_means_to_boxplot(ax4, data_riegos, range(1, len(riegos_orden)+1))
ax4.set_title('Rendimiento por Riego', fontsize=12, fontweight='bold')
ax4.set_xlabel('Riego')
ax4.set_ylabel('Rendimiento (kg)')
ax4.grid(True, alpha=0.3)
ax4.legend()

# 8.5 Boxplot: Variedad × Bloque
ax5 = plt.subplot(3, 4, 5)
df_grouped = df.groupby(['Variedad', 'Bloque'])['Rendimiento_kg'].apply(list).reset_index()
positions = []
data_to_plot = []
labels = []
pos = 1
for var in variedades_orden:
    for bloque in bloques_orden:
        subset = df[(df['Variedad'] == var) & (df['Bloque'] == bloque)]['Rendimiento_kg'].values
        if len(subset) > 0:
            data_to_plot.append(subset)
            positions.append(pos)
            labels.append(f'{var}\n{bloque}')
            pos += 1
bp5 = ax5.boxplot(data_to_plot, positions=positions, labels=labels, patch_artist=True)
for i, patch in enumerate(bp5['boxes']):
    patch.set_facecolor(['lightblue', 'lightgreen', 'lightyellow'][i % 3])
    patch.set_alpha(0.7)
ax5.set_title('Interacción Variedad × Bloque', fontsize=12, fontweight='bold')
ax5.set_xlabel('Variedad - Bloque')
ax5.set_ylabel('Rendimiento (kg)')
ax5.tick_params(axis='x', rotation=45, labelsize=8)
ax5.grid(True, alpha=0.3)

# 8.6 Boxplot: Fertilizante × Bloque
ax6 = plt.subplot(3, 4, 6)
data_to_plot = []
labels = []
for fert in fertilizantes_orden:
    for bloque in bloques_orden:
        subset = df[(df['Fertilizante'] == fert) & (df['Bloque'] == bloque)]['Rendimiento_kg'].values
        if len(subset) > 0:
            data_to_plot.append(subset)
            labels.append(f'{fert}\n{bloque}')
bp6 = ax6.boxplot(data_to_plot, labels=labels, patch_artist=True)
for i, patch in enumerate(bp6['boxes']):
    patch.set_facecolor(['lightblue', 'lightgreen', 'lightyellow'][i % 3])
    patch.set_alpha(0.7)
ax6.set_title('Interacción Fertilizante × Bloque', fontsize=12, fontweight='bold')
ax6.set_xlabel('Fertilizante - Bloque')
ax6.set_ylabel('Rendimiento (kg)')
ax6.tick_params(axis='x', rotation=45, labelsize=8)
ax6.grid(True, alpha=0.3)

# 8.7 Boxplot: Riego × Bloque
ax7 = plt.subplot(3, 4, 7)
data_to_plot = []
labels = []
for riego in riegos_orden:
    for bloque in bloques_orden:
        subset = df[(df['Riego'] == riego) & (df['Bloque'] == bloque)]['Rendimiento_kg'].values
        if len(subset) > 0:
            data_to_plot.append(subset)
            labels.append(f'{riego}\n{bloque}')
bp7 = ax7.boxplot(data_to_plot, labels=labels, patch_artist=True)
for i, patch in enumerate(bp7['boxes']):
    patch.set_facecolor(['lightblue', 'lightgreen', 'lightyellow'][i % 3])
    patch.set_alpha(0.7)
ax7.set_title('Interacción Riego × Bloque', fontsize=12, fontweight='bold')
ax7.set_xlabel('Riego - Bloque')
ax7.set_ylabel('Rendimiento (kg)')
ax7.tick_params(axis='x', rotation=45, labelsize=8)
ax7.grid(True, alpha=0.3)

# 8.8 Boxplot: Variedad × Fertilizante
ax8 = plt.subplot(3, 4, 8)
data_to_plot = []
labels = []
for var in variedades_orden:
    for fert in fertilizantes_orden:
        subset = df[(df['Variedad'] == var) & (df['Fertilizante'] == fert)]['Rendimiento_kg'].values
        if len(subset) > 0:
            data_to_plot.append(subset)
            labels.append(f'{var}-{fert}')
bp8 = ax8.boxplot(data_to_plot, labels=labels, patch_artist=True)
for i, patch in enumerate(bp8['boxes']):
    patch.set_facecolor(['lightcoral', 'lightblue', 'lightgreen'][i % 3])
    patch.set_alpha(0.7)
ax8.set_title('Interacción Variedad × Fertilizante', fontsize=12, fontweight='bold')
ax8.set_xlabel('Variedad - Fertilizante')
ax8.set_ylabel('Rendimiento (kg)')
ax8.tick_params(axis='x', rotation=45, labelsize=8)
ax8.grid(True, alpha=0.3)

# 8.9 Boxplot: Variedad × Riego
ax9 = plt.subplot(3, 4, 9)
data_to_plot = []
labels = []
for var in variedades_orden:
    for riego in riegos_orden:
        subset = df[(df['Variedad'] == var) & (df['Riego'] == riego)]['Rendimiento_kg'].values
        if len(subset) > 0:
            data_to_plot.append(subset)
            labels.append(f'{var}-{riego}')
bp9 = ax9.boxplot(data_to_plot, labels=labels, patch_artist=True)
for i, patch in enumerate(bp9['boxes']):
    patch.set_facecolor(['lightblue', 'lightgreen', 'lightyellow', 'lightcoral'][i % 4])
    patch.set_alpha(0.7)
ax9.set_title('Interacción Variedad × Riego', fontsize=12, fontweight='bold')
ax9.set_xlabel('Variedad - Riego')
ax9.set_ylabel('Rendimiento (kg)')
ax9.tick_params(axis='x', rotation=45, labelsize=8)
ax9.grid(True, alpha=0.3)

# 8.10 Boxplot: Fertilizante × Riego
ax10 = plt.subplot(3, 4, 10)
data_to_plot = []
labels = []
for fert in fertilizantes_orden:
    for riego in riegos_orden:
        subset = df[(df['Fertilizante'] == fert) & (df['Riego'] == riego)]['Rendimiento_kg'].values
        if len(subset) > 0:
            data_to_plot.append(subset)
            labels.append(f'{fert}-{riego}')
bp10 = ax10.boxplot(data_to_plot, labels=labels, patch_artist=True)
for i, patch in enumerate(bp10['boxes']):
    patch.set_facecolor(['lightblue', 'lightgreen', 'lightyellow', 'lightcoral', 'lightpink', 'lightgray'][i % 6])
    patch.set_alpha(0.7)
ax10.set_title('Interacción Fertilizante × Riego', fontsize=12, fontweight='bold')
ax10.set_xlabel('Fertilizante - Riego')
ax10.set_ylabel('Rendimiento (kg)')
ax10.tick_params(axis='x', rotation=45, labelsize=8)
ax10.grid(True, alpha=0.3)

# 8.11 Boxplot: Todos los Tratamientos
ax11 = plt.subplot(3, 4, 11)
tratamientos_orden = sorted(df['Tratamiento'].unique())
data_tratamientos = [df[df['Tratamiento'] == t]['Rendimiento_kg'].values for t in tratamientos_orden]
bp11 = ax11.boxplot(data_tratamientos, labels=tratamientos_orden, patch_artist=True)
colors = plt.cm.Set3(np.linspace(0, 1, len(tratamientos_orden)))
for i, patch in enumerate(bp11['boxes']):
    patch.set_facecolor(colors[i])
    patch.set_alpha(0.7)
ax11.set_title('Rendimiento por Tratamiento Completo', fontsize=12, fontweight='bold')
ax11.set_xlabel('Tratamiento')
ax11.set_ylabel('Rendimiento (kg)')
ax11.tick_params(axis='x', rotation=90, labelsize=7)
ax11.grid(True, alpha=0.3)

# 8.12 Violin Plot: Distribución por Bloque
ax12 = plt.subplot(3, 4, 12)
parts = ax12.violinplot([df[df['Bloque'] == b]['Rendimiento_kg'].values for b in bloques_orden],
                        positions=range(1, len(bloques_orden)+1),
                        showmeans=True, showmedians=True)
for i, pc in enumerate(parts['bodies']):
    pc.set_facecolor(['lightblue', 'lightgreen', 'lightyellow'][i % 3])
    pc.set_alpha(0.7)
ax12.set_xticks(range(1, len(bloques_orden)+1))
ax12.set_xticklabels(bloques_orden)
ax12.set_title('Distribución por Bloque (Violin Plot)', fontsize=12, fontweight='bold')
ax12.set_xlabel('Bloque')
ax12.set_ylabel('Rendimiento (kg)')
ax12.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('DBCA_boxplots_python.png', dpi=300, bbox_inches='tight')
print("✓ Boxplots guardados en: DBCA_boxplots_python.png")

# ============================================================================
# 9. VISUALIZACIONES DE DIAGNÓSTICO
# ============================================================================

print("\n\n9. GENERANDO VISUALIZACIONES DE DIAGNÓSTICO...")
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
