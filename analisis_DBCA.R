# Análisis de Diseño en Bloques Completamente al Azar (DBCA) - Quinua
# Autor: Análisis Experimental
# Fecha: 2025-12-10

# Cargar librerías
if (!require(ggplot2)) install.packages("ggplot2")
if (!require(agricolae)) install.packages("agricolae")

library(ggplot2)
library(agricolae)

# 1. Cargar datos
if (file.exists("quinua_simulada_es.csv")) {
  df <- read.csv("quinua_simulada_es.csv")
} else {
  df <- read.csv("quinua_simulada.csv")
  colnames(df)[colnames(df) == "Rendimiento_kg"] <- "Rendimiento"
}

cat("=========================================\n")
cat(" ANÁLISIS DBCA - CULTIVO DE QUINUA\n")
cat("=========================================\n\n")

# Estructura
# Convertir Bloque a factor
df$Bloque <- as.factor(df$Bloque)
df$Variedad <- as.factor(df$Variedad)
df$Fertilizante <- as.factor(df$Fertilizante)
df$Riego <- as.factor(df$Riego)

cat("Diseño experimental con", nlevels(df$Bloque), "bloques.\n")

# ==========================================================
# 2. ANOVA DBCA - Controlando por Bloque
# ==========================================================
cat("\n2. ANOVA DBCA (Modelo: Rendimiento ~ Bloque + Variedad)\n")
modelo_dbca <- aov(Rendimiento_kg ~ Bloque + Variedad, data = df)
print(summary(modelo_dbca))

# Comparar eficiencia con DCA
mse_dbca <- deviance(modelo_dbca)/df.residual(modelo_dbca)
cat("Cuadrado Medio del Error (DBCA):", mse_dbca, "\n")

# Prueba de Tukey (Variedad)
cat("\nPrueba de Tukey bajo DBCA (Variedad):\n")
tukey_dbca <- HSD.test(modelo_dbca, "Variedad", group = TRUE)
print(tukey_dbca$groups)

# ==========================================================
# 3. DBCA Factorial
# ==========================================================
cat("\n3. ANOVA Factorial en Bloques (Bloque + Var*Fert*Riego)\n")
modelo_fact_dbca <- aov(Rendimiento_kg ~ Bloque + Variedad * Fertilizante * Riego, data = df)
print(summary(modelo_fact_dbca))

# ==========================================================
# 4. Verificación de Supuestos
# ==========================================================
cat("\n4. Verificación de Supuestos\n")
par(mfrow = c(2, 2))
plot(modelo_fact_dbca)

# Normalidad
shapiro_res <- shapiro.test(residuals(modelo_fact_dbca))
cat("\nTest de Normalidad (Shapiro-Wilk): p-value =", shapiro_res$p.value, "\n")

cat("\nAnálisis DBCA completado.\n")
