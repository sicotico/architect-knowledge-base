---
title: Configurar plugin Ollama
date: 2026-07-08
category: IA/ML
slug: configurar-plugin-ollama
tags: ['IA/ML']
---

# Configurar plugin Ollama


> **Pregunta original:**
> 
https://github.com/ollama/ollama-vscode este es el proyecto de github para la extensión, revisalo y dime si me falta algo o que requisitos tiene  porque uso el vscode sin login de github y no se si eso es un problema
> Activated Ollama language model provider.
Refreshing Ollama language models.
Providing 4 Ollama model(s) from http://192.168.68.67:11434 with Ollama 0.31.1.
Refreshing Ollama language models.
Providing 4 Ollama model(s) from http://serveria.local:11434 with Ollama 0.31.1.
--- Diagnostics ---
Providing 4 Ollama model(s) from http://serveria.local:11434 with Ollama 0.31.1.
VS Code returned 4 total language model(s).
- ollama-models/VladimirGav/gemma4-26b-16GB-VRAM-Uncensored:latest (VladimirGav/gemma4-26b-16GB-VRAM-Uncensored:latest)
- ollama-models/batiai/qwen3.6-27b:iq4 (batiai/qwen3.6-27b:iq4)
- ollama-models/qwen3.6:27b-q4_K_M (qwen3.6:27b-q4_K_M)
- ollama-models/qwen3:8b (qwen3:8b)
VS Code returned 4 Ollama language model(s).
Direct Ollama API returned 4 model(s).
- VladimirGav/gemma4-26b-16GB-VRAM-Uncensored:latest
- batiai/qwen3.6-27b:iq4
- qwen3.6:27b-q4_K_M
- qwen3:8b
--- End Diagnostics ---
> ME esta  pidiendo login "You need to set up GitHub Copilot and be signed in to use Chat."
> 
> *...y 9 preguntas de seguimiento*


---


## Respuesta


Sí, tiene sentido: si en el portátil hay un Ollama local escuchando en `localhost:11434`, Zed probablemente está usando ese por defecto en vez del remoto.

## Prueba rápida

En el portátil:

```bash
curl http://localhost:11434/api/version
curl http://serveria.local:11434/api/version
```

Si ambos responden, Zed puede estar cogiendo el local por configuración por defecto.

## Parar Ollama local en el portátil

Primero mira cómo está corriendo:

```bash
ps aux | grep ollama
systemctl --user status ollama
systemctl status ollama
```

Para pararlo temporalmente:

```bash
pkill ollama
```

Si es servicio de usuario:

```bash
systemctl --user stop ollama
```

Si es servicio del sistema:

```bash
sudo systemctl stop ollama
```

Comprueba que ya no responde local:

```bash
curl http://localhost:11434/api/version
```

Debería fallar.

## Configurar Zed hacia el remoto

En Zed, configura el proveedor Ollama con:

```text
http://serveria.local:11434
```

No uses `/v1`.

Es decir:

```text
Ollama API URL / Host:
http://serveria.local:11434
```

Después refresca los modelos o reinicia Zed.

## Lo bueno / lo malo

**Lo bueno:** parar Ollama local elimina ambigüedad. Si Zed empieza a ver los 4 modelos de `serveria`, confirmas que antes estaba usando `localhost`.

**Lo malo:** si alguna app del portátil dependía del Ollama local, dejará de funcionar hasta que lo arranques otra vez.

Para volver a arrancarlo:

```bash
ollama serve
```

o:

```bash
systemctl --user start ollama
```

según cómo esté instalado.
---


Eso confirma que **la extensión ya está funcionando**.

El diagnóstico dice:

```text
Providing 4 Ollama model(s) from http://serveria.local:11434 with Ollama 0.31.1.
VS Code returned 4 Ollama language model(s).
Direct Ollama API returned 4 model(s).
```

## Estado actual

| Componente | Estado |
|---|---|
| Ollama en `serveria` | OK |
| Red desde `sico-Modern` | OK |
| Header `Authorization` | OK |
| Endpoint `serveria.local:11434` | OK |
| Extensión `ollama-vscode` | OK |
| Modelos detectados por VS Code | OK |
| Login GitHub | No es necesario para esto |

## Lo que te falta ahora

Probablemente nada a nivel de conexión. Solo tienes que **seleccionar uno de esos modelos en el Chat de VS Code**.

En el Chat de VS Code, abre el selector de modelo y busca alguno como:

```text
qwen3:8b
```

o:

```text
qwen3.6:27b-q4_K_M
```

Para probar, usa primero:

```text
qwen3:8b
```

porque es el más ligero.

## Ojo con el rendimiento

Tienes una RTX 5060 Ti con 16 GB VRAM. Según tu lista:

| Modelo | Tamaño aproximado | Comentario |
|---|---:|---|
| `qwen3:8b` | 5.2 GB | Mejor para probar |
| `VladimirGav/gemma4-26b...` | 13.9 GB | Puede entrar justo |
| `batiai/qwen3.6-27b:iq4` | 15.0 GB | Muy justo |
| `qwen3.6:27b-q4_K_M` | 17.4 GB | Probablemente excede VRAM y puede offloadear a RAM |

Lo bueno: VS Code ya ve los 4 modelos.

Lo malo: los modelos de 26B/27B pueden tardar mucho en arrancar o ir lentos si no caben completos en VRAM. Para validar que todo está bien, empieza con `qwen3:8b`.
---


El `ping` confirma que:

```text
sico-Modern -> serveria.local / 192.168.68.67
```

sí tiene conectividad IP. Entonces el problema queda casi reducido a **puerto 11434 bloqueado** o **Ollama no aceptando conexiones TCP reales desde fuera**, aunque `ss` muestre `*:11434`.

Haz estas pruebas en este orden.

## 1. Desde `sico-Modern`, prueba el puerto

```bash
nc -vz serveria.local 11434
```

o:

```bash
nc -vz 192.168.68.67 11434
```

Resultados esperados:

```text
succeeded
```

Si ves `Connection refused`, el puerto no está aceptando desde fuera.

Si ves `timed out`, suele ser firewall.

## 2. En `serveria`, prueba localmente la IP LAN

En `serveria`:

```bash
curl http://127.0.0.1:11434/api/version
curl http://192.168.68.67:11434/api/version
curl http://serveria.local:11434/api/version
```

Interpretación:

| Resultado | Diagnóstico |
|---|---|
| `127.0.0.1` funciona, `192.168.68.67` falla | Algo raro con bind/interfaz |
| Ambos funcionan en `serveria`, pero falla desde `sico-Modern` | Firewall o política de red |
| Ninguno funciona | Ollama no está sirviendo correctamente |

## 3. Revisa firewall en `serveria`

```bash
sudo ufw status verbose
```

Si UFW está activo:

```bash
sudo ufw allow from 192.168.68.0/24 to any port 11434 proto tcp
sudo ufw reload
```

Después desde `sico-Modern`:

```bash
curl http://serveria.local:11434/api/version
```

## 4. Prueba temporal apagando firewall

Solo para confirmar:

```bash
sudo ufw disable
```

Desde `sico-Modern`:

```bash
curl http://serveria.local:11434/api/version
```

Si funciona, ya está: era firewall. Luego vuelve a activarlo con regla restringida:

```bash
sudo ufw enable
sudo ufw allow from 192.168.68.0/24 to any port 11434 proto tcp
```

## 5. Mira si llegan paquetes al servidor

En `serveria`, deja corriendo:

```bash
sudo tcpdump -ni any port 11434
```

Luego desde `sico-Modern` ejecuta:

```bash
curl http://serveria.local:11434/api/version
```

Interpretación:

| `tcpdump` | Significado |
|---|---|
| No aparece nada | El tráfico no llega a `serveria`; router/red/firewall externo |
| Aparecen SYN pero no respuesta | Firewall local o servicio no responde |
| Aparece conexión completa | El problema está más arriba, quizá proxy/curl/config |

## Para VS Code

Cuando este comando funcione:

```bash
curl http://serveria.local:11434/api/version
```

pon en la extensión:

```text
Ollama: Endpoint
http://serveria.local:11434
```

Headers:

```text
Authorization = Bearer ollama
```

Lo bueno: DNS local y conectividad base están bien.

Lo malo: todavía no hay prueba de que el puerto `11434` sea accesible desde el cliente. Ese es el punto que falta validar.
---


Bien. Con esos resultados, **la red y el puerto están bien**:

```text
sico-Modern -> serveria.local:11434 OK
sico-Modern -> 192.168.68.67:11434 OK
serveria -> Ollama API OK
```

Ahora falta probar **HTTP desde `sico-Modern`**, no solo TCP.

## 1. Prueba `curl` otra vez desde `sico-Modern`

Ejecuta exactamente:

```bash
curl -v http://serveria.local:11434/api/version
```

y también:

```bash
curl -v http://192.168.68.67:11434/api/version
```

Si `nc` funciona, estos deberían devolver:

```json
{"version":"0.31.1"}
```

Si ahora `curl` funciona, el problema original ya estaba resuelto o era temporal.

## 2. Prueba con el header

```bash
curl -v -H "Authorization: Bearer ollama" \
  http://serveria.local:11434/api/version
```

Si también funciona, VS Code debería ir con esta configuración:

```text
Ollama: Endpoint
http://serveria.local:11434
```

Headers:

```text
Authorization = Bearer ollama
```

Yo usaría `serveria.local` en vez de la IP, porque ya resuelve bien y te evita problemas si cambia la IP por DHCP.

## 3. Prueba listar modelos desde `sico-Modern`

