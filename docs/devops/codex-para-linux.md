---
title: Codex para Linux
date: 2026-06-17
category: DevOps
slug: codex-para-linux
tags: ['DevOps']
---

# Codex para Linux


> **Pregunta original:**
> 
Puedo usar el CLI con bun ?
> Lo que he visto en youtube , en videos patrocinado por OpenAI, es que nativa significa un sandbox propio  ,uso de PowerShell , optimizada en Rust. Si uso el CLI tendré esas optimizaciones en Linux , shellScript en vez de PowerShell pero con orientacion a sistemas  linux  ?
> que hace la intalacion standalone ?
> 
> *...y 1 preguntas de seguimiento*


---


## Respuesta


Sí, **pero hay dos sentidos distintos**:

## 1. Usar Codex CLI *en un proyecto Bun*

**Sí. Sin problema.**  
Codex CLI corre en tu terminal, inspecciona el repositorio, edita archivos y puede ejecutar comandos locales dentro del directorio seleccionado. OpenAI lo describe como un agente local de terminal que puede leer, cambiar y ejecutar código en tu máquina. citeturn159098view0

En un proyecto Bun, lo normal sería:

```bash
cd tu-proyecto
codex
```

Y dentro de Codex podrías pedirle cosas como:

```text
Revisa este proyecto Bun, ejecuta los tests con bun test y corrige los fallos mínimos necesarios.
```

O:

```text
Convierte este script de Node a Bun, usando bun:sqlite y bun test cuando tenga sentido.
```

Codex podrá usar comandos como:

```bash
bun install
bun run dev
bun test
bun run build
```

siempre que **Bun esté instalado y disponible en tu PATH**.

## 2. Instalar o ejecutar Codex CLI *con Bun*

Aquí sería más prudente.

La instalación oficial recomendada para macOS/Linux es el instalador standalone:

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

OpenAI también documenta instalación por `npm` y Homebrew, y el repositorio oficial menciona descarga directa de binarios para Linux x86_64 y arm64. citeturn159098view0turn159098view1

También podrías probar algo tipo:

```bash
bunx @openai/codex
```

o:

```bash
bun install -g @openai/codex
```

pero **no lo tomaría como la vía más fiable**. He visto incidencias reportadas con `bunx @openai/codex` en ciertas versiones/entornos, por ejemplo WSL2, y también casos donde instalaciones globales vía Bun causaron conflictos con la versión de Codex. citeturn460405search8turn460405search9

## Recomendación práctica

Para Linux + Bun, yo haría esto:

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

Luego:

```bash
which codex
codex --version
bun --version
```

Y en tu proyecto:

```bash
cd mi-app-bun
codex
```

## Lo bueno

- **Codex puede trabajar perfectamente sobre proyectos Bun**.
- No depende de Node para entender o modificar un repo Bun.
- Puede ejecutar `bun test`, `bun run`, `bun install`, etc., si tú lo permites.
- La CLI actual está construida en Rust para velocidad y eficiencia, según la documentación oficial. citeturn159098view0

## Lo malo

- **No instalaría Codex con Bun como primera opción**.
- `bunx` puede funcionar, pero no parece la ruta más estable ni la más documentada.
- Puede haber conflictos si tienes varias instalaciones globales: `npm`, `bun`, standalone, Homebrew.
- Si Codex ejecuta comandos Bun, sigues necesitando revisar permisos y diffs; `bun install` o scripts de paquete pueden ejecutar código de terceros.

## Conclusión

**Sí, puedes usar Codex CLI con Bun en Linux**, especialmente para desarrollar, probar y refactorizar proyectos Bun.

La combinación más limpia sería:

```text
Codex CLI instalado con el instalador oficial
+
Bun instalado como runtime/package manager del proyecto
```

No usaría Bun para instalar Codex salvo que aceptes más fricción experimental.
---


Sí, **pero con matiz importante**:

## Estado actual

**No parece haber una app de escritorio nativa de Codex para Linux todavía.**  
La documentación oficial de OpenAI dice que la **Codex app** está disponible en **macOS y Windows**, y en la misma página aparece una opción de **“Get notified for Linux”**, lo que indica que Linux aún no está disponible como app de escritorio. citeturn182511view0

