---
title: Usar Whisper GGUF
date: 2025-04-09
category: General
slug: usar-whisper-gguf
tags: ['General']
---

# Usar Whisper GGUF


> **Pregunta original:**
> 
ahora como ejecuto whisper
> 
El audio estab en ingles y la trascripcion en español. Esto no tiene sentido. 
> Conviertela a PDF
> 
> *...y 7 preguntas de seguimiento*


---


## Respuesta


Aquí tienes tu infografía con los parámetros y ejemplos de uso para `whisper-cli`. ¡Lista para guardar o compartir!  
📁 [Descargar infografía](sandbox:/mnt/data/An_infographic_in_digital_graphic_design_format_ti.png)
---


¡Perfecto, Luis! 🎉 Ya lo tienes todo compilado con éxito, ahora viene lo divertido: **ejecutar Whisper para transcribir audio**.

---

## ✅ 1. Mueve tu modelo `.gguf` a la carpeta
Coloca tu modelo descargado (por ejemplo: `whisper-large-v3.gguf`) en un subdirectorio llamado `models`, dentro de `whisper.cpp`:

```bash
mkdir models
mv ~/Downloads/whisper-large-v3.gguf models/
```

*(Ajusta la ruta según dónde lo tengas descargado.)*

---

## 🎙️ 2. Coloca un archivo de audio

Ponte en el directorio raíz de `whisper.cpp` (ya estás ahí), y asegúrate de tener un archivo `.mp3`, `.wav`, o `.m4a`.

Ejemplo: digamos que tienes `audio.mp3` en `~/Documents`. Muévelo aquí también:

```bash
cp ~/Documents/audio.mp3 .
```

---

## 🚀 3. Ejecuta la transcripción

Desde el directorio `whisper.cpp`, ejecuta:

```bash
./build/bin/whisper-cli -m models/whisper-large-v3.gguf -f audio.mp3 -l es -otxt
```

### 📌 Explicación rápida:
- `-m`: modelo `.gguf`
- `-f`: archivo de audio
- `-l es`: idioma forzado a español
- `-otxt`: guarda la transcripción como `.txt` (además de mostrarla en consola)

---

## 📂 4. Ver el resultado

Se creará un archivo `audio.txt` con la transcripción. Puedes abrirlo con:

```bash
open audio.txt
```

---

¿Quieres que te prepare un script `.sh` para automatizar esto? ¿O necesitas convertir algún audio antes de probar?
---


Aquí tienes la infografía convertida a PDF:

📄 [Descargar PDF](sandbox:/mnt/data/An_infographic_in_digital_graphic_design_format_ti.pdf)
---


Totalmente de acuerdo, Luis — **¡eso no tiene sentido!** 😅 Si el audio está en inglés pero la transcripción salió en español, lo más probable es que el idioma se haya **forzado a español** por esta opción que usaste:

```bash
-l es
```

---

## 🧠 ¿Qué pasó?

Con `-l es`, le estás diciendo a Whisper:  
> “Transcribe como si el audio **fuera español** sí o sí.”

Entonces aunque el audio esté en inglés, Whisper **intentará encontrar palabras españolas que suenen como lo que escucha**. Resultado: una transcripción sin sentido. 😂

---

## ✅ Solución rápida

### 🔄 Deja que Whisper detecte el idioma automáticamente:

Simplemente **quita `-l es`** del comando:

```bash
./build/bin/whisper-cli -m models/whisper-large-v3-f16.gguf -f audio.wav -otxt
```

Así Whisper detectará que el audio está en inglés y hará la transcripción correcta.

---

## 📌 ¿Y si quieres traducirlo al español?

Si más adelante quieres **transcribir y traducir al español**, puedes usar la opción `-t translate` junto con `-l es`:

```bash
./build/bin/whisper-cli -m models/whisper-large-v3-f16.gguf -f audio.wav -l es -otxt -t translate
```

Esto dice:  
🎙️ audio en cualquier idioma → 📄 traducción al español.

---