Esto es clave para la extensión:

```bash
curl -v -H "Authorization: Bearer ollama" \
  http://serveria.local:11434/api/tags
```

Si devuelve modelos, la extensión debería poder descubrirlos.

Si devuelve algo como:

```json
{"models":[]}
```

entonces la extensión conecta, pero no tendrá modelos locales disponibles. En `serveria`, verifica:

```bash
ollama list
```

## 4. Configuración final en VS Code

En la extensión oficial `ollama-vscode`:

```text
Ollama: Endpoint
http://serveria.local:11434
```

Y en headers:

| Key | Value |
|---|---|
| `Authorization` | `Bearer ollama` |

Después ejecuta en VS Code:

```text
Ollama: Refresh Models
```

Si no aparecen:

```text
Ollama: Diagnose Models
```

y mira el panel:

```text
View > Output > Ollama
```

## Lo bueno / lo malo

**Lo bueno:** ya descartaste red, DNS, bind de Ollama y puerto TCP.

**Lo malo:** si VS Code sigue fallando, el problema ya queda en uno de estos puntos:

1. `curl` HTTP desde `sico-Modern` aún falla por algún proxy/env raro.
2. `/api/tags` devuelve vacío o error.
3. La extensión no está leyendo bien `ollama.endpoint` / `ollama.headers`.
4. VS Code está usando otro perfil, remote window, dev container, WSL o configuración distinta a la que estás editando.

El siguiente dato decisivo es la salida de:

```bash
curl -v -H "Authorization: Bearer ollama" http://serveria.local:11434/api/tags
```
---


Sí. Ahí hay una distinción importante:

## Lo que ya funciona

La extensión **Ollama** está bien instalada y detecta tus modelos:

```text id="t0itst"
VS Code returned 4 Ollama language model(s).
Direct Ollama API returned 4 model(s).
```

Eso significa que el proveedor de modelos local está registrado correctamente.

## Lo que está fallando

El panel que estás usando es el **Chat de GitHub Copilot**. Ese panel te está bloqueando con:

```text id="tokr1w"
You need to set up GitHub Copilot and be signed in to use Chat.
```

Según la documentación actual de Ollama para VS Code, **VS Code requiere estar logueado para usar su model selector incluso con modelos personalizados**, aunque no hace falta una cuenta Copilot de pago para modelos locales. citeturn901565search0

También hay documentación reciente de VS Code que dice que los modelos BYOK/locales pueden funcionar sin cuenta GitHub ni plan Copilot, pero eso depende del flujo nuevo de **Chat: Manage Language Models** y de la versión/canal de VS Code; tu UI actual está claramente entrando por Copilot Chat y por eso pide login. citeturn901565search2turn901565search5

## Qué hacer ahora

Tienes dos caminos.

### Opción A — Usar ese Chat de VS Code

Haz login en VS Code con GitHub.

No necesariamente necesitas pagar Copilot para usar Ollama local, pero ese panel de Chat necesita que VS Code/Copilot quede inicializado.

En tu captura hay botón:

```text id="fswm9z"
Sign In
```

Después de iniciar sesión:

1. Vuelve al Chat.
2. Abre el selector de modelo.
3. Selecciona `qwen3:8b` o el modelo que quieras.
4. Asegúrate de que abajo aparezca `Local`.

Lo bueno: usas el chat integrado de VS Code con tus modelos Ollama ya detectados.

Lo malo: requiere login GitHub en esa ruta de UI, aunque el modelo sea local.

### Opción B — Evitar Copilot Chat

Si no quieres login de GitHub, no uses ese panel. Usa otra extensión que tenga chat propio contra Ollama, por ejemplo:

```text id="71l0uu"
Continue
Cline
Roo Code
Open WebUI
Page Assist
```

Lo bueno: puedes trabajar sin GitHub/Copilot.

Lo malo: no estarías usando el panel nativo de Chat de VS Code; sería otro flujo.

## Mi lectura de tu caso

Tu instalación de Ollama **no tiene problema**.

El bloqueo viene de esta capa:

```text id="ir6e7j"
VS Code Chat / Copilot Chat UI
```

no de esta:

```text id="q8c8sb"
ollama-vscode -> serveria.local:11434
```

## Recomendación concreta

Como ya tienes la extensión oficial funcionando, haría esto:

1. Prueba login GitHub normal en VS Code.
2. No actives ni pagues Copilot salvo que VS Code te lo exija para otra función.
3. Selecciona `qwen3:8b` como modelo local.
4. Comprueba que abajo ponga `Local`.

Si quieres cero login de GitHub, entonces la vía más limpia es cambiar a una extensión con chat propio, no al Chat/Copilot integrado.
---


En ese plugin, el **nombre de la key/header** debe ser:

```text
Authorization
```

Y el **valor** debe ser:

```text
Bearer ollama
```

