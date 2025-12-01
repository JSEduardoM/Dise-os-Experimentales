# ============================================
# 1) Cargar librerías
# ============================================
library(readxl)
library(dplyr)
library(tidyr)
library(stringr)
library(ggplot2)
library(agricolae)

# ============================================
# 2) Leer datos
# ============================================
df <- read_excel("Datos_Quinua.xlsx")

head(df)

str(df)

# Exploración rápida
df %>% group_by(Variedad, Fertilizante, Riego) %>%
  summarise(n=n(), mean_y = mean(Rendimiento_kg), sd_y = sd(Rendimiento_kg))

# Boxplot
ggplot(df, aes(x=Fertilizante, y=Rendimiento_kg, fill=Riego)) +
  geom_boxplot() + facet_wrap(~Variedad)

# Modelo mixto (Bloque como efecto aleatorio)
mod <- lmer(Rendimiento_kg ~ Variedad * Fertilizante * Riego + (1|Bloque), data=df)
summary(mod)
anova(mod)

# Comprobación de supuestos
plot(resid(mod) ~ fitted(mod))
library(lmtest)
bptest(lm(Rendimiento_kg ~ Variedad*Fertilizante*Riego + Bloque, data=df)) # Breusch-Pagan

# Comparaciones post-hoc
emm <- emmeans(mod, ~ Fertilizante | Variedad)
pairs(emm, adjust="tukey")