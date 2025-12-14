# ============================================================================
# Análisis de Diseño en Bloques Completamente al Azar (DBCA) para datos de Quinua
# Traducción completa del código Python a R
# Autor: Análisis Experimental
# Fecha: 2025-12-10
# ============================================================================

# Cargar librerías necesarias
if (!require(ggplot2)) install.packages("ggplot2")
if (!require(agricolae)) install.packages("agricolae")
if (!require(car)) install.packages("car")
if (!require(gridExtra)) install.packages("gridExtra")
if (!require(reshape2)) install.packages("reshape2")
if (!require(dplyr)) install.packages("dplyr")

library(ggplot2)
library(agricolae)
library(car)
library(gridExtra)
library(reshape2)
library(dplyr)

# Configuración de visualización
options(width = 100)

# ============================================================================
# 1. CARGA Y PREPARACIÓN DE DATOS
# ============================================================================

cat(rep("=", 80), "\n", sep = "")
cat("ANÁLISIS DE DISEÑO EN BLOQUES COMPLETAMENTE AL AZAR (DBCA)\n")
cat("Dataset: Quinua con 5 Réplicas (60 Unidades Experimentales)\n")
cat(rep("=", 80), "\n", sep = "")

# Cargar datos (priorizar archivo de 5 réplicas)
if (file.exists("quinua_5replicas.csv")) {
  df <- read.csv("quinua_5replicas.csv", stringsAsFactors = FALSE)
  cat("\n✓ Datos cargados: quinua_5replicas.csv (5 réplicas, 60 UE)\n")
} else if (file.exists("quinua_simulada_es.csv")) {
  df <- read.csv("quinua_simulada_es.csv", stringsAsFactors = FALSE)
  cat("\n✓ Datos cargados: quinua_simulada_es.csv\n")
} else {
  df <- read.csv("quinua_simulada.csv", stringsAsFactors = FALSE)
  cat("\n✓ Datos cargados: quinua_simulada.csv\n")
}

# Asegurar tipos de datos correctos
df$Bloque <- as.factor(df$Bloque)
df$Variedad <- as.factor(df$Variedad)
df$Fertilizante <- as.factor(df$Fertilizante)
df$Riego <- as.factor(df$Riego)

cat("\n1. ESTRUCTURA DE LOS DATOS\n")
cat(rep("-", 80), "\n", sep = "")
cat("Total de observaciones:", nrow(df), "\n\n")
cat("Primeras filas:\n")
print(head(df, 10))

cat("\nDistribución de observaciones por Bloque:\n")
print(table(df$Bloque))

cat("\nCaracterísticas de cada Bloque:\n")
caracteristicas <- aggregate(cbind(Altitud_m, Precipitacion_mm, pH_Suelo) ~ Bloque,
  data = df, FUN = mean
)
print(caracteristicas)

# ============================================================================
# 2. ANÁLISIS DBCA - EFECTO DE VARIEDAD (CONTROLANDO POR BLOQUES)
# ============================================================================

cat("\n\n2. ANÁLISIS DBCA: EFECTO DE VARIEDAD EN RENDIMIENTO\n")
cat(rep("=", 80), "\n", sep = "")

# Estadísticas descriptivas por variedad y bloque
cat("\nRendimiento medio por Variedad y Bloque:\n")
tabla_var_bloque <- tapply(
  df$Rendimiento_kg,
  list(df$Variedad, df$Bloque),
  mean
)
print(round(tabla_var_bloque, 3))

# Modelo DBCA - Variedad con efecto de Bloque
modelo_var_dbca <- aov(Rendimiento_kg ~ Bloque + Variedad, data = df)
anova_var_dbca <- summary(modelo_var_dbca)

cat("\nTabla ANOVA - DBCA (Variedad):\n")
print(anova_var_dbca)

# ============================================================================
# 3. ANÁLISIS DBCA - EFECTO DE FERTILIZANTE (CONTROLANDO POR BLOQUES)
# ============================================================================