No pongas `API-Key` como nombre, porque eso enviaría este header:

```http
API-Key: ollama
```

Pero tu `curl` usa este:

```http
Authorization: Bearer ollama
```

Así que en VS Code debería quedar:

| Item | Value |
|---|---|
| `Authorization` | `Bearer ollama` |

Además, para endpoint OpenAI-compatible normalmente conviene usar:

```text
http://192.168.68.67:11434/v1
```

No:

```text
http://192.168.68.67:11434
```

### Resumen

En el plugin:

```text
Ollama: Endpoint
http://192.168.68.67:11434/v1
```

```text
Ollama: Headers
Authorization = Bearer ollama
```

Lo bueno: tu `curl` ya está correcto para el endpoint `/v1/chat/completions`.

Lo malo: si el plugin espera API nativa de Ollama en vez de OpenAI-compatible, puede que `/v1` falle. En ese caso usa:

```text
http://192.168.68.67:11434
```

pero **mantén el header** como:

```text
Authorization = Bearer ollama
```
---


Ya está demostrado que **Ollama remoto funciona correctamente desde `sico-Modern`**:

```text
/api/version -> 200 OK
/api/tags    -> 200 OK
modelos      -> disponibles
Authorization header -> aceptado
```

Así que el problema, si VS Code sigue sin ver modelos, está en **configuración de la extensión / perfil de VS Code**, no en red ni en Ollama.

## Configuración correcta en VS Code

En `settings.json`, ponlo explícitamente así:

```json
{
  "ollama.endpoint": "http://serveria.local:11434",
  "ollama.headers": {
    "Authorization": "Bearer ollama"
  }
}
```

O si la UI de settings te pide pares clave/valor:

| Key | Value |
|---|---|
| `Authorization` | `Bearer ollama` |

No pongas:

```text
API-Key = ollama
```

ni:

```text
Bearer = ollama
```

ni:

```text
Authorization = ollama
```

Tiene que ser exactamente:

```text
Authorization = Bearer ollama
```

## Luego en VS Code

Ejecuta desde la Command Palette:

```text
Ollama: Refresh Models
```

Si no aparecen:

```text
Ollama: Diagnose Models
```

Y abre:

```text
View > Output > Ollama
```

Ahí debería verse si está intentando conectar a `127.0.0.1` en vez de `serveria.local`.

## Posible problema: estás editando settings de otro contexto

Esto pasa mucho en VS Code.

Revisa si estás usando alguno de estos modos:

| Caso | Problema típico |
|---|---|
| VS Code normal local | Usa `User Settings` |
| Workspace abierto | Puede haber `.vscode/settings.json` pisando la config |
| Remote SSH | La extensión corre en el host remoto, no en tu PC |
| WSL | La extensión corre dentro de WSL |
| Dev Container | La extensión corre dentro del contenedor |
| Perfil distinto de VS Code | Tiene settings separados |

Busca en VS Code:

```text
Preferences: Open User Settings (JSON)
```

y confirma que está ahí.

También revisa:

```text
Preferences: Open Workspace Settings (JSON)
```

por si tiene algo como:

```json
"ollama.endpoint": "http://127.0.0.1:11434"
```

## Prueba de chat directa desde cliente

Desde `sico-Modern`, prueba que no solo lista modelos sino que genera:

```bash
curl -s -H "Authorization: Bearer ollama" \
  http://serveria.local:11434/api/chat \
  -d '{
    "model": "qwen3:8b",
    "messages": [
      {"role": "user", "content": "Responde solo OK"}
    ],
    "stream": false
  }'
```

Si responde, la API nativa que usa la extensión está operativa.

## Sobre los modelos

Tu `/api/tags` devuelve modelos válidos:

```text
qwen3:8b
qwen3.6:27b-q4_K_M
batiai/qwen3.6-27b:iq4
VladimirGav/gemma4-26b-16GB-VRAM-Uncensored:latest
```

Para probar VS Code, yo empezaría con:

```text
qwen3:8b
```

Lo bueno: es más ligero y reduce variables.

Lo malo: los modelos grandes pueden tardar en cargar y parecer que “no funciona” si VS Code no muestra bien el progreso.

## Punto clave

No necesitas login de GitHub para esto.

Tu servidor Ollama, el header y la red ya están bien. Lo que falta revisar es que la extensión esté leyendo estos valores:

```text
endpoint = http://serveria.local:11434
header   = Authorization: Bearer ollama
```
---


Estás en **Edit Predictions**, no en el chat/agente principal de Zed. Son dos cosas distintas.

## 1. Sobre esa pantalla

La pantalla muestra:

```text
User / AI / Edit Predictions / Configure Providers
```

Eso configura la función tipo “autocompletado predictivo” de Zed, no necesariamente el chat/agente.

En esa sección, Zed tiene soporte específico para Ollama con:

```json
"edit_predictions": {
  "provider": "ollama",
  "ollama": {
    "api_url": "http://localhost:11434",
    "model": "qwen2.5-coder:7b-base",
    "prompt_format": "infer",
    "max_output_tokens": 64
  }
}
```

La documentación de Zed indica que **Edit Prediction tiene su propia configuración de proveedor**, separada del agente/chat. citeturn839774search2turn839774search13

## 2. No estás viendo tus modelos porque ese desplegable es limitado

El modelo que aparece:

```text
qwen2.5-coder:7b-base
```

es el modelo recomendado/típico para **edit predictions**, pero eso no significa que Zed haya listado todos tus modelos remotos.

Tus modelos reales en `serveria` son:

```text
qwen3:8b
qwen3.6:27b-q4_K_M
batiai/qwen3.6-27b:iq4
VladimirGav/gemma4-26b-16GB-VRAM-Uncensored:latest
```

Para edit predictions, Zed espera modelos orientados a predicción de edición, especialmente `qwen2.5-coder:7b-base` o variantes Zeta. La documentación de Zed muestra precisamente `qwen2.5-coder:7b-base` como ejemplo para Ollama en edit predictions. citeturn839774search13

## 3. Te falta instalar ese modelo en el Ollama remoto

En `serveria`, ejecuta:

```bash
ollama pull qwen2.5-coder:7b-base
```

Luego desde el portátil:

```bash
curl http://serveria.local:11434/api/tags
```

Debería aparecer:

```text
qwen2.5-coder:7b-base
```

Después reinicia Zed o vuelve a abrir esa configuración.

## 4. Dónde poner `Authorization`

En la sección **Ollama** de esa pantalla no se ve campo para header/API key. El campo de API Key que aparece abajo pertenece a:

```text
OpenAI Compatible API
```

y dice que lo manda como:

```text
Authorization: Bearer {key}
```

Eso no aplica a la sección Ollama de arriba.

En tu caso hay dos posibilidades:

### Opción A — Usar Ollama nativo sin Authorization

Tu Ollama ya responde sin header:

```bash
curl http://serveria.local:11434/api/version
```

te dio `200 OK`.

Entonces en Zed/Ollama puedes dejar:

```text
API URL: http://serveria.local:11434
```

sin API key.

**Lo bueno:** simple y directo.

**Lo malo:** cualquier equipo de tu LAN que alcance `serveria.local:11434` puede usar Ollama, salvo que tengas un proxy o firewall restringiendo.

### Opción B — Usar OpenAI Compatible API con API Key

Si necesitas sí o sí mandar:

```text
Authorization: Bearer ollama
```

entonces usa la sección:

```text
OpenAI Compatible API
```

y configura la URL como OpenAI-compatible:

```text
http://serveria.local:11434/v1
```

API key:

```text
ollama
```

Porque Zed dice que ese campo se envía como:

```text
Authorization: Bearer {key}
```

Así que `ollama` se convierte en:

```text
Authorization: Bearer ollama
```

**Lo bueno:** coincide con tu esquema de header.

**Lo malo:** para **Edit Predictions**, puede que la integración nativa de Ollama funcione mejor que OpenAI-compatible. Además, no todos los modelos son buenos para esta función.

## 5. Configuración recomendada para ti

Para Zed **Edit Predictions**:

```text
Provider: Ollama
API URL: http://serveria.local:11434
Model: qwen2.5-coder:7b-base
Prompt Format: Infer
Max Output Tokens: 64
```

Y en `serveria`:

```bash
ollama pull qwen2.5-coder:7b-base
```

Para Zed **Agent/Chat**, configura aparte el proveedor Ollama con:

```text
http://serveria.local:11434
```

y usa primero:

```text
qwen3:8b
```

## Lo bueno / lo malo

**Lo bueno:** tu URL remota está bien; Zed debería poder llegar a `serveria.local:11434`.

**Lo malo:** estás configurando **Edit Predictions**, que no usa cualquier modelo igual de bien. Además, el campo de API key que ves abajo no pertenece al proveedor Ollama, sino al proveedor OpenAI-compatible.
---


El fallo ya no parece de VS Code. Es de red/servicio:

```text
curl: (7) Failed to connect to 192.168.68.67 port 11434
```

Eso significa que desde `sico-Modern` **no hay ningún servidor escuchando accesible** en `192.168.68.67:11434`.

## Diagnóstico más probable

En `serveria` tienes Ollama corriendo:

```text
/home/sico/.local/bin/ollama serve
```

pero probablemente está escuchando solo en `127.0.0.1:11434`, no en la IP LAN. Ollama, por defecto, se enlaza a `127.0.0.1:11434`; para exponerlo en red hay que cambiar `OLLAMA_HOST`. citeturn494646search0

## En `serveria`, comprueba dónde escucha Ollama

Ejecuta:

```bash
ss -ltnp | grep 11434
```