¿Quieres que te prepare un mini script para automatizar esto según idioma? ¿O prefieres usar detección automática siempre?
---


¡Buen trabajo hasta ahora, Luis! 🙌 Ya estás ejecutando el modelo **a toda máquina**, pero el resultado es un archivo `.txt` **vacío**. Y eso tiene sentido por este mensaje clave:

---

### ⚠️ Mensaje importante:
```
whisper_full_with_state: input is too short - 380 ms < 1000 ms. consider padding the input audio with silence
```

Esto significa que el audio dentro de `Costes_IA.mp4` **solo dura 0.38 segundos**, y Whisper necesita **al menos 1 segundo** para funcionar bien. Como es demasiado corto, no genera nada útil.

---

## 🛠️ Soluciones rápidas:

### ✅ Opción 1: Verifica si el vídeo tiene audio

Prueba esto en terminal para ver cuánto dura el audio real:
```bash
ffmpeg -i Costes_IA.mp4
```

Busca una línea tipo:
```
Duration: 00:00:00.38, ...
```

Y asegúrate de que **sí tiene audio**. A veces los vídeos tienen imagen pero no pista de audio.

---

### ✅ Opción 2: Extrae el audio del vídeo (si hay uno más largo)

Si tienes otro vídeo más largo, puedes extraer solo el audio:

```bash
ffmpeg -i video_largo.mp4 -vn -acodec pcm_s16le -ar 16000 -ac 1 audio.wav
```

Y luego transcribir con Whisper:

```bash
./build/bin/whisper-cli -m models/whisper-large-v3-f16.gguf -f audio.wav -l es -otxt
```

---

### ✅ Opción 3: Rellenar con silencio artificial (si quieres forzar el test)

Si solo estás probando y quieres "engañar" a Whisper, puedes crear un archivo de audio con un segundo de silencio:

```bash
ffmpeg -f lavfi -i anullsrc=r=16000:cl=mono -t 1 silencio.wav
```

Y luego:

```bash
./build/bin/whisper-cli -m models/whisper-large-v3-f16.gguf -f silencio.wav -l es -otxt
```

---

¿Tienes otro archivo que quieras probar? Si me lo nombras o me dices dónde está, te ayudo con el comando exacto 👇
---


¡Sí, Luis! Con un **Mac con chip M4**, tienes **potencia de sobra**, y Whisper puede ir **mucho más rápido** si le das un poco más de cariño 💪.

Aquí te dejo cómo **exprimir al máximo tu Mac M4** para que Whisper vuele:

---

## ⚡️ 1. Usa más hilos de CPU

Por defecto, Whisper usa 4 hilos. Pero tu M4 tiene muchos más disponibles. Puedes decirle cuántos quieres usar con la opción `-t` (de **threads**):

```bash
./build/bin/whisper-cli -m models/whisper-large-v3-f16.gguf -f audio.wav -otxt -t 10
```

🧠 Recomendación:
- Usa **la mitad o un poco más** de los núcleos totales para evitar que se ralentice el sistema.
- Si tienes un **M4 Pro**, puedes probar con `-t 10` a `-t 14`.

---

## 🚀 2. Usa Metal (aceleración GPU)

Ya lo estás haciendo sin darte cuenta 😎. Este log que mostraste:

```
ggml_metal_init: GPU name:   Apple M4 Pro
...
whisper_backend_init_gpu: using Metal backend
```

Significa que ya está usando la **GPU integrada** gracias a Metal. Así que por ese lado estás full equipado.

---

## 🛠 3. ¿Otras opciones de rendimiento?

### ➕ Aumentar `-b` (beams) para más precisión (más lento, pero mejor calidad)
```bash
-b 5      # predeterminado
-b 7      # mejor precisión, más recursos
```

### ➕ Modo multiaudio (varios archivos)
Puedes procesar varios audios en lote para aprovechar más tiempo de ejecución:

```bash
for file in *.wav; do
  ./build/bin/whisper-cli -m models/whisper-large-v3-f16.gguf -f "$file" -otxt -t 12
done
```

