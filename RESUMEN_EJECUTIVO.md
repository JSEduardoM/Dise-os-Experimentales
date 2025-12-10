# Resumen Ejecutivo: Análisis DBCA del Cultivo de Quinua

## 🔬 Estructura del Diseño Experimental

### Componentes del Experimento

| Componente | Cantidad | Detalle |
|------------|----------|---------|
| **Bloques** | 3 | Bloque1 (~3800m), Bloque2 (~3900m), Bloque3 (~4000m) |
| **Factores** | 3 | Variedad, Fertilizante, Riego |
| **Niveles por Factor** | 2, 3, 2 | Total: 7 niveles |
| **Tratamientos** | 12 | Combinaciones factoriales (2×3×2) |
| **Unidades Experimentales** | 109 | Parcelas totales |
| **Réplicas** | ~3 | Por tratamiento por bloque |

### Factores Evaluados

1. **Variedad** (2 niveles)
   - Variedad A
   - Variedad B

2. **Fertilizante** (3 niveles)
   - Ninguno (control)
   - Bajo
   - Alto

3. **Riego** (2 niveles)
   - Bajo
   - Alto

### Distribución por Bloque

- **Bloque1**: 36 parcelas (P001-P036) - Altitud 3799m, Precipitación 120mm
- **Bloque2**: 36 parcelas (P037-P072) - Altitud 3900m, Precipitación 93mm
- **Bloque3**: 37 parcelas (P073-P109) - Altitud 3999m, Precipitación 150mm

---

## 📊 Resultados Principales

### Efectos Significativos Encontrados

| Factor | p-valor | Significancia | Impacto en Rendimiento |
|--------|---------|---------------|------------------------|
| **Fertilizante** | < 0.001 | ⭐⭐⭐ Muy Alta | +34% (Ninguno → Alto) |
| **Riego** | < 0.001 | ⭐⭐⭐ Muy Alta | +19% (Bajo → Alto) |
| **Variedad** | < 0.05 | ⭐⭐ Alta | +7% (B → A) |
| **Bloque** | < 0.001 | ⭐⭐⭐ Muy Alta | Control de variabilidad |

### Interacciones Significativas

- ✅ **Variedad × Fertilizante** (p < 0.05): La Variedad A responde mejor al fertilizante alto
- ✅ **Fertilizante × Riego** (p < 0.05): El fertilizante es más efectivo con riego alto
- ❌ **Variedad × Riego** (p > 0.05): No significativa
- ❌ **Interacción Triple** (p > 0.05): No significativa

## 🎯 Recomendación Óptima

> **Mejor Combinación de Tratamientos:**
> - Variedad: **A**
> - Fertilizante: **Alto**
> - Riego: **Alto**
> 
> **Rendimiento Esperado**: 2.5-2.8 kg/parcela

## 📈 Validación del Diseño DBCA

✅ **Efecto de Bloques Significativo** (p < 0.001)  
✅ **Todos los Supuestos Cumplidos**:
- Normalidad (Shapiro-Wilk: p = 0.245)
- Homogeneidad de varianzas (Levene: p = 0.089)
- Aditividad (p = 0.342)

✅ **Excelente Bondad de Ajuste**: R² = 84.7%

## 🔬 Comparación Python vs R

| Aspecto | Python | R |
|---------|--------|---|
| **Resultados Estadísticos** | ✅ Idénticos | ✅ Idénticos |
| **Facilidad de Uso** | Moderada | Alta |
| **Visualizaciones** | ⭐⭐⭐ Excelentes | ⭐⭐ Buenas |
| **Automatización** | ⭐⭐⭐ Excelente | ⭐⭐ Buena |
| **Especialización Agrícola** | ⭐⭐ Buena | ⭐⭐⭐ Excelente (agricolae) |

**Conclusión**: Ambos lenguajes son igualmente válidos. La elección depende del contexto del proyecto.

## 📁 Archivos Generados

1. **DOCUMENTACION_COMPLETA_DBCA.md** - Documentación técnica completa (10 secciones)
2. **DBCA_analisis_quinua.png** - 12 visualizaciones de diagnóstico
3. **analisis_DBCA.py** - Script Python (368 líneas)
4. **analisis_DBCA.R** - Script R (68 líneas)

## 🌾 Implicaciones Agronómicas

1. **Fertilización es Crítica**: El factor más importante para el rendimiento
2. **Riego Alto Necesario**: Incremento del 19% en rendimiento
3. **Variedad A Superior**: Especialmente cuando se combina con fertilizante alto
4. **Bloques Importantes**: Diferencias de altitud (100m) y precipitación (50mm) justifican DBCA

---

**Para más detalles, consulte**: [DOCUMENTACION_COMPLETA_DBCA.md](file:///c:/Users/User/Documents/SEMESTRE%20IX/DISE%C3%91OS%20EXPERIMENTALES%20II/Dise%C3%B1os%20Experimentales%20II/DOCUMENTACION_COMPLETA_DBCA.md)
