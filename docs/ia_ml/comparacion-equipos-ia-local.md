---
title: Comparación equipos IA local
date: 2026-06-01
category: IA/ML
slug: comparacion-equipos-ia-local
tags: ['IA/ML']
---

# Comparación equipos IA local


> **Pregunta original:**
> 
Que tal este por 200€ AMD Ryzen 5 6600H 16GB 512G
> Tengo estos dos equipos y quiero ejecutar Ia local , principalmente llama.cpp y ollama.
AMD R7 8745HS con OCulink, 16GB, 512GB SSD - 400€
AMD Ryzen5 5500U 16GB 512GB - 140€
Tambien adujon el coste
> No pieso comprar GU externa

---


## Respuesta


Por **200€**, el **Ryzen 5 6600H** me parece el punto más interesante de los tres.

## Cómo los ordenaría para IA local

| CPU | Precio | Valor |
|------|------:|------|
| Ryzen 5 5500U | 140€ | Muy barato pero limitado |
| Ryzen 5 6600H | 200€ | Mejor equilibrio |
| Ryzen 7 8745HS + OCuLink | 400€ | Mejor plataforma a largo plazo |

## Comparativa

| Aspecto | 5500U | 6600H | 8745HS |
|----------|----------:|----------:|----------:|
| Arquitectura | Zen 2 | Zen 3+ | Zen 4 |
| Núcleos/Hilos | 6/12 | 6/12 | 8/16 |
| PassMark aprox | 12-13k | 18k | 28k | 
| RAM | DDR4 | DDR5 | DDR5 |
| PCIe | 3.0 | 4.0 | 4.0 |
| IA CPU | Básica | Buena | Muy buena |
| Expansión GPU | Normal | Depende modelo | OCuLink | 

El salto entre 5500U y 6600H es bastante grande. En benchmarks CPU el 6600H suele estar alrededor de un **40-50% por encima** del 5500U. citeturn0search1turn0search5

Y el 8745HS sigue estando aproximadamente otro **50% por encima del 6600H**. citeturn0search2turn0search4

## Para Ollama y llama.cpp

### Ryzen 5 5500U

- Llama 3 8B Q4 → usable.
- Qwen 8B → usable.
- 14B → empieza a ser lento.
- Contextos grandes → se nota.

### Ryzen 5 6600H

- 8B Q4/Q5 → bastante cómodo.
- 14B Q4 → razonable.
- Embeddings → mejor.
- RAG pequeño → viable.
- Mucho mejor tiempo de respuesta.

Además tiene DDR5 y más ancho de banda de memoria, algo que ayuda bastante en inferencia CPU. citeturn0search1turn0search5

### Ryzen 7 8745HS

- Mejor para 14B.
- Más margen para multitarea.
- Mucho más interesante si luego añades GPU externa.

## Mi valoración por precio

### 5500U por 140€

Compra racional si:

- quieres gastar casi nada;
- aprender Ollama;
- ejecutar 7B/8B.

### 6600H por 200€

Probablemente la mejor compra.

Pagas 60€ más y obtienes:

- arquitectura más moderna;
- DDR5;
- PCIe 4.0;
- ~45% más rendimiento CPU;
- mejor longevidad. citeturn0search1turn0search5

### 8745HS por 400€

Sólo lo elegiría si:

- tiene RAM ampliable;
- realmente vas a usar OCuLink;
- planeas poner una RTX más adelante.

Sin GPU externa, la diferencia de precio empieza a ser difícil de justificar.

## Mi ranking

1. **6600H por 200€** → mejor relación rendimiento/precio.
2. **8745HS por 400€** → mejor plataforma futura.
3. **5500U por 140€** → sólo si el presupuesto es muy ajustado.

Si me dices el modelo exacto del 6600H (GMKtec, Beelink, Firebat, Chuwi, etc.) puedo mirar si lleva RAM soldada, número de SSD, consumo real y si tiene alguna forma de expansión interesante.
---


Entonces cambia bastante la recomendación.

Si **descartas completamente GPU externa**, el valor del 8745HS baja mucho.

## Lo que realmente importa para Ollama sin GPU

En CPU pura, el orden sería:

1. Ryzen 7 8745HS
2. Ryzen 5 6600H
3. Ryzen 5 5500U

Pero el problema es el coste.

| CPU | Precio | Rendimiento relativo aprox |
|------|------:|------:|
| 5500U | 140€ | 1.0x |
| 6600H | 200€ | 1.4-1.5x |
| 8745HS | 400€ | 2.0-2.3x |

La mejora del 8745HS existe, pero no es proporcional al precio.

## Para los modelos que probablemente usarás

### Llama 3.1 8B Q4
### Qwen3 8B Q4
### Gemma 3 12B Q4

El 6600H ya ofrece una experiencia bastante razonable.

No vas a decir:
> "esto es insufrible"

como puede ocurrir con CPUs U antiguas.

## Además el 6600H tiene varias ventajas modernas

- Zen 3+
- DDR5
- PCIe 4.0
- mejor eficiencia energética
- iGPU bastante mejor
- mejor ancho de banda de memoria

Y en llama.cpp el ancho de banda de memoria importa mucho.

## El problema real sigue siendo la RAM

