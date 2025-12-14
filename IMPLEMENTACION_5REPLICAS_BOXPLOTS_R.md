# Implementación de Diseño Experimental con 5 Réplicas y 60 Unidades Experimentales

## 📋 Resumen de Cambios Implementados

### Fecha: 10 de Diciembre, 2025

---

## 1. Nuevo Dataset Generado

### Archivo: `quinua_5replicas.csv`

**Características del Diseño:**
- **Réplicas por tratamiento**: 5
- **Total de unidades experimentales**: 60
- **Diseño**: DBCA (Diseño en Bloques Completamente al Azar)
- **Factores**:
  - Variedad: 2 niveles (A, B)
  - Fertilizante: 3 niveles (None, Low, High)
  - Riego: 2 niveles (Low, High)
- **Tratamientos totales**: 2 × 3 × 2 = 12
- **Bloques**: 3 (Bloque1, Bloque2, Bloque3)

**Distribución:**
- Bloque 1: 24 parcelas
- Bloque 2: 24 parcelas
- Bloque 3: 12 parcelas
- **Total**: 60 parcelas (perfectamente balanceado por tratamiento)

**Script de Generación**: `generar_datos_5replicas.py`

---

## 2. Análisis Completo en Python con Boxplots

### Archivo Actualizado: `analisis_DBCA.py`

**Nuevas Características Agregadas:**

#### 2.1 Carga Automática del Nuevo Dataset
- Prioriza `quinua_5replicas.csv`
- Fallback a datasets anteriores si no existe
- Mensaje de confirmación del dataset cargado

#### 2.2 Sección de Boxplots Detallados (12 Visualizaciones)

**Boxplots por Factor Individual:**
1. ✅ Rendimiento por Bloque (con medias marcadas)
2. ✅ Rendimiento por Variedad (con medias marcadas)
3. ✅ Rendimiento por Fertilizante (con medias marcadas)
4. ✅ Rendimiento por Riego (con medias marcadas)

**Boxplots de Interacciones de Dos Factores:**
5. ✅ Variedad × Bloque
6. ✅ Fertilizante × Bloque
7. ✅ Riego × Bloque
8. ✅ Variedad × Fertilizante
9. ✅ Variedad × Riego
10. ✅ Fertilizante × Riego

**Visualizaciones Especiales:**
11. ✅ Todos los Tratamientos Completos (12 combinaciones)
12. ✅ Violin Plot - Distribución por Bloque

**Archivo Generado**: `DBCA_boxplots_python.png` (300 DPI, 20×16 pulgadas)

**Características Visuales:**
- Cajas con colores distintivos por factor
- Puntos rojos (diamantes) marcando las medias
- Transparencia (alpha=0.7) para mejor visualización
- Grillas para facilitar lectura
- Etiquetas rotadas cuando necesario
- Leyendas apropiadas

---

## 3. Traducción Completa a R

### Archivo Completamente Reescrito: `analisis_DBCA.R`

**Contenido Completo (600+ líneas):**

#### 3.1 Estructura del Código R

**Sección 1: Configuración y Carga de Datos**
- Instalación automática de paquetes necesarios
- Carga de librerías: `ggplot2`, `agricolae`, `car`, `gridExtra`, `reshape2`, `dplyr`
- Carga inteligente de datos (prioriza 5 réplicas)
- Conversión a factores

**Sección 2-4: Análisis DBCA por Factor**
- Análisis de Variedad (controlando por bloques)
- Análisis de Fertilizante (controlando por bloques)
- Análisis de Riego (controlando por bloques)
- Tablas ANOVA para cada factor
- Pruebas de Tukey para comparaciones múltiples

**Sección 5: Modelo Factorial Completo**
- ANOVA factorial con todas las interacciones
- Modelo: `Rendimiento_kg ~ Bloque + Variedad * Fertilizante * Riego`
- Resumen completo del modelo
- R² y R² ajustado

**Sección 6: Evaluación del Efecto de Bloques**
- Estadísticas descriptivas por bloque
- Características ambientales por bloque
- Test de significancia del efecto de bloques

**Sección 7: Verificación de Supuestos**
- ✅ Test de Normalidad (Shapiro-Wilk)
- ✅ Test de Homogeneidad de Varianzas (Levene)
- ✅ Test de Aditividad (Interacción Bloque × Tratamiento)
- Interpretación automática de resultados