Si ves algo como:

```text
127.0.0.1:11434
```

entonces solo acepta conexiones locales.

Lo correcto para acceso desde otros equipos sería ver algo como:

```text
0.0.0.0:11434
```

o:

```text
192.168.68.67:11434
```

## Solución rápida para probar

En `serveria`, para el proceso actual:

```bash
pkill ollama
OLLAMA_HOST=0.0.0.0:11434 ollama serve
```

Déjalo abierto en esa terminal.

Luego, desde `sico-Modern`, prueba:

```bash
curl http://192.168.68.67:11434/api/version
```

o con tu header:

```bash
curl -H "Authorization: Bearer ollama" \
  http://192.168.68.67:11434/api/version
```

Si responde, VS Code debería poder usar:

```text
Endpoint: http://192.168.68.67:11434
Header: Authorization = Bearer ollama
```

## Hacerlo permanente con systemd

Si quieres que quede fijo como servicio, revisa si tienes unidad systemd:

```bash
systemctl --user status ollama
systemctl status ollama
```

Como en tu caso el binario está en:

```text
/home/sico/.local/bin/ollama
```

puede que lo estés lanzando manualmente, no como servicio.

Para servicio de usuario, puedes crear:

```bash
mkdir -p ~/.config/systemd/user
nano ~/.config/systemd/user/ollama.service
```

Contenido:

```ini
[Unit]
Description=Ollama

[Service]
ExecStart=/home/sico/.local/bin/ollama serve
Environment=OLLAMA_HOST=0.0.0.0:11434
Restart=always
RestartSec=3

[Install]
WantedBy=default.target
```

Luego:

```bash
systemctl --user daemon-reload
systemctl --user enable --now ollama
```

Comprueba:

```bash
systemctl --user status ollama
ss -ltnp | grep 11434
```

## Revisa firewall

Si Ollama ya escucha en `0.0.0.0:11434` pero desde otro equipo sigue fallando, mira firewall en `serveria`.

Con UFW:

```bash
sudo ufw status
```

Si está activo:

```bash
sudo ufw allow from 192.168.68.0/24 to any port 11434 proto tcp
```

No abriría `11434` a todo internet. Mejor limitarlo a tu LAN.

## Prueba local en `serveria`

Antes de probar desde `sico-Modern`, confirma en el propio servidor:

```bash
curl http://127.0.0.1:11434/api/version
curl http://192.168.68.67:11434/api/version
```

Interpretación:

| Resultado | Significado |
|---|---|
| `127.0.0.1` funciona, `192.168.68.67` falla | Ollama está binded solo a localhost |
| Ambos funcionan en `serveria`, pero falla desde `sico-Modern` | firewall/ruta/red |
| Ninguno funciona | Ollama no está sirviendo bien aunque el proceso exista |

## Nota sobre GPU

`ollama ps` vacío y `nvidia-smi` sin procesos no es problema ahora. Ollama solo cargará el modelo en GPU cuando hagas una inferencia. El problema actual ocurre antes: ni siquiera llegas al puerto HTTP.
---


Sí: lo revisé. **No necesitas estar logueado en GitHub para usar modelos locales de Ollama en VS Code**. El login solo aparece como requisito para **modelos cloud de Ollama**, vía `ollama signin`; los modelos locales no requieren sign-in. citeturn684473view0

## Requisitos de la extensión oficial `ollama/ollama-vscode`

Según el README del proyecto:

| Requisito | Detalle |
|---|---|
| VS Code | **1.120 o superior** |
| Ollama | Instalado y corriendo |
| Modelos | Al menos un modelo local o cloud disponible |
| Ollama recomendado | **0.17.6 o superior**, sobre todo para cloud/sign-in y metadata |
| Login | **No para local**, sí para cloud |

La extensión descubre modelos desde:

```text
http://127.0.0.1:11434
```

por defecto. citeturn684473view0

## Punto importante: esta extensión NO usa `/v1`

Antes te dije que para OpenAI-compatible podría ser `/v1`, pero revisando el código de esta extensión concreta, **no es lo correcto aquí**.

Esta extensión usa el cliente oficial `ollama` de JS y llama a endpoints nativos de Ollama como:

```text
/api/tags
/api/chat
/api/version
```

No está usando el endpoint OpenAI-compatible `/v1/chat/completions`. En `package.json` y el código fuente, el valor por defecto es:

```text
http://127.0.0.1:11434
```

y la setting se llama `ollama.endpoint`. citeturn646631view0

Para tu caso remoto, el endpoint correcto debería ser:

```text
http://192.168.68.67:11434
```

No:

```text
http://192.168.68.67:11434/v1
```

## Header correcto

En la configuración de VS Code, para que coincida con tu curl:

```bash
-H "Authorization: Bearer ollama"
```

debes poner:

| Item | Value |
|---|---|
| `Authorization` | `Bearer ollama` |