cat("\n\n3. ANÁLISIS DBCA: EFECTO DE FERTILIZANTE EN RENDIMIENTO\n")
cat(rep("=", 80), "\n", sep = "")

# Estadísticas descriptivas
cat("\nRendimiento medio por Fertilizante y Bloque:\n")
tabla_fert_bloque <- tapply(
  df$Rendimiento_kg,
  list(df$Fertilizante, df$Bloque),
  mean
)
print(round(tabla_fert_bloque, 3))

# Modelo DBCA
modelo_fert_dbca <- aov(Rendimiento_kg ~ Bloque + Fertilizante, data = df)
anova_fert_dbca <- summary(modelo_fert_dbca)

cat("\nTabla ANOVA - DBCA (Fertilizante):\n")
print(anova_fert_dbca)

# Prueba de Tukey
cat("\nPrueba de Tukey (Comparaciones múltiples - Fertilizante):\n")
tukey_fert <- HSD.test(modelo_fert_dbca, "Fertilizante", group = TRUE)
print(tukey_fert$groups)

# ============================================================================
# 4. ANÁLISIS DBCA - EFECTO DE RIEGO (CONTROLANDO POR BLOQUES)
# ============================================================================

cat("\n\n4. ANÁLISIS DBCA: EFECTO DE RIEGO EN RENDIMIENTO\n")
cat(rep("=", 80), "\n", sep = "")

# Estadísticas descriptivas
cat("\nRendimiento medio por Riego y Bloque:\n")
tabla_riego_bloque <- tapply(
  df$Rendimiento_kg,
  list(df$Riego, df$Bloque),
  mean
)
print(round(tabla_riego_bloque, 3))

# Modelo DBCA
modelo_riego_dbca <- aov(Rendimiento_kg ~ Bloque + Riego, data = df)
anova_riego_dbca <- summary(modelo_riego_dbca)

cat("\nTabla ANOVA - DBCA (Riego):\n")
print(anova_riego_dbca)

# Prueba de Tukey
cat("\nPrueba de Tukey (Comparaciones múltiples - Riego):\n")
tukey_riego <- HSD.test(modelo_riego_dbca, "Riego", group = TRUE)
print(tukey_riego$groups)

# ============================================================================
# 5. ANÁLISIS DBCA - MODELO FACTORIAL COMPLETO
# ============================================================================

cat("\n\n5. ANÁLISIS DBCA: MODELO FACTORIAL COMPLETO\n")
cat(rep("=", 80), "\n", sep = "")

# Modelo factorial con bloques
modelo_factorial_dbca <- aov(
  Rendimiento_kg ~ Bloque +
    Variedad * Fertilizante * Riego,
  data = df
)
anova_factorial_dbca <- summary(modelo_factorial_dbca)

cat("\nTabla ANOVA - DBCA Factorial:\n")
print(anova_factorial_dbca)

cat("\nResumen del modelo:\n")
print(summary.lm(modelo_factorial_dbca))

# ============================================================================
# 6. EVALUACIÓN DEL EFECTO DE BLOQUES
# ============================================================================

cat("\n\n6. EVALUACIÓN DEL EFECTO DE BLOQUES\n")
cat(rep("=", 80), "\n", sep = "")

# Estadísticas por bloque
cat("\nEstadísticas de Rendimiento por Bloque:\n")
stats_bloque <- df %>%
  group_by(Bloque) %>%
  summarise(
    count = n(),
    mean = mean(Rendimiento_kg),
    std = sd(Rendimiento_kg),
    min = min(Rendimiento_kg),
    q25 = quantile(Rendimiento_kg, 0.25),
    median = median(Rendimiento_kg),
    q75 = quantile(Rendimiento_kg, 0.75),
    max = max(Rendimiento_kg)
  )
print(stats_bloque)