**Sección 8: Boxplots con ggplot2 (12 Visualizaciones)**
- Todos los boxplots del análisis Python
- Uso de `ggplot2` para gráficos de alta calidad
- Medias marcadas con puntos rojos
- Colores distintivos y transparencia
- Archivo generado: `DBCA_boxplots_R.png` (300 DPI)

**Sección 9: Gráficos de Diagnóstico (12 Visualizaciones)**
- Perfiles de interacción con bloques
- Heatmaps de interacciones (usando `fields`)
- Q-Q Plot para normalidad
- Residuos vs Valores Ajustados
- Residuos por Bloque
- Histograma de residuos
- Scale-Location Plot
- Archivo generado: `DBCA_diagnosticos_R.png` (300 DPI)

**Sección 10: Resumen de Resultados**
- Tabla completa de p-valores
- Efectos principales e interacciones
- Bondad de ajuste (R², R² ajustado)
- Conclusiones automáticas

---

## 4. Archivos Generados

### Scripts
1. ✅ `generar_datos_5replicas.py` - Generador del nuevo dataset
2. ✅ `analisis_DBCA.py` - Análisis Python actualizado con boxplots
3. ✅ `analisis_DBCA.R` - Traducción completa a R (600+ líneas)

### Datos
4. ✅ `quinua_5replicas.csv` - Dataset con 5 réplicas y 60 UE

### Visualizaciones (generadas al ejecutar)
5. `DBCA_boxplots_python.png` - 12 boxplots desde Python
6. `DBCA_boxplots_R.png` - 12 boxplots desde R
7. `DBCA_diagnosticos_R.png` - 12 gráficos de diagnóstico desde R
8. `DBCA_analisis_quinua.png` - Análisis completo desde Python

---

## 5. Comparación Python vs R

### Funcionalidades Equivalentes

| Funcionalidad | Python | R |
|---------------|--------|---|
| Carga de datos | ✅ | ✅ |
| ANOVA por factor | ✅ | ✅ |
| ANOVA factorial | ✅ | ✅ |
| Pruebas de Tukey | ✅ | ✅ |
| Test de normalidad | ✅ (Shapiro-Wilk) | ✅ (Shapiro-Wilk) |
| Test de homogeneidad | ✅ (Levene) | ✅ (Levene) |
| Test de aditividad | ✅ | ✅ |
| Boxplots (12) | ✅ | ✅ |
| Gráficos diagnóstico | ✅ | ✅ |
| Heatmaps | ✅ (seaborn) | ✅ (fields) |
| Violin plots | ✅ | ✅ |
| Exportación PNG | ✅ (300 DPI) | ✅ (300 DPI) |

### Librerías Utilizadas

**Python:**
- `pandas` - Manipulación de datos
- `numpy` - Operaciones numéricas
- `matplotlib` - Visualizaciones base
- `seaborn` - Visualizaciones avanzadas
- `scipy.stats` - Tests estadísticos
- `statsmodels` - Modelos ANOVA

**R:**
- `ggplot2` - Visualizaciones
- `agricolae` - Diseños experimentales y Tukey
- `car` - Test de Levene
- `gridExtra` - Organización de gráficos
- `reshape2` - Manipulación de datos
- `dplyr` - Manipulación de datos
- `fields` - Heatmaps

---

## 6. Cómo Ejecutar los Análisis

### Python
```bash
# Generar datos de 5 réplicas
python generar_datos_5replicas.py

# Ejecutar análisis completo
python analisis_DBCA.py
```

**Salidas:**
- Análisis estadístico completo en consola
- `DBCA_boxplots_python.png` - 12 boxplots
- `DBCA_analisis_quinua.png` - Análisis completo

### R
```bash
# Ejecutar análisis completo
Rscript analisis_DBCA.R
```

**Salidas:**
- Análisis estadístico completo en consola
- `DBCA_boxplots_R.png` - 12 boxplots
- `DBCA_diagnosticos_R.png` - 12 gráficos de diagnóstico

---

## 7. Ventajas del Diseño de 5 Réplicas

### Estadísticas
- ✅ **Mayor poder estadístico**: Mejor detección de diferencias
- ✅ **Menor error estándar**: Estimaciones más precisas
- ✅ **Diseño balanceado**: Facilita análisis e interpretación
- ✅ **48 grados de libertad del error**: Suficiente para tests robustos

### Prácticas
- ✅ **Menor costo**: 60 parcelas vs 109 parcelas originales
- ✅ **Mayor eficiencia de campo**: Más fácil de manejar
- ✅ **Mejor organización**: Distribución clara en 3 bloques
- ✅ **Robustez**: Tolera mejor datos faltantes

