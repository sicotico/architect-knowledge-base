---
title: Instalar Codex en servidor
date: 2026-07-05
category: Programación
tags: ['Programación']
slug: instalar-codex-en-servidor
---

# Instalar Codex en servidor

> **Pregunta original:** para acotar codex , hay que ejecutarlo dentro del proyecto de tabbyAPI no  ?...


Para tu caso con TabbyAPI en el servidor, no lo miraría como “servidor o cliente” sino como dos piezas: dónde se ejecutan los comandos y dónde está la interfaz cómoda. Si Codex debe tocar ese entorno Python/uv real, el servidor empieza a ganar peso.

Voy a sacar el comando desde la referencia actual de Codex, porque la forma de instalación puede variar según versión y plataforma.

Para **instalar Docker en el sistema**, no hace falta ejecutarlo dentro de una carpeta de Docker. Eso es una tarea de sistema: `apt`, repos, grupos, `systemd`, permisos. Ahí lo importante es que Codex te pida aprobación antes de usar `sudo`.

Por ejemplo podrías lanzarlo desde una carpeta neutra:

```bash
mkdir -p ~/admin
cd ~/admin
codex --sandbox workspace-write --ask-for-approval on-request
```

Y pedirle:

```text
Quiero instalar Docker en este servidor Ubuntu. Primero inspecciona el sistema y dime el plan. No ejecutes comandos con sudo sin preguntarme.
```

Para **crear y administrar contenedores concretos**, sí conviene estar dentro de la carpeta del stack:

```bash
mkdir -p /opt/openwebui
cd /opt/openwebui
codex --sandbox workspace-write --ask-for-approval on-request
```

Ahí puede preparar `docker-compose.yml`, `.env`, volúmenes, documentación, etc.

Resumen: **Docker como paquete del sistema: carpeta neutra/admin. Apps en Docker: carpeta propia por app.**

Sí, esa estructura tiene mucho sentido. En ese caso yo ejecutaría Codex **dentro de la carpeta del servicio concreto**, no en `~/pods` salvo que quieras que vea o reorganice varios servicios a la vez.

Ejemplo:

```bash
~/pods/
  WebUI/
    docker-compose.yml
    .env
  app-propia/
    docker-compose.yml
    .env
  postgres-lab/
    docker-compose.yml
    .env
```

Para trabajar solo Open WebUI:

```bash
cd ~/pods/WebUI
codex --sandbox workspace-write --ask-for-approval on-request
```

Para tu app propia:

```bash
cd ~/pods/app-propia
codex --sandbox workspace-write --ask-for-approval on-request
```

Lo bueno: Codex queda acotado al servicio que estás tocando y no mezcla composiciones, variables ni volúmenes de otros stacks.

Lo malo: si necesitas cambios transversales, por ejemplo una red Docker compartida, Traefik/Caddy, backups globales o naming común, entonces sí puede convenir lanzarlo desde:

```bash
cd ~/pods
codex --sandbox workspace-write --ask-for-approval on-request
```

Mi recomendación: usa `~/pods` como raíz organizada, pero abre Codex normalmente en cada subcarpeta de servicio. Para cosas globales, una sesión puntual en `~/pods`.

Estoy usando la ruta de documentación de Codex porque aquí importa distinguir bien entre “instalar el agente donde está el código” y “manejarlo desde otra máquina”.

Voy a contrastarlo con la documentación actual de Codex/OpenAI antes de darte una recomendación, porque los detalles de instalación y autenticación cambian bastante rápido.

En Ubuntu, el comando de instalación es:

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

Luego comprueba:

```bash
codex --version
```

Y para iniciar sesión en un servidor sin navegador:

```bash
codex login --device-auth
```

Después ya lo usarías así:

```bash
cd ~/pods/WebUI
codex --sandbox workspace-write --ask-for-approval on-request
```

La parte clave que encuentro: Codex no es solo “un binario”; hay varias superficies. La CLI trabaja muy bien pegada al repositorio/local shell, mientras que la app/web/remote connections cambian bastante el modelo operativo.

