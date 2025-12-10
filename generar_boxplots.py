"""
Script para generar boxplots detallados del análisis DBCA
Incluye visualizaciones por factor, bloque e interacciones
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configuración de estilo
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("Set2")

# Cargar datos
try:
    df = pd.read_csv('quinua_simulada_es.csv')
except FileNotFoundError:
    df = pd.read_csv('quinua_simulada.csv')

# Convertir a categóricos
cols_cat = ['Bloque', 'Variedad', 'Fertilizante', 'Riego']
for col in cols_cat:
    df[col] = df[col].astype(str)

print("="*80)
print("GENERACIÓN DE BOXPLOTS DETALLADOS - ANÁLISIS DBCA")
print("="*80)

# Crear figura con múltiples boxplots
fig = plt.figure(figsize=(20, 16))

# ============================================================================
# BOXPLOT 1: Rendimiento por Bloque
# ============================================================================
ax1 = plt.subplot(3, 4, 1)
sns.boxplot(data=df, x='Bloque', y='Rendimiento_kg', palette='Set2', ax=ax1)
ax1.set_title('Rendimiento por Bloque', fontsize=12, fontweight='bold')
ax1.set_xlabel('Bloque', fontsize=10)
ax1.set_ylabel('Rendimiento (kg)', fontsize=10)
ax1.grid(True, alpha=0.3)

# Agregar media
means = df.groupby('Bloque')['Rendimiento_kg'].mean()
for i, (bloque, mean) in enumerate(means.items()):
    ax1.plot(i, mean, marker='D', color='red', markersize=8, label='Media' if i == 0 else '')
ax1.legend()

# ============================================================================
# BOXPLOT 2: Rendimiento por Variedad
# ============================================================================
ax2 = plt.subplot(3, 4, 2)
sns.boxplot(data=df, x='Variedad', y='Rendimiento_kg', palette='Set1', ax=ax2)
ax2.set_title('Rendimiento por Variedad', fontsize=12, fontweight='bold')
ax2.set_xlabel('Variedad', fontsize=10)
ax2.set_ylabel('Rendimiento (kg)', fontsize=10)
ax2.grid(True, alpha=0.3)

# Agregar media
means = df.groupby('Variedad')['Rendimiento_kg'].mean()
for i, (var, mean) in enumerate(means.items()):
    ax2.plot(i, mean, marker='D', color='red', markersize=8)

# ============================================================================
# BOXPLOT 3: Rendimiento por Fertilizante
# ============================================================================
ax3 = plt.subplot(3, 4, 3)
sns.boxplot(data=df, x='Fertilizante', y='Rendimiento_kg', 
            order=['', 'Bajo', 'Alto'], palette='YlOrRd', ax=ax3)
ax3.set_title('Rendimiento por Nivel de Fertilizante', fontsize=12, fontweight='bold')
ax3.set_xlabel('Fertilizante', fontsize=10)
ax3.set_ylabel('Rendimiento (kg)', fontsize=10)
ax3.grid(True, alpha=0.3)

# Agregar media
means = df.groupby('Fertilizante')['Rendimiento_kg'].mean().reindex(['', 'Bajo', 'Alto'])
for i, mean in enumerate(means):
    ax3.plot(i, mean, marker='D', color='darkred', markersize=8)

# ============================================================================
# BOXPLOT 4: Rendimiento por Riego
# ============================================================================
ax4 = plt.subplot(3, 4, 4)
sns.boxplot(data=df, x='Riego', y='Rendimiento_kg', palette='Blues', ax=ax4)
ax4.set_title('Rendimiento por Nivel de Riego', fontsize=12, fontweight='bold')
ax4.set_xlabel('Riego', fontsize=10)
ax4.set_ylabel('Rendimiento (kg)', fontsize=10)
ax4.grid(True, alpha=0.3)

# Agregar media
means = df.groupby('Riego')['Rendimiento_kg'].mean()
for i, (riego, mean) in enumerate(means.items()):
    ax4.plot(i, mean, marker='D', color='darkblue', markersize=8)

# ============================================================================
# BOXPLOT 5: Variedad × Bloque
# ============================================================================
ax5 = plt.subplot(3, 4, 5)
sns.boxplot(data=df, x='Bloque', y='Rendimiento_kg', hue='Variedad', palette='Set1', ax=ax5)
ax5.set_title('Rendimiento: Variedad × Bloque', fontsize=12, fontweight='bold')
ax5.set_xlabel('Bloque', fontsize=10)
ax5.set_ylabel('Rendimiento (kg)', fontsize=10)
ax5.legend(title='Variedad', loc='upper right')
ax5.grid(True, alpha=0.3)

# ============================================================================
# BOXPLOT 6: Fertilizante × Bloque
# ============================================================================
ax6 = plt.subplot(3, 4, 6)
sns.boxplot(data=df, x='Bloque', y='Rendimiento_kg', hue='Fertilizante', 
            hue_order=['', 'Bajo', 'Alto'], palette='YlOrRd', ax=ax6)
ax6.set_title('Rendimiento: Fertilizante × Bloque', fontsize=12, fontweight='bold')
ax6.set_xlabel('Bloque', fontsize=10)
ax6.set_ylabel('Rendimiento (kg)', fontsize=10)
ax6.legend(title='Fertilizante', loc='upper right')
ax6.grid(True, alpha=0.3)

# ============================================================================
# BOXPLOT 7: Riego × Bloque
# ============================================================================
ax7 = plt.subplot(3, 4, 7)
sns.boxplot(data=df, x='Bloque', y='Rendimiento_kg', hue='Riego', palette='Blues', ax=ax7)
ax7.set_title('Rendimiento: Riego × Bloque', fontsize=12, fontweight='bold')
ax7.set_xlabel('Bloque', fontsize=10)
ax7.set_ylabel('Rendimiento (kg)', fontsize=10)
ax7.legend(title='Riego', loc='upper right')
ax7.grid(True, alpha=0.3)

# ============================================================================
# BOXPLOT 8: Variedad × Fertilizante
# ============================================================================
ax8 = plt.subplot(3, 4, 8)
sns.boxplot(data=df, x='Fertilizante', y='Rendimiento_kg', hue='Variedad',
            order=['', 'Bajo', 'Alto'], palette='Set1', ax=ax8)
ax8.set_title('Rendimiento: Variedad × Fertilizante', fontsize=12, fontweight='bold')
ax8.set_xlabel('Fertilizante', fontsize=10)
ax8.set_ylabel('Rendimiento (kg)', fontsize=10)
ax8.legend(title='Variedad', loc='upper right')
ax8.grid(True, alpha=0.3)

# ============================================================================
# BOXPLOT 9: Variedad × Riego
# ============================================================================
ax9 = plt.subplot(3, 4, 9)
sns.boxplot(data=df, x='Riego', y='Rendimiento_kg', hue='Variedad', palette='Set1', ax=ax9)
ax9.set_title('Rendimiento: Variedad × Riego', fontsize=12, fontweight='bold')
ax9.set_xlabel('Riego', fontsize=10)
ax9.set_ylabel('Rendimiento (kg)', fontsize=10)
ax9.legend(title='Variedad', loc='upper right')
ax9.grid(True, alpha=0.3)

# ============================================================================
# BOXPLOT 10: Fertilizante × Riego
# ============================================================================
ax10 = plt.subplot(3, 4, 10)
sns.boxplot(data=df, x='Fertilizante', y='Rendimiento_kg', hue='Riego',
            order=['', 'Bajo', 'Alto'], palette='Blues', ax=ax10)
ax10.set_title('Rendimiento: Fertilizante × Riego', fontsize=12, fontweight='bold')
ax10.set_xlabel('Fertilizante', fontsize=10)
ax10.set_ylabel('Rendimiento (kg)', fontsize=10)
ax10.legend(title='Riego', loc='upper right')
ax10.grid(True, alpha=0.3)

# ============================================================================
# BOXPLOT 11: Todos los Tratamientos
# ============================================================================
ax11 = plt.subplot(3, 4, 11)
df['Tratamiento'] = df['Variedad'] + '-' + df['Fertilizante'].replace('', 'N') + '-' + df['Riego']
tratamientos_ordenados = sorted(df['Tratamiento'].unique())
sns.boxplot(data=df, x='Tratamiento', y='Rendimiento_kg', palette='tab20', ax=ax11)
ax11.set_title('Rendimiento por Tratamiento Completo', fontsize=12, fontweight='bold')
ax11.set_xlabel('Tratamiento', fontsize=8)
ax11.set_ylabel('Rendimiento (kg)', fontsize=10)
ax11.tick_params(axis='x', rotation=90, labelsize=7)
ax11.grid(True, alpha=0.3)

# ============================================================================
# BOXPLOT 12: Violin Plot - Distribución General
# ============================================================================
ax12 = plt.subplot(3, 4, 12)
sns.violinplot(data=df, x='Bloque', y='Rendimiento_kg', palette='Set2', ax=ax12)
ax12.set_title('Distribución de Rendimiento por Bloque\n(Violin Plot)', 
               fontsize=12, fontweight='bold')
ax12.set_xlabel('Bloque', fontsize=10)
ax12.set_ylabel('Rendimiento (kg)', fontsize=10)
ax12.grid(True, alpha=0.3)

# Ajustar layout
plt.tight_layout()

# Guardar figura
plt.savefig('DBCA_boxplots_detallados.png', dpi=300, bbox_inches='tight')
print("\n✓ Boxplots guardados en: DBCA_boxplots_detallados.png")

# ============================================================================
# ESTADÍSTICAS DESCRIPTIVAS POR GRUPO
# ============================================================================
print("\n" + "="*80)
print("ESTADÍSTICAS DESCRIPTIVAS")
print("="*80)

print("\n1. Por Bloque:")
print(df.groupby('Bloque')['Rendimiento_kg'].describe())

print("\n2. Por Variedad:")
print(df.groupby('Variedad')['Rendimiento_kg'].describe())

print("\n3. Por Fertilizante:")
print(df.groupby('Fertilizante')['Rendimiento_kg'].describe())

print("\n4. Por Riego:")
print(df.groupby('Riego')['Rendimiento_kg'].describe())

print("\n5. Por Tratamiento Completo:")
print(df.groupby('Tratamiento')['Rendimiento_kg'].describe())

print("\n" + "="*80)
print("ANÁLISIS DE BOXPLOTS COMPLETADO")
print("="*80)

plt.show()
