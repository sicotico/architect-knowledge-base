---
title: Análisis de log de servidor
date: 2026-07-21
category: General
slug: analisis-de-log-de-servidor
tags: ['General']
---

# Análisis de log de servidor


> **Pregunta original:**
> 
#!/usr/bin/env bash
set -euo pipefail

# llama-server para Gemma4 26B A4B IT QAT Q4_0 desde el blob de Ollama.
# Configuración pensada para RTX 5060 Ti 16 GB: contexto prudente, 1 slot,
# offload GPU completo cuando quepa y KV cache q8_0 para ahorrar VRAM.
#
# Variables útiles:
   LLAMA_HOST=0.0.0.0
   LLAMA_PORT=8080
   LLAMA_CTX=65536          # subir consume mucha VRAM/RAM
#   LLAMA_BATCH=1024
#   LLAMA_UBATCH=256
#   LLAMA_PARALLEL=1
#   LLAMA_THREADS=8
#   LLAMA_THREADS_BATCH=16
#   LLAMA_CACHE_RAM=4096
#   LLAMA_REASONING=auto    # auto|on|off

export LD_LIBRARY_PATH="$HOME/opt/llama.cpp-cuda/lib:$HOME/micromamba/envs/llama-cpp-cuda/lib:${LD_LIBRARY_PATH:-}"

LLAMA_SERVER="${LLAMA_SERVER:-$HOME/opt/llama.cpp-cuda/bin/llama-server}"
MODEL="${LLAMA_MODEL:-$HOME/.ollama/models/blobs/sha256-4c856523d61d77922dbc0b26753a6bf6208e5d69d80db0c04dcd776832d054c5}"

if [[ ! -x "$LLAMA_SERVER" ]]; then
  echo "ERROR: no existe o no es ejecutable: $LLAMA_SERVER" >&2
  exit 1
fi

if [[ ! -f "$MODEL" ]]; then
  echo "ERROR: no existe el modelo: $MODEL" >&2
  exit 1
fi

exec "$LLAMA_SERVER" \
  -m "$MODEL" \
  --alias "gemma4:26b-a4b-it-qat-q4_0,gemma4" \
  --host "${LLAMA_HOST:-0.0.0.0}" \
  --port "${LLAMA_PORT:-8080}" \
  --n-gpu-layers "${LLAMA_GPU_LAYERS:-999}" \
  --ctx-size "${LLAMA_CTX:-4096}" \
  --parallel "${LLAMA_PARALLEL:-1}" \
  --batch-size "${LLAMA_BATCH:-1024}" \
  --ubatch-size "${LLAMA_UBATCH:-256}" \
  --threads "${LLAMA_THREADS:-8}" \
  --threads-batch "${LLAMA_THREADS_BATCH:-16}" \
  --flash-attn on \
  --kv-offload \
  --op-offload \
  --repack \
  --mmap \
  --warmup \
  --cache-type-k q8_0 \
  --cache-type-v q8_0 \
  --cache-prompt \
  --cache-idle-slots \
  --cache-ram "${LLAMA_CACHE_RAM:-4096}" \
  --reasoning "${LLAMA_REASONING:-auto}" \
  --temp "${LLAMA_TEMP:-0.7}" \
  --top-p "${LLAMA_TOP_P:-0.95}" \
  --top-k "${LLAMA_TOP_K:-40}" \
  --min-p "${LLAMA_MIN_P:-0.0}" \
  --repeat-penalty "${LLAMA_REPEAT_PENALTY:-1.05}" \
  --prio "${LLAMA_PRIO:-2}" \
  --prio-batch "${LLAMA_PRIO_BATCH:-2}" \
  --poll "${LLAMA_POLL:-50}" \
  --poll-batch "${LLAMA_POLL_BATCH:-1}" \
  --threads-http "${LLAMA_THREADS_HTTP:-2}" \
  "$@"