### Académicas
- ✅ **Diseño estándar**: Ampliamente aceptado en literatura
- ✅ **Fácil replicación**: Otros pueden reproducir el diseño
- ✅ **Enseñanza clara**: Ideal para propósitos educativos

---

## 8. Interpretación de Boxplots

### Elementos Visuales

**Caja (Box):**
- Límite inferior: Percentil 25 (Q1)
- Línea central: Mediana (Q2)
- Límite superior: Percentil 75 (Q3)
- Altura de la caja: Rango intercuartílico (IQR = Q3 - Q1)

**Bigotes (Whiskers):**
- Extensión: Hasta 1.5 × IQR desde los cuartiles
- Representan el rango de datos "normales"

**Puntos Rojos (Diamantes):**
- Representan la **media** del grupo
- Útil para comparar con la mediana

**Puntos Individuales:**
- Valores atípicos (outliers)
- Datos fuera de 1.5 × IQR

### Interpretación

**Caja Ancha:**
- Mayor variabilidad en ese grupo
- Datos más dispersos

**Caja Estrecha:**
- Menor variabilidad
- Grupo más consistente

**Media ≠ Mediana:**
- Distribución asimétrica
- Posible sesgo en los datos

**Muchos Outliers:**
- Revisar calidad de datos
- Posibles errores de medición

---

## 9. Resultados Esperados

### Con el Dataset de 5 Réplicas

**Efectos Principales:**
- Fertilizante: Efecto significativo esperado (p < 0.05)
- Riego: Efecto significativo esperado (p < 0.05)
- Variedad: Efecto moderado

**Interacciones:**
- Fertilizante × Riego: Interacción significativa esperada
- Variedad × Fertilizante: Posible interacción
- Triple interacción: Probablemente no significativa

**Efecto de Bloques:**
- Significativo (p < 0.05)
- Justifica el uso de DBCA

**Supuestos:**
- Normalidad: Cumplida (p > 0.05 en Shapiro-Wilk)
- Homogeneidad: Cumplida (p > 0.05 en Levene)
- Aditividad: Cumplida (p > 0.05 en test de interacción)

---

## 10. Próximos Pasos Sugeridos

### Análisis Adicionales
1. **Análisis de Contrastes**: Comparaciones específicas planeadas
2. **Análisis de Regresión**: Relación con variables continuas
3. **Análisis de Correlación**: Entre variables de respuesta
4. **Análisis de Componentes Principales**: Reducción de dimensionalidad

### Visualizaciones Adicionales
1. **Gráficos de Perfiles**: Interacciones más claras
2. **Mapas de Calor Avanzados**: Con clustering
3. **Gráficos de Barras con Errores**: Para presentaciones
4. **Gráficos 3D**: Interacciones triples

### Reportes
1. **Informe Técnico**: Documento completo en LaTeX/Word
2. **Presentación**: Diapositivas para defensa
3. **Artículo Científico**: Formato de revista

---

## ✅ Checklist de Implementación

- [x] Crear script generador de datos (`generar_datos_5replicas.py`)
- [x] Generar dataset con 5 réplicas (`quinua_5replicas.csv`)
- [x] Actualizar `analisis_DBCA.py` para usar nuevo dataset
- [x] Agregar 12 boxplots a `analisis_DBCA.py`
- [x] Traducir completamente código Python a R
- [x] Implementar boxplots en R con ggplot2
- [x] Implementar gráficos de diagnóstico en R
- [x] Verificar todos los tests estadísticos en R
- [x] Documentar cambios en este archivo
- [x] Probar ejecución de ambos scripts

---

## 📚 Referencias

### Diseño Experimental
- Montgomery, D. C. (2017). *Design and Analysis of Experiments*. 9th Edition.
- Kuehl, R. O. (2000). *Design of Experiments: Statistical Principles of Research Design and Analysis*.

### Análisis Estadístico en R
- Crawley, M. J. (2012). *The R Book*. 2nd Edition.
- Field, A., Miles, J., & Field, Z. (2012). *Discovering Statistics Using R*.

### Análisis Estadístico en Python
- McKinney, W. (2017). *Python for Data Analysis*. 2nd Edition.
- VanderPlas, J. (2016). *Python Data Science Handbook*.

---

**Autor**: Análisis Experimental  
**Fecha**: 10 de Diciembre, 2025  
**Versión**: 1.0
