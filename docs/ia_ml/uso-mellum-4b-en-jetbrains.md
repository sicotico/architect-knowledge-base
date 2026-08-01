---
title: Uso Mellum-4b en JetBrains
date: 2026-07-11
category: IA/ML
slug: uso-mellum-4b-en-jetbrains
tags: ['IA/ML']
---

# Uso Mellum-4b en JetBrains


> **Pregunta original:**
> 
que quier decir base y sft ?
> como uso los modelos Mellum-4b-base en los IDe de jetbrains ?
> SFT e como otro modelos que indican IT ?

---


## Respuesta


Voy a verificar qué integración admite JetBrains actualmente y qué limitaciones tiene **Mellum-4B-base**, porque el modelo base no suele funcionar como asistente de chat sin una capa adicional.
---


**Base** y **SFT** indican dos etapas distintas de entrenamiento del modelo.

## Base

Un modelo **base** es el modelo “en bruto” después del preentrenamiento.

Aprende patrones de lenguaje y código, pero no está especialmente entrenado para obedecer instrucciones.

Por ejemplo, ante:

```text
Corrige esta función y explica el error
```

un modelo base puede continuar el texto de forma poco predecible, en vez de responder de manera ordenada.

Es más útil para:

- investigación;
- fine-tuning propio;
- completar texto o código;
- construir modelos especializados encima.

## SFT

**SFT** significa **Supervised Fine-Tuning**, o ajuste supervisado.

El modelo base se entrena después con ejemplos del tipo:

```text
Instrucción → respuesta esperada
```

Por ejemplo:

```text
Usuario: completa esta función Python
Asistente: código corregido
```

Eso hace que el modelo siga mejor instrucciones y produzca respuestas más útiles para una tarea concreta.

## Diferencia práctica

| Tipo | Qué hace mejor |
|---|---|
| `Mellum-4b-base` | Continuar código, experimentación, fine-tuning |
| `Mellum-4b-sft-all` | Completar código de forma más controlada |
| `Mellum-4b-sft-python` | Completar principalmente Python |
| `Mellum-4b-sft-kotlin` | Completar principalmente Kotlin |

Una comparación simple:

- **Base**: sabe programar, pero no necesariamente sabe comportarse como asistente.
- **SFT**: sabe programar y ha sido entrenado para responder de una forma más concreta.

Para usarlo dentro de JetBrains como autocompletado, normalmente conviene más una variante **SFT**. Para entrenar tu propia variante, conviene empezar por **base**.
---


## Opción recomendada: Ollama + JetBrains AI Assistant

Puedes ejecutar **Mellum-4b-base localmente** y conectarlo a IntelliJ IDEA, PyCharm, WebStorm, GoLand, Rider y otros IDE de JetBrains mediante **AI Assistant**. Las versiones recientes de AI Assistant admiten modelos locales servidos por Ollama, LM Studio o endpoints compatibles con OpenAI. citeturn181542search4turn858037search5

### 1. Instala Ollama

Instala Ollama para tu sistema operativo y comprueba que funciona:

```bash
ollama --version
```

Descarga el modelo:

```bash
ollama pull JetBrains/Mellum-4b-base
```

El modelo publicado en Ollama ocupa aproximadamente **4,3 GB**, utiliza una ventana de contexto de **8192 tokens** y está cuantizado en Q8. citeturn858037search0turn858037search4turn858037search14

Comprueba que responde:

```bash
ollama run JetBrains/Mellum-4b-base
```

O prueba directamente la API:

```bash
curl http://localhost:11434/api/generate \
  -d '{
    "model": "JetBrains/Mellum-4b-base",
    "prompt": "def fibonacci(n):",
    "stream": false
  }'
```

Ollama normalmente expone su servidor en:

```text
http://localhost:11434
```

---

### 2. Instala AI Assistant en el IDE

En el IDE:

```text
Settings / Preferences
→ Plugins
→ Marketplace
→ AI Assistant
→ Install
```

Reinicia el IDE si lo solicita.

Las versiones actuales de JetBrains ofrecen soporte gratuito para modelos locales y completado de código; determinadas funciones cloud continúan sujetas a cuotas o planes de JetBrains AI. citeturn858037search15turn181542search6

---

### 3. Conecta Ollama

Abre:

```text
Settings / Preferences
→ Tools
→ AI Assistant
→ Providers & API Keys
```

Selecciona **Ollama** como proveedor local y configura:

```text
URL: http://localhost:11434
```

Pulsa la opción para comprobar la conexión o actualizar la lista de modelos. Debería aparecer:

```text
JetBrains/Mellum-4b-base
```

JetBrains documenta esta integración en la sección de modelos locales y proveedores externos. citeturn181542search4turn181542search10

---

### 4. Asigna Mellum al completado de código

En la configuración de AI Assistant, entra en la asignación de modelos o funciones:

```text
Settings
→ Tools
→ AI Assistant
→ Models
```

En **Code completion**, selecciona:

```text
JetBrains/Mellum-4b-base
```

Según la versión exacta del IDE, puede aparecer como:

```text
Feature configuration
→ Code completion
```

o dentro de:

```text
Providers & API Keys
→ Ollama
→ Configure feature models
```

Las versiones recientes permiten asignar explícitamente un modelo local al completado de código. citeturn181542search23turn181542search4

Después, abre un archivo compatible y empieza a escribir. Las sugerencias deberían aparecer como texto gris; normalmente se aceptan con `Tab`.

---

## Problema importante: `Mellum-4b-base` no es un modelo de chat