# Características ambientales por Bloque
cat("\nCaracterísticas ambientales por Bloque:\n")
caracteristicas_bloques <- df %>%
  group_by(Bloque) %>%
  summarise(
    Altitud_m = mean(Altitud_m),
    Precipitacion_mm = mean(Precipitacion_mm),
    pH_Suelo = mean(pH_Suelo),
    Rendimiento_kg = mean(Rendimiento_kg)
  )
print(caracteristicas_bloques)

# Test de significancia del efecto de bloques
anova_table <- anova(modelo_factorial_dbca)
p_valor_bloques <- anova_table["Bloque", "Pr(>F)"]
cat("\nSignificancia del efecto de Bloques:\n")
cat("  p-valor:", sprintf("%.4f", p_valor_bloques), "\n")
cat(
  "  Conclusión:",
  ifelse(p_valor_bloques < 0.05,
    "Bloques tienen efecto significativo (p < 0.05)",
    "Bloques NO tienen efecto significativo (p > 0.05)"
  ), "\n"
)

# ============================================================================
# 7. VERIFICACIÓN DE SUPUESTOS
# ============================================================================

cat("\n\n7. VERIFICACIÓN DE SUPUESTOS DEL ANOVA\n")
cat(rep("=", 80), "\n", sep = "")

# Residuos
residuos <- residuals(modelo_factorial_dbca)
valores_ajustados <- fitted(modelo_factorial_dbca)

# Test de normalidad (Shapiro-Wilk)
shapiro_test <- shapiro.test(residuos)
cat("\nTest de Normalidad (Shapiro-Wilk):\n")
cat("  Estadístico:", sprintf("%.4f", shapiro_test$statistic), "\n")
cat("  p-valor:", sprintf("%.4f", shapiro_test$p.value), "\n")
cat(
  "  Conclusión:",
  ifelse(shapiro_test$p.value > 0.05,
    "Residuos normales (p > 0.05)",
    "Residuos NO normales (p < 0.05)"
  ), "\n"
)

# Test de homogeneidad de varianzas (Levene)
df$Tratamiento <- paste(df$Variedad, df$Fertilizante, df$Riego, sep = "_")
levene_test <- leveneTest(Rendimiento_kg ~ Tratamiento, data = df)
cat("\nTest de Homogeneidad de Varianzas (Levene):\n")
cat("  Estadístico:", sprintf("%.4f", levene_test$`F value`[1]), "\n")
cat("  p-valor:", sprintf("%.4f", levene_test$`Pr(>F)`[1]), "\n")
cat(
  "  Conclusión:",
  ifelse(levene_test$`Pr(>F)`[1] > 0.05,
    "Varianzas homogéneas (p > 0.05)",
    "Varianzas NO homogéneas (p < 0.05)"
  ), "\n"
)

# Test de aditividad (Tukey)
df$Tratamiento <- as.factor(df$Tratamiento)
modelo_aditividad <- aov(Rendimiento_kg ~ Bloque * Tratamiento, data = df)
anova_aditividad <- anova(modelo_aditividad)
p_interaccion <- anova_aditividad["Bloque:Tratamiento", "Pr(>F)"]
cat("\nTest de Aditividad (Interacción Bloque × Tratamiento):\n")
cat("  p-valor:", sprintf("%.4f", p_interaccion), "\n")
cat(
  "  Conclusión:",
  ifelse(p_interaccion > 0.05,
    "Modelo aditivo apropiado (p > 0.05)",
    "Posible falta de aditividad (p < 0.05)"
  ), "\n"
)

# ============================================================================
# 8. BOXPLOTS - VISUALIZACIONES DETALLADAS
# ============================================================================

cat("\n\n8. GENERANDO BOXPLOTS Y VISUALIZACIONES...\n")
cat(rep("-", 80), "\n", sep = "")

# Crear directorio para gráficos si no existe
if (!dir.exists("graficos")) {
  dir.create("graficos")
}

# Función para agregar medias a boxplots
add_mean_points <- function(p) {
  p + stat_summary(
    fun = mean, geom = "point",
    shape = 23, size = 3, fill = "red", color = "darkred"
  )
}