Lo que **sí existe para Linux** es **Codex CLI**, que corre localmente desde la terminal. OpenAI indica que Codex CLI está soportado en **macOS, Windows y Linux**, y que en macOS/Linux se instala con:

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

citeturn182511view1

## Resumen práctico

| Opción | Linux |
|---|---:|
| **Codex app de escritorio nativa** | **No disponible públicamente** |
| **Codex CLI** | **Sí disponible** |
| **Extensión IDE / VS Code, Cursor, Windsurf** | Sí, según entorno |
| **Codex en la web** | Sí, vía navegador |

## Lo bueno

- En Linux ya puedes usar Codex de forma real mediante **CLI**.
- Es la vía más natural si trabajas con repositorios, terminal, Git, scripts y entornos Unix.
- OpenAI documenta soporte oficial para Linux en Codex CLI. citeturn182511view4

## Lo malo

- No hay, por ahora, una **app gráfica nativa para Linux** equivalente a la de macOS/Windows.
- Si querías la experiencia de “command center” con interfaz de escritorio, worktrees visuales y gestión paralela desde una app, Linux todavía queda fuera.
- La existencia de “Get notified for Linux” sugiere que OpenAI puede estar preparando algo, pero no confirma fecha ni beta pública. citeturn182511view0

**Conclusión:** OpenAI **no ha lanzado aún una app Codex nativa para Linux**, ni siquiera veo una beta pública documentada. Para Linux, la opción oficial hoy es **Codex CLI**.
---


Voy a comprobar la documentación actual porque aquí importan dos cosas distintas: si Codex CLI se instala/ejecuta con Bun y si puede trabajar en proyectos Bun.
---


Voy a verificarlo en fuentes actuales, porque los productos de OpenAI y Codex han cambiado varias veces recientemente.
---


Sí: **si usas Codex CLI en Linux, estás usando la vía “nativa” para Linux en el sentido técnico que describes**: binario/implementación mantenida en Rust, ejecución local, integración con shell Unix, y sandboxing Linux. Lo que **no** tienes en Linux —al menos públicamente documentado— es la **app gráfica de escritorio** equivalente a macOS/Windows.

## 1. “Nativa” no significa lo mismo en cada plataforma

En el material de Windows, OpenAI usa “nativo” para decir: **no necesitas WSL ni VM**; Codex puede correr en **PowerShell** con un **sandbox nativo de Windows**. La documentación dice que en Windows puede usar sandbox nativo de Windows si corre en PowerShell, o sandbox Linux si corre dentro de WSL2. citeturn229319search4

En Linux, el equivalente conceptual no sería PowerShell, sino:

```bash
bash
zsh
fish
sh
```

y herramientas estándar del sistema:

```bash
git
make
python
node
cargo
gcc
docker
systemctl
journalctl
grep
sed
awk
```

OpenAI documenta Codex CLI como disponible en **macOS, Windows y Linux**. citeturn229319search0

## 2. ¿Tendrás las optimizaciones en Rust en Linux?

**Sí, en principio.** La implementación Rust es la CLI mantenida por OpenAI. El repositorio oficial indica que la implementación en Rust es ahora la experiencia mantenida por defecto del Codex CLI, con funciones que la antigua CLI TypeScript no tenía. citeturn229319search17

Eso implica que en Linux no estarías usando una versión “de segunda clase” basada en scripts; estarías usando la misma línea principal del producto CLI.

La diferencia importante:

| Elemento | Linux con Codex CLI |
|---|---|
| Implementación Rust | **Sí** |
| Ejecución local | **Sí** |
| Orientación terminal/shell | **Sí** |
| Sandbox OS-level | **Sí** |
| PowerShell | No, salvo que tú lo instales |
| Shell Unix/Linux | **Sí** |
| App gráfica Codex desktop | No públicamente disponible |

## 3. ¿Tiene sandbox propio en Linux?

**Sí, pero no lo llamaría “sandbox propio” en el sentido de una VM cerrada de OpenAI.** Es más preciso decir que Codex usa un **sandbox aplicado por el sistema operativo**.

OpenAI describe que localmente Codex usa un sandbox impuesto por el OS para limitar qué puede tocar, normalmente el workspace actual, junto con una política de aprobaciones para controlar cuándo puede salir de esos límites. citeturn229319search19

