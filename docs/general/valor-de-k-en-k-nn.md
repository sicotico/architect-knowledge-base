---
title: Valor de k en k-NN
date: 2025-05-27
category: General
slug: valor-de-k-en-k-nn
tags: ['General']
---

# Valor de k en k-NN


> **Pregunta original:**
> 
Se quiere implementar un algoritmo de k-vecinos más cercanos y se desea que el modelo sea bastante flexible. ¿Qué valor del parámetro k

se debe tomar?
Pregunta 4 Respuesta
a.

Un valor bajo
b.

Un valor alto


---


## Respuesta


La respuesta correcta es:

**a. Un valor bajo**

### Explicación:
El parámetro **k** en el algoritmo de **k-vecinos más cercanos (k-NN)** controla cuántos vecinos se consideran al tomar una decisión de clasificación o regresión.

- Un **valor bajo de k** (por ejemplo, 1 o 3) hace que el modelo sea **más flexible** y se adapte más a los datos de entrenamiento. Esto puede capturar patrones locales con más precisión, pero también puede llevar al **sobreajuste (overfitting)** si no se controla adecuadamente.
- Un **valor alto de k** suaviza las decisiones del modelo y lo hace **menos flexible**, ya que promedia entre más puntos y puede pasar por alto detalles finos del conjunto de datos. Esto reduce el riesgo de sobreajuste, pero también puede causar **subajuste (underfitting)**.

Como la pregunta dice explícitamente que se desea que el modelo sea **bastante flexible**, entonces la opción correcta es:

> **a. Un valor bajo**.

---
*Generado desde conversación con 2 mensajes.*
*General*
