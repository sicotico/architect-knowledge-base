---
title: Paquete nodejs Ubuntu 26.04
date: 2026-07-07
category: Programación
slug: paquete-nodejs-ubuntu-26-04
tags: ['Programación']
---

# Paquete nodejs Ubuntu 26.04


> **Pregunta original:**
> 
comparadoconla web oficial es el estable ?
> hay paquete de bunenubuntu ?
> cual es paquete de ubutnu 26.04 para nodejs  
> 
> *...y 1 preguntas de seguimiento*


---


## Respuesta


El registro devuelve 403 desde este entorno, así que voy por la fuente pública del proyecto en GitHub. Si el `package.json` está allí, nos dirá la versión mínima sin depender de npm.
---


Para **Pi en Ubuntu**, lo importante es esto: Pi declara en su `package.json` que necesita **Node `>=22.19.0`**. La guía de Pi recomienda instalarlo con npm así:

```bash
npm install -g --ignore-scripts @earendil-works/pi-coding-agent
```

Eso está en la documentación de [Pi Quick start](https://pi.dev/docs/latest), y el requisito de Node aparece en el `package.json` del proyecto en GitHub.

En **Ubuntu 26.04**, el paquete oficial `nodejs` es **Node 22.22.1**, así que **sí cumple** el requisito de Pi:

```bash
sudo apt update
sudo apt install nodejs npm
node --version
npm --version
npm install -g --ignore-scripts @earendil-works/pi-coding-agent
pi
```

Lo bueno de esta vía: usa paquetes de Ubuntu, es simple y suficiente para Pi en 26.04.

Lo malo: Ubuntu trae Node 22, mientras que la LTS oficial más reciente de Node es 24. Si quieres ir más alineado con Node oficial, instala Node 24 LTS con `nvm`, `fnm` o NodeSource. Para Pi, ambas deberían valer: **Node 22.22 de Ubuntu 26.04 ya es compatible**.
---


La documentación rápida de Pi recomienda instalar con `npm install -g --ignore-scripts ...`; no da ahí la receta de Node para Ubuntu. Voy a comprobar el paquete npm para ver la versión mínima declarada, que es lo que manda para que funcione bien.
---


Voy a comprobarlo en una fuente actual, porque los paquetes de Ubuntu cambian entre versiones y conviene no tirar de memoria.
---


No exactamente.

El paquete de Ubuntu 26.04 es **Node.js 22.22.1** según Ubuntu, mientras que la web oficial de Node.js muestra ahora:

| Fuente | Versión | Estado |
|---|---:|---|
| Ubuntu 26.04 `apt install nodejs` | `22.22.1` | LTS, pero rama antigua en mantenimiento |
| Node.js oficial recomendada | `24.15.0` | Latest LTS |
| Node.js oficial más nueva | `26.1.0` | Current, no LTS todavía |

Así que: **sí es estable en el sentido de que Node 22 es LTS**, pero **no es la LTS estable recomendada más reciente**. La oficial recomendada para la mayoría de usuarios ahora es **Node 24 LTS** desde [nodejs.org](https://nodejs.org/en/download?lang=node). Además, el calendario oficial marca Node 22 como **Maintenance LTS** y Node 24 como **Active LTS** ([Node.js Release schedule](https://github.com/nodejs/release)).

Lo bueno del paquete de Ubuntu: integración limpia con `apt`, actualizaciones de seguridad de Ubuntu, menos lío en servidores.

Lo malo: vas por detrás de la LTS oficial actual. Para desarrollo moderno o si necesitas versiones recientes de npm/Node, mejor instalar desde NodeSource, `nvm`, `fnm`, o el tarball oficial.
---


En la portada ya aparece que Pi se instala vía `curl`, `npm`, `pnpm` o `bun`, y el comando `npm` usa un paquete global. Voy a mirar la documentación para ver si fijan una versión mínima de Node o una vía preferida.
---


En Ubuntu 26.04 LTS, el paquete es:

```bash
sudo apt install nodejs
```

Está en el repositorio `universe`, y para Ubuntu 26.04 “resolute” aparece como `nodejs` versión `22.22.1...` en [Ubuntu Packages](https://packages.ubuntu.com/resolute/nodejs).

Si también quieres `npm`:

```bash
sudo apt install nodejs npm
```
---


Voy a revisar la recomendación concreta de `pi.dev`, porque las guías de instalación suelen depender de versiones exactas de Node y de cómo esperan que se resuelvan `npm`, permisos y binarios.
---


La página de npm bloqueó la vista web, así que usaré el registro de npm directamente para leer los metadatos del paquete. Eso suele ser más preciso para `engines.node`.
---


Voy a mirarlo en los paquetes de Ubuntu y, si hace falta, contrastarlo con la instalación oficial de Bun. Aquí importa distinguir “paquete en los repos de Ubuntu” de “paquete instalable en Ubuntu”.
---


En los repos oficiales de Ubuntu 26.04 no parece haber un paquete `bun` equivalente a `apt install bun`.

Lo normal en Ubuntu es instalar Bun con el método oficial:

```bash
sudo apt install unzip
curl -fsSL https://bun.com/install | bash
```

Eso instala el binario de Bun en tu usuario, no como paquete `.deb` gestionado por `apt`. La documentación oficial de Bun indica ese método para Linux y menciona que hace falta `unzip` ([Bun installation](https://bun.com/docs/installation)).

Lo bueno: tendrás Bun actualizado y oficial.

Lo malo: no queda gestionado por `apt` como `nodejs`; para entornos de servidor muy controlados puede ser menos limpio que un paquete de Ubuntu.
---


Voy a contrastarlo con la web oficial de Node.js, porque “estable” puede significar dos cosas distintas: la rama LTS recomendada o la versión Current más nueva.

---
*Generado desde conversación con 16 mensajes.*
*Programación*