# 8.1 Boxplot: Rendimiento por Bloque
p1 <- ggplot(df, aes(x = Bloque, y = Rendimiento_kg, fill = Bloque)) +
  geom_boxplot(alpha = 0.7) +
  stat_summary(
    fun = mean, geom = "point", shape = 23, size = 3,
    fill = "red", color = "darkred"
  ) +
  labs(
    title = "Rendimiento por Bloque",
    x = "Bloque", y = "Rendimiento (kg)"
  ) +
  theme_minimal() +
  theme(legend.position = "none")

# 8.2 Boxplot: Rendimiento por Variedad
p2 <- ggplot(df, aes(x = Variedad, y = Rendimiento_kg, fill = Variedad)) +
  geom_boxplot(alpha = 0.7) +
  stat_summary(
    fun = mean, geom = "point", shape = 23, size = 3,
    fill = "red", color = "darkred"
  ) +
  labs(
    title = "Rendimiento por Variedad",
    x = "Variedad", y = "Rendimiento (kg)"
  ) +
  theme_minimal() +
  theme(legend.position = "none")

# 8.3 Boxplot: Rendimiento por Fertilizante
p3 <- ggplot(df, aes(x = Fertilizante, y = Rendimiento_kg, fill = Fertilizante)) +
  geom_boxplot(alpha = 0.7) +
  stat_summary(
    fun = mean, geom = "point", shape = 23, size = 3,
    fill = "red", color = "darkred"
  ) +
  labs(
    title = "Rendimiento por Fertilizante",
    x = "Fertilizante", y = "Rendimiento (kg)"
  ) +
  theme_minimal() +
  theme(legend.position = "none")

# 8.4 Boxplot: Rendimiento por Riego
p4 <- ggplot(df, aes(x = Riego, y = Rendimiento_kg, fill = Riego)) +
  geom_boxplot(alpha = 0.7) +
  stat_summary(
    fun = mean, geom = "point", shape = 23, size = 3,
    fill = "red", color = "darkred"
  ) +
  labs(
    title = "Rendimiento por Riego",
    x = "Riego", y = "Rendimiento (kg)"
  ) +
  theme_minimal() +
  theme(legend.position = "none")

# 8.5 Boxplot: Variedad × Bloque
p5 <- ggplot(df, aes(x = Variedad, y = Rendimiento_kg, fill = Bloque)) +
  geom_boxplot(alpha = 0.7) +
  labs(
    title = "Interacción Variedad × Bloque",
    x = "Variedad", y = "Rendimiento (kg)"
  ) +
  theme_minimal()

# 8.6 Boxplot: Fertilizante × Bloque
p6 <- ggplot(df, aes(x = Fertilizante, y = Rendimiento_kg, fill = Bloque)) +
  geom_boxplot(alpha = 0.7) +
  labs(
    title = "Interacción Fertilizante × Bloque",
    x = "Fertilizante", y = "Rendimiento (kg)"
  ) +
  theme_minimal()

# 8.7 Boxplot: Riego × Bloque
p7 <- ggplot(df, aes(x = Riego, y = Rendimiento_kg, fill = Bloque)) +
  geom_boxplot(alpha = 0.7) +
  labs(
    title = "Interacción Riego × Bloque",
    x = "Riego", y = "Rendimiento (kg)"
  ) +
  theme_minimal()

# 8.8 Boxplot: Variedad × Fertilizante
p8 <- ggplot(df, aes(x = Variedad, y = Rendimiento_kg, fill = Fertilizante)) +
  geom_boxplot(alpha = 0.7) +
  labs(
    title = "Interacción Variedad × Fertilizante",
    x = "Variedad", y = "Rendimiento (kg)"
  ) +
  theme_minimal()

# 8.9 Boxplot: Variedad × Riego
p9 <- ggplot(df, aes(x = Variedad, y = Rendimiento_kg, fill = Riego)) +
  geom_boxplot(alpha = 0.7) +
  labs(
    title = "Interacción Variedad × Riego",
    x = "Variedad", y = "Rendimiento (kg)"
  ) +
  theme_minimal()

# 8.10 Boxplot: Fertilizante × Riego
p10 <- ggplot(df, aes(x = Fertilizante, y = Rendimiento_kg, fill = Riego)) +
  geom_boxplot(alpha = 0.7) +
  labs(
    title = "Interacción Fertilizante × Riego",
    x = "Fertilizante", y = "Rendimiento (kg)"
  ) +
  theme_minimal()

# 8.11 Boxplot: Todos los Tratamientos
p11 <- ggplot(df, aes(
  x = reorder(Tratamiento, Rendimiento_kg, median),
  y = Rendimiento_kg, fill = Tratamiento
)) +
  geom_boxplot(alpha = 0.7) +
  labs(
    title = "Rendimiento por Tratamiento Completo",
    x = "Tratamiento", y = "Rendimiento (kg)"
  ) +
  theme_minimal() +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1),
    legend.position = "none"
  )

# 8.12 Violin Plot: Distribución por Bloque
p12 <- ggplot(df, aes(x = Bloque, y = Rendimiento_kg, fill = Bloque)) +
  geom_violin(alpha = 0.7) +
  geom_boxplot(width = 0.2, alpha = 0.5) +
  labs(
    title = "Distribución de Rendimiento por Bloque (Violin Plot)",
    x = "Bloque", y = "Rendimiento (kg)"
  ) +
  theme_minimal() +
  theme(legend.position = "none")

# Guardar boxplots en un solo archivo
png("DBCA_boxplots_R.png", width = 20, height = 16, units = "in", res = 300)
grid.arrange(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, ncol = 4)
dev.off()
cat("✓ Boxplots guardados en: DBCA_boxplots_R.png\n")

# ============================================================================
# 9. GRÁFICOS DE DIAGNÓSTICO Y ANÁLISIS
# ============================================================================

cat("\n9. GENERANDO GRÁFICOS DE DIAGNÓSTICO...\n")
cat(rep("-", 80), "\n", sep = "")

# Crear figura con gráficos de diagnóstico
png("DBCA_diagnosticos_R.png", width = 18, height = 14, units = "in", res = 300)
par(mfrow = c(3, 4))

# 9.1 Rendimiento por Variedad (con bloques)
medias_var <- aggregate(Rendimiento_kg ~ Variedad + Bloque, data = df, FUN = mean)
plot(1,
  type = "n", xlim = c(0.5, 2.5), ylim = range(medias_var$Rendimiento_kg),
  xlab = "Variedad", ylab = "Rendimiento medio (kg)",
  main = "Rendimiento por Variedad (por Bloque)", xaxt = "n"
)
axis(1, at = 1:2, labels = levels(df$Variedad))
colors <- c("red", "blue", "green")
for (i in 1:length(levels(df$Bloque))) {
  bloque <- levels(df$Bloque)[i]
  data_bloque <- medias_var[medias_var$Bloque == bloque, ]
  lines(as.numeric(data_bloque$Variedad), data_bloque$Rendimiento_kg,
    col = colors[i], lwd = 2, type = "o", pch = 19
  )
}
legend("topright", legend = levels(df$Bloque), col = colors, lwd = 2, pch = 19)
grid()

# 9.2 Rendimiento por Fertilizante (con bloques)
medias_fert <- aggregate(Rendimiento_kg ~ Fertilizante + Bloque, data = df, FUN = mean)
plot(1,
  type = "n", xlim = c(0.5, 3.5), ylim = range(medias_fert$Rendimiento_kg),
  xlab = "Fertilizante", ylab = "Rendimiento medio (kg)",
  main = "Rendimiento por Fertilizante (por Bloque)", xaxt = "n"
)
axis(1, at = 1:3, labels = levels(df$Fertilizante))
for (i in 1:length(levels(df$Bloque))) {
  bloque <- levels(df$Bloque)[i]
  data_bloque <- medias_fert[medias_fert$Bloque == bloque, ]
  lines(as.numeric(data_bloque$Fertilizante), data_bloque$Rendimiento_kg,
    col = colors[i], lwd = 2, type = "o", pch = 19
  )
}
legend("topright", legend = levels(df$Bloque), col = colors, lwd = 2, pch = 19)
grid()

