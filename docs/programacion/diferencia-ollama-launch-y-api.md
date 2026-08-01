---
title: Diferencia Ollama Launch y API
date: 2026-07-08
category: Programación
slug: diferencia-ollama-launch-y-api
tags: ['Programación']
---

# Diferencia Ollama Launch y API


> **Pregunta original:**
> 
no entiendo de ollama la parte de ollama lauch para integrarlo en vscode o lanzarharness , tepaso la documentacion para que expliquesque diferencia hay entre lanzar un harness y comunicarlo con un olla ylanzarlo como ollama lucn , al igual que el vscode https://docs.ollama.com/

---


## Respuesta


Voy a separar tres conceptos que suelen mezclarse: **Ollama como servidor local**, **un harness que llama a Ollama**, y **“Ollama Launch”/integración con VS Code**. Revisaré la documentación para no basarlo solo en memoria.
---


Sí. La confusión viene de que **“launch” no es lo mismo que “usar la API”**.

## Idea base

**Ollama** tiene dos papeles:

1. **Motor / servidor de modelos**
   - Ejecuta modelos locales o cloud.
   - Expone una API local por defecto en:
     ```text
     http://localhost:11434/api
     ```
   - No requiere autenticación cuando accedes localmente a `localhost:11434`. citeturn478338view3 citeturn478338view4

2. **Launcher de integraciones**
   - El comando `ollama launch ...` prepara o abre herramientas externas para que usen Ollama.
   - No “convierte” VS Code o Claude Code en Ollama. Solo los configura/conecta.

---

## Diferencia principal

| Caso | Qué haces | Quién manda la petición al modelo | Ejemplo |
|---|---|---|---|
| **Ollama directo** | Hablas con el modelo desde terminal | Ollama CLI | `ollama run gemma4` |
| **Harness conectado a Ollama** | Tu programa/test/agent llama a la API de Ollama | Tu harness | `POST http://localhost:11434/api/chat` |
| **`ollama launch ...`** | Ollama lanza o configura una herramienta externa | La herramienta externa | `ollama launch vscode` |
| **VS Code con Ollama** | VS Code usa modelos Ollama desde Copilot Chat/model picker | VS Code / Copilot Chat | seleccionar modelo local en VS Code |

---

## 1. Lanzar un modelo con Ollama

Esto es lo más simple:

```bash
ollama run gemma4
```

Ahí estás hablando directamente con el modelo desde la terminal. La documentación lo presenta como “Start a chat” después de instalar Ollama. citeturn478338view0

**Bueno:**
- Muy simple.
- Ideal para probar modelos.
- No necesitas VS Code ni otro programa.

**Malo:**
- No tienes integración con tu repo, edición de archivos, workflows, tests, etc.
- Es una conversación manual.

---

## 2. Comunicar un harness con Ollama

Un **harness** normalmente es una capa de ejecución/evaluación/orquestación. Puede ser:

- Un script de Python.
- Un agente de coding.
- Un benchmark.
- Un test runner.
- Un sistema que manda prompts, recoge respuestas y evalúa resultados.

En este caso, **el harness no se “lanza como Ollama”**. El harness simplemente llama a Ollama por HTTP.

Ejemplo conceptual:

```text
Harness ──HTTP──> Ollama ──> Modelo
```

Ejemplo API:

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "gemma3",
  "messages": [
    {
      "role": "user",
      "content": "explícame este código"
    }
  ]
}'
```

Ollama documenta `/api/chat` como endpoint para generar el siguiente mensaje de una conversación. citeturn674667search3

**Bueno:**
- Control total.
- Puedes automatizar pruebas, benchmarks, agentes, pipelines.
- Puedes cambiar modelo, temperatura, contexto, prompts, herramientas, etc.
- Es la forma correcta si estás construyendo algo propio.

**Malo:**
- Tienes que programar la lógica.
- Tienes que gestionar errores, streaming, contexto, memoria, formato de respuesta.
- No te da automáticamente una UI ni integración con VS Code.

---

## 3. Qué hace `ollama launch`

`ollama launch` es más parecido a un **asistente de configuración/arranque**.

Por ejemplo, en la documentación de VS Code aparece:

```bash
ollama launch vscode
```

Eso configura/lanza VS Code para que pueda usar modelos de Ollama desde el selector de modelos de Copilot Chat. citeturn478338view1

También existe:

```bash
ollama launch claude
```

En ese caso lanza Claude Code conectado a Ollama mediante una API compatible con Anthropic. La documentación dice que Claude Code puede leer el código, editar archivos y ejecutar comandos, y que Ollama lo conecta a modelos locales o cloud. citeturn478338view2

La forma mental correcta es:

```text
ollama launch X = "prepara X para usar Ollama"
```

No significa:

```text
X se ejecuta dentro de Ollama
```

Tampoco significa:

```text
Ollama se convierte en VS Code / Claude / harness
```

---

## 4. VS Code con Ollama

En VS Code, la integración documentada usa **GitHub Copilot Chat** y el selector de modelos. Según Ollama, necesitas Ollama v0.18.3+, VS Code 1.113+ y GitHub Copilot Chat 0.41.0+. Además, VS Code requiere estar logueado para usar el selector de modelos, aunque no necesariamente una cuenta de Copilot de pago. citeturn478338view1

El flujo es:

```text
VS Code / Copilot Chat ──> Ollama local ──> modelo local o cloud
```

Con:

```bash
ollama launch vscode
```

O directamente con modelo:

```bash
ollama launch vscode --model qwen3.5:cloud
```

**Bueno:**
- Cómodo para programar.
- Usas modelos Ollama dentro del editor.
- No tienes que escribir tu propio harness.
- Mejor experiencia para chat sobre código.

**Malo:**
- Dependencia de VS Code + Copilot Chat.
- Menos control fino que un harness propio.
- Algunas capacidades dependen de cómo VS Code implemente el model picker.
- Para tareas agentic más complejas quizá Roo Code, Cline, Claude Code u OpenCode sean más adecuados.

---

## 5. Entonces, ¿qué diferencia hay entre “lanzar un harness” y “ollama launch”?

### A. Harness conectado manualmente

```text
Tu harness ──API──> Ollama
```

Tú decides:

- qué endpoint usar;
- qué modelo;
- cómo construir prompts;
- cómo parsear respuestas;
- cómo ejecutar tests;
- cómo guardar logs;
- cómo evaluar resultados.

Ejemplo:

```python
import requests

response = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "qwen3",
        "messages": [
            {"role": "user", "content": "Resume este archivo"}
        ],
        "stream": False
    }
)

print(response.json())
```

Eso es integración programática.

---

### B. `ollama launch vscode`

```text
Ollama ──configura/abre──> VS Code
VS Code ──usa──> Ollama
```

Tú no programas la integración. Ollama ayuda a que VS Code detecte/use modelos Ollama.

---

### C. `ollama launch claude`

```text
Ollama ──configura/abre──> Claude Code
Claude Code ──usa API compatible Anthropic──> Ollama
```

La documentación incluso muestra el equivalente manual:

```bash
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL=http://localhost:11434
claude --model qwen3.5
```

Es decir: `ollama launch claude` automatiza una configuración que podrías hacer a mano. citeturn478338view2

---

## Resumen corto

```text
ollama run modelo
```

Usas Ollama directamente.

```text
tu_harness -> localhost:11434
```

Tu programa usa Ollama como backend de inferencia.

```text
ollama launch vscode
```

Ollama prepara VS Code para usar modelos Ollama.

```text
ollama launch claude
```

Ollama prepara Claude Code para usar modelos Ollama.

---

## Recomendación práctica

Si estás aprendiendo:

1. Primero prueba:
   ```bash
   ollama run qwen3
   ```

2. Luego prueba API:
   ```bash
   curl http://localhost:11434/api/generate -d '{
     "model": "qwen3",
     "prompt": "Di hola"
   }'
   ```

3. Si quieres usarlo en VS Code:
   ```bash
   ollama launch vscode
   ```

4. Si quieres un agente/harness de coding con más autonomía:
   - Claude Code:
     ```bash
     ollama launch claude
     ```
   - Roo Code en VS Code: configurar provider `Ollama`, base URL `http://localhost:11434`, modelo `qwen3` o similar. La documentación recomienda al menos 32K de contexto para coding. citeturn478338view5

La distinción clave: **Ollama es el motor; el harness o VS Code son clientes. `ollama launch` solo facilita conectar esos clientes al motor.**

---
*Generado desde conversación con 3 mensajes.*
*Programación*