Sí, exactamente: para instalar Open WebUI u otras apps en Docker, lo razonable es que Codex en el servidor trabaje como asistente y **te pregunte antes de tocar cosas de sistema o root**.

Yo lo usaría así:

```bash
cd /opt/o/la/ruta/donde-guardes-tus-stacks
codex --sandbox workspace-write --ask-for-approval on-request
```

Con ese enfoque, Codex puede preparar archivos como:

```text
docker-compose.yml
.env.example
README.md
scripts/
```

y ejecutar comandos normales dentro del proyecto. Pero para cosas como estas debería pedirte aprobación:

```bash
sudo apt install ...
sudo systemctl ...
sudo docker ...
docker compose up -d
ufw ...
chown/chmod en rutas sensibles
```

Para Docker hay un matiz importante: si tu usuario pertenece al grupo `docker`, entonces `docker` equivale casi a root. Es cómodo, pero poderoso. Lo bueno: Codex podría levantar y revisar contenedores sin pedir `sudo`. Lo malo: también podría montar volúmenes sensibles o tocar demasiado. Si quieres control, mejor que los comandos Docker importantes también pasen por aprobación.

Para Open WebUI, yo le pediría algo así:

```text
Quiero instalar Open WebUI en Docker en este servidor. Primero inspecciona el sistema y propón un docker-compose.yml seguro. No ejecutes nada con sudo ni levantes contenedores sin preguntarme.
```

Y luego, cuando ya te guste el plan:

```text
Aplica el compose en /opt/openwebui y pídeme aprobación antes de ejecutar docker compose up -d.
```

Mi postura: **sí instalaría Codex en el servidor**, especialmente si vas a gestionar Docker. Pero mantendría `--ask-for-approval on-request`, trabajaría en `/opt/...` o en un repo claro, y evitaría darle “modo libre” con root.

Sí, exactamente. Ese es el flujo que yo usaría.

```bash
ssh servidor
cd ~/pods/WebUI        # o /opt/tabbyapi, ~/pods/app-propia, etc.
codex --sandbox workspace-write --ask-for-approval on-request
```

Así Codex queda centrado en esa carpeta y te ayuda con ese servicio concreto. Si necesita hacer algo fuera, como instalar paquetes, tocar Docker, reiniciar servicios o escribir en `/etc`, debería pedirte aprobación.

Lo bueno: simple, seguro razonablemente, y muy claro mentalmente.
Lo malo: si una tarea afecta a varios servicios, tendrás que lanzarlo desde `~/pods` o explicarle rutas adicionales.

Para tu caso: **sí, SSH al servidor, `cd` a la carpeta de trabajo, lanzar Codex ahí**.

Sí, pero con matiz: instalar Codex en el servidor no significa dejarlo “administrando el servidor” de forma autónoma. Significa que **puede ayudarte a administrarlo desde dentro**, con tu supervisión.

En la práctica te serviría para cosas como:

- revisar configuración de TabbyAPI;
- tocar scripts de `uv`, `systemd`, logs, rutas y permisos;
- migrar más adelante de `uv` a Python del repo/sistema;
- preparar cambios de configuración;
- ejecutar pruebas;
- comparar antes/después;
- documentar comandos de mantenimiento.

Lo bueno es que, estando en el servidor, Codex ve el entorno real. Para una futura migración como la que dices, eso ayuda bastante: puede inspeccionar `pyproject.toml`, `.venv`, servicios, rutas, versiones de Python, variables de entorno y dependencias reales.

Lo malo es que conviene ponerle límites claros. Yo no le daría permisos amplios tipo root por defecto. Mejor:

```bash
ssh servidor
cd /opt/tabbyapi-o-tu-ruta
codex --sandbox workspace-write --ask-for-approval on-request
```

Y cuando haga falta tocar algo de sistema:

```bash
sudo systemctl status tabbyapi
sudo systemctl restart tabbyapi
sudo journalctl -u tabbyapi -n 100
```