> 0.00.169.799 I cmn  common_param: common_params_print_info: verbosity = 3 (adjust with the `-lv N` CLI arg)
0.00.271.080 I srv    load_model: loading model '/home/sico/.ollama/models/blobs/sha256-4c856523d61d77922dbc0b26753a6bf6208e5d69d80db0c04dcd776832d054c5'
0.00.728.719 W common_fit_params: failed to fit params to free device memory: n_gpu_layers already set by user to 999, abort
0.01.016.652 W load: override 'tokenizer.ggml.add_bos_token' to 'true' for Gemma4
0.01.065.812 W load: control-looking token:    212 '</s>' was not control-type; this is probably a bug in the model. its type will be overridden
0.01.066.168 W load: control-looking token:     50 '<|tool_response>' was not control-type; this is probably a bug in the model. its type will be overridden
0.01.084.845 W load: special_eog_ids contains '<|tool_response>', removing '</s>' token from EOG list
0.02.870.465 I srv    load_model: initializing, n_slots = 1, n_ctx_slot = 65536, kv_unified = 'false'
0.02.875.276 I srv  llama_server: model loaded
0.02.875.279 I srv  llama_server: listening on http://0.0.0.0:8080
0.58.344.858 I slot get_availabl: id  0 | task -1 | selected slot by LRU, t_last = -1
0.58.345.135 I slot launch_slot_: id  0 | task 0 | processing task, is_child = 0
1.00.013.207 I slot print_timing: id  0 | task 0 | prompt eval time =    1668.05 ms /  3553 tokens (    0.47 ms per token,  2130.03 tokens per second)
1.00.013.209 I slot print_timing: id  0 | task 0 |        eval time =       0.00 ms /     1 tokens (    0.00 ms per token, 1000000.00 tokens per second)
1.00.013.209 I slot print_timing: id  0 | task 0 |       total time =    1668.05 ms /  3554 tokens
1.00.013.210 I slot print_timing: id  0 | task 0 |    graphs reused =          1
1.00.013.406 I slot      release: id  0 | task 0 | stop processing: n_tokens = 3553, truncated = 0
> {
  "providers": {
    "ollama": {
      "baseUrl": "http://localhost:11434/v1",
      "api": "openai-completions",
      "apiKey": "ollama",
      "compat": {
        "supportsDeveloperRole": false,
        "supportsReasoningEffort": false
      },
      "models": [
        {
          "id": "gemma4:e4b",
          "name": "Gemma 4 8B (Local Ollama)",
          "reasoning": false,
          "input": ["text"],
          "contextWindow": 8192,
          "maxTokens": 4096,
          "cost": {
            "input": 0,
            "output": 0,
            "cacheRead": 0,
            "cacheWrite": 0
          }
        }
      ]
    },
    "tabby": {
      "baseUrl": "http://serveria.local:5000/v1",
      "api": "openai-completions",
      "apiKey": "$TABBY_API_KEY",
      "compat": {
        "supportsDeveloperRole": false,
        "supportsReasoningEffort": false,
        "supportsUsageInStreaming": false,
        "maxTokensField": "max_tokens"
      },
      "models": [
        {
          "id": "tabbyapi",
          "name": "TabbyAPI",
          "reasoning": false,
          "input": ["text"],
          "contextWindow": 32768,
          "maxTokens": 4096,
          "cost": {
            "input": 0,
            "output": 0,
            "cacheRead": 0,
            "cacheWrite": 0
          }
        }
      ]
    },
    "gemma4-llamacpp": {
      "baseUrl": "http://serveria.local:8080/v1",
      "api": "openai-completions",
      "apiKey": "no-key",
      "compat": {
        "supportsDeveloperRole": false,
        "supportsReasoningEffort": false,
        "supportsUsageInStreaming": false,
        "maxTokensField": "max_tokens"
      },
      "models": [
        {
          "id": "gemma4",
          "name": "Gemma4 25B (llama.cpp serveria.local)",
          "reasoning": false,
          "input": ["text"],
          "contextWindow": 4096,
          "maxTokens": 4096,
          "cost": {
            "input": 0,
            "output": 0,
            "cacheRead": 0,
            "cacheWrite": 0
          }
        }
      ]
    }
  }
}
> 
> *...y 3 preguntas de seguimiento*


---


## Respuesta


Ahora sí tiene sentido. Estás usando el **Pi Coding Agent** de pi.dev.

Y el log que has pasado indica un problema conocido en la integración entre **Pi + llama.cpp + algunos modelos**, especialmente **Gemma 4**.

## Lo que demuestra tu log

Hay dos evidencias claras:

1. El servidor recibe una petición para generar **un único token**:

```text
stopped by limit, n_decoded = 1, n_predict = 1
```

2. El servidor devuelve:

```json
"finish_reason":"length"
```

fileciteturn0file0L217-L240

