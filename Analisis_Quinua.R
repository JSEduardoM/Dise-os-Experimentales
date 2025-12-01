# ============================================
# 1) Cargar librerías
# ============================================
library(readxl)
library(dplyr)
library(tidyr)
library(stringr)
library(ggplot2)
library(agricolae)
library(lme4)        # Para lmer (modelos mixtos)
library(emmeans)     # Para comparaciones post-hoc
library(lmtest)      # Para pruebas de diagnóstico

# ============================================
# 2) Leer datos
# ============================================
# df <- read_excel("Datos_Quinua.xlsx")
df <- read.csv("~/SEMESTRE IX/DISEÑOS EXPERIMENTALES II/Diseños Experimentales II/quinua_simulada.csv",
               header = TRUE)

# Traducir nombres de columnas al español
df <- df %>%
  rename(
    Parcela = PlotID,
    Densidad_plantas_m2 = Densidad_plants_m2,
    Altitud_m = Altitud_m,
    Lluvia_mm = Lluvia_mm,
    pH_suelo = Soil_pH,
    Dias_a_cosecha = Dias_cosecha,
    Calidad_del_grano = Calidad_grano
  )

# Traducir valores de las variables categóricas
df <- df %>%
  mutate(
    Fertilizante = case_when(
      Fertilizante == "None" ~ "Ninguno",
      Fertilizante == "Low" ~ "Bajo",
      Fertilizante == "High" ~ "Alto",
      TRUE ~ Fertilizante
    ),
    Riego = case_when(
      Riego == "Low" ~ "Bajo",
      Riego == "High" ~ "Alto",
      TRUE ~ Riego
    )
  )

head(df)
str(df)

# ============================================
# 3) Exploración de datos
# ============================================
# Resumen por grupo
df %>% 
  group_by(Variedad, Fertilizante, Riego) %>%
  summarise(n = n(), 
            mean_y = mean(Rendimiento_kg), 
            sd_y = sd(Rendimiento_kg),
            .groups = 'drop')

# Boxplot
ggplot(df, aes(x = Fertilizante, y = Rendimiento_kg, fill = Riego)) +
  geom_boxplot() + 
  facet_wrap(~Variedad) +
  theme_minimal() +
  labs(title = "Rendimiento de Quinua por Tratamiento",
       y = "Rendimiento (kg)",
       x = "Fertilizante")

# ============================================
# 4) Modelo mixto (Bloque como efecto aleatorio)
# ============================================
mod <- lmer(Rendimiento_kg ~ Variedad * Fertilizante * Riego + (1|Bloque), 
            data = df)

# Resultados del modelo
summary(mod)
anova(mod)

# ============================================
# 5) Comprobación de supuestos
# ============================================
# Gráfico de residuos vs valores ajustados
plot(resid(mod) ~ fitted(mod),
     xlab = "Valores ajustados",
     ylab = "Residuos",
     main = "Residuos vs Valores Ajustados")
abline(h = 0, col = "red", lty = 2)

# QQ-plot para normalidad
qqnorm(resid(mod))
qqline(resid(mod), col = "red")

# Prueba de Breusch-Pagan para homocedasticidad
bptest(lm(Rendimiento_kg ~ Variedad*Fertilizante*Riego + Bloque, data = df))

# ============================================
# 6) Comparaciones post-hoc
# ============================================
# Comparaciones por Fertilizante dentro de cada Variedad
emm <- emmeans(mod, ~ Fertilizante | Variedad)
pairs(emm, adjust = "tukey")

# Comparaciones por Riego dentro de cada Variedad
emm_riego <- emmeans(mod, ~ Riego | Variedad)
pairs(emm_riego, adjust = "tukey")

# Interacción triple
emm_triple <- emmeans(mod, ~ Fertilizante * Riego | Variedad)
pairs(emm_triple, adjust = "tukey")

# ============================================
# 7) Visualización de medias estimadas
# ============================================
# Gráfico de interacción
emmip(mod, Fertilizante ~ Riego | Variedad, CIs = TRUE) +
  theme_minimal() +
  labs(title = "Interacción Fertilizante x Riego por Variedad",
       y = "Rendimiento estimado (kg)")

