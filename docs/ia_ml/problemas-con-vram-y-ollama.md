---
title: Problemas con VRAM y Ollama
date: 2026-07-25
category: IA/ML
slug: problemas-con-vram-y-ollama
tags: ['IA/ML']
---

# Problemas con VRAM y Ollama


> **Pregunta original:**
> 
no tengo rocminfo
> veo rocm0 backend
> estoy en un ams AI 395 con 32 GB de ram unificada. Cuando le asigno 24GB a VRAM y 8 GB a sistema no, ollama no carga modelso de 18gbs  y no se el porque 

---


## Respuesta


Eso es una buena señal.

Si ves **`ROCm0 backend`**, significa que **Ollama sí está detectando la iGPU AMD y está usando el backend ROCm**. Es decir, el problema **no es que esté ejecutando en CPU**. citeturn0search2turn0search0

Entonces el problema probablemente esté en otro punto:

1. **El modelo no cabe realmente en la memoria disponible.** Un GGUF de 18 GB no necesita solo 18 GB. También requiere memoria para:
   - KV cache (depende del contexto).
   - Buffers temporales.
   - Espacio de trabajo de HIP/ROCm.
   
   En la práctica puede necesitar 22-26 GB o más. citeturn0search2

2. **La memoria libre de la iGPU no son los 24 GB completos.** Aunque reserves 24 GB en la BIOS, parte ya está ocupada por el sistema gráfico y por el propio runtime de ROCm.

3. **El contexto (`num_ctx`) puede estar consumiendo varios GB.** Ollama usa por defecto 4096 tokens, pero si has aumentado el contexto a 8192, 16384 o más, el consumo de memoria crece de forma importante. citeturn0search1

### Lo que necesito ver ahora

¿Puedes ejecutar estos dos comandos?

```bash
ollama ps
```

y

```bash
OLLAMA_DEBUG=1 ollama run <nombre_del_modelo>
```

(o, si Ollama está como servicio):

```bash
journalctl -u ollama -n 100
```

Lo que busco es una línea similar a:

```
runner.vram="xx.x GiB"
runner.size="xx.x GiB"
```

Esa información indica cuánto **calcula Ollama que necesita realmente** el modelo. En muchos casos el modelo ocupa 18 GB en disco, pero Ollama estima una necesidad de VRAM bastante superior y por eso rechaza cargarlo completamente en la GPU. citeturn0search2

Una última pregunta: **¿qué modelo exacto es?** (por ejemplo, `gemma3:27b`, `qwen3:30b-q4_K_M`, `qwen3-coder`, etc.). Con el nombre exacto puedo estimar el consumo esperado de memoria.
---


Hay varias posibilidades. El hecho de que asignes **24 GB de UMA/VRAM en BIOS** no significa que Ollama pueda utilizar automáticamente esos 24 GB para el modelo.

Necesitaría ver tres cosas para confirmarlo, pero te adelanto las causas más probables.

## 1. La RAM unificada no funciona como una VRAM dedicada

En un Ryzen AI 9 HX 395, esos **24 GB son memoria reservada para la iGPU**. Sin embargo:

- el driver AMD puede no permitir que un único proceso use toda esa memoria.
- llama.cpp (que usa Ollama) tiene sus propios límites.
- el modelo necesita memoria adicional para el contexto (KV cache), no solo para los pesos.

Por ejemplo, un modelo GGUF de **18 GB** puede terminar necesitando:

- 18 GB → pesos
- 2-6 GB → KV Cache
- 500 MB-2 GB → buffers

En total puede superar fácilmente los **22-25 GB**.

Si realmente solo quedan 24 GB para la GPU, ya vas muy justo.

---

## 2. ¿Está cargando en CPU?

Lo primero que comprobaría es:

```bash
ollama ps
```

y

```bash
ollama run tu_modelo
```

En otra terminal:

```bash
radeontop
```

o

```bash
rocm-smi
```

Si la GPU no tiene actividad, significa que Ollama ha decidido no usarla.

---

## 3. ¿Usas ROCm?

En Linux ejecuta:

```bash
rocminfo
```

Si no aparece tu iGPU Strix Point, Ollama probablemente esté ejecutando únicamente en CPU.

---

## 4. El modelo puede ser demasiado grande para la aceleración parcial

Ollama no hace exactamente:

> "24 GB disponibles → cargo un modelo de 24 GB"

Hace algo parecido a:

```
modelo
+
KV Cache
+
workspace
+
buffers
+
fragmentación
```

Si cualquiera de esos supera el límite, rechaza la carga GPU.

---

## 5. ¿Qué modelo es?

No es lo mismo:

- Gemma 3 27B Q4
- Qwen3 30B A3B
- DeepSeek R1
- Llama 3.3 70B

El tamaño del GGUF por sí solo no dice toda la historia.

---

## 6. La versión de Ollama importa

Las últimas versiones han mejorado bastante el soporte para las APU Ryzen AI.

Comprueba:

```bash
ollama --version
```

---

# Lo que me gustaría ver

Pásame la salida de estos comandos:

```bash
ollama --version
```

```bash
ollama ps
```

```bash
rocminfo
```

```bash
free -h
```

y también:

```bash
cat /proc/meminfo | grep -E "MemTotal|MemAvailable"
```

Y dime:

- distribución (Ubuntu 26.04, Fedora 42, etc.)
- versión del kernel (`uname -r`)
- versión de ROCm instalada
- nombre exacto del modelo (por ejemplo `qwen3:30b-q4_K_M`)

Con esos datos normalmente se puede identificar el cuello de botella con bastante precisión. También me interesa saber **qué error muestra Ollama**: si indica que no hay memoria suficiente, si descarga el modelo a CPU, o si simplemente termina el proceso.
---


Ese dato ya es bastante revelador.

Si **no tienes `rocminfo`**, es muy probable que **no tengas instalado ROCm** (o al menos no sus herramientas), y ahí puede estar el problema.

## Primero: ¿qué sistema operativo usas?

- Ubuntu 24.04 / 26.04
- Fedora
- Arch
- Windows
- Otro

Porque el soporte cambia bastante.

## Segundo: comprueba si Ollama está usando la GPU

Ejecuta:

```bash
ollama ps
```

Si ves algo parecido a:

```
PROCESS          MODEL        PROCESSOR
qwen3:30b        100% CPU
```

entonces ya sabemos que no está usando la iGPU.

Si aparece algo como:

```
PROCESSOR
80% GPU
20% CPU
```

entonces sí la está utilizando.

## Tercero: comprueba qué detecta Ollama

Ejecuta:

```bash
ollama serve
```

(o si ya está ejecutándose como servicio:)

```bash
journalctl -u ollama -f
```

Al arrancar suele escribir mensajes como:

```
AMD GPU detected
```

o

```
no compatible GPUs found
```

Eso nos dice inmediatamente qué está ocurriendo.

## Hay otro detalle importante

Has comentado que estás en un **Ryzen AI 9 HX 395 con 32 GB de memoria unificada**.

El soporte de las **iGPU RDNA 3.5 (Radeon 890M)** en Ollama/Linux ha mejorado mucho, pero depende de tres cosas:

- Kernel suficientemente reciente (6.12+ suele ir mejor).
- Drivers Mesa/AMDGPU actualizados.
- Una versión de Ollama con soporte para esa generación de GPU.

No siempre es necesario instalar el paquete completo de ROCm, porque Ollama puede usar sus propias bibliotecas o depender del stack del sistema. Pero si no detecta la GPU, no aprovechará esos 24 GB reservados.

### Lo siguiente que necesito

Pásame la salida de estos comandos:

```bash
uname -r
```

```bash
cat /etc/os-release
```

```bash
ollama --version
```

```bash
ollama ps
```

Con esos cuatro datos podremos determinar si el problema es:
- que Ollama no detecta la iGPU,
- que la versión de Ollama no soporta correctamente el HX 395,
- o que la memoria reservada no es el factor limitante.

---
*Generado desde conversación con 6 mensajes.*
*IA/ML*