No uses `API-Key = ollama`, porque eso mandaría otro header distinto:

```http
API-Key: ollama
```

La extensión permite headers arbitrarios en `ollama.headers`, y los pasa tanto al descubrimiento de modelos como a las requests de chat. citeturn646631view0turn646631view1

## Lo que probablemente te falta

Por lo que muestras, yo corregiría esto:

```text
Ollama: Endpoint
http://192.168.68.67:11434
```

Y en headers:

```text
Authorization = Bearer ollama
```

Luego ejecuta en VS Code:

```text
Ollama: Refresh Models
```

Si no aparecen modelos:

```text
Ollama: Diagnose Models
```

La propia extensión recomienda `Refresh Models` y `Diagnose Models` para verificar descubrimiento de modelos en el canal de salida `Ollama`. citeturn684473view0

## Pruebas que deberías hacer desde el equipo con VS Code

Primero prueba API nativa, no OpenAI-compatible:

```bash
curl -H "Authorization: Bearer ollama" \
  http://192.168.68.67:11434/api/version
```

Luego:

```bash
curl -H "Authorization: Bearer ollama" \
  http://192.168.68.67:11434/api/tags
```

La extensión necesita poder listar modelos; si `/api/tags` falla, VS Code no tendrá modelos que mostrar.

## Sobre GitHub login

No debería ser el problema.

Lo bueno:

```text
VS Code sin login de GitHub + modelos locales Ollama = debería funcionar
```

Lo malo:

```text
Si estás intentando usar el chat integrado de VS Code/Copilot como interfaz,
puede haber dependencia de componentes de VS Code/Copilot, no de GitHub.com como tal.
```

Pero según el repo `ollama-vscode`, la extensión registra un proveedor de modelos de lenguaje de VS Code y expone modelos en el selector. No hay nada en los requisitos que diga que debas iniciar sesión en GitHub para modelos locales. citeturn428989view0

## Config final recomendada para tu pantalla

Deja así:

```text
Ollama: Endpoint
http://192.168.68.67:11434
```

Headers:

```text
Authorization    Bearer ollama
```

Después:

1. Reinicia VS Code.
2. Abre el Chat de VS Code.
3. Abre el selector de modelos abajo.
4. Busca sección `Ollama`.
5. Ejecuta `Ollama: Diagnose Models` si no sale nada.

Tu error más probable ahora mismo es usar el header con nombre `API-Key` o usar `/v1` con una extensión que espera la API nativa de Ollama.
---


Ese `ss` confirma que **Ollama sí está escuchando en todas las interfaces**:

```text
*:11434
```

Así que ya no parece un problema de `OLLAMA_HOST`. Ahora las causas probables son:

1. **IP equivocada**: `192.168.68.67` quizá no es la IP actual de `serveria`.
2. **Firewall en `serveria`** bloqueando el puerto.
3. **Red/VLAN/AP isolation** entre `sico-Modern` y `serveria`.
4. **Ruta incorrecta** desde `sico-Modern`.

## 1. En `serveria`, confirma la IP real

Ejecuta:

```bash
ip -br addr
```

Busca la interfaz LAN/Wi-Fi y confirma si realmente tiene:

```text
192.168.68.67
```

También prueba en el propio `serveria`:

```bash
curl http://127.0.0.1:11434/api/version
curl http://192.168.68.67:11434/api/version
```

Si el segundo falla en el propio servidor, la IP no es correcta o hay algo raro con la interfaz.

## 2. Desde `sico-Modern`, prueba conectividad básica

```bash
ping -c 3 192.168.68.67
```

Luego:

```bash
nc -vz 192.168.68.67 11434
```

Si no tienes `nc`:

```bash
sudo apt install netcat-openbsd
```

Interpretación:

| Prueba | Resultado | Significado |
|---|---|---|
| `ping` falla | No hay conectividad IP básica o ICMP bloqueado |
| `ping` funciona, `nc` falla | Puerto bloqueado o filtrado |
| `nc` funciona, `curl` falla | Problema HTTP/header/proxy, menos probable |
| `nc` y `curl` funcionan | VS Code es lo único mal configurado |

## 3. Revisa firewall en `serveria`

En `serveria`:

```bash
sudo ufw status verbose
```

Si está activo, permite solo tu LAN:

```bash
sudo ufw allow from 192.168.68.0/24 to any port 11434 proto tcp
```

Luego:

```bash
sudo ufw reload
```

Vuelve a probar desde `sico-Modern`:

```bash
curl http://192.168.68.67:11434/api/version
```

## 4. Verifica que no estás en otra subred

Desde `sico-Modern`:

```bash
ip -br addr
ip route
```

Si `sico-Modern` no está en algo tipo:

```text
192.168.68.x/24
```

puede estar en otra red. En ese caso el router/firewall puede bloquear tráfico entre clientes.

