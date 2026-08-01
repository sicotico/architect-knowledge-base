---
title: Familias de procesadores AMD
date: 2026-07-10
category: IA/ML
slug: familias-de-procesadores-amd
tags: ['IA/ML']
---

# Familias de procesadores AMD


> **Pregunta original:**
> 
Con todas esta gamas , lo que busco es memoria unificada para ejecutar llm , la NPU me da igual. ¿Que cpu es la que tengo que elegir?
> esto de AMD esta siendo una locura AMD Ryzen™ 7 H 255,AMD Ryzen™ 7 255, AMD Ryzen™ AI 9 HX 370. Explicame las familia 

---


## Respuesta


## Elección directa

Para ejecutar LLM aprovechando **memoria unificada/compartida**, la familia que debes buscar es:

# **AMD Ryzen AI Max / Ryzen AI Max+ — “Strix Halo”**

No el **Ryzen 7 255**, ni el **Ryzen AI 9 HX 370**.

Mi elección concreta sería:

- **Mejor equilibrio:** **Ryzen AI Max+ 392 con 128 GB**
- **Máximo rendimiento:** **Ryzen AI Max+ 395 con 128 GB**
- **Alternativa más económica:** **Ryzen AI Max 390 o 385 con 128 GB**

La cantidad de memoria es crítica: **elige 128 GB**, no 32 ni 64 GB, porque normalmente la LPDDR5X está soldada y no puede ampliarse después.

---

## Por qué Strix Halo es diferente

El Ryzen AI Max+ 395 utiliza:

- Bus de memoria **LPDDR5X de 256 bits**
- LPDDR5X-8000
- Aproximadamente **256 GB/s de ancho de banda**
- Hasta **128 GB de memoria unificada**
- Radeon 8060S integrada con **40 Compute Units**
- Hasta **96 GB configurables como memoria gráfica** oficialmente en equipos de 128 GB

AMD está utilizando precisamente esta plataforma para inferencia local de LLM grandes. citeturn547762search0turn238664search3turn238664search10

Esto es lo decisivo: no se trata únicamente de que la GPU pueda tomar RAM del sistema. Muchas iGPU hacen eso. La ventaja de Strix Halo es la combinación de:

1. Mucha RAM compartida.
2. Bus de 256 bits.
3. 256 GB/s de ancho de banda.
4. Una iGPU suficientemente grande para aprovecharlo.

---

## Comparación de las opciones

| Familia | Memoria | Bus/ancho de banda | iGPU | Valor para LLM |
|---|---:|---:|---:|---|
| Ryzen 7 255/H 255 | Depende del equipo | DDR5 dual-channel, relativamente lento | Radeon 780M, 12 CU | Bajo |
| Ryzen AI 9 HX 370 | Hasta 256 GB teóricos según plataforma | 2 canales, normalmente LPDDR5X | Radeon 890M, 16 CU | Aceptable para modelos pequeños/medianos |
| Ryzen AI Max 385/390 | Hasta 128 GB | 256-bit LPDDR5X-8000 | Radeon 8050S, 32 CU | Muy bueno |
| Ryzen AI Max+ 392/395 | Hasta 128 GB | 256-bit LPDDR5X-8000 | Radeon 8060S, 40 CU | La mejor opción AMD |

El HX 370 admite configuraciones de memoria amplias sobre el papel, pero solo tiene **16 CU** y una interfaz de memoria convencional de dos canales. Strix Halo duplica aproximadamente el ancho del bus y sube a 32 o 40 CU. citeturn547762search1turn547762search8turn238664search0turn238664search1

---

## Qué modelo elegir dentro de Strix Halo

### Ryzen AI Max+ 395

- 16 núcleos CPU.
- Radeon 8060S, 40 CU.
- Hasta 128 GB.
- Opción de máximo rendimiento.

Es apropiado si también harás compilaciones grandes, virtualización, renderizado o trabajo intensivo de CPU. Para inferencia LLM pura, sus 16 núcleos no siempre justifican todo el sobreprecio.

### Ryzen AI Max+ 392

- 12 núcleos CPU.
- La misma Radeon 8060S de **40 CU**.
- El mismo bus LPDDR5X de 256 bits.
- Hasta 128 GB.

