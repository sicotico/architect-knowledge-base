---
title: Conectar LM Studio servidor
date: 2026-07-07
category: General
slug: conectar-lm-studio-servidor
tags: ['General']
---

# Conectar LM Studio servidor


> **Pregunta original:**
> 
acabod einstalar en mi servidor lm studio daemon, pero no se como conectar  ellm studio de mi portatil con el server 
> Puedo usar una interfaz graficaen el portatil para adminsitrar el lm studio del servidor ?
> si quiero cambiar el modelo del daemondel lm studio , como lo haria ?

---


## Respuesta


Sí, pero con matiz importante: **la app gráfica de LM Studio en tu portátil no parece ser un “panel de administración remoto completo” para controlar todo el llmster del servidor**. Lo que sí puedes hacer oficialmente es:

1. **Usar modelos remotos desde la GUI del portátil con LM Link**  
   LM Link permite que un modelo cargado en el servidor se use desde el portátil “como si fuera local”. La propia documentación dice que el portátil puede llamar a `localhost` y que el trabajo lo sirva la máquina remota. citeturn183781search2  
   Esto es lo más parecido a “usar el servidor desde la interfaz gráfica”.

2. **Administrar por CLI desde el portátil**  
   Puedes usar comandos `lms` con `--host` para operar contra una instancia remota, por ejemplo listar o cargar modelos. La documentación menciona `lms ps --host <host>`, `lms ls --host <host>` y `lms load <model_key> --host <host>`. citeturn183781search9 citeturn183781search10 citeturn183781search3

3. **Usar otra GUI externa tipo Open WebUI / AnythingLLM / LibreChat**  
   Esto no administra LM Studio internamente como la app oficial, pero sí te da una interfaz web para chatear contra el endpoint del servidor:
   ```text
   http://IP_DEL_SERVIDOR:1234/v1
   ```
   Es práctico si lo que quieres es “usar” los modelos, no gestionar todo LM Studio.

**Lo bueno:** con LM Link o con el endpoint HTTP puedes trabajar cómodamente desde el portátil sin mover los modelos ni consumir GPU local.  
**Lo malo:** para administración fina del servidor headless, hoy parece que el camino real es `lms` por terminal, SSH, o scripts; la GUI oficial del portátil no sustituye del todo a una consola de administración remota.

Yo lo montaría así: **LM Link para uso desde la app del portátil**, y **SSH + `lms --host` o comandos en el servidor** para administrar.
---


Para cambiar el modelo del daemon `llmster`/LM Studio, lo normal es hacerlo con `lms` desde terminal.

**En el servidor**, primero mira qué modelos tienes:

```bash
lms ls
```

Mira qué está cargado ahora:

```bash
lms ps
```

Descarga un modelo si todavía no lo tienes:

```bash
lms get publisher/model-name
```

Por ejemplo:

```bash
lms get lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF
```

Luego descarga/carga el nuevo modelo:

```bash
lms load publisher/model-name
```

Si quieres quitar el modelo anterior antes:

```bash
lms unload --all
lms load publisher/model-name
```

Después comprueba:

```bash
lms ps
```

Si estás administrándolo desde el portátil contra el servidor remoto, usa `--host`:

```bash
lms ps --host IP_DEL_SERVIDOR:1234
lms ls --host IP_DEL_SERVIDOR:1234
lms unload --all --host IP_DEL_SERVIDOR:1234
lms load publisher/model-name --host IP_DEL_SERVIDOR:1234
```

Ejemplo:

```bash
lms unload --all --host 192.168.1.50:1234
lms load lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF --host 192.168.1.50:1234
```

Lo bueno de `lms load` es que dejas explícitamente qué modelo quieres tener en memoria. Lo malo: si tu cliente llama a un modelo por nombre concreto, también tienes que cambiar el `model` en ese cliente. Por ejemplo, en una llamada OpenAI-compatible:

```json
{
  "model": "lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF",
  "messages": [
    { "role": "user", "content": "Hola" }
  ]
}
```

Para verificar desde el portátil:

```bash
curl http://IP_DEL_SERVIDOR:1234/v1/models
```

Si ves el modelo nuevo ahí, el servidor ya lo está exponiendo.
---


Ya encontré dos caminos oficiales: exponer el servidor API en la red local, o usar LM Link si quieres que el portátil vea los modelos del servidor como remotos de forma más integrada y cifrada. Te doy el camino directo primero, que suele ser el más fácil de depurar.
---


Voy a separar “cambiar el modelo cargado” de “cambiar el modelo que usa tu cliente”, porque en LM Studio/llmster esas dos cosas se mezclan fácil y dan errores raros si queda un modelo viejo en memoria.
---


Sí. Tienes dos opciones, y conviene elegir según tu caso.

**Opción A: misma red local**
En el servidor, arranca LM Studio/llmster escuchando en la red, no solo en localhost:

```bash
lms server start --bind 0.0.0.0 --port 1234
```

LM Studio documenta `--bind 0.0.0.0` para permitir acceso desde otros dispositivos de la red, y avisa que conviene activar autenticación porque ya no queda limitado a `127.0.0.1`. citeturn916599search1

Luego, desde el portátil prueba:

```bash
curl http://IP_DEL_SERVIDOR:1234/v1/models
```

Ejemplo:

```bash
curl http://192.168.1.50:1234/v1/models
```

Si responde, ya puedes usar esa URL como endpoint en apps compatibles con OpenAI:

```text
Base URL: http://192.168.1.50:1234/v1
API key: lm-studio
```

Si no conecta, revisa firewall:

```bash
sudo ufw allow 1234/tcp
```

Y confirma en el servidor:

```bash
lms server status
```

**Opción B: LM Link**
Si quieres conectar portátil y servidor aunque no estén en la misma red, LM Studio tiene **LM Link**, pensado para usar modelos de otros dispositivos como si fueran locales, con conexión cifrada basada en Tailscale. citeturn916599search18

En ese caso, en el servidor con llmster deberías mirar/activar LM Link, y en el portátil activar LM Link desde LM Studio. La ventaja es seguridad y acceso remoto; lo malo es que dependes más de la integración de LM Studio y su sistema de enlace.

Mi recomendación: primero prueba la opción A en LAN. Si funciona, ya sabes que el daemon y el modelo están bien. Después decides si necesitas LM Link para acceso fuera de casa/oficina.
---


Voy a comprobar la forma actual recomendada por LM Studio para conectar el cliente con un daemon remoto, porque en estas herramientas los nombres de comandos y puertos cambian con cierta frecuencia.
---


Voy a verificarlo con la documentación actual de LM Studio, porque aquí hay una diferencia importante entre “usar el modelo remoto” y “administrar toda la instancia remota desde la GUI”.

---
*Generado desde conversación con 10 mensajes.*
*General*