---

## 🧪 BONUS: ¿Quieres saber cuántos hilos puedes usar?

Desde terminal:

```bash
sysctl -n hw.logicalcpu
```

Te dirá cuántos hilos lógicos tienes disponibles. Usa ese número como máximo para `-t`.

---

¿Quieres que te prepare un pequeño script que lo ejecute con los parámetros ideales para tu M4? ¿O te gustaría una GUI para no tener que recordar comandos?
---


¡Sí! 🙌 Si ya tienes **LM Studio**, te lo pongo fácil:

### 🔥 Pero... malas noticias (por ahora):  
**LM Studio actualmente solo sirve para modelos de lenguaje (LLMs)** como LLaMA, Mistral, etc., **pero no es compatible con modelos de audio como Whisper**, incluso si están en formato `.gguf`.

> ❌ **No puedes usar modelos Whisper en LM Studio directamente.**

---

### ✅ ¿Qué puedes hacer?

Ya que tienes LM Studio, lo más probable es que también estés en un entorno donde puedes usar herramientas similares. Aquí te dejo dos opciones fáciles:

---

## 🔁 Opción 1: Usar `whisper.cpp` (recomendado)
Como dijimos antes, puedes usar el modelo GGUF descargado con `whisper.cpp`.

👉 Esto funciona tanto en **Windows**, **macOS** como **Linux**.