que te lo proponga y tú apruebas.

Para tu plan de quitar `uv`, yo lo vería así:

1. Ahora: instalar Codex en servidor y usarlo como asistente operativo.
2. Después: pedirle que haga inventario del entorno actual.
3. Luego: preparar migración controlada a Python nativo/repo.
4. Finalmente: limpiar `uv`, `.venv`, scripts antiguos y documentación.

Conclusión: **sí lo instalaría**, pero como copiloto de administración, no como administrador automático con barra libre.

Puedes ser más permisivo, sí. Yo lo haría **por niveles**, no directamente con barra libre para todo.

Para administración general del servidor, una opción práctica sería:

```bash
cd ~/admin-servidor
codex --sandbox workspace-write --ask-for-approval on-request
```

y dentro le dices explícitamente:

```text
Puedes inspeccionar el sistema y proponer cambios. Puedes ejecutar comandos de lectura sin preguntarme. Antes de instalar paquetes, editar /etc, cambiar firewall, reiniciar servicios o borrar datos, pídeme confirmación.
```

Si quieres subir un nivel de libertad para tareas de mantenimiento, puedes usar:

```bash
codex --sandbox workspace-write --ask-for-approval never
```

Lo bueno: menos interrupciones.
Lo malo: si un comando dentro del workspace hace algo con Docker, scripts o credenciales, no se va a parar tanto a preguntarte.

Yo **no usaría de forma habitual**:

```bash
codex --dangerously-bypass-approvals-and-sandbox
```

Eso ya es equivalente a “haz lo que quieras en mi sistema”. Solo lo usaría en una VM desechable, laboratorio o entorno que puedas restaurar fácil.

Mi recomendación para tu servidor real:

```bash
cd ~/admin-servidor
codex --sandbox workspace-write --ask-for-approval on-request
```

Y cuando estés haciendo una tarea concreta donde aceptas más autonomía:

```bash
codex --sandbox workspace-write --ask-for-approval never
```

Pero para firewall, Docker, usuarios, `sudo`, `/etc`, servicios y borrados, yo seguiría prefiriendo confirmación. Es justo donde un pequeño error te deja fuera por SSH o te rompe un servicio.

Sí: **seguiría recomendando instalar Codex también en el servidor**.

Tener Codex en tu cliente no basta para que “trabaje remoto” de forma natural. Desde el cliente podría usar `ssh` para ejecutar comandos en el servidor, pero su espacio de trabajo principal seguiría siendo el del cliente, y editar archivos remotos, revisar diffs, ejecutar tests, leer logs, etc. se vuelve bastante más torpe.

La opción cómoda y limpia es:

```bash
ssh tu-servidor
cd /ruta/proyecto-tabbyapi
codex
```