`Mellum-4b-base` es un modelo base entrenado principalmente para **continuación y completado de código**. No está ajustado para seguir instrucciones conversacionales. Por ello:

- Es apropiado para completar código.
- Puede funcionar mal en AI Chat.
- Puede ignorar instrucciones como “refactoriza esta clase”.
- Puede generar continuaciones en lugar de respuestas explicativas.
- Requiere que el cliente forme correctamente el contexto o el prompt de completado.

JetBrains describe Mellum-4b-base como un modelo centrado específicamente en code completion, no como un asistente general. citeturn181542search2turn858037search3

### Modelo preferible para uso cotidiano

Para completado multilenguaje, usaría:

```bash
ollama pull JetBrains/Mellum-4b-sft-all
```

Después selecciónalo en AI Assistant:

```text
JetBrains/Mellum-4b-sft-all
```

Este modelo deriva de Mellum-4b-base, pero ha sido ajustado para completado con contexto y múltiples lenguajes. También soporta el esquema fill-in-the-middle utilizado para insertar código en la posición del cursor. citeturn858037search2turn858037search6

También existen variantes específicas:

```bash
ollama pull JetBrains/Mellum-4b-sft-python
ollama pull JetBrains/Mellum-4b-sft-kotlin
```

La elección práctica sería:

| Uso | Modelo |
|---|---|
| Experimentos o fine-tuning | `Mellum-4b-base` |
| Proyectos multilenguaje | `Mellum-4b-sft-all` |
| Principalmente Python | `Mellum-4b-sft-python` |
| Principalmente Kotlin | `Mellum-4b-sft-kotlin` |
| Chat y razonamiento | Mellum2 Instruct/Thinking u otro modelo instruct |

---

## Lo bueno y lo malo

### Ventajas

- El código puede permanecer en tu equipo.
- No dependes de una API cloud para cada completado.
- El modelo es relativamente pequeño.
- La latencia puede ser baja con GPU adecuada.
- Está especializado en programación.
- Puedes ejecutarlo sin conexión después de descargarlo.

### Limitaciones

- La versión `base` no es apropiada para chat.
- 8192 tokens es un contexto relativamente limitado para proyectos grandes.
- La cuantización de Ollama consume alrededor de 4,3 GB solo para el archivo del modelo; durante la ejecución necesitarás memoria adicional.
- En CPU puede resultar lento.
- Un modelo de 4B parámetros suele tener peor razonamiento y comprensión global del proyecto que modelos más grandes.
- El código generado puede contener errores o vulnerabilidades; JetBrains advierte expresamente que las sugerencias no deben considerarse automáticamente seguras. citeturn858037search0
- No todas las funciones de AI Assistant son compatibles con todos los modelos locales; JetBrains puede recurrir a otro proveedor para funciones no soportadas cuando hay un servicio cloud configurado. citeturn181542search4

## Configuración que usaría

Para una instalación práctica:

```bash
ollama pull JetBrains/Mellum-4b-sft-all
ollama serve
```

Y en JetBrains:

```text
Proveedor: Ollama
Servidor: http://localhost:11434
Code completion: JetBrains/Mellum-4b-sft-all
AI Chat: un modelo Instruct distinto
```

Usaría `Mellum-4b-base` únicamente para pruebas, investigación o ajustes propios; para programar directamente dentro del IDE, `Mellum-4b-sft-all` es una elección más adecuada.
---


Sí. En muchos nombres de modelos, **IT** significa **Instruction-Tuned**.

La relación es:

- **SFT** describe el **método de entrenamiento**: ajuste supervisado con pares de entrada y respuesta.
- **IT** describe el **resultado o propósito**: un modelo ajustado para seguir instrucciones.

En la práctica, muchos modelos `-IT` han sido entrenados mediante SFT, aunque también pueden incluir otras etapas posteriores.

## Ejemplo

Un modelo base recibe durante el preentrenamiento textos como:

```text
def sumar(a, b):
```

y aprende a continuarlos.

Un modelo IT recibe ejemplos estructurados:

```text
Usuario: Escribe una función para sumar dos números.
Asistente: def sumar(a, b): return a + b
```

Por eso entiende mejor órdenes como:

```text
Explica este error
Refactoriza esta clase
Genera pruebas unitarias
```

## Diferencia de etiquetas

| Etiqueta | Significado |
|---|---|
| `Base` | Modelo preentrenado, sin ajuste conversacional específico |
| `SFT` | Modelo ajustado mediante aprendizaje supervisado |
| `IT` | Modelo preparado para seguir instrucciones |
| `Instruct` | Normalmente equivalente a `IT` |
| `Chat` | Ajustado específicamente para conversación |
| `RLHF` | Ajustado usando preferencias humanas |
| `DPO` | Ajustado mediante comparación de respuestas preferidas |

Un modelo puede ser simultáneamente:

```text
Base → SFT → IT → DPO
```

Por ejemplo, un modelo llamado `Model-7B-Instruct` probablemente partió de `Model-7B-Base`, pasó por SFT y quizá por DPO o RLHF.

Para JetBrains:

- **Autocompletado de código**: una variante SFT especializada en code completion puede ser mejor.
- **Chat, explicación y refactorización**: una variante `IT`, `Instruct` o `Chat` suele ser más adecuada.
- **Entrenamiento propio**: normalmente se empieza desde `Base`.

Así que **SFT e IT están relacionados, pero no significan exactamente lo mismo**. SFT es la técnica; IT es el tipo de comportamiento obtenido.

---
*Generado desde conversación con 7 mensajes.*
*IA/ML*