#### Pasos rápidos (resumen):
1. Descarga [`whisper.cpp`](https://github.com/ggerganov/whisper.cpp).
2. Compílalo (o baja un ejecutable precompilado si usas Windows).
3. Ejecuta el modelo con tu archivo de audio.

Si me dices tu sistema operativo, te paso instrucciones detalladas con enlaces directos.

---

## 💡 Opción 2: Usar una herramienta GUI con soporte Whisper

Si prefieres una interfaz gráfica similar a LM Studio, aquí hay algunas apps que **sí usan Whisper GGUF**:

### 🎧 [`Whisper WebUI`](https://github.com/khanhas/whisper-webui)
- Interfaz gráfica en el navegador.
- Usa Whisper.cpp con modelos GGUF.
- Fácil de instalar con Python o como app de escritorio.
- Transcribe audios y vídeos con arrastrar y soltar.

También hay otras como:
- [`audacium`](https://github.com/Audacium/audacium) (Audacity moderno con soporte ASR).
- [`whisper-live`](https://github.com/pluja/whisper-live) (para transcripción en tiempo real).

---

¿Quieres que te guíe paso a paso con alguna de estas herramientas? ¿O prefieres seguir por consola con `whisper.cpp`?
---


¡Perfecto, ya estás casi! El error que tienes es este:

```
make: cmake: No such file or directory
```

### 🔧 ¿Qué significa?
Tu sistema no tiene instalado **CMake**, que es una herramienta necesaria para compilar `whisper.cpp`.

---

## ✅ Solución: Instalar CMake en macOS

Como estás en un Mac, puedes instalar CMake fácilmente usando **Homebrew**.

### 📦 Paso 1: Instala Homebrew (si no lo tienes)
Abre la terminal y ejecuta:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

> Si ya tienes Homebrew, puedes saltarte este paso.

---

### 📦 Paso 2: Instala CMake

```bash
brew install cmake
```

Esto instalará `cmake` y lo pondrá en tu PATH.

---

### 🚀 Paso 3: Vuelve a compilar

Una vez instalado CMake, vuelve al directorio donde clonaste `whisper.cpp` y ejecuta:

```bash
make
```

Esto debería compilar correctamente y generar el ejecutable `main`.

---

¿Quieres que luego te ayude con un ejemplo para transcribir un audio usando tu modelo `.gguf`?
---


¡Buena pregunta, Luis! En **macOS 15.4**, la forma más rápida y universal de extraer el audio de un vídeo es usando **`ffmpeg`**, que funciona de lujo desde la terminal.

---

## 🧰 Paso 1: Instala `ffmpeg` (si no lo tienes)

Si aún no lo tienes instalado, solo tienes que hacer esto en la terminal:

```bash
brew install ffmpeg
```

> Requiere [Homebrew](https://brew.sh), pero ya que antes usaste `brew`, probablemente ya lo tienes.

---

## 🎧 Paso 2: Extraer el audio del vídeo

Una vez instalado, ejecuta este comando:

```bash
ffmpeg -i Costes_IA.mp4 -vn -acodec pcm_s16le -ar 16000 -ac 1 audio.wav
```

### 🔍 Explicación:
- `-i Costes_IA.mp4`: tu archivo de vídeo
- `-vn`: ignora el vídeo
- `-acodec pcm_s16le`: guarda el audio sin compresión (formato compatible con Whisper)
- `-ar 16000`: tasa de muestreo (16 kHz, ideal para Whisper)
- `-ac 1`: audio mono
- `audio.wav`: archivo de salida

---

## ✅ Paso 3: Transcribe con Whisper

Luego simplemente:

```bash
./build/bin/whisper-cli -m models/whisper-large-v3-f16.gguf -f audio.wav -l es -otxt
```

---

Si el vídeo tiene varias pistas de audio (ej: español e inglés), puedes listarlas y seleccionar una específica. ¿Quieres que te enseñe eso también?
---


¡Perfecto! Has descargado un modelo de **Whisper** en formato **GGUF**, que es un formato optimizado para uso con **llama.cpp**, **whisper.cpp**, o aplicaciones que usen **GGML**/**GGUF** como backend, como **llamafile**, **llm**, o **chat-with-whisper**.

### 🧠 ¿Qué es Whisper?
[Whisper](https://github.com/openai/whisper) es un sistema de reconocimiento automático de voz (ASR) de OpenAI que convierte audio en texto. La versión que descargaste está en formato **GGUF**, lo que permite usarlo de forma eficiente sin necesidad de tener toda la potencia de una GPU.

---

## ✅ ¿Cómo usar un modelo GGUF de Whisper?

Lo más directo es usar el repositorio **whisper.cpp**, una reimplementación ligera y en C/C++ del modelo Whisper.

---

### 🔧 PASOS PARA USAR `whisper.cpp` CON TU MODELO GGUF

#### 1. **Clona el repositorio `whisper.cpp`** (si no lo tienes aún)
```bash
git clone https://github.com/ggerganov/whisper.cpp
cd whisper.cpp
```

#### 2. **Compílalo**
```bash
make
```

Esto generará un ejecutable llamado `main`.

---

#### 3. **Coloca el modelo `.gguf` donde quieras**
Por ejemplo, puedes ponerlo en un directorio llamado `models/`.

#### 4. **Transcribe un audio**
Asegúrate de tener un archivo de audio, por ejemplo `audio.mp3`, y ejecuta:

```bash
./main -m models/whisper-large-v3.gguf -f audio.mp3
```

Esto transcribirá el audio y mostrará el texto por pantalla.

---

### 🔄 Convertir otros formatos de audio (opcional)
Whisper soporta `.mp3`, `.wav`, `.m4a`, etc., pero si hay problemas puedes convertir el audio a un formato compatible:

```bash
ffmpeg -i entrada.mp3 -ar 16000 -ac 1 salida.wav
```

---

### 💡 Opciones útiles:
- `-m`: Ruta al modelo `.gguf`.
- `-f`: Archivo de audio.
- `-l`: Idioma forzado (por ejemplo `es` para español).
- `-otxt`: Guarda el resultado en un `.txt`.
- `-of`: Prefijo del archivo de salida.

Ejemplo completo:
```bash
./main -m models/whisper-large-v3.gguf -f mi_audio.mp3 -l es -otxt -of transcripcion
```

---

¿Quieres que te ayude a hacer un script para automatizar esto o a preparar un entorno (por ejemplo en Windows o Linux)? ¿O prefieres usar una interfaz gráfica?

---
*Generado desde conversación con 20 mensajes.*
*General*
