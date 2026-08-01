---
title: Diferencia agentes búsqueda
date: 2026-07-21
category: IA/ML
slug: diferencia-agentes-busqueda
tags: ['IA/ML']
---

# Diferencia agentes búsqueda


> **Pregunta original:**
> 
Poruqe OpenClaw y Hermen agent pueden buscar en internet y  mi pi-agent no 

---


## Respuesta


La diferencia no suele estar en el modelo de IA, sino en **las herramientas (tools)** que tiene disponibles el agente.

En tu caso:

| Agente | Puede buscar en Internet | ¿Por qué? |
|--------|--------------------------|------------|
| **OpenClaw** | Sí | Tiene una herramienta de `web_search` configurable (Brave, SearXNG, Perplexity, Tavily, Ollama Web Search, etc.) que el modelo puede invocar cuando la necesita. citeturn0search0turn0search2 |
| **Hermes Agent** | Depende de la configuración | Normalmente integra herramientas de búsqueda o navegación web. |
| **Tu pi-agent** | No (según describes) | Probablemente sólo tiene acceso al LLM y a los archivos locales, pero no dispone de ninguna herramienta de búsqueda web. |

### Un LLM por sí solo no sabe buscar

Aunque uses un modelo muy potente (Gemma, Qwen, GPT OSS, etc.), el modelo **no puede acceder a Internet por iniciativa propia**.

Necesita que el framework le ofrezca una función del estilo:

```text
search_web(query)
```

Entonces el agente hace algo como:

1. El usuario pregunta.
2. El modelo decide "necesito buscar".
3. Llama a `search_web()`.
4. Recibe los resultados.
5. Genera la respuesta.

Sin ese paso, únicamente responde con el conocimiento que tenía al entrenarse.

### OpenClaw viene preparado para ello

OpenClaw incorpora soporte para varios proveedores de búsqueda web. Puedes elegir, por ejemplo:

- Brave Search
- SearXNG
- Perplexity
- Tavily
- Ollama Web Search
- DuckDuckGo (integración no oficial)

y el agente utilizará esa herramienta automáticamente cuando sea necesario. citeturn0search0turn0search2

### ¿Y pi-agent?

Depende de qué "pi-agent" estés utilizando, porque existen varios proyectos con ese nombre.

Las posibilidades más habituales son:

- **No implementa herramientas web.**
- **Las implementa pero están deshabilitadas.**
- **Necesita instalar un plugin o MCP de búsqueda.**
- **Necesita configurar un proveedor (Brave, SearXNG, etc.).**

### Si estás montando un agente local

Como sé que estás montando un entorno local con OpenClaw y modelos locales, una arquitectura típica sería:

- **LLM local:** Qwen, Gemma, Llama...
- **Web Search:** SearXNG o Brave
- **RAG:** para documentos propios
- **MCPs:** GitHub, filesystem, terminal, etc.

Así el modelo decide cuándo consultar Internet y cuándo responder sólo con su conocimiento.

**Una pregunta para concretar:** ¿a qué proyecto te refieres exactamente con **"pi-agent"**? ¿Es el de Pipecat, PydanticAI, un agente de Raspberry Pi, o puedes pasarme el enlace al repositorio que estás usando?

---
*Generado desde conversación con 2 mensajes.*
*IA/ML*