Probablemente es la opción más racional para tu caso. Conserva la parte que más interesa para LLM —GPU y subsistema de memoria— y reduce la CPU respecto al 395. citeturn238664search1

### Ryzen AI Max 390

- 12 núcleos CPU.
- Radeon 8050S de 32 CU.
- 128 GB y LPDDR5X-8000 de 256 bits.

Pierdes alrededor de un 20 % de unidades gráficas frente a la 8060S, pero mantienes la característica clave: los 128 GB y el bus ancho. Puede ser una compra mejor si existe una diferencia grande de precio. citeturn238664search0

### Ryzen AI Max 385

- 8 núcleos CPU.
- Radeon 8050S de 32 CU.
- Mismo subsistema de memoria potencial.

Es la opción mínima que consideraría para una máquina dedicada principalmente a inferencia. citeturn238664search2

---

## Qué modelos caben aproximadamente

El tamaño exacto depende de la cuantización, la longitud de contexto y la caché KV.

| RAM total | Uso razonable |
|---:|---|
| 32 GB | 7B–14B cómodos; algunos 20B/30B muy cuantizados |
| 64 GB | 32B cómodos; 70B Q4 con restricciones |
| **128 GB** | 70B con cuantizaciones de mayor calidad; modelos MoE y algunos modelos de más de 100B cuantizados |

Un modelo 70B en Q4 suele ocupar alrededor de 40–45 GB solamente en pesos. Después hay que dejar espacio para:

- Sistema operativo.
- Aplicación.
- Caché KV.
- Contexto largo.
- Capas auxiliares.
- Otros procesos.

Por eso **64 GB puede cargar un 70B**, pero **128 GB es mucho más práctico**. AMD anuncia hasta 96 GB como memoria gráfica variable en configuraciones de 128 GB y ha mostrado uso local de modelos 70B; también ha ampliado el soporte de Vulkan/llama.cpp para modelos de hasta 128B cuantizados, aunque que “quepa” no significa que vaya a generar rápidamente. citeturn238664search5turn238664search15turn238664search18

---

## La limitación: ancho de banda

Para generación de tokens, muchos LLM cuantizados están limitados por el movimiento de pesos desde memoria, no por la potencia matemática máxima.

Los **256 GB/s** de Strix Halo son buenos para una APU, pero siguen por debajo de:

- GPU dedicada de gama alta.
- Apple M-series Max/Ultra.
- Aceleradores profesionales.

Como aproximación teórica, un modelo que ocupe 40 GB y que deba recorrerse una vez por token tendría un techo ideal de:

\[
256\ \text{GB/s} \div 40\ \text{GB} \approx 6,4\ \text{tokens/s}
\]

La implementación real puede quedar por debajo o comportarse de otra manera debido a cachés, atención, contexto, kernels y reparto CPU/GPU. Esto explica por qué Strix Halo es especialmente atractivo por **capacidad**, pero no necesariamente por máxima velocidad en modelos enormes.

---

## Software: la parte menos sólida

Actualmente las rutas más relevantes son:

- **llama.cpp con Vulkan**
- **llama.cpp con ROCm/HIP**
- **Ollama con backend ROCm**
- **LM Studio**, especialmente en Windows
- Herramientas compatibles con GGUF

AMD tiene soporte ROCm específico para Ryzen y documentación para Strix Halo, pero todavía existen requisitos concretos de kernel y posibles incidencias según la versión. AMD recomienda configuraciones específicas de Ubuntu/kernel para cargas LLM sobre Ryzen AI Max. citeturn547762search2turn547762search14turn547762search22turn547762search27

Por tanto:

- **Windows:** Vulkan suele ser la vía más sencilla.
- **Linux:** ROCm puede dar mejor rendimiento, pero requiere más atención a versiones y compatibilidad.
- No compraría el equipo suponiendo que cualquier aplicación CUDA funcionará sin modificaciones.

---

## Recomendación final

Para tu objetivo concreto:

> **Compra un equipo con Ryzen AI Max+ 392 y 128 GB LPDDR5X.**

Escogería el **Max+ 395** solamente si la diferencia de precio es pequeña o necesitas también mucha CPU.

Escogería un **Max 390 de 128 GB** si cuesta sensiblemente menos que el 392/395.

Evitaría:

- Ryzen 7 255/H 255.
- Ryzen AI 9 HX 370 para modelos grandes.
- Cualquier Strix Halo de solo 32 GB.
- 64 GB si pretendes usar regularmente modelos 70B.
- Equipos cuya BIOS o firmware no permita asignar una cantidad elevada de memoria a la iGPU.

La especificación prioritaria en el anuncio no es “Ryzen AI” ni los TOPS de la NPU. Debe decir:

> **Ryzen AI Max/Max+ + 128 GB LPDDR5X + Radeon 8050S/8060S.**
---


Voy a separar dos cosas que suelen confundirse: **memoria compartida con la iGPU** y una plataforma realmente adecuada para LLM grandes. Para este uso, pesan más el ancho de banda, la cantidad de RAM direccionable por la GPU y el soporte del software que la NPU.
---


Sí, la nomenclatura de AMD se ha vuelto especialmente confusa porque mezcla **arquitectura, gama comercial, consumo y capacidad de IA**, y además está rebautizando procesadores anteriores.

## La idea fundamental

Estos nombres pertenecen realmente a **dos familias tecnológicas diferentes**:

| Procesador | Familia comercial | Arquitectura | CPU | Gráfica integrada | NPU |
|---|---|---|---:|---|---|
| **Ryzen 7 H 255** | Ryzen 200 | Zen 4, Hawk Point | 8 núcleos / 16 hilos | Radeon 780M | No |
| **Ryzen 7 255** | Ryzen 200 | Zen 4, Hawk Point | 8 núcleos / 16 hilos | Radeon 780M | No |
| **Ryzen AI 9 HX 370** | Ryzen AI 300 | Zen 5/Zen 5c, Strix Point | 12 núcleos / 24 hilos | Radeon 890M | Sí, 50 TOPS |

El **Ryzen AI 9 HX 370 está una generación tecnológica por encima**. Los 255 son básicamente una continuación o renombrado de productos Zen 4 anteriores. citeturn173798search2turn392321search2turn392321search23

---

# 1. Ryzen 7 H 255

El **Ryzen 7 H 255** pertenece a la serie Ryzen 200, pero utiliza la arquitectura **Zen 4 “Hawk Point”**, no Zen 5.

Sus características principales son:

- 8 núcleos y 16 hilos.
- Frecuencia aproximada de hasta 4,9 GHz.
- Radeon 780M integrada, con 12 unidades de cómputo.
- TDP nominal de unos 45 W, configurable aproximadamente entre 35 y 54 W.
- Memoria DDR5-5600 o LPDDR5X-7500.
- Sin NPU Ryzen AI habilitada. citeturn173798search2turn173798search8

El punto importante es que se parece muchísimo al anterior **Ryzen 7 8745H**. En la práctica, puede considerarse una actualización comercial o rebautizado de ese procesador, no un diseño realmente nuevo. citeturn173798search8turn173798search16

### Lo bueno

- CPU todavía muy competente.
- Radeon 780M excelente para una iGPU Zen 4.
- Adecuado para mini-PC, programación, virtualización ligera y juegos sin gráfica dedicada.
- Suele aparecer en equipos con buena relación precio/rendimiento.

### Lo malo

- No tiene NPU activa.
- No es una arquitectura nueva pese al nombre “255”.
- La eficiencia depende mucho de la refrigeración y configuración de potencia del fabricante.
- Algunos vendedores lo promocionan como “AI PC” aunque el procesador no tenga acelerador neuronal habilitado.

---

# 2. Ryzen 7 255, sin la H

Aquí está una de las mayores fuentes de confusión.

El **Ryzen 7 255** que aparece en algunos mini-PC es, en esencia, la misma clase de procesador que el **Ryzen 7 H 255**:

- Zen 4.
- 8 núcleos y 16 hilos.
- Radeon 780M.
- Alrededor de 4,9–4,95 GHz.
- Sin NPU habilitada. citeturn173798search9turn173798search12

La diferencia entre “255” y “H 255” parece estar relacionada principalmente con el **mercado, el fabricante del equipo y la forma en que AMD registra el producto**, no con un salto arquitectónico relevante.

En otras palabras:

> **Ryzen 7 255 ≈ Ryzen 7 H 255 ≈ Ryzen 7 8745H**, con pequeñas diferencias de frecuencia o configuración de potencia.

No conviene asumir automáticamente que el 255 sin H es una versión de bajo consumo o de sobremesa. En mini-PC, el fabricante puede configurarlo a distintas potencias.

### El problema práctico

En una ficha de producto puede aparecer como:

- Ryzen 7 255.
- Ryzen 7 H 255.
- R7 255.
- Ryzen 7 255, 45 W.

Antes de comprar hay que comprobar:

1. Número de núcleos.
2. Radeon integrada.
3. Potencia sostenida configurada.
4. Refrigeración.
5. Existencia o no de NPU.

La letra ausente no garantiza que sea otro chip.

---

# 3. Ryzen AI 9 HX 370

Este sí pertenece a una familia nueva: **Ryzen AI 300**, nombre interno **Strix Point**.

Tiene una configuración híbrida:

- 4 núcleos Zen 5.
- 8 núcleos compactos Zen 5c.
- 12 núcleos y 24 hilos en total.
- Hasta 5,1 GHz en los núcleos Zen 5.
- Radeon 890M con 16 unidades de cómputo RDNA 3.5.
- NPU XDNA 2 de hasta 50 TOPS.
- Potencia configurable entre 15 y 54 W. citeturn392321search2turn392321search9turn392321search23

Aquí “AI” no es solamente marketing. El procesador incluye una **NPU dedicada**, diseñada para ejecutar ciertos modelos y funciones de IA con menor consumo que utilizando continuamente CPU o GPU. citeturn392321search15turn392321search22

## Qué significa cada parte

### Ryzen AI

Indica la nueva familia con NPU más potente y arquitectura moderna. No debe confundirse con antiguos Ryzen 7040, 8040 o algunos Ryzen 200 que también podían incorporar una NPU más pequeña.

### 9

Es la categoría de producto. Está por encima de Ryzen AI 7 y Ryzen AI 5.

### HX

En esta nomenclatura señala un modelo de prestaciones elevadas. Sin embargo, el HX 370 sigue teniendo una ventana de potencia muy flexible: un fabricante puede configurarlo a 28 W y otro cerca de 54 W.

Por eso dos portátiles con el mismo HX 370 pueden rendir de forma bastante diferente.

### 370

Es el posicionamiento dentro de Ryzen AI 300. No significa “tercera generación, modelo 70” de una manera tan directa como ocurría antiguamente.

### Lo bueno

- CPU claramente más potente en multihilo que los Ryzen 7 255.
- Gráfica Radeon 890M más rápida.
- NPU de 50 TOPS.
- Mejor plataforma para portátiles premium y tareas futuras de IA local.
- Muy buen equilibrio entre CPU, iGPU y eficiencia.

### Lo malo

- Suele ser considerablemente más caro.
- La NPU todavía no acelera cualquier aplicación automáticamente.
- Su rendimiento depende mucho de los límites térmicos del portátil.
- En un equipo con gráfica dedicada potente, la ventaja de la Radeon 890M pierde importancia.
- Para ofimática, navegación o servidor doméstico, puede ser gasto innecesario.

---

# Cómo están organizadas las familias móviles recientes

## Ryzen 7000 y 8000

Aquí AMD mezcló múltiples arquitecturas bajo el mismo número de serie.

Por ejemplo, dentro de Ryzen 7000 móvil podían existir procesadores Zen 2, Zen 3, Zen 3+ y Zen 4. El tercer dígito ayudaba a identificar la arquitectura, pero para el comprador normal resultaba poco intuitivo.

Ejemplos conocidos:

- Ryzen 7 7730U: Zen 3.
- Ryzen 7 7840HS: Zen 4.
- Ryzen 7 8845HS: Zen 4 con una NPU ligeramente mejorada.

## Ryzen 200

Es una gama basada principalmente en tecnología **Hawk Point, Zen 4**, muy relacionada con Ryzen 8040 y otros modelos anteriores.

No debe confundirse con los Ryzen AI 300.

Dentro de esta familia aparecen nombres como:

- Ryzen 7 250.
- Ryzen 7 255.
- Ryzen 7 H 255.
- Ryzen 7 260.
- Ryzen 9 270.

Algunos modelos tienen una NPU antigua de hasta 16 TOPS; otros, como el H 255, no la tienen habilitada. Por ejemplo, el Ryzen 7 260 sí figura con NPU de hasta 16 TOPS, mientras que el H 255 aparece sin Ryzen AI disponible. citeturn392321search21turn173798search2

## Ryzen AI 300

Es la generación Zen 5 denominada Strix Point:

- Ryzen AI 5.
- Ryzen AI 7.
- Ryzen AI 9.
- Ryzen AI 9 HX.

Aquí encontramos el AI 9 365 y el AI 9 HX 370, entre otros. Es la familia diseñada específicamente alrededor de CPU Zen 5, GPU RDNA 3.5 y NPU XDNA 2. citeturn392321search17turn392321search23

---

# Traducción práctica de los sufijos

| Sufijo | Significado práctico |
|---|---|
| **U** | Bajo consumo, portátiles finos |
| **HS** | Alto rendimiento con consumo relativamente controlado |
| **H** | Alto rendimiento móvil, generalmente más potencia sostenida |
| **HX** | Categoría de máximo rendimiento, aunque depende de la familia |
| **PRO** | Funciones empresariales, gestión y seguridad |
| **X3D** | Caché 3D adicional, especialmente orientada a juegos |
| **AI** | Familia o modelo con NPU dedicada |

Estas letras son orientativas. Ya no permiten conocer por sí solas la arquitectura ni el rendimiento.

---

# Comparación directa

## CPU

El HX 370 dispone de 12 núcleos frente a los 8 de los 255. En trabajos como renderizado, compilación grande, máquinas virtuales o edición de vídeo, su ventaja puede ser considerable.

Para navegación, ofimática y programación normal, el Ryzen 7 255 ya ofrece potencia suficiente.

## Gráficos integrados

- **Radeon 780M:** muy buena iGPU, todavía capaz de ejecutar numerosos juegos a 1080p con ajustes moderados.
- **Radeon 890M:** aproximadamente la evolución superior, con 16 unidades de cómputo frente a 12 y arquitectura gráfica más reciente.

Pero la memoria importa muchísimo. Una 780M con DDR5 rápida y doble canal puede superar a una implementación mal configurada.

## IA

- Ryzen 7 255/H 255: sin NPU.
- Ryzen AI 9 HX 370: NPU de 50 TOPS.

Esto afecta principalmente a aplicaciones específicamente compatibles. No significa que el HX 370 sea automáticamente cinco veces más rápido en ChatGPT, navegación o IA ejecutada en servidores remotos.

## Consumo

El HX 370 es técnicamente más eficiente, pero también puede configurarse para consumir bastante. Un HX 370 limitado térmicamente puede rendir peor de lo esperado, mientras que un H 255 con buena refrigeración puede mantener frecuencias altas durante más tiempo.

---

# Mi lectura de esos tres nombres

**Ryzen 7 H 255 y Ryzen 7 255:** trátalos prácticamente como el mismo nivel. Son una plataforma Zen 4 madura, potente y normalmente más económica. Muy apropiada para mini-PC y equipos de buena relación calidad-precio.

**Ryzen AI 9 HX 370:** pertenece a otra categoría. Tiene más CPU, mejor iGPU, una NPU mucho más avanzada y una plataforma más moderna. Interesa para un portátil premium sin gráfica dedicada, desarrollo pesado, edición, multitarea intensa o IA local.

La regla más útil es esta:

> No compares el número 255 con el 370 como si fueran escalones consecutivos. El “Ryzen AI” y la arquitectura importan más que el número.

Para una compra concreta, el orden lógico sería:

**Ryzen AI 9 HX 370 > Ryzen 7 255 ≈ Ryzen 7 H 255**, pero el precio, la refrigeración, la RAM y los límites de potencia pueden alterar mucho el resultado final.
---


Voy a ordenar primero la nomenclatura y luego comparar esos tres modelos por arquitectura, iGPU, NPU y tipo de portátil. AMD mezcla generaciones y sufijos de forma bastante confusa.

---
*Generado desde conversación con 6 mensajes.*
*IA/ML*