Más que la CPU.

Si esos equipos tienen:

- 16 GB soldada → me lo pensaría.
- 16 GB ampliables a 32 GB → mucho mejor.
- 2 slots DDR5 → ideal.

Para Ollama, pasar de 16 GB a 32 GB suele notarse más que pasar de 6600H a una CPU ligeramente superior.

## Qué compraría yo

### 140€ → 5500U

Sólo si quieres el mínimo gasto posible.

### 200€ → 6600H

Es el punto dulce.

Por 60€ más que el 5500U obtienes una mejora importante.

### 400€ → 8745HS

Sin eGPU, me cuesta justificarlo.

Por esos 200€ extra no duplicas la experiencia real en Ollama.

## Mi conclusión

Si los tres están en buen estado:

- **6600H por 200€ → compra más equilibrada.**
- **5500U por 140€ → compra económica muy razonable.**
- **8745HS por 400€ → sólo tendría sentido si valoras mucho el rendimiento CPU y planeas usarlo varios años.**

Ahora mismo, para ejecutar modelos 7B–14B cuantizados en Ollama y llama.cpp, yo me quedaría con el **Ryzen 5 6600H** casi sin dudarlo, siempre que la RAM sea ampliable a 32 GB.
---


Para **IA local con llama.cpp y Ollama**, la diferencia entre esos dos equipos es mucho mayor de lo que parece viendo solo el precio.

## Comparación rápida

| Aspecto | Ryzen 7 8745HS + OCuLink | Ryzen 5 5500U |
|----------|----------|----------|
| Arquitectura | Zen 4 | Zen 2 |
| Núcleos / hilos | 8 / 16 | 6 / 12 |
| Rendimiento CPU | Muy superior | Aceptable |
| Memoria soportada | Más rápida | Más limitada |
| Posibilidad eGPU | Sí (OCuLink) | No |
| LLM en CPU | Bastante mejor | Justito |
| Futuro | Muy ampliable | Limitado |
| Precio | 400€ | 140€ |

## Para llama.cpp

Si vas a ejecutar modelos cuantizados en CPU:

- 7B Q4/Q5 → ambos pueden hacerlo.
- 8B modernos (Llama 3.1, Qwen 3, Gemma 3) → mejor en el 8745HS.
- 14B → el 8745HS sigue siendo usable; el 5500U empieza a sufrir.
- 32B → ninguno es ideal sólo con CPU.

El 8745HS suele dar aproximadamente entre **2 y 3 veces más rendimiento real** en inferencia CPU respecto al 5500U dependiendo del modelo y del contexto.

## Lo importante: OCuLink

Aquí está la clave.

Con OCuLink puedes conectar:

- RTX 3060 12GB
- RTX 4060 8GB
- RTX 4070 12GB
- RTX 3090 24GB
- RTX A5000 24GB

y convertir el mini-PC en una estación de IA bastante seria.

Con una RTX 3090 de segunda mano:

- Llama 3.1 8B → muy rápido.
- Qwen3 32B Q4 → viable.
- DeepSeek distill 32B → viable.
- Modelos de visión → mucho mejor.

El 5500U no tiene esa vía de crecimiento.

## Problema común: RAM

Ambos vienen con **16 GB**.

Para IA local esto es más preocupante que la CPU.

### 16 GB

Bien para:

- 7B Q4
- 8B Q4
- pequeños modelos de embedding

### 32 GB

Empieza a ser cómodo para:

- 14B Q4
- multitarea
- contextos grandes

### 64 GB

Ideal si vas en serio con llama.cpp CPU.

Antes de comprar el 8745HS comprobaría:

- si la RAM es ampliable;
- máximo soportado (32 o 64 GB);
- número de slots.

## Relación rendimiento/precio

### Ryzen 5 5500U — 140€

Ventajas:

- extremadamente barato;
- excelente para experimentar;
- difícil encontrar algo mejor por 140€.

Desventajas:

- poco recorrido;
- CPU antigua;
- sin camino claro hacia GPU dedicada.

### Ryzen 7 8745HS — 400€

Ventajas:

- mucho más rápido;
- Zen 4;
- OCuLink;
- mejor inversión a medio plazo.

Desventajas:

- cuesta casi 3 veces más;
- sigue necesitando ampliar RAM para sacarle partido.

## Qué compraría según objetivo

### Quiero gastar lo mínimo y probar Ollama

→ Ryzen 5 5500U por 140€.

Por ese precio es difícil equivocarse.

### Quiero un equipo para IA local durante varios años

→ Ryzen 7 8745HS.

El sobrecoste no está en la CPU; está en el **OCuLink** y en la posibilidad de añadir una GPU potente después.

### Quiero montar algo serio

Mi estrategia sería:

- 8745HS (400€)
- ampliar a 32 GB o 64 GB
- más adelante RTX 3090 usada

Eso acaba siendo muchísimo más potente que cualquier configuración basada en el 5500U.

Si me dices el modelo exacto del mini-PC 8745HS y si la RAM es ampliable, puedo estimar cuántos tokens/s obtendrías en llama.cpp con Llama 3.1 8B, Qwen3 14B y Qwen3 32B.

---
*Generado desde conversación con 6 mensajes.*
*IA/ML*