Eso confirma que **el límite llega en la petición HTTP**, no desde tu script.

---

## Pero hay un detalle importante

Justo antes aparece:

```text
Grammar (tool_calls)
chat format: peg-gemma4
reasoning-budget...
```

fileciteturn0file0L57-L87

Eso significa que Pi no está haciendo una conversación normal.

Está iniciando una conversación **con herramientas (tool calling)**.

---

## Mi hipótesis

Creo que no es simplemente un `max_tokens=1` mal configurado.

Creo que Pi está haciendo una llamada inicial de negociación para decidir si el modelo quiere:

- responder,
- pensar,
- o llamar a una herramienta.

Con OpenAI esto funciona.

Con Gemma 4 parece que el primer token es:

```
<|channel>
```

y Pi corta la generación inmediatamente.

Hay varios usuarios reportando problemas muy parecidos con Gemma 4 y el formato de tool calling; algunos los han mitigado cambiando el chat template o ajustando cómo Pi interpreta las llamadas a herramientas. citeturn0reddit12turn0search2

---

# Hay una cosa que quiero comprobar

¿Puedes enseñar el contenido de:

```text
~/.pi/agent/models.json
```

Ahí debería aparecer algo parecido a:

```json
{
  "providers": {
    "llama-cpp": {
      "baseUrl": "http://serveria.local:8080/v1",
      "api": "openai-completions",
      "models": [
        {
          "id": "gemma4"
        }
      ]
    }
  }
}
```

Pi permite configurar compatibilidad por modelo, como `supportsDeveloperRole`, `supportsReasoningEffort` y otros parámetros específicos para servidores OpenAI compatibles. citeturn0search2

---

## También revisaría la versión de Pi

Hoy mismo se ha anunciado **Pi 0.81.0**, que añade soporte integrado para `llama.cpp`. Si estás usando una versión anterior, puede ser relevante actualizar antes de seguir depurando. citeturn0reddit18

## Mi valoración

### Lo que parece correcto

- `llama.cpp`: correcto.
- Tu script de arranque: correcto.
- Gemma 4 carga correctamente.
- El contexto de 65k no está provocando este fallo.

### Lo que parece estar fallando

La compatibilidad entre **Pi y Gemma 4** durante el inicio del flujo de herramientas. No descarto un bug en Pi o una incompatibilidad con el formato de chat de Gemma 4.

**El siguiente paso más útil** es revisar tu `models.json`. Con ese archivo podré decirte si es un problema de configuración (probablemente solucionable) o si estás chocando con una limitación conocida de la versión actual de Pi.
---


Ese log no muestra ningún error crítico. De hecho, el servidor ha cargado el modelo correctamente y está escuchando peticiones. Vamos línea por línea.

| Línea | Significado | ¿Preocupante? |
|-------|-------------|---------------|
| `verbosity = 3` | Nivel de log detallado. | No |
| `loading model ...` | Está cargando el GGUF. | No |
| `failed to fit params to free device memory` | Intentó ajustar automáticamente los parámetros a la VRAM libre, pero detectó que tú ya fijaste `n_gpu_layers=999`. Respeta tu configuración. | No |
| `override tokenizer.ggml.add_bos_token` | Ajuste específico para Gemma 4. | No |
| `control-looking token ...` | El modelo tiene algunos tokens especiales mal marcados y llama.cpp los corrige al cargar. | No |
| `special_eog_ids...` | Otra corrección automática del tokenizer. | No |
| `initializing n_ctx_slot = 65536` | Has configurado un contexto de **65.536 tokens**. | Sí, pero sólo por consumo de memoria. |
| `model loaded` | Modelo cargado correctamente. | Perfecto |
| `listening on http://0.0.0.0:8080` | Servidor listo. | Perfecto |

Luego llega una petición:

```
prompt eval time = 1668 ms / 3553 tokens
```

Eso significa:

- Prompt recibido: **3553 tokens**
- Procesados en **1,66 segundos**
- Velocidad de ingestión:
  **2130 tokens/s**

Es una velocidad muy buena para la fase de carga del prompt.

Después aparece:

```
eval time = 0 ms / 1 tokens
```

Eso llama la atención porque normalmente debería generar bastantes tokens.

Esto suele ocurrir cuando el cliente:

- pide `max_tokens=0`,
- cancela inmediatamente la generación,
- sólo solicita tokenización,
- o el modelo devuelve un token de fin (`EOS`) nada más empezar.

No parece un problema del servidor porque inmediatamente libera el slot:

```
stop processing: n_tokens = 3553
```

Es decir, ha terminado normalmente.

## Lo único que vigilaría

Esta línea:

```
n_ctx_slot = 65536
```

Con Gemma 4 es un contexto enorme.

Si tienes una RTX 5060 Ti de 16 GB, un contexto de 65k puede consumir varios GB únicamente en la caché KV.

Si no necesitas conversaciones tan largas, valores como:

- 8192
- 16384
- 32768

suelen ofrecer una mejor relación entre memoria y rendimiento.

## Lo que me gustaría comprobar

Si tu objetivo es optimizar OpenClaw con esa 5060 Ti, me interesa ver el bloque completo que aparece justo después de cargar el modelo. En concreto, busca las líneas similares a estas:

```
llama_model_loader:
llm_load_tensors:
CUDA0 model buffer size
KV self size
CPU buffer size
offloaded XX/XX layers
```

Esas líneas indican:

- cuánta VRAM ocupa realmente el modelo,
- cuánto ocupa la KV Cache,
- si todas las capas están en la GPU,
- y si estás desaprovechando memoria o vas muy justo.

Con ese bloque puedo decirte si `--ctx-size 65536` es una buena configuración para tu equipo o si conviene reducirlo.
---


Ese error **no parece venir de `llama.cpp`**, sino del cliente (Open WebUI o pi-agent). Significa que **la generación se ha cortado al alcanzar el límite de tokens de salida** (`max_tokens` o `num_predict`), no porque el modelo haya fallado.

Además, tu pregunta:

> ¿Qué modelo eres?, ¿cómo se llama el servidor donde te estás ejecutando?, ¿cuánto contexto tienes?

es interesante porque mezcla información que el modelo **conoce** con información que **no conoce**.

El modelo puede responder:

- "Soy Gemma 4 27B..." (si el sistema se lo indica o por el nombre del modelo).
- Explicar qué es el contexto.

Pero **no sabe**:

- que el servidor se llama `serveria.local`,
- que el contexto es de `65536`,
- ni que está ejecutándose en llama.cpp.

Eso sólo lo sabe el servidor o el cliente que hace la llamada.

---

## Lo primero que comprobaría

### 1. ¿Qué valor tiene `n_predict` en llama.cpp?

Si arrancas el servidor con algo como:

```bash
--n-predict 128
```

o

```bash
-n 128
```

el servidor nunca generará más de 128 tokens.

---

### 2. ¿Qué está enviando pi-agent?

Muchos clientes envían automáticamente:

```json
"max_tokens": 256
```

o incluso

```json
"max_tokens": 64
```

Cuando llega al límite aparece exactamente ese mensaje:

> Model stopped because it reached the maximum output token limit.

---

### 3. ¿Ocurre también desde Open WebUI?

Haz la misma pregunta directamente desde Open WebUI.

Si responde correctamente, entonces:

- llama.cpp está bien.
- El problema está en la configuración de pi-agent.

Si también falla desde Open WebUI, entonces el límite lo está imponiendo el servidor.

---

## Ese mensaje es típico de OpenAI

Me llama la atención el texto exacto:

> **Error: Model stopped because it reached the maximum output token limit.**

Ese mensaje no es el que genera `llama.cpp`; es muy parecido al que muestran clientes compatibles con la API de OpenAI. Es decir, probablemente **pi-agent** detecta que la respuesta terminó por alcanzar `max_tokens` y muestra ese aviso.

---

## Para localizar el origen

Necesitaría ver una de estas dos cosas:

1. **Cómo arrancas `llama-server`** (el comando completo).

o bien

2. La configuración del proveedor en **pi-agent** (captura o JSON), especialmente los campos:

- `max_tokens`
- `temperature`
- `context_window`
- `provider`
- `base_url`

Con eso podremos determinar si el límite lo está imponiendo el servidor o el cliente.
---


Ya está. El log identifica el problema con bastante precisión.

La línea clave es esta:

```text
stopped by limit, n_decoded = 1, n_predict = 1
```

y unas líneas después:

```text
finish_reason":"length"
```

fileciteturn0file0L217-L240

## ¿Qué significa?

`llama-server` **ha recibido una petición indicando que sólo puede generar 1 token**.

No es que el modelo decida parar.

No es que Gemma falle.

No es un problema del contexto.

Es literalmente:

```
n_predict = 1
```

Por eso únicamente genera:

```
<|channel>
```

y se detiene.

---

## ¿Quién está poniendo `n_predict = 1`?

No tu script.

Tu script no especifica `--n-predict`.

Por tanto el origen está en el cliente.

En este caso, **pi-agent**.

---

## Hay otra pista muy importante

Fíjate en esto:

```text
Grammar (tool_calls)
```

y después

```text
chat format: peg-gemma4
```

y justo el primer token que intenta generar es

```text
<|channel>
```

fileciteturn0file0L57-L87 fileciteturn0file0L214-L240

Eso indica que **pi-agent está usando el modo de herramientas (tool calling)**.

Gemma 4, cuando trabaja con herramientas, comienza generando precisamente tokens internos como:

```
<|channel>
<|tool_call>
```

Si el cliente sólo le permite generar **1 token**, nunca llega a escribir la respuesta.

---

# Conclusión

El problema **no está en llama.cpp**.

El problema **no está en Gemma**.

El problema es que **pi-agent está enviando `max_tokens=1` (o `n_predict=1`)**.

---

# Lo que haría ahora

Necesito ver la petición HTTP que envía pi-agent.

Lo más sencillo es capturarla.

Si tienes `curl` hacia el servidor, también puedes probar manualmente:

```bash
curl http://serveria.local:8080/v1/chat/completions \
-H "Content-Type: application/json" \
-d '{
  "model":"gemma4",
  "messages":[
    {"role":"user","content":"Hola"}
  ],
  "max_tokens":256
}'
```

Si eso funciona, queda confirmado al 100 % que el problema es pi-agent.

---

## Mi sospecha

Creo que conozco el origen.

Veo que el modelo intenta usar:

```
peg-gemma4
Grammar (tool_calls)
```

Eso suele ocurrir cuando el cliente activa **tool calling**.

Hay clientes que, al activar herramientas, hacen primero una llamada con:

```
max_tokens = 1
```

para comprobar si el modelo quiere invocar una herramienta.

Eso funciona con OpenAI, pero con llama.cpp + Gemma puede provocar exactamente el comportamiento que estás viendo.

### ¿Puedes decirme qué pi-agent estás usando?

Pásame el enlace del repositorio de GitHub (o el nombre exacto del proyecto). Con eso puedo revisar la implementación y localizar exactamente dónde está enviando `max_tokens=1`.
---


Gracias. La configuración es bastante razonable y **no veo nada que justifique un `max_tokens=1`**.

De hecho, veo varias cosas correctas:

- `maxTokens: 4096` ✔️
- `maxTokensField: "max_tokens"` ✔️ (llama.cpp usa ese campo)
- `api: "openai-completions"` ✔️
- `reasoning: false` ✔️

Por tanto, **el `models.json` no es el culpable**.

---

# Lo que sí sabemos con certeza

El log demuestra esto:

```
n_predict = 1
```

No hay interpretación posible. Al servidor **le ha llegado** una petición para generar un solo token. fileciteturn0file0L217-L240

---

# Entonces falta una pieza

Nos falta ver **la petición HTTP**.

Porque el `models.json` dice:

```
maxTokens = 4096
```

pero el servidor recibe

```
n_predict = 1
```

Eso significa que **alguien está sobrescribiendo ese valor antes de hacer la llamada**.

Puede ser:

- el propio agente,
- el modo Tool Calling,
- el SDK de Pi,
- o un bug.

---

# Yo probaría dos cosas

## 1. Probar con curl

Haz esta petición directamente al servidor:

```bash
curl http://serveria.local:8080/v1/chat/completions \
-H "Content-Type: application/json" \
-d '{
  "model":"gemma4",
  "messages":[
    {
      "role":"user",
      "content":"Hola"
    }
  ],
  "max_tokens":100
}'
```

Si Gemma responde normalmente, ya sabemos que:

- llama.cpp funciona
- el servidor funciona
- la API funciona

y el problema está exclusivamente en Pi.

---

## 2. Activar el log HTTP de llama.cpp

Dependiendo de la versión de llama.cpp puedes arrancarlo con mayor verbosidad (por ejemplo `-lv 5` o equivalente). El objetivo es ver el JSON que recibe.

