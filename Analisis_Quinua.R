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