# 9.3 Rendimiento por Riego (con bloques)
medias_riego <- aggregate(Rendimiento_kg ~ Riego + Bloque, data = df, FUN = mean)
plot(1,
  type = "n", xlim = c(0.5, 2.5), ylim = range(medias_riego$Rendimiento_kg),
  xlab = "Riego", ylab = "Rendimiento medio (kg)",
  main = "Rendimiento por Riego (por Bloque)", xaxt = "n"
)
axis(1, at = 1:2, labels = levels(df$Riego))
for (i in 1:length(levels(df$Bloque))) {
  bloque <- levels(df$Bloque)[i]
  data_bloque <- medias_riego[medias_riego$Bloque == bloque, ]
  lines(as.numeric(data_bloque$Riego), data_bloque$Rendimiento_kg,
    col = colors[i], lwd = 2, type = "o", pch = 19
  )
}
legend("topright", legend = levels(df$Bloque), col = colors, lwd = 2, pch = 19)
grid()

# 9.4 Heatmap: Variedad × Bloque
library(fields)
matriz_var <- acast(df, Variedad ~ Bloque, value.var = "Rendimiento_kg", fun.aggregate = mean)
image.plot(1:ncol(matriz_var), 1:nrow(matriz_var), t(matriz_var),
  xlab = "Bloque", ylab = "Variedad",
  main = "Heatmap: Variedad × Bloque",
  xaxt = "n", yaxt = "n"
)
axis(1, at = 1:ncol(matriz_var), labels = colnames(matriz_var))
axis(2, at = 1:nrow(matriz_var), labels = rownames(matriz_var))

# 9.5 Heatmap: Fertilizante × Bloque
matriz_fert <- acast(df, Fertilizante ~ Bloque, value.var = "Rendimiento_kg", fun.aggregate = mean)
image.plot(1:ncol(matriz_fert), 1:nrow(matriz_fert), t(matriz_fert),
  xlab = "Bloque", ylab = "Fertilizante",
  main = "Heatmap: Fertilizante × Bloque",
  xaxt = "n", yaxt = "n"
)
axis(1, at = 1:ncol(matriz_fert), labels = colnames(matriz_fert))
axis(2, at = 1:nrow(matriz_fert), labels = rownames(matriz_fert))

# 9.6 Heatmap: Riego × Bloque
matriz_riego <- acast(df, Riego ~ Bloque, value.var = "Rendimiento_kg", fun.aggregate = mean)
image.plot(1:ncol(matriz_riego), 1:nrow(matriz_riego), t(matriz_riego),
  xlab = "Bloque", ylab = "Riego",
  main = "Heatmap: Riego × Bloque",
  xaxt = "n", yaxt = "n"
)
axis(1, at = 1:ncol(matriz_riego), labels = colnames(matriz_riego))
axis(2, at = 1:nrow(matriz_riego), labels = rownames(matriz_riego))

# 9.7 Interacción Variedad × Fertilizante
interaction.plot(df$Variedad, df$Fertilizante, df$Rendimiento_kg,
  xlab = "Variedad", ylab = "Rendimiento medio (kg)",
  main = "Interacción Variedad × Fertilizante",
  col = 1:3, lwd = 2
)

# 9.8 Q-Q Plot
qqnorm(residuos, main = "Q-Q Plot (Normalidad)")
qqline(residuos, col = "red", lwd = 2)
grid()

# 9.9 Residuos vs Valores Ajustados
plot(valores_ajustados, residuos,
  xlab = "Valores Ajustados", ylab = "Residuos",
  main = "Residuos vs Valores Ajustados",
  pch = 19, col = rgb(0, 0, 1, 0.5)
)
abline(h = 0, col = "red", lwd = 2, lty = 2)
grid()

# 9.10 Residuos por Bloque
boxplot(residuos ~ df$Bloque,
  xlab = "Bloque", ylab = "Residuos",
  main = "Residuos por Bloque",
  col = c("lightblue", "lightgreen", "lightyellow")
)
abline(h = 0, col = "red", lwd = 2, lty = 2)

# 9.11 Histograma de residuos
hist(residuos,
  breaks = 20, col = "lightblue", border = "black",
  xlab = "Residuos", ylab = "Frecuencia",
  main = "Histograma de Residuos"
)
grid()

# 9.12 Scale-Location Plot
plot(valores_ajustados, sqrt(abs(residuos)),
  xlab = "Valores Ajustados", ylab = "√|Residuos|",
  main = "Scale-Location Plot",
  pch = 19, col = rgb(0, 0, 1, 0.5)
)
abline(h = mean(sqrt(abs(residuos))), col = "red", lwd = 2, lty = 2)
grid()

dev.off()
cat("✓ Gráficos de diagnóstico guardados en: DBCA_diagnosticos_R.png\n")

# ============================================================================
# 10. RESUMEN DE RESULTADOS
# ============================================================================

cat("\n\n10. RESUMEN DE RESULTADOS - DBCA\n")
cat(rep("=", 80), "\n", sep = "")

anova_table <- anova(modelo_factorial_dbca)

cat("\nEfecto de Bloques:\n")
cat("  p-valor:", sprintf("%.4f", anova_table["Bloque", "Pr(>F)"]), "\n")
cat("  Suma de cuadrados:", sprintf("%.4f", anova_table["Bloque", "Sum Sq"]), "\n")

cat("\nEfectos principales (p-valores):\n")
cat("  - Variedad: p =", sprintf("%.4f", anova_table["Variedad", "Pr(>F)"]), "\n")
cat("  - Fertilizante: p =", sprintf("%.4f", anova_table["Fertilizante", "Pr(>F)"]), "\n")
cat("  - Riego: p =", sprintf("%.4f", anova_table["Riego", "Pr(>F)"]), "\n")

cat("\nInteracciones (p-valores):\n")
cat(
  "  - Variedad × Fertilizante: p =",
  sprintf("%.4f", anova_table["Variedad:Fertilizante", "Pr(>F)"]), "\n"
)
cat(
  "  - Variedad × Riego: p =",
  sprintf("%.4f", anova_table["Variedad:Riego", "Pr(>F)"]), "\n"
)
cat(
  "  - Fertilizante × Riego: p =",
  sprintf("%.4f", anova_table["Fertilizante:Riego", "Pr(>F)"]), "\n"
)
cat(
  "  - Variedad × Fertilizante × Riego: p =",
  sprintf("%.4f", anova_table["Variedad:Fertilizante:Riego", "Pr(>F)"]), "\n"
)

cat("\nBondad de ajuste:\n")
modelo_summary <- summary.lm(modelo_factorial_dbca)
cat("  R² del modelo:", sprintf("%.4f", modelo_summary$r.squared), "\n")
cat("  R² ajustado:", sprintf("%.4f", modelo_summary$adj.r.squared), "\n")

cat("\n", rep("=", 80), "\n", sep = "")
cat("ANÁLISIS COMPLETADO\n")
cat(rep("=", 80), "\n", sep = "")

cat("\nArchivos generados:\n")
cat("  - DBCA_boxplots_R.png (12 boxplots detallados)\n")
cat("  - DBCA_diagnosticos_R.png (12 gráficos de diagnóstico)\n")
cat("\n✓ Análisis DBCA completo en R finalizado exitosamente.\n")
