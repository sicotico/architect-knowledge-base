---
title: Problemas con extensión Ollama
date: 2026-07-07
category: IA/ML
slug: problemas-con-extension-ollama
tags: ['IA/ML']
---

# Problemas con extensión Ollama


> **Pregunta original:**
> 
Tengo un vscode en mi portátil y un server de ollama en la misma red . He instalado un extensión súper nueva de ollama pero no me deja cargar modelos 
> Existe la extensión de ollama para vscode ?

---


## Respuesta


Sí, existen varias extensiones para usar Ollama en VS Code, pero ojo: no hay “la extensión oficial única” de Ollama para VS Code que yo tomaría como referencia universal.

Algunas que aparecen en el Marketplace son:

| Extensión | Para qué sirve |
|---|---|
| [Ollama Code](https://marketplace.visualstudio.com/items?itemName=cgaspard.ollama-code) | Chat/agente de código con modelos locales de Ollama |
| [Ollama AI](https://marketplace.visualstudio.com/items?itemName=RivanMota.ollama-ai) | Chat, generar código, explicar/refactorizar |
| [Ollama Enhanced](https://marketplace.visualstudio.com/items?itemName=CarlosPacheco.vscode-ollama-enhanced) | Asistente de código con integración Ollama |
| [VSCode Ollama Modelfile](https://marketplace.visualstudio.com/items?itemName=warm3snow.vscode-ollama-modelfile) | Gestionar modelos/Modelfiles |
| [MCP Ollama Manager](https://marketplace.visualstudio.com/items?itemName=Internetics.mcp-ollama-extension) | Gestionar servidor/modelos Ollama vía MCP |

Lo bueno: sí hay opciones.  
Lo malo: muchas son nuevas, de terceros, y algunas asumen que Ollama está en `localhost:11434`, lo que te puede fallar si tu Ollama está en otro equipo de la red.

Para tu caso, busca una que permita configurar explícitamente la URL del servidor, por ejemplo:

```text
http://IP_DEL_SERVER:11434
```

Antes de pelearte con la extensión, prueba desde el portátil:

```bash
curl http://IP_DEL_SERVER:11434/api/tags
```

Si eso funciona, la extensión correcta debería poder listar modelos.
---


Voy a comprobarlo con una fuente actual, porque las extensiones de VS Code cambian bastante rápido y hay varias con nombres parecidos.
---


Puede fallar por varias capas distintas. Lo bueno: si Ollama ya corre en otro equipo de la misma red, normalmente se arregla con configuración de host/CORS/firewall, no con reinstalar todo. Lo malo: muchas extensiones nuevas de VS Code asumen `localhost:11434`, y desde tu portátil eso apunta al portátil, no al servidor.

Revisa esto en orden:

1. En el servidor de Ollama, confirma que escucha fuera de `localhost`:

```bash
OLLAMA_HOST=0.0.0.0:11434 ollama serve
```

Si lo tienes como servicio, hay que configurar esa variable en el servicio, no solo en la terminal.

2. Desde el portátil, prueba acceso directo:

```bash
curl http://IP_DEL_SERVER:11434/api/tags
```

Si eso no devuelve JSON con modelos, la extensión tampoco podrá verlos.

3. Si el `curl` falla, mira firewall/red:

```bash
nc -vz IP_DEL_SERVER 11434
```

En Linux suele hacer falta abrir el puerto `11434`. En Windows/macOS, revisar firewall de entrada.

4. En VS Code, busca en los ajustes de la extensión algo como:

```text
Ollama Host
Ollama Base URL
Ollama Endpoint
```

Y pon:

```text
http://IP_DEL_SERVER:11434
```

No uses `localhost` salvo que Ollama esté corriendo en el mismo portátil.

5. Si la extensión “no deja cargar modelos” pero sí conecta, puede ser que espere que los modelos estén ya descargados en el servidor. En el servidor ejecuta:

```bash
ollama list
ollama pull llama3.1
```

Luego reinicia VS Code o recarga la ventana:

```text
Developer: Reload Window
```

6. Si la extensión usa navegador/webview, puede necesitar CORS. En el servidor prueba arrancar Ollama así:

```bash
OLLAMA_HOST=0.0.0.0:11434 OLLAMA_ORIGINS=* ollama serve
```

Para dejarlo bien, luego se puede restringir el origen, pero para diagnosticar sirve.

La prueba clave es esta: si desde el portátil `curl http://IP_DEL_SERVER:11434/api/tags` funciona, el problema está en la configuración de la extensión. Si no funciona, el problema está en cómo Ollama está expuesto en la red.

---
*Generado desde conversación con 5 mensajes.*
*IA/ML*
