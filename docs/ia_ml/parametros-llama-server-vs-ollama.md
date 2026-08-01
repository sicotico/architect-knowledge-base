---
title: Parámetros llama-server vs Ollama
date: 2026-07-14
category: IA/ML
slug: parametros-llama-server-vs-ollama
tags: ['IA/ML']
---

# Parámetros llama-server vs Ollama


> **Pregunta original:**
> 
llama-server tiene un parametro m y mm , en ollama es igual ?

---


## Respuesta


No exactamente. Aunque ambos usan modelos GGUF basados en **llama.cpp** en muchos casos, la nomenclatura no es la misma.

En **llama-server** (llama.cpp) los parámetros más habituales son:

- `-m` → ruta al **modelo principal** (`.gguf`).
  ```bash
  llama-server -m model.gguf
  ```

- `--mmproj` (a veces abreviado en algunos ejemplos como `-mm` dependiendo de la versión) → ruta al **modelo multimodal** (`mmproj.gguf`), necesario para modelos con visión como LLaVA, Qwen2.5-VL, Gemma 3 Vision, etc.
  ```bash
  llama-server \
    -m gemma-3-4b-it.gguf \
    --mmproj mmproj.gguf
  ```

## En Ollama

No existe un equivalente directo a `--mmproj`.

El `mmproj` se gestiona internamente cuando creas el modelo.

Por ejemplo, en un `Modelfile`:

```text
FROM gemma-3-4b-it.gguf

PARAMETER temperature 0.7

ADAPTER ...
```

o, para modelos de visión convertidos desde GGUF:

```text
FROM ./gemma-3-4b-it.gguf
```

Si el modelo requiere un `mmproj`, Ollama espera que esté junto al modelo o que haya sido incluido durante la importación. El usuario no lo especifica en cada ejecución.

Después simplemente haces:

```bash
ollama run mi-modelo
```

## Resumen

| llama-server | Ollama |
|--------------|---------|
| `-m model.gguf` | `FROM model.gguf` al crear el modelo |
| `--mmproj mmproj.gguf` | Se detecta/gestiona automáticamente; no se pasa como parámetro en `ollama run` |
| Parámetros en la línea de comandos | Parámetros en el `Modelfile` o mediante la API |

Si tu intención es migrar un comando de `llama-server` a `ollama`, dime el comando exacto que usas y te indico cuál es el equivalente en Ollama.

---
*Generado desde conversación con 2 mensajes.*
*IA/ML*