Para Linux y WSL2, la documentación de sandboxing de Codex dice que usa la implementación de sandbox Linux; en Windows con PowerShell usa la implementación nativa de Windows. citeturn229319search8

En términos prácticos: en Linux, Codex debería estar más alineado con el modelo de permisos, procesos y filesystem de Linux que con el modelo de PowerShell/Windows.

## 4. ¿Está orientado a sistemas Linux?

**Sí, en el uso práctico.** Codex CLI trabaja desde tu terminal y ejecuta comandos en el entorno donde está instalado. En Linux eso significa que sus acciones se expresan naturalmente como comandos Unix/Linux.

Ejemplos típicos:

```bash
codex
```

Dentro de un repo podrías pedirle cosas como:

```text
Revisa este servicio systemd, encuentra por qué no arranca y propón un fix.
```

O:

```text
Ejecuta los tests, identifica el fallo y modifica el código mínimo necesario.
```

O:

```text
Convierte este script bash en una versión más robusta con set -euo pipefail y logging.
```

La CLI puede moverse muy bien en tareas de:

- repositorios Git;
- scripts Bash;
- Makefiles;
- Dockerfiles;
- servicios systemd;
- toolchains C/C++/Rust/Python/Node;
- logs locales;
- CI/CD;
- administración de proyectos Linux.

## 5. Lo bueno

- **Linux no depende de WSL**: ya estás en el entorno Linux real.
- **La CLI Rust es la rama mantenida**: no parece una implementación obsoleta o secundaria. citeturn229319search17
- **El sandboxing encaja mejor con Linux** que una capa traducida desde Windows.
- **La experiencia terminal es probablemente más natural en Linux** que en Windows si tu flujo de trabajo ya usa Bash, Git, Make, Docker, SSH, systemd, etc.
- **No necesitas PowerShell** para obtener la orientación “de sistemas”; en Linux el shell nativo es precisamente Bash/Zsh/etc.

## 6. Lo malo

- **No tienes la app gráfica de escritorio para Linux**, al menos no documentada públicamente.
- Algunas demos patrocinadas pueden mezclar varios conceptos: app desktop, CLI, sandbox, PowerShell, Rust, IDE y Codex Web. No todo eso aplica igual en Linux.
- El sandbox no debe confundirse con seguridad absoluta. Un agente local que ejecuta comandos sigue siendo una superficie de riesgo; conviene mantener aprobaciones, revisar diffs y no darle acceso amplio a secretos.
- Si ciertas funciones visuales de la app desktop están pensadas para Windows/macOS, es posible que no estén presentes en CLI puro.

## Conclusión

**Sí:** usando **Codex CLI en Linux** deberías obtener la parte relevante: **CLI mantenida en Rust, ejecución local, integración con shell Linux y sandboxing Linux**.

**No:** no obtienes una **app nativa gráfica de Linux** como producto separado.

La equivalencia correcta sería:

```text
Windows app/CLI + PowerShell + Windows sandbox
≈
Linux CLI + bash/zsh/sh + Linux sandbox
```

Para un perfil orientado a sistemas Linux, la CLI probablemente es incluso la forma más coherente de usar Codex.
---


Voy a separar lo que está documentado oficialmente de lo que normalmente hace un instalador standalone en Linux, porque no conviene ejecutar scripts `curl | sh` sin entenderlos.
---


La instalación **standalone** de Codex CLI es básicamente: **descargar un binario precompilado de Codex para tu plataforma y dejar un comando `codex` accesible en tu PATH**, sin depender de `npm`, `bun`, Homebrew ni compilar Rust localmente.

## Qué hace en Linux/macOS

El comando oficial es:

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

OpenAI lo documenta como el instalador standalone para macOS/Linux. Luego ejecutas:

```bash
codex
```

y en el primer arranque te pedirá autenticarte con tu cuenta de ChatGPT o una API key. citeturn990765view1

## En términos prácticos

La instalación standalone normalmente hace esto:

| Paso | Qué implica |
|---|---|
| Detecta plataforma | Linux/macOS y arquitectura: x86_64 o arm64 |
| Descarga paquete | Baja el archivo correcto de Codex CLI |
| Verifica/instala | Usa metadatos/checksum del paquete cuando aplica |
| Copia el ejecutable | Deja `codex` en un directorio ejecutable |
| Crea estado local | Usa `~/.codex` para configuración, auth, logs, sesiones y metadatos |
| No usa Node/Bun | No depende de `npm install -g` ni de `bun install -g` |

OpenAI documenta que `CODEX_HOME` por defecto es:

```bash
~/.codex
```

y ahí se guarda estado de Codex: configuración, autenticación, logs, sesiones, skills y metadatos de paquetes standalone. citeturn990765view0

El comando visible `codex` se instala por defecto en:

```bash
~/.local/bin
```

en macOS/Linux, salvo que cambies la variable `CODEX_INSTALL_DIR`. citeturn990765view0

## Dónde queda instalado

Por defecto:

```bash
~/.local/bin/codex
~/.codex/
```

Además, la documentación dice que la caché del paquete standalone queda bajo:

```bash
~/.codex/packages/standalone
```

o bajo la ruta equivalente si cambias `CODEX_HOME`. citeturn990765view0

Puedes comprobarlo con:

```bash
which codex
codex --version
ls -la ~/.codex
ls -la ~/.codex/packages/standalone
```

## Cómo cambiar el directorio de instalación

Puedes instalar el comando `codex` en otra ruta:

```bash
CODEX_INSTALL_DIR="$HOME/bin" sh install.sh
```

Con el método directo:

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | CODEX_INSTALL_DIR="$HOME/bin" sh
```

Para instalación sin prompts:

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | CODEX_NON_INTERACTIVE=1 sh
```

OpenAI documenta `CODEX_NON_INTERACTIVE=1` para instalaciones desatendidas; usa las respuestas por defecto y sirve más para scripts/updates que para una primera configuración manual. citeturn990765view0

## Qué **no** hace

No debería hacer estas cosas:

| No hace | Comentario |
|---|---|
| No instala Bun | Bun va aparte |
| No instala Node | No debería necesitarlo para standalone |
| No compila Rust | Descarga binario ya compilado |
| No instala Docker | Codex puede usar tu entorno, pero no te monta todo |
| No configura todo tu sistema Linux | Instala el CLI y su estado de usuario |
| No convierte Linux en sandbox global | El sandbox opera cuando Codex ejecuta tareas, no como política general del sistema |

## Lo bueno

- **Menos dependencias**: no dependes de `npm`, `bun`, `pnpm` ni Homebrew.
- **Más limpio para Linux**: ejecutable directo en `~/.local/bin`.
- **Actualización sencilla**: OpenAI indica que para actualizar una instalación standalone basta con volver a ejecutar el instalador. citeturn990765view1
- **Evita conflictos de package managers**: no mezclas `bun install -g`, `npm install -g` y binarios sueltos.
- **Usa el Codex CLI Rust actual**, que OpenAI describe como construido en Rust para velocidad y eficiencia. citeturn990765view1

## Lo malo / riesgos

- `curl | sh` **ejecuta un script remoto directamente**. Es cómodo, pero no es lo más auditable.
- El script cambia archivos en tu `$HOME`, al menos en `~/.local/bin` y `~/.codex`.
- Si `~/.local/bin` no está en tu `PATH`, después de instalar puede que `codex` no se encuentre.
- Hay reportes recientes en GitHub de problemas puntuales con el instalador standalone/checksums en algunas distribuciones Linux, así que no asumiría que es infalible en todos los sistemas. citeturn662914search9turn662914search12

## Forma más prudente de instalar

En vez de ejecutar directamente:

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

puedes inspeccionarlo primero:

```bash
curl -fsSL https://chatgpt.com/codex/install.sh -o /tmp/codex-install.sh
less /tmp/codex-install.sh
sh /tmp/codex-install.sh
```

Después verifica:

```bash
which codex
codex --version
codex
```

## Conclusión

La instalación standalone **instala Codex como binario local de usuario**, normalmente en:

```bash
~/.local/bin/codex
```

y guarda su configuración/estado en:

```bash
~/.codex
```

Para Linux, es la vía más limpia si quieres usar Codex CLI sin acoplarlo a Bun o npm.

---
*Generado desde conversación con 11 mensajes.*
*DevOps*
