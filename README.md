# Análisis Experimental de Cultivo de Quinua: Diseño DBCA

Este proyecto implementa un **Diseño en Bloques Completamente al Azar (DBCA)** para analizar un experimento de cultivo de quinua. 

**¿Por qué DBCA?**
El análisis preliminar de los datos mostró diferencias significativas de altitud y condiciones del suelo entre las diferentes secciones del terreno (Bloques). El DBCA es el diseño más eficiente en este caso porque permite controlar esta variabilidad sistemática, aislando el efecto de los bloques para medir con mayor precisión el impacto real de los tratamientos (Variedad, Fertilizante, Riego).

## 🔬 Estructura del Diseño Experimental

### Componentes del Experimento

| Componente | Cantidad | Detalle |
|------------|----------|---------|
| **Bloques** | 3 | Bloque1 (~3800m), Bloque2 (~3900m), Bloque3 (~4000m) |
| **Factores** | 3 | Variedad, Fertilizante, Riego |
| **Niveles** | 2, 3, 2 | Total: 7 niveles |
| **Tratamientos** | 12 | Combinaciones factoriales (2×3×2) |
| **Parcelas Totales** | 109 | Unidades experimentales |
| **Réplicas** | ~3 | Por tratamiento por bloque |

### Factores y Niveles

- **Variedad**: A, B (2 niveles)
- **Fertilizante**: Ninguno, Bajo, Alto (3 niveles)
- **Riego**: Bajo, Alto (2 niveles)

### Recomendación para Diseños Futuros

> **💡 Diseño Optimizado**: Se recomienda trabajar con **5 réplicas** por tratamiento, resultando en **60 unidades experimentales** (12 tratamientos × 5 réplicas) para:
> - Mayor poder estadístico
> - Diseño perfectamente balanceado
> - Menor costo y mayor eficiencia de campo

## 📄 Archivos del Proyecto

### Datos
- **`quinua_simulada_es.csv`**: Dataset principal en español, listo para análisis.
- *(Original: `quinua_simulada.csv` incluido como respaldo)*

### Scripts de Análisis
1.  **`traducir_datos.py`**: Utilidad para regenerar el dataset en español si es necesario.
2.  **`verificar_normativa.py`**: Valida que los datos cumplan con rangos agronómicos estándares (pH, Altitud, Calidad, etc.).
3.  **`analisis_DBCA.py`**: **Script Principal (Python)**. Realiza el ANOVA con bloqueo, pruebas de Tukey, verificación de supuestos y genera gráficos comparativos.
4.  **`generar_boxplots.py`**: **Script de Visualización**. Genera 12 boxplots detallados mostrando factores e interacciones.
5.  **`analisis_DBCA.R`**: **Script Complementario (R)**. Réplica del análisis en R para validación cruzada.

## 📊 Resultados del Análisis DBCA

### Factores Evaluados
- **Bloque**: Control de variabilidad (Altitud/Suelo).
- **Variedad**: A vs B.
- **Fertilizante**: Ninguno, Bajo, Alto.
- **Riego**: Bajo, Alto.

### Cumplimiento Normativo
Se verificó que el experimento simulado cumple con condiciones realistas:
- ✅ **pH Suelo**: 6.0 - 8.5
- ✅ **Altitud**: 2500 - 4500 msnm (Altiplano)
- ✅ **Calidad**: Aceptable para mercado

## 🚀 Instrucciones de Ejecución

### Opción 1: Python
Ejecuta el análisis completo y genera visualizaciones:
```bash
python analisis_DBCA.py
```
*Esto generará un archivo de imagen `DBCA_analisis_quinua.png` con los gráficos de diagnóstico.*

### Opción 2: Lenguaje R
Si prefieres R para análisis estadístico puro:
```bash
Rscript analisis_DBCA.R
```

### Verificación de Normas
```bash
python verificar_normativa.py
```

## 📦 Requisitos
- **Python**: `pandas`, `numpy`, `matplotlib`, `seaborn`, `statsmodels`, `scipy`
- **R**: `ggplot2`, `agricolae`

---

## 📖 Documentación Completa

### Documentos Disponibles

1. **[DOCUMENTACION_COMPLETA_DBCA.md](DOCUMENTACION_COMPLETA_DBCA.md)** ⭐ **PRINCIPAL**
   - Documentación técnica exhaustiva (400+ líneas)
   - 10 secciones: Introducción, Marco Teórico, Metodología, Implementaciones, Resultados
   - Comparación detallada Python vs R
   - Incluye teoría estadística, código explicado y hallazgos

2. **[RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md)**
   - Resumen de 1 página con hallazgos clave
   - Tabla de efectos significativos
   - Recomendaciones agronómicas óptimas

3. **Visualizaciones**: 
   - `DBCA_analisis_quinua.png` - 12 gráficos de diagnóstico y análisis (heatmaps, Q-Q plots, interacciones)
   - `DBCA_boxplots_detallados.png` - 12 boxplots detallados de factores e interacciones

### Hallazgos Principales

✅ **Efecto de Bloques Significativo** (p < 0.001) - DBCA justificado  
✅ **Fertilizante**: Factor más importante (+34% rendimiento)  
✅ **Riego Alto**: Incremento del 19% en rendimiento  
✅ **Variedad A**: Superior, especialmente con fertilizante alto  
✅ **Todos los Supuestos Cumplidos**: Normalidad, homogeneidad, aditividad  
✅ **R² = 84.7%**: Excelente bondad de ajuste

### Recomendación Óptima

> **Mejor Combinación**: Variedad A + Fertilizante Alto + Riego Alto  
> **Rendimiento Esperado**: 2.5-2.8 kg/parcela
