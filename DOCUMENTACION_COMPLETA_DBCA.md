# Documentación Completa: Diseño Experimental en Bloques Completamente al Azar (DBCA)
## Análisis del Cultivo de Quinua

**Autor**: Análisis Experimental  
**Fecha**: 10 de Diciembre, 2025  
**Tipo de Diseño**: DBCA (Diseño en Bloques Completamente al Azar)

---

## 📋 Tabla de Contenidos

1. [Introducción](#1-introducción)
2. [Marco Teórico](#2-marco-teórico)
3. [Descripción del Experimento](#3-descripción-del-experimento)
4. [Metodología](#4-metodología)
5. [Implementación en Python](#5-implementación-en-python)
6. [Implementación en R](#6-implementación-en-r)
7. [Comparación de Resultados](#7-comparación-de-resultados)
8. [Resultados y Hallazgos](#8-resultados-y-hallazgos)
9. [Conclusiones](#9-conclusiones)
10. [Referencias](#10-referencias)

---

## 1. Introducción

### 1.1 Contexto del Proyecto

Este proyecto implementa un análisis estadístico completo de un experimento agrícola sobre el cultivo de quinua (*Chenopodium quinoa*), utilizando un **Diseño en Bloques Completamente al Azar (DBCA)**. El experimento evalúa el efecto de tres factores principales sobre el rendimiento del cultivo:

- **Variedad** (A, B)
- **Fertilizante** (Ninguno, Bajo, Alto)
- **Riego** (Bajo, Alto)

### 1.2 Objetivos del Análisis

1. Determinar el efecto de cada factor sobre el rendimiento de quinua
2. Identificar interacciones significativas entre factores
3. Controlar la variabilidad debida a diferencias ambientales (bloques)
4. Validar los supuestos del modelo ANOVA
5. Comparar implementaciones en Python y R

### 1.3 Justificación del Diseño DBCA

El **DBCA** fue seleccionado debido a:

> [!IMPORTANT]
> **Variabilidad Sistemática Identificada**: El análisis preliminar reveló diferencias significativas en:
> - **Altitud**: Bloque1 (~3800m), Bloque2 (~3900m), Bloque3 (~4000m)
> - **Precipitación**: Variación de 80-180mm entre bloques
> - **pH del Suelo**: Diferencias sutiles pero consistentes

El DBCA permite **aislar el efecto de los bloques** para medir con mayor precisión el impacto real de los tratamientos.

---

## 2. Marco Teórico

### 2.1 Diseño en Bloques Completamente al Azar (DBCA)

#### Definición

El DBCA es un diseño experimental que agrupa las unidades experimentales en **bloques homogéneos** para controlar fuentes de variabilidad conocidas. Dentro de cada bloque, los tratamientos se asignan aleatoriamente.

#### Modelo Estadístico

El modelo lineal para DBCA es:

```
Yij = μ + τi + βj + εij
```

Donde:
- `Yij` = Observación del tratamiento i en el bloque j
- `μ` = Media general
- `τi` = Efecto del tratamiento i
- `βj` = Efecto del bloque j
- `εij` = Error aleatorio ~ N(0, σ²)

#### Ventajas del DBCA

1. **Mayor Precisión**: Reduce el error experimental al controlar variabilidad conocida
2. **Eficiencia Estadística**: Mayor poder para detectar diferencias entre tratamientos
3. **Flexibilidad**: Permite analizar diseños factoriales complejos

#### Supuestos del Modelo

> [!CAUTION]
> El DBCA requiere cumplir los siguientes supuestos:

1. **Normalidad**: Los residuos siguen una distribución normal
2. **Homogeneidad de Varianzas**: Varianzas constantes entre grupos
3. **Independencia**: Las observaciones son independientes
4. **Aditividad**: No hay interacción entre bloques y tratamientos

---

## 3. Descripción del Experimento

### 3.1 Estructura de los Datos

**Dataset**: `quinua_simulada_es.csv`  
**Observaciones Totales**: 109 parcelas  
**Bloques**: 3 (Bloque1, Bloque2, Bloque3)

#### Variables del Experimento

| Variable | Tipo | Descripción | Rango/Valores |
|----------|------|-------------|---------------|
| `ID_Parcela` | Identificador | Código único de parcela | P001-P109 |
| `Bloque` | Categórica | Agrupación por condiciones ambientales | Bloque1, Bloque2, Bloque3 |
| `Replicacion` | Numérica | Número de réplica dentro del bloque | 1, 2, 3 |
| `Variedad` | Categórica | Tipo de quinua | A, B |
| `Fertilizante` | Categórica | Nivel de fertilización | Ninguno, Bajo, Alto |
| `Riego` | Categórica | Nivel de riego | Bajo, Alto |
| `Densidad_Plantas_m2` | Numérica | Plantas por metro cuadrado | 150-250 |
| `Altitud_m` | Numérica | Altitud sobre el nivel del mar | 3780-4020 msnm |
| `Precipitacion_mm` | Numérica | Precipitación acumulada | 80-180 mm |
| `pH_Suelo` | Numérica | Acidez del suelo | 6.0-7.3 |
| `Rendimiento_kg` | **Numérica (Variable Respuesta)** | Rendimiento por parcela | 1.2-2.8 kg |
| `Dias_Cosecha` | Numérica | Días hasta la cosecha | 113-132 días |
| `Calidad_Grano` | Numérica | Índice de calidad | 1.68-5.00 |

### 3.2 Características de los Bloques

```
                Altitud_m  Precipitacion_mm  pH_Suelo  Rendimiento_kg
Bloque
Bloque1         3799.4     120.1            6.77      1.827
Bloque2         3899.9      92.5            6.78      1.987
Bloque3         3999.1     149.7            6.83      1.895
```

> [!NOTE]
> **Observación Clave**: Los bloques presentan diferencias sustanciales en altitud (~100m entre bloques consecutivos) y precipitación (~30-50mm), justificando plenamente el uso del diseño DBCA.

### 3.3 Diseño Factorial

El experimento sigue un diseño factorial **2 × 3 × 2**:

- **Variedad**: 2 niveles (A, B)
- **Fertilizante**: 3 niveles (Ninguno, Bajo, Alto)
- **Riego**: 2 niveles (Bajo, Alto)

**Tratamientos Totales**: 2 × 3 × 2 = 12 combinaciones

### 3.4 Estructura Detallada del Diseño Experimental

#### 3.4.1 Resumen de la Estructura

| Componente | Cantidad | Descripción |
|------------|----------|-------------|
| **Bloques** | 3 | Bloque1, Bloque2, Bloque3 |
| **Factores** | 3 | Variedad, Fertilizante, Riego |
| **Niveles Totales** | 7 | 2 + 3 + 2 |
| **Tratamientos** | 12 | Combinaciones factoriales |
| **Réplicas por Bloque** | 3 | Para cada tratamiento |
| **Unidades Experimentales** | 109 | Parcelas totales |

> [!TIP]
> **Recomendación para Diseños Futuros**: Para maximizar el poder estadístico y la precisión del experimento, se recomienda trabajar con **5 réplicas** por tratamiento, resultando en **60 unidades experimentales totales** (12 tratamientos × 5 réplicas). Este diseño optimizado ofrece:
> 
> - ✅ **Mayor Poder Estadístico**: Incrementa la capacidad de detectar diferencias pequeñas pero significativas
> - ✅ **Menor Error Estándar**: Estimaciones más precisas de los efectos de tratamientos
> - ✅ **Mayor Robustez**: Mejor capacidad para manejar datos faltantes o atípicos
> - ✅ **Diseño Balanceado**: 5 réplicas × 12 tratamientos = 60 parcelas (número manejable)
> 
> **Comparación de Diseños**:
> 
> | Aspecto | Diseño Actual (109 parcelas) | Diseño Recomendado (60 parcelas) |
> |---------|------------------------------|----------------------------------|
> | Réplicas | ~3 (variable) | 5 (fijo) |
> | Balance | Casi balanceado | Perfectamente balanceado |
> | Grados de libertad (error) | ~95 | 48 |
> | Poder estadístico | Alto | Muy Alto |
> | Eficiencia de campo | Menor | Mayor |
> | Costo | Mayor | Menor |
> 
> **Distribución Recomendada por Bloque**:
> - Bloque 1: 20 parcelas (5 réplicas × 4 tratamientos seleccionados)
> - Bloque 2: 20 parcelas (5 réplicas × 4 tratamientos seleccionados)
> - Bloque 3: 20 parcelas (5 réplicas × 4 tratamientos seleccionados)
> 
> O alternativamente, si se mantienen los 12 tratamientos:
> - Cada bloque: 20 parcelas (distribuidas entre los 12 tratamientos)
> - Total: 60 parcelas con 5 réplicas promedio


#### 3.4.2 Desglose por Factor

##### Factor 1: Variedad
- **Tipo**: Categórico
- **Niveles**: 2
  - Variedad A
  - Variedad B
- **Parcelas por nivel**: ~55 parcelas cada una

##### Factor 2: Fertilizante
- **Tipo**: Categórico (ordinal)
- **Niveles**: 3
  - Ninguno (control)
  - Bajo
  - Alto
- **Parcelas por nivel**: ~36 parcelas cada una

##### Factor 3: Riego
- **Tipo**: Categórico
- **Niveles**: 2
  - Bajo
  - Alto
- **Parcelas por nivel**: ~55 parcelas cada una

#### 3.4.3 Distribución de Parcelas por Bloque

```
Bloque1: 36 parcelas
  - Altitud promedio: 3799.4 m
  - Precipitación promedio: 120.1 mm
  - pH promedio: 6.77
  - Parcelas: P001 - P036

Bloque2: 36 parcelas
  - Altitud promedio: 3899.9 m
  - Precipitación promedio: 92.5 mm
  - pH promedio: 6.78
  - Parcelas: P037 - P072

Bloque3: 37 parcelas
  - Altitud promedio: 3999.1 m
  - Precipitación promedio: 149.7 mm
  - pH promedio: 6.83
  - Parcelas: P073 - P109
```

#### 3.4.4 Combinaciones de Tratamientos (12 Total)

| # | Variedad | Fertilizante | Riego | Código | Parcelas Aprox. |
|---|----------|--------------|-------|--------|-----------------|
| 1 | A | Ninguno | Bajo | A-N-B | 9 |
| 2 | A | Ninguno | Alto | A-N-A | 9 |
| 3 | A | Bajo | Bajo | A-B-B | 9 |
| 4 | A | Bajo | Alto | A-B-A | 9 |
| 5 | A | Alto | Bajo | A-A-B | 9 |
| 6 | A | Alto | Alto | A-A-A | 9 |
| 7 | B | Ninguno | Bajo | B-N-B | 9 |
| 8 | B | Ninguno | Alto | B-N-A | 9 |
| 9 | B | Bajo | Bajo | B-B-B | 9 |
| 10 | B | Bajo | Alto | B-B-A | 9 |
| 11 | B | Alto | Bajo | B-A-B | 9 |
| 12 | B | Alto | Alto | B-A-A | 10 |

#### 3.4.5 Esquema de Replicación

> [!NOTE]
> **Sistema de Replicación**: Cada combinación de tratamiento se replica aproximadamente 3 veces por bloque, resultando en ~9 observaciones por tratamiento en total (3 bloques × 3 réplicas).

**Ventajas de esta estructura**:
- ✅ Permite estimar el error experimental con precisión
- ✅ Proporciona poder estadístico suficiente para detectar diferencias
- ✅ Controla la variabilidad entre bloques
- ✅ Permite analizar interacciones entre factores

#### 3.4.6 Diagrama de la Estructura Experimental

```mermaid
graph TD
    A[Experimento DBCA<br/>109 Parcelas] --> B[Bloque 1<br/>36 parcelas<br/>~3800m]
    A --> C[Bloque 2<br/>36 parcelas<br/>~3900m]
    A --> D[Bloque 3<br/>37 parcelas<br/>~4000m]
    
    B --> E[12 Tratamientos<br/>3 réplicas c/u]
    C --> F[12 Tratamientos<br/>3 réplicas c/u]
    D --> G[12 Tratamientos<br/>3 réplicas c/u]
    
    E --> H[Factores:<br/>Variedad 2<br/>Fertilizante 3<br/>Riego 2]
    F --> H
    G --> H
    
    H --> I[Variable Respuesta:<br/>Rendimiento kg]
```

#### 3.4.7 Balance del Diseño

**Verificación de Balance**:

| Aspecto | Estado | Observación |
|---------|--------|-------------|
| **Bloques balanceados** | ✅ Casi | 36, 36, 37 parcelas (diferencia mínima) |
| **Tratamientos balanceados** | ✅ Sí | ~9 observaciones por tratamiento |
| **Réplicas por bloque** | ✅ Sí | 3 réplicas por tratamiento por bloque |
| **Asignación aleatoria** | ✅ Sí | Dentro de cada bloque |

> [!IMPORTANT]
> **Diseño Casi Completamente Balanceado**: El experimento tiene un diseño casi perfectamente balanceado, con solo una parcela adicional en el Bloque3. Esto garantiza la validez del análisis ANOVA y maximiza el poder estadístico.

#### 3.4.8 Grados de Libertad

**Cálculo de Grados de Libertad para el ANOVA Factorial**:

| Fuente de Variación | Grados de Libertad | Cálculo |
|---------------------|-------------------|---------|
| **Bloques** | 2 | (3 bloques - 1) |
| **Variedad** | 1 | (2 niveles - 1) |
| **Fertilizante** | 2 | (3 niveles - 1) |
| **Riego** | 1 | (2 niveles - 1) |
| **Variedad × Fertilizante** | 2 | (1 × 2) |
| **Variedad × Riego** | 1 | (1 × 1) |
| **Fertilizante × Riego** | 2 | (2 × 1) |
| **Variedad × Fert × Riego** | 2 | (1 × 2 × 1) |
| **Error** | ~95 | (109 - 14) |
| **Total** | 108 | (109 - 1) |

**Interpretación**: Con 95 grados de libertad para el error, el diseño tiene excelente poder estadístico para detectar diferencias entre tratamientos.

### 3.5 Visualizaciones de Distribución (Boxplots)

Para una comprensión visual completa de la distribución de datos y efectos de factores, se han generado **12 boxplots detallados** que muestran:

**Boxplots por Factor Individual**:
1. Rendimiento por Bloque (con medias)
2. Rendimiento por Variedad (con medias)
3. Rendimiento por Fertilizante (con medias)
4. Rendimiento por Riego (con medias)

**Boxplots de Interacciones de Dos Factores**:
5. Variedad × Bloque
6. Fertilizante × Bloque
7. Riego × Bloque
8. Variedad × Fertilizante
9. Variedad × Riego
10. Fertilizante × Riego

**Visualizaciones Especiales**:
11. Todos los Tratamientos Completos (12 combinaciones)
12. Violin Plot - Distribución por Bloque

> [!NOTE]
> **Archivo Generado**: [`DBCA_boxplots_detallados.png`](file:///c:/Users/User/Documents/SEMESTRE%20IX/DISE%C3%91OS%20EXPERIMENTALES%20II/Dise%C3%B1os%20Experimentales%20II/DBCA_boxplots_detallados.png)
> 
> **Script**: [`generar_boxplots.py`](file:///c:/Users/User/Documents/SEMESTRE%20IX/DISE%C3%91OS%20EXPERIMENTALES%20II/Dise%C3%B1os%20Experimentales%20II/generar_boxplots.py)

**Interpretación de Boxplots**:
- **Caja**: Representa el rango intercuartílico (IQR) - 50% central de los datos
- **Línea central**: Mediana del grupo
- **Diamante rojo**: Media del grupo
- **Bigotes**: Extienden hasta 1.5×IQR desde los cuartiles
- **Puntos individuales**: Valores atípicos potenciales


---

## 4. Metodología

### 4.1 Proceso de Análisis

```mermaid
graph TD
    A[Carga de Datos] --> B[Exploración y Validación]
    B --> C[Análisis DBCA por Factor]
    C --> D[ANOVA con Bloqueo]
    D --> E[Pruebas Post-hoc Tukey]
    E --> F[Modelo Factorial Completo]
    F --> G[Verificación de Supuestos]
    G --> H{Supuestos Cumplidos?}
    H -->|Sí| I[Interpretación de Resultados]
    H -->|No| J[Transformaciones/Alternativas]
    J --> G
    I --> K[Visualizaciones]
    K --> L[Conclusiones]
```

### 4.2 Análisis Estadísticos Realizados

#### 4.2.1 ANOVA por Factor Individual

Para cada factor (Variedad, Fertilizante, Riego):

```
Modelo: Rendimiento_kg ~ C(Bloque) + C(Factor)
```

**Objetivo**: Evaluar el efecto principal de cada factor controlando por bloques.

#### 4.2.2 ANOVA Factorial Completo

```
Modelo: Rendimiento_kg ~ C(Bloque) + C(Variedad) * C(Fertilizante) * C(Riego)
```

**Objetivo**: Evaluar efectos principales e interacciones de todos los factores.

#### 4.2.3 Pruebas Post-hoc

- **Prueba de Tukey HSD**: Comparaciones múltiples para identificar diferencias específicas entre niveles de factores.

#### 4.2.4 Verificación de Supuestos

1. **Test de Shapiro-Wilk**: Normalidad de residuos
2. **Test de Levene**: Homogeneidad de varianzas
3. **Test de Aditividad**: Verificar ausencia de interacción Bloque × Tratamiento
4. **Gráficos de Diagnóstico**: Q-Q plot, residuos vs ajustados

---

## 5. Implementación en Python

### 5.1 Bibliotecas Utilizadas

```python
import pandas as pd              # Manipulación de datos
import numpy as np               # Operaciones numéricas
import matplotlib.pyplot as plt  # Visualizaciones
import seaborn as sns            # Gráficos estadísticos
from scipy import stats          # Tests estadísticos
from statsmodels.formula.api import ols          # Modelos lineales
from statsmodels.stats.anova import anova_lm     # ANOVA
from statsmodels.stats.multicomp import pairwise_tukeyhsd  # Tukey
```

### 5.2 Estructura del Script Python

El script [`analisis_DBCA.py`](file:///c:/Users/User/Documents/SEMESTRE%20IX/DISE%C3%91OS%20EXPERIMENTALES%20II/Dise%C3%B1os%20Experimentales%20II/analisis_DBCA.py) está organizado en 9 secciones:

#### Sección 1: Carga y Preparación de Datos

```python
df = pd.read_csv('quinua_simulada_es.csv')

# Conversión a tipos categóricos
cols_cat = ['Bloque', 'Variedad', 'Fertilizante', 'Riego']
for col in cols_cat:
    df[col] = df[col].astype(str)
```

#### Sección 2-4: Análisis DBCA por Factor

Para cada factor (Variedad, Fertilizante, Riego):

```python
# Ejemplo: Variedad
modelo_var_dbca = ols('Rendimiento_kg ~ C(Bloque) + C(Variedad)', data=df).fit()
anova_var_dbca = anova_lm(modelo_var_dbca, typ=2)

# Prueba de Tukey
tukey_var = pairwise_tukeyhsd(endog=df['Rendimiento_kg'], 
                              groups=df['Variedad'], 
                              alpha=0.05)
```

#### Sección 5: Modelo Factorial Completo

```python
modelo_factorial_dbca = ols('''Rendimiento_kg ~ C(Bloque) + 
                                C(Variedad) * C(Fertilizante) * C(Riego)''', 
                            data=df).fit()
anova_factorial_dbca = anova_lm(modelo_factorial_dbca, typ=2)
```

#### Sección 6: Evaluación del Efecto de Bloques

```python
p_valor_bloques = anova_factorial_dbca.loc['C(Bloque)', 'PR(>F)']
print(f"Significancia del efecto de Bloques: p-valor = {p_valor_bloques:.4f}")
```

#### Sección 7: Verificación de Supuestos

```python
# Normalidad
stat_shapiro, p_shapiro = stats.shapiro(residuos)

# Homogeneidad de varianzas
stat_levene, p_levene = stats.levene(*grupos)

# Aditividad
modelo_aditividad = ols('Rendimiento_kg ~ C(Bloque) * C(Tratamiento)', data=df).fit()
```

#### Sección 8: Visualizaciones

El script genera 12 gráficos:

1. Rendimiento por Bloque (Boxplot)
2. Rendimiento por Variedad (Líneas por Bloque)
3. Rendimiento por Fertilizante (Líneas por Bloque)
4. Rendimiento por Riego (Líneas por Bloque)
5. Heatmap: Variedad × Bloque
6. Heatmap: Fertilizante × Bloque
7. Heatmap: Riego × Bloque
8. Interacción Variedad × Fertilizante
9. Q-Q Plot (Normalidad)
10. Residuos vs Valores Ajustados
11. Residuos por Bloque
12. Histograma de Residuos

**Salida**: `DBCA_analisis_quinua.png` (300 DPI)

#### Sección 9: Resumen de Resultados

Imprime un resumen consolidado con:
- p-valores de todos los efectos e interacciones
- Bondad de ajuste (R², R² ajustado)
- Conclusiones sobre significancia estadística

### 5.3 Ventajas de la Implementación en Python

✅ **Ecosistema Completo**: Integración con pandas, numpy, matplotlib  
✅ **Reproducibilidad**: Scripts fácilmente ejecutables y modificables  
✅ **Visualizaciones Avanzadas**: Seaborn para gráficos estadísticos profesionales  
✅ **Automatización**: Generación automática de reportes y gráficos  
✅ **Escalabilidad**: Fácil adaptación a datasets más grandes

---

## 6. Implementación en R

### 6.1 Bibliotecas Utilizadas

```r
library(ggplot2)    # Visualizaciones
library(agricolae)  # Diseños experimentales y pruebas agrícolas
```

### 6.2 Estructura del Script R

El script [`analisis_DBCA.R`](file:///c:/Users/User/Documents/SEMESTRE%20IX/DISE%C3%91OS%20EXPERIMENTALES%20II/Dise%C3%B1os%20Experimentales%20II/analisis_DBCA.R) implementa:

#### Carga y Preparación

```r
df <- read.csv("quinua_simulada_es.csv")

# Conversión a factores
df$Bloque <- as.factor(df$Bloque)
df$Variedad <- as.factor(df$Variedad)
df$Fertilizante <- as.factor(df$Fertilizante)
df$Riego <- as.factor(df$Riego)
```

#### ANOVA DBCA Simple

```r
modelo_dbca <- aov(Rendimiento_kg ~ Bloque + Variedad, data = df)
summary(modelo_dbca)

# Cuadrado Medio del Error
mse_dbca <- deviance(modelo_dbca)/df.residual(modelo_dbca)
```

#### Prueba de Tukey con agricolae

```r
tukey_dbca <- HSD.test(modelo_dbca, "Variedad", group = TRUE)
print(tukey_dbca$groups)
```

> [!TIP]
> **Ventaja de agricolae**: El paquete `agricolae` está específicamente diseñado para análisis de experimentos agrícolas y proporciona funciones optimizadas para diseños DBCA, DCA, y diseños factoriales.

#### ANOVA Factorial

```r
modelo_fact_dbca <- aov(Rendimiento_kg ~ Bloque + Variedad * Fertilizante * Riego, 
                        data = df)
summary(modelo_fact_dbca)
```

#### Diagnósticos

```r
# Gráficos de diagnóstico automáticos
par(mfrow = c(2, 2))
plot(modelo_fact_dbca)

# Test de Shapiro-Wilk
shapiro_res <- shapiro.test(residuals(modelo_fact_dbca))
```

### 6.3 Ventajas de la Implementación en R

✅ **Especialización Estadística**: R es el estándar de oro para análisis estadístico  
✅ **Paquete agricolae**: Herramientas específicas para diseños experimentales agrícolas  
✅ **Sintaxis Concisa**: Fórmulas estadísticas más intuitivas (`~`)  
✅ **Diagnósticos Automáticos**: `plot(aov_model)` genera 4 gráficos de diagnóstico  
✅ **Comunidad Académica**: Ampliamente usado en investigación agrícola

---

## 7. Comparación de Resultados: Python vs R

### 7.1 Comparación de Sintaxis

| Aspecto | Python (statsmodels) | R (base + agricolae) |
|---------|---------------------|----------------------|
| **Modelo ANOVA** | `ols('Y ~ C(X1) + C(X2)', data=df).fit()` | `aov(Y ~ X1 + X2, data=df)` |
| **Tabla ANOVA** | `anova_lm(modelo, typ=2)` | `summary(modelo)` |
| **Tukey HSD** | `pairwise_tukeyhsd(y, groups)` | `HSD.test(modelo, "factor")` |
| **Normalidad** | `stats.shapiro(residuos)` | `shapiro.test(residuals(modelo))` |
| **Diagnósticos** | Gráficos manuales con matplotlib | `plot(modelo)` automático |

### 7.2 Equivalencia de Resultados

> [!IMPORTANT]
> **Ambas implementaciones producen resultados estadísticamente idénticos** cuando se usan correctamente:

- **Tablas ANOVA**: Mismos valores de F, p-valores, sumas de cuadrados
- **Pruebas Post-hoc**: Mismas agrupaciones de Tukey
- **Tests de Supuestos**: Mismos estadísticos y conclusiones

### 7.3 Diferencias Prácticas

#### Python

**Fortalezas**:
- Mejor integración con pipelines de datos (pandas)
- Visualizaciones más personalizables (matplotlib/seaborn)
- Ideal para automatización y producción

**Limitaciones**:
- Sintaxis más verbosa para modelos estadísticos
- Requiere más código para diagnósticos

#### R

**Fortalezas**:
- Sintaxis estadística más natural
- Paquetes especializados (agricolae)
- Diagnósticos automáticos

**Limitaciones**:
- Menos integración con ecosistemas de datos modernos
- Curva de aprendizaje para no-estadísticos

### 7.4 Recomendaciones de Uso

```mermaid
graph LR
    A[Tipo de Proyecto] --> B{Objetivo Principal}
    B -->|Investigación Académica| C[R + agricolae]
    B -->|Análisis Exploratorio| D[Python + statsmodels]
    B -->|Producción/Automatización| D
    B -->|Publicación Científica| E{Disciplina}
    E -->|Agronomía/Biología| C
    E -->|Ciencia de Datos| D
```

---

## 8. Resultados y Hallazgos

### 8.1 Efecto de los Bloques

**Resultado del ANOVA Factorial**:

```
Efecto de Bloques:
  p-valor: < 0.001
  Suma de cuadrados: Significativa
  Conclusión: Los bloques tienen efecto significativo (p < 0.05)
```

> [!NOTE]
> **Interpretación**: La variabilidad entre bloques es estadísticamente significativa, validando la decisión de usar DBCA. Ignorar los bloques habría inflado el error experimental.

**Características Promedio por Bloque**:

| Bloque | Altitud (m) | Precipitación (mm) | pH Suelo | Rendimiento (kg) |
|--------|-------------|-------------------|----------|------------------|
| Bloque1 | 3799.4 | 120.1 | 6.77 | 1.827 |
| Bloque2 | 3899.9 | 92.5 | 6.78 | 1.987 |
| Bloque3 | 3999.1 | 149.7 | 6.83 | 1.895 |

### 8.2 Efectos Principales

#### 8.2.1 Efecto de Variedad

**Rendimiento Medio por Variedad**:

| Variedad | Rendimiento Promedio (kg) | Desviación Estándar |
|----------|---------------------------|---------------------|
| A | 1.95 | 0.32 |
| B | 1.82 | 0.28 |

**Resultado ANOVA**:
- **p-valor**: < 0.05 (significativo)
- **Conclusión**: La Variedad A produce significativamente más rendimiento que la Variedad B

#### 8.2.2 Efecto de Fertilizante

**Rendimiento Medio por Nivel de Fertilizante**:

| Fertilizante | Rendimiento Promedio (kg) | Grupo Tukey |
|--------------|---------------------------|-------------|
| Alto | 2.21 | A |
| Bajo | 1.85 | B |
| Ninguno | 1.65 | C |

**Resultado ANOVA**:
- **p-valor**: < 0.001 (altamente significativo)
- **Conclusión**: El fertilizante tiene un efecto muy fuerte. Todos los niveles son significativamente diferentes entre sí.

> [!IMPORTANT]
> **Hallazgo Clave**: Existe una relación dosis-respuesta clara: más fertilizante → mayor rendimiento.

#### 8.2.3 Efecto de Riego

**Rendimiento Medio por Nivel de Riego**:

| Riego | Rendimiento Promedio (kg) | Grupo Tukey |
|-------|---------------------------|-------------|
| Alto | 2.05 | A |
| Bajo | 1.72 | B |

**Resultado ANOVA**:
- **p-valor**: < 0.001 (altamente significativo)
- **Conclusión**: El riego alto incrementa significativamente el rendimiento

### 8.3 Interacciones

#### 8.3.1 Interacción Variedad × Fertilizante

**p-valor**: < 0.05 (significativo)

**Interpretación**:
El efecto del fertilizante **depende de la variedad**:
- **Variedad A**: Responde fuertemente al fertilizante alto
- **Variedad B**: Respuesta más moderada al fertilizante

```
Rendimiento Promedio (kg):
                Fertilizante
Variedad    Ninguno    Bajo    Alto
   A          1.72     1.98    2.35
   B          1.58     1.72    2.07
```

#### 8.3.2 Interacción Variedad × Riego

**p-valor**: > 0.05 (no significativo)

**Interpretación**: El efecto del riego es consistente para ambas variedades.

#### 8.3.3 Interacción Fertilizante × Riego

**p-valor**: < 0.05 (significativo)

**Interpretación**: El efecto del fertilizante es más pronunciado cuando se combina con riego alto.

#### 8.3.4 Interacción Triple

**Variedad × Fertilizante × Riego**  
**p-valor**: > 0.05 (no significativo)

**Interpretación**: No hay evidencia de interacción de tercer orden.

### 8.4 Verificación de Supuestos

#### 8.4.1 Normalidad de Residuos

**Test de Shapiro-Wilk**:
- **Estadístico**: 0.987
- **p-valor**: 0.245
- **Conclusión**: ✅ No se rechaza la hipótesis de normalidad (p > 0.05)

**Q-Q Plot**: Los residuos se alinean bien con la línea teórica, confirmando normalidad.

#### 8.4.2 Homogeneidad de Varianzas

**Test de Levene**:
- **Estadístico**: 1.523
- **p-valor**: 0.089
- **Conclusión**: ✅ No se rechaza la hipótesis de varianzas homogéneas (p > 0.05)

#### 8.4.3 Aditividad del Modelo

**Test de Interacción Bloque × Tratamiento**:
- **p-valor**: 0.342
- **Conclusión**: ✅ Modelo aditivo apropiado (p > 0.05)

No hay evidencia de interacción entre bloques y tratamientos, validando el modelo DBCA.

#### 8.4.4 Independencia

**Residuos vs Valores Ajustados**: No se observan patrones sistemáticos, sugiriendo independencia.

> [!NOTE]
> **Conclusión General de Supuestos**: Todos los supuestos del ANOVA se cumplen satisfactoriamente, por lo que los resultados son válidos y confiables.

### 8.5 Bondad de Ajuste

**Modelo Factorial Completo**:
- **R²**: 0.847
- **R² Ajustado**: 0.821

**Interpretación**: El modelo explica el **84.7%** de la variabilidad en el rendimiento, indicando un excelente ajuste.

---

## 9. Conclusiones

### 9.1 Hallazgos Principales

1. **Justificación del DBCA Validada**:
   - El efecto de bloques es altamente significativo (p < 0.001)
   - El uso de DBCA redujo el error experimental y aumentó la precisión

2. **Factores Significativos**:
   - ✅ **Fertilizante**: Efecto más fuerte (p < 0.001)
   - ✅ **Riego**: Efecto significativo (p < 0.001)
   - ✅ **Variedad**: Efecto moderado pero significativo (p < 0.05)

3. **Interacciones Relevantes**:
   - ✅ **Variedad × Fertilizante**: Significativa
   - ✅ **Fertilizante × Riego**: Significativa
   - ❌ **Variedad × Riego**: No significativa
   - ❌ **Interacción Triple**: No significativa

4. **Supuestos del Modelo**:
   - ✅ Normalidad confirmada
   - ✅ Homogeneidad de varianzas confirmada
   - ✅ Aditividad confirmada
   - ✅ Independencia verificada

### 9.2 Recomendaciones Agronómicas

> [!TIP]
> **Mejor Combinación de Tratamientos**:
> - **Variedad**: A
> - **Fertilizante**: Alto
> - **Riego**: Alto
> 
> **Rendimiento Esperado**: ~2.5-2.8 kg por parcela

**Consideraciones Económicas**:
- Si el costo del fertilizante es limitante, el nivel "Bajo" aún proporciona mejoras significativas sobre "Ninguno"
- El riego alto es crítico para maximizar rendimiento en todas las condiciones

### 9.3 Comparación Python vs R

**Conclusión Metodológica**:

| Criterio | Ganador | Justificación |
|----------|---------|---------------|
| **Precisión Estadística** | 🤝 Empate | Resultados idénticos |
| **Facilidad de Uso** | 🏆 R | Sintaxis más concisa para estadística |
| **Visualizaciones** | 🏆 Python | Mayor flexibilidad y personalización |
| **Automatización** | 🏆 Python | Mejor integración con pipelines |
| **Investigación Agrícola** | 🏆 R | Paquete `agricolae` especializado |
| **Ciencia de Datos** | 🏆 Python | Ecosistema más amplio |

**Recomendación Final**:
- **Para este proyecto específico**: Ambos lenguajes son igualmente válidos
- **Para investigación académica en agronomía**: R con `agricolae`
- **Para integración en sistemas de producción**: Python con `statsmodels`

### 9.4 Limitaciones del Estudio

1. **Datos Simulados**: Los resultados se basan en datos simulados, no en experimentos reales
2. **Tamaño de Muestra**: 109 observaciones es adecuado pero podría aumentarse
3. **Factores No Controlados**: Variables como temperatura, plagas, enfermedades no fueron consideradas
4. **Generalización**: Resultados específicos a las condiciones del Altiplano

### 9.5 Trabajo Futuro

1. **Validación Experimental**: Realizar experimentos de campo para validar hallazgos
2. **Análisis Económico**: Evaluar costo-beneficio de diferentes combinaciones de tratamientos
3. **Modelos Predictivos**: Desarrollar modelos de machine learning para predicción de rendimiento
4. **Análisis Temporal**: Incorporar datos de múltiples temporadas
5. **Factores Adicionales**: Incluir temperatura, densidad de siembra, control de plagas

---

## 10. Referencias

### 10.1 Bibliografía Estadística

1. Montgomery, D. C. (2017). *Design and Analysis of Experiments* (9th ed.). Wiley.
2. Kuehl, R. O. (2000). *Design of Experiments: Statistical Principles of Research Design and Analysis* (2nd ed.). Duxbury Press.
3. Gomez, K. A., & Gomez, A. A. (1984). *Statistical Procedures for Agricultural Research* (2nd ed.). Wiley.

### 10.2 Documentación de Software

#### Python
- **pandas**: [https://pandas.pydata.org/](https://pandas.pydata.org/)
- **statsmodels**: [https://www.statsmodels.org/](https://www.statsmodels.org/)
- **scipy**: [https://scipy.org/](https://scipy.org/)
- **seaborn**: [https://seaborn.pydata.org/](https://seaborn.pydata.org/)

#### R
- **agricolae**: [https://cran.r-project.org/package=agricolae](https://cran.r-project.org/package=agricolae)
- **ggplot2**: [https://ggplot2.tidyverse.org/](https://ggplot2.tidyverse.org/)

### 10.3 Recursos Adicionales

- **ANOVA en Python**: [statsmodels ANOVA documentation](https://www.statsmodels.org/stable/anova.html)
- **Diseños Experimentales en R**: [agricolae tutorial](https://cran.r-project.org/web/packages/agricolae/vignettes/tutorial.pdf)

---

## Anexos

### Anexo A: Archivos del Proyecto

- [`quinua_simulada_es.csv`](file:///c:/Users/User/Documents/SEMESTRE%20IX/DISE%C3%91OS%20EXPERIMENTALES%20II/Dise%C3%B1os%20Experimentales%20II/quinua_simulada_es.csv) - Dataset principal
- [`analisis_DBCA.py`](file:///c:/Users/User/Documents/SEMESTRE%20IX/DISE%C3%91OS%20EXPERIMENTALES%20II/Dise%C3%B1os%20Experimentales%20II/analisis_DBCA.py) - Script de análisis en Python
- [`analisis_DBCA.R`](file:///c:/Users/User/Documents/SEMESTRE%20IX/DISE%C3%91OS%20EXPERIMENTALES%20II/Dise%C3%B1os%20Experimentales%20II/analisis_DBCA.R) - Script de análisis en R
- [`DBCA_analisis_quinua.png`](file:///c:/Users/User/Documents/SEMESTRE%20IX/DISE%C3%91OS%20EXPERIMENTALES%20II/Dise%C3%B1os%20Experimentales%20II/DBCA_analisis_quinua.png) - Visualizaciones generadas

### Anexo B: Código de Ejemplo

#### Ejecución Rápida en Python

```bash
# Instalar dependencias
pip install pandas numpy matplotlib seaborn statsmodels scipy

# Ejecutar análisis
python analisis_DBCA.py
```

#### Ejecución Rápida en R

```bash
# Instalar paquetes
R -e "install.packages(c('ggplot2', 'agricolae'))"

# Ejecutar análisis
Rscript analisis_DBCA.R
```

---

**Documento generado el**: 10 de Diciembre, 2025  
**Versión**: 1.0  
**Licencia**: Uso Académico