O, si usas Codex App con conexión SSH, la documentación indica que para abrir proyectos en un SSH host el servidor remoto debe tener `codex` instalado, autenticado y disponible en el `PATH` [Remote connections](https://developers.openai.com/codex/remote-connections).

**En tu caso concreto, lo bueno de instalarlo en el servidor:**
- Codex trabaja donde están `uv`, Python 3.13, TabbyAPI, logs y servicios reales.
- Puede usar `localhost` si TabbyAPI solo escucha en la red local o en la propia máquina.
- No necesitas exponer nada a internet; sigues entrando por SSH.
- Tu cliente queda como terminal/interfaz, no como entorno de ejecución.

**Lo malo:**
- Hay que instalar y autenticar Codex una vez en el servidor.
- Debes proteger `~/.codex/auth.json` si usas login/cache en archivo.
- Si el servidor es headless, probablemente te convenga `codex login --device-auth`.

Yo lo montaría así: **Codex instalado en cliente y servidor**. El del cliente para proyectos locales; el del servidor para TabbyAPI. Y accedería por SSH normal, sin abrir puertos públicos.

Sí merece la pena instalar Codex en el servidor si quieres que trabaje de verdad sobre ese entorno: `uv`, Python 3.13, TabbyAPI, rutas reales, logs, systemd, permisos y dependencias locales. La CLI de Codex está soportada en Linux y puede leer, modificar y ejecutar código en el directorio donde la lanzas [OpenAI Codex CLI](https://developers.openai.com/codex/cli).

Mi recomendación práctica: **instala Codex en el servidor, pero adminístralo desde tu cliente por SSH o desde la Codex App conectada al host SSH**. La documentación de remote connections dice que, para proyectos en un SSH host, la app ejecuta los hilos contra el filesystem y shell remotos, y requiere que `codex` esté instalado/autenticado en el host remoto y disponible en el `PATH` [Remote connections](https://developers.openai.com/codex/remote-connections).

**Lo bueno de instalarlo en el servidor**
- Codex ve el entorno real donde corre TabbyAPI.
- Puede ejecutar `uv`, tests, scripts, logs y comandos de servicio sin reproducir nada en tu portátil.
- Puedes configurarlo para hablar con un endpoint OpenAI-compatible local, por ejemplo TabbyAPI, mediante `model_providers` o `openai_base_url` en `~/.codex/config.toml` [Advanced configuration](https://developers.openai.com/codex/config-advanced).
- Si el servidor está siempre encendido, puedes retomarlo desde otro dispositivo con menos fricción.

**Lo malo**
- Hay que cuidar mucho credenciales: Codex puede guardar tokens en `~/.codex/auth.json` si usas almacenamiento en archivo, y eso debe tratarse como una contraseña [Authentication](https://developers.openai.com/codex/auth).
- En servidor headless, el login puede requerir device-code auth, túnel SSH o copiar el auth cache.
- No expondría `codex app-server` abierto a internet. Si lo usas, mejor por SSH/VPN y con autenticación; para uso normal, SSH es suficiente.
- Con modelos locales vía TabbyAPI, la comodidad puede bajar si el modelo no es tan fuerte en edición, herramientas y razonamiento como los modelos OpenAI.

**Conclusión corta:** para tu caso, **sí: Codex en el servidor**. Usa el cliente solo como interfaz cómoda. La ruta limpia sería:

```bash
ssh tu-servidor
cd /ruta/de/tu/proyecto
codex login --device-auth
codex
```

Y si quieres integrarlo con TabbyAPI local, lo pondría en `~/.codex/config.toml` del servidor, no dentro del repo, porque los proveedores/model providers son configuración de usuario, no proyecto.

Para administrar Ubuntu en general, yo no lo lanzaría dentro de TabbyAPI ni dentro de un stack Docker concreto. Crearía una carpeta “admin” y trabajaría desde ahí:

```bash
mkdir -p ~/admin-servidor
cd ~/admin-servidor
codex --sandbox workspace-write --ask-for-approval on-request
```

Desde ahí le puedes pedir tareas de sistema:

```text
Analiza el estado del firewall y proponme reglas seguras. No apliques cambios sin pedirme confirmación.
```

O:

```text
Revisa logs de systemd para encontrar errores recientes. Puedes leer logs, pero no reinicies servicios ni cambies configuración sin preguntarme.
```

Lo bueno de este enfoque: Codex no está “metido” en una app concreta y puedes usarlo como asistente de administración. Además, con `--ask-for-approval on-request`, las acciones delicadas deberían pasar por tu confirmación.

Lo malo: para muchas tareas de administración necesitará comandos con permisos elevados, por ejemplo:

```bash
sudo journalctl -xe
sudo journalctl -u tabbyapi -n 200
sudo ufw status verbose
sudo iptables -S
sudo systemctl status servicio
```

Leer logs suele ser bastante seguro. Cambiar firewall, reiniciar servicios, instalar paquetes, editar `/etc`, tocar usuarios/grupos o Docker ya es otra cosa: ahí yo exigiría siempre confirmación.

Mi regla práctica sería:

- Para una app: `cd ~/pods/WebUI` o `/opt/tabbyapi`.
- Para Docker global: `cd ~/pods`.
- Para Ubuntu/firewall/logs/sistema: `cd ~/admin-servidor`.
- Para cambios con `sudo`: que Codex proponga, tú revisas, luego autorizas.

Sí: según la referencia actual de Codex, para `--ask-for-approval` las opciones principales son:

```bash
--ask-for-approval untrusted
--ask-for-approval on-request
--ask-for-approval never
```

También existía `on-failure`, pero está **deprecated**; mejor no usarla [Codex CLI reference](https://developers.openai.com/codex/cli/reference).

La diferencia práctica:

| Opción | Qué implica |
|---|---|
| `untrusted` | Más prudente. Pide aprobación con más frecuencia, especialmente en contextos no confiados. |
| `on-request` | Equilibrada. Codex trabaja y pide aprobación cuando la necesita para acciones sensibles o fuera de permisos. |
| `never` | Más permisiva. Codex no te pide aprobación; si algo no puede hacerse por sandbox/permisos, fallará o buscará alternativa. |

Para tu servidor, yo usaría normalmente:

```bash
codex --sandbox workspace-write --ask-for-approval on-request
```

Si quieres más autonomía pero sin quitar sandbox:

```bash
codex --sandbox workspace-write --ask-for-approval never
```

Pero entre `on-request` y `never`, como punto intermedio real, **no hay otra opción recomendada**.

Sí: **por defecto, yo lo lanzaría siempre así en el servidor**:

```bash
codex --sandbox workspace-write --ask-for-approval on-request
```

Es una buena base para casi todo.

Lo bueno:
- Codex puede trabajar dentro de la carpeta donde lo lanzas.
- Si necesita hacer algo delicado, debería pararse y pedirte aprobación.
- Evitas darle libertad total sobre el servidor.

Lo malo:
- Algunas tareas de administración serán más lentas porque tendrá que pedir permiso.
- Para instalar Docker, tocar firewall, editar `/etc`, reiniciar servicios o usar `sudo`, habrá más confirmaciones.

Yo solo usaría algo más permisivo si estás en una máquina de pruebas o tienes clarísimo que no hay riesgo. En tu servidor real, con TabbyAPI y posibles servicios Docker, mantendría esa combinación como costumbre.

Ejemplo completo:

```bash
ssh servidor
cd ~/pods/WebUI
codex --sandbox workspace-write --ask-for-approval on-request
```

Y para administración:

```bash
cd ~/admin-servidor
codex --sandbox workspace-write --ask-for-approval on-request
```

Sí. Para acotarlo bien, lo normal es **entrar en la carpeta del proyecto y lanzar Codex desde ahí**:

```bash
ssh servidor
cd /opt/tabbyapi
codex --sandbox workspace-write --ask-for-approval on-request
```

Así Codex toma esa carpeta como espacio principal de trabajo. Con `workspace-write`, en principio puede escribir dentro del proyecto, pero no debería tocar libremente el resto del sistema. Si necesita leer logs, reiniciar servicios, tocar Docker, `systemd`, `/etc`, `/opt/openwebui`, etc., debería proponértelo y pedir aprobación.

También puedes hacerlo sin cambiar de carpeta:

```bash
codex --cd /opt/tabbyapi --sandbox workspace-write --ask-for-approval on-request
```

Lo bueno de lanzarlo dentro de TabbyAPI es que verá bien el repo, `.venv`, `pyproject.toml`, scripts, configs y contexto real. Lo malo es que si luego quieres administrar Open WebUI u otro stack Docker, mejor abrir otra sesión desde su propia carpeta, por ejemplo:

```bash
cd /opt/openwebui
codex --sandbox workspace-write --ask-for-approval on-request
```

Yo separaría cada app en su directorio: `/opt/tabbyapi`, `/opt/openwebui`, `/opt/stacks/...`. Así Codex queda más acotado y tú mantienes claro qué está tocando.

---
*Generado desde conversación con 67 mensajes.*
*Categoría: Programación*