## 5. Prueba temporal sin firewall

Solo para aislar el problema, en `serveria`:

```bash
sudo ufw disable
```

Prueba desde `sico-Modern`:

```bash
curl http://192.168.68.67:11434/api/version
```

Si ahora funciona, ya está identificado: era firewall. Después vuelve a activarlo:

```bash
sudo ufw enable
sudo ufw allow from 192.168.68.0/24 to any port 11434 proto tcp
```

## Lo importante

Tu salida:

```text
LISTEN *:11434
```

es buena. Significa que Ollama está listo para aceptar conexiones externas.

Lo malo: el error `Could not connect to server` desde `sico-Modern` indica que el bloqueo está **entre el cliente y el puerto**, no en VS Code ni en el header `Authorization`.

Cuando `curl` funcione desde `sico-Modern`, la extensión debería usar:

```text
Endpoint: http://192.168.68.67:11434
Authorization: Bearer ollama
```
---


Sí. Para usar **Ollama local/remoto sin depender del Chat de Copilot**, estas son las opciones razonables.

## Recomendación principal: Zed

**Zed** tiene integración directa con Ollama. En su documentación: vas al icono de agente, configuras proveedor **Ollama**, pones el host, conectas y seleccionas modelo. Por defecto usa `http://localhost:11434`, pero en tu caso usarías `http://serveria.local:11434`. citeturn901612search2

Para tu caso:

```text
Host URL:
http://serveria.local:11434
```

**Lo bueno**
- No depende del panel de GitHub Copilot.
- Tiene integración de IA bastante nativa.
- Disponible para Linux, macOS y Windows. citeturn901612search1
- Encaja bien con Ollama remoto.

**Lo malo**
- Es otro editor; no es VS Code.
- Algunas funciones/extensiones de VS Code no las tendrás igual.
- Si necesitas workflows muy específicos de VS Code, puede quedarse corto.

## Segunda opción: VS Code + Continue

Aunque sigas usando VS Code, puedes evitar el Chat de Copilot usando **Continue**. Continue funciona como asistente open-source dentro de VS Code y JetBrains, y Ollama publicó una guía donde explica usarlo con modelos open-source locales o con Ollama desplegado en un servidor remoto. citeturn901612search4

Tu configuración conceptual sería:

```text
Provider: ollama
API base / host: http://serveria.local:11434
Modelo: qwen3:8b
```

**Lo bueno**
- Sigues en VS Code.
- No dependes del Chat de Copilot.
- Sirve para chat y asistencia sobre código.
- Buena opción si quieres cero login de GitHub.

**Lo malo**
- Es otra extensión más.
- La configuración puede requerir tocar JSON.
- La experiencia puede variar según versión y modelo.

## Tercera opción: JetBrains + Continue

Si usas IntelliJ, PyCharm, WebStorm, etc., puedes usar **Continue** también ahí. La guía de Ollama menciona Continue para VS Code y JetBrains. citeturn901612search4

**Ojo:** la integración oficial de Ollama con JetBrains AI parece requerir **JetBrains AI Subscription** según la propia documentación de Ollama. citeturn901612search9 Por eso, para JetBrains sin pagar, miraría antes Continue.

**Lo bueno**
- JetBrains es muy fuerte para Java, Python, JS/TS, PHP, Go, etc.
- Continue evita depender de JetBrains AI oficial.

**Lo malo**
- JetBrains consume más recursos.
- La integración oficial de IA local puede pasar por suscripciones.
- Continue puede no sentirse tan integrado como la IA oficial.

## Cline / Roo Code

Ollama lista **Cline** y **Roo Code** entre sus integraciones de editores/IDEs. citeturn901612search0 Son útiles si quieres un agente que pueda editar archivos, ejecutar comandos y trabajar por tareas.

**Lo bueno**
- Más “agente” que chat simple.
- Pueden trabajar sobre proyectos completos.
- Funcionan dentro de VS Code.

**Lo malo**
- Más riesgo operativo: pueden tocar muchos archivos o ejecutar comandos.
- Hay que configurar bien aprobaciones.
- Para empezar, son más pesados que Continue o Zed.

## Mi recomendación para ti

Dado que ya tienes Ollama remoto funcionando en:

```text
http://serveria.local:11434
```

yo elegiría así:

| Caso | Opción |
|---|---|
| Quieres cambiar de editor | **Zed** |
| Quieres seguir en VS Code sin login GitHub | **Continue** |
| Quieres un agente que modifique archivos | **Roo Code** o **Cline** |
| Usas JetBrains | **Continue en JetBrains**, no JetBrains AI oficial |

Para probar rápido y con bajo riesgo: **VS Code + Continue** usando `qwen3:8b`. Zed sería mi segunda prueba si quieres salir del ecosistema VS Code/Copilot.

---
*Generado desde conversación con 24 mensajes.*
*IA/ML*