Quiero encontrar algo parecido a:

```json
{
  "model":"gemma4",
  "messages":[...],
  "max_tokens":1
}
```

o

```json
{
  "n_predict":1
}
```

Si aparece eso, ya no habría ninguna duda.

---

# Hay una cosa que me llama muchísimo la atención

En tu log aparece:

```
Grammar (tool_calls)
```

Después:

```
<|channel>
```

Y se corta.

Eso es exactamente lo que ocurre cuando un cliente intenta hacer **Tool Calling** con Gemma.

Pi probablemente está haciendo una llamada previa para decidir si debe ejecutar una herramienta.

---

# Mi sospecha principal

Diría que el problema **no es de configuración**, sino de compatibilidad.

Gemma 4 utiliza un formato de chat y de tool calling diferente al de modelos como GPT o Qwen. Si Pi está implementando el protocolo pensando en esos modelos, puede enviar una primera petición de "sondeo" con un límite de un token para detectar llamadas a herramientas. En tu caso, el primer token generado es `<|channel>`, la generación termina por el límite y Pi interpreta que la respuesta quedó truncada.

---

## Una prueba muy útil

¿Qué ocurre si cambias temporalmente el proveedor a uno de estos modelos?

- Qwen 3 Instruct
- Llama 3.3 Instruct
- Gemma 4 desde **Ollama**

Si con cualquiera de ellos Pi funciona correctamente y **solo falla con Gemma 4 en llama.cpp**, la causa estaría muy acotada: una incompatibilidad específica entre Pi y el formato de chat/tool calling de Gemma en `llama.cpp`.

**Una última pregunta:** ¿qué versión exacta de `llama.cpp` estás usando? Puedes obtenerla ejecutando:

```bash
llama-server --version
```

Esa información es importante porque el soporte para Gemma 4 y su chat template ha cambiado bastante entre versiones recientes.
---


He revisado el script y **no veo nada que limite la longitud de la respuesta**.

De hecho, **no aparece ninguno de estos parámetros**:

```bash
--n-predict
-n
```

Por tanto, **llama-server no está imponiendo ese límite**.

---

# Entonces, ¿de dónde sale el error?

Las posibilidades, ordenadas de mayor a menor probabilidad, son:

## 1. pi-agent está enviando `max_tokens`

Es la explicación más probable.

En la API OpenAI-compatible, el cliente envía algo como:

```json
{
  "model": "gemma4",
  "messages": [...],
  "max_tokens": 256
}
```

Cuando llega a 256 tokens, aparece exactamente el mensaje que has visto.

---

## 2. Open WebUI tiene un límite configurado

En Open WebUI existe un parámetro parecido a:

```
Max Tokens
```

Muchas instalaciones vienen con:

```
256
512
1024
```

Si ese valor es pequeño también aparecerá ese aviso.

---

## 3. pi-agent está usando la Responses API

El texto

> Model stopped because it reached the maximum output token limit.

es muy característico de clientes compatibles con OpenAI.

No es un mensaje generado por llama.cpp.

---

# Hay otra cosa que me llama la atención

Has definido el alias:

```bash
--alias "gemma4:26b-a4b-it-qat-q4_0,gemma4"
```

No es incorrecto, pero normalmente el alias es un único nombre:

```bash
--alias gemma4
```

o

```bash
--alias gemma4-26b
```

No creo que sea el origen del problema, pero comprobaría qué modelo ve realmente el servidor.

Puedes ejecutar:

```bash
curl http://serveria.local:8080/v1/models
```

Deberías obtener algo parecido a:

```json
{
  "data": [
    {
      "id": "gemma4"
    }
  ]
}
```

Si aparece un nombre raro con la coma incluida, convendría cambiar el alias.

---

# También reduciría el contexto

Tienes:

```bash
LLAMA_CTX=65536
```

Con una 5060 Ti de 16 GB yo empezaría con:

```bash
LLAMA_CTX=32768
```

o incluso:

```bash
16384
```

**Ventajas:**

- menos RAM
- menos VRAM
- menor tiempo de warmup
- menor latencia

**Inconveniente:**

- menos historial disponible

Si vas a usar Open WebUI o pi-agent, 16k o 32k suele ser suficiente.

---

# Lo siguiente que haría

Quiero ver **la petición HTTP exacta** que llega a llama.cpp.

Arranca el servidor con más nivel de log:

```bash
-v 5
```

o

```bash
--log-verbosity 5
```

(según la versión de `llama-server` que tengas).

Cuando pi-agent haga la petición, debería aparecer algo similar a:

```text
POST /v1/chat/completions

{
    "model":"gemma4",
    "messages":[...],
    "max_tokens":256,
    ...
}
```

Ahí veremos inmediatamente quién está imponiendo el límite.

## Una pregunta

¿Qué versión de **pi-agent** estás usando? ¿Es el proyecto `pi-agent` de **Pi-Apps/Pi-Agent** o es otro proyecto con ese nombre? Si me indicas el repositorio o el enlace de GitHub, podré decirte exactamente dónde se configura `max_tokens`.
---


Perfecto. Esa versión es muy reciente:

```text
llama.cpp
commit: c749cb0
```

Así que **descartamos que sea un bug antiguo de llama.cpp**.

Con todo lo que has enseñado, mi diagnóstico ahora sería:

| Componente | Estado |
|------------|--------|
| llama.cpp | ✅ Correcto |
| Gemma 4 GGUF | ✅ Correcto |
| Tu script | ✅ Correcto |
| API OpenAI | ✅ Parece correcta |
| Pi | ⚠️ Muy probablemente el origen del problema |

## Hay una prueba definitiva

Quiero comprobar si el problema es realmente Pi o el servidor.

Ejecuta exactamente este `curl`:

```bash
curl http://serveria.local:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model":"gemma4",
    "messages":[
      {
        "role":"user",
        "content":"¿Quién eres?"
      }
    ],
    "max_tokens":128,
    "stream":false
  }'
```

### Si responde correctamente

Entonces ya no hay dudas.

**Pi está enviando una petición distinta** de la que creemos.

---

## Hay algo muy sospechoso en el log

Observa estas líneas:

```
Grammar (tool_calls)
```

después

```
chat format: peg-gemma4
```

después

```
reasoning-budget
```

después

```
next token: <|channel>
```

y finalmente

```
n_predict = 1
```

fileciteturn0file0L57-L87 fileciteturn0file0L214-L240

Eso no es el flujo de una conversación normal.

Es el flujo de **tool calling**.

---

# Mi hipótesis (90% de probabilidad)

Pi está intentando usar **herramientas** con Gemma.

Para detectar si el modelo quiere invocar una herramienta, hace una primera generación extremadamente corta (1 token).

Con GPT eso funciona.

Con Gemma 4 el primer token es:

```
<|channel>
```

Pi interpreta que ha terminado por límite y muestra:

> Model stopped because it reached the maximum output token limit.

---

# Una cosa que no me gusta de tu configuración

Has puesto:

```json
"reasoning": false
```

Pero en el log llama.cpp dice:

```
reasoning = 1
```

y

```
reasoning-budget...
```

fileciteturn0file0L50-L51 fileciteturn0file0L86-L87

Eso significa que **llama.cpp ha detectado automáticamente que Gemma es un modelo con capacidades de razonamiento**, independientemente de lo que Pi indique.

No creo que sea la causa principal, pero es una diferencia entre lo que Pi cree y lo que el servidor está haciendo.

---

# Lo siguiente que investigaría

Si puedes, prueba otro modelo en el mismo servidor `llama.cpp`, por ejemplo:

- Qwen3 30B
- Llama 3.3
- Mistral Small

Si todos funcionan en Pi y **solo Gemma 4 falla**, entonces es casi seguro que estamos ante una incompatibilidad entre Pi y el formato `peg-gemma4`.

## Mi conclusión

Con la evidencia que has aportado, asignaría las probabilidades así:

- **70%**: incompatibilidad de Pi con el formato de herramientas de Gemma 4 en `llama.cpp`.
- **20%**: Pi está sobrescribiendo `max_tokens` a `1` durante una llamada interna de tool calling.
- **10%**: un detalle específico de la API OpenAI-compatible de `llama.cpp` que Pi no está manejando correctamente.

Ya no dedicaría tiempo a cambiar parámetros como `ctx-size`, `batch-size` o `threads`: nada de eso explica un `n_predict = 1`. La siguiente fase de depuración debe centrarse en **la petición HTTP que Pi envía** o en **probar otro modelo con Pi** para confirmar si el problema es específico de Gemma 4.

---
*Generado desde conversación con 13 mensajes.*
*General*
