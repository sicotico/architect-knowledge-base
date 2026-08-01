---
title: Error en PowerShell Docker
date: 2025-03-24
category: DevOps
slug: error-en-powershell-docker
tags: ['DevOps']
---

# Error en PowerShell Docker


> **Pregunta original:**
> 
Como soluciono esto:

ERROR: failed to solve: process "/bin/sh -c pwsh -Command \"Set-PSRepository -Name PSGallery -InstallationPolicy Trusted\"" did not complete successfully: exit code: 1

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/oisytxgxlygqzhidzvx47y992
[2560 ms] Error: Command failed: docker buildx build --load --build-arg BUILDKIT_INLINE_CACHE=1 -f /var/folders/s5/8n40yvcx5mg727jg9htj0bf80000gn/T/devcontainercli/container-features/0.72.0-1742836818554/Dockerfile-with-features -t vsc-ari-cf6f648992ac3339ff951e80de6a252374810d2b26b249c17d71b8fc018a53be --target dev_containers_target_stage --build-arg _DEV_CONTAINERS_BASE_IMAGE=dev_container_auto_added_stage_label /Users/luis/ARI/.devcontainer
[2560 ms]     at RtA (/Users/luis/.cursor/extensions/ms-vscode-remote.remote-containers-0.394.0/dist/spec-node/devContainersSpecCLI.js:466:1933)
[2560 ms]     at async _m (/Users/luis/.cursor/extensions/ms-vscode-remote.remote-containers-0.394.0/dist/spec-node/devContainersSpecCLI.js:465:1896)
[2560 ms]     at async bH (/Users/luis/.cursor/extensions/ms-vscode-remote.remote-containers-0.394.0/dist/spec-node/devContainersSpecCLI.js:465:610)
[2560 ms]     at async TtA (/Users/luis/.cursor/extensions/ms-vscode-remote.remote-containers-0.394.0/dist/spec-node/devContainersSpecCLI.js:482:3848)
[2561 ms]     at async iB (/Users/luis/.cursor/extensions/ms-vscode-remote.remote-containers-0.394.0/dist/spec-node/devContainersSpecCLI.js:482:4963)
[2561 ms]     at async wrA (/Users/luis/.cursor/extensions/ms-vscode-remote.remote-containers-0.394.0/dist/spec-node/devContainersSpecCLI.js:663:203)
[2561 ms]     at async DrA (/Users/luis/.cursor/extensions/ms-vscode-remote.remote-containers-0.394.0/dist/spec-node/devContainersSpecCLI.js:662:14830)
[2561 ms]     at async /Users/luis/.cursor/extensions/ms-vscode-remote.remote-containers-0.394.0/dist/spec-node/devContainersSpecCLI.js:482:1190
[2565 ms] Exit code 1
[2566 ms] Command failed: /Applications/Cursor.app/Contents/Frameworks/Cursor Helper (Plugin).app/Contents/MacOS/Cursor Helper (Plugin) /Users/luis/.cursor/extensions/ms-vscode-remote.remote-containers-0.394.0/dist/spec-node/devContainersSpecCLI.js up --user-data-folder /Users/luis/Library/Application Support/Cursor/User/globalStorage/ms-vscode-remote.remote-containers/data --container-session-data-folder /tmp/devcontainers-392dad97-7287-4021-967b-3c6dc304caa91742836817669 --workspace-folder /Users/luis/ARI --workspace-mount-consistency cached --gpu-availability detect --id-label devcontainer.local_folder=/Users/luis/ARI --id-label devcontainer.config_file=/Users/luis/ARI/.devcontainer/devcontainer.json --log-level debug --log-format json --config /Users/luis/ARI/.devcontainer/devcontainer.json --default-user-env-probe loginInteractiveShell --mount type=volume,source=vscode,target=/vscode,external=true --skip-post-create --update-remote-user-uid-default on --mount-workspace-git-root --include-configuration --include-merged-configuration
[2566 ms] Exit code 1

---


## Respuesta


Este error indica que durante la construcción del *dev container* se intentó ejecutar un comando de PowerShell (`pwsh`) dentro del contenedor, y ese comando falló:

```
pwsh -Command "Set-PSRepository -Name PSGallery -InstallationPolicy Trusted"
```

La causa puede variar, pero te doy una guía para depurar y resolverlo:

---

### ✅ **Posibles causas y soluciones**

#### 1. **PowerShell no instalado correctamente en la imagen base**
Si el contenedor no tiene `pwsh` (PowerShell Core) correctamente instalado, este comando fallará.

**Solución:**
Asegúrate de que la imagen base en tu `Dockerfile` o `.devcontainer/devcontainer.json` incluye PowerShell. Puedes añadirlo en tu Dockerfile:

```Dockerfile
RUN apt-get update && apt-get install -y wget apt-transport-https software-properties-common \
    && wget -q "https://packages.microsoft.com/config/debian/11/packages-microsoft-prod.deb" \
    && dpkg -i packages-microsoft-prod.deb \
    && apt-get update \
    && apt-get install -y powershell
```

Y luego:

```Dockerfile
RUN pwsh -Command "Set-PSRepository -Name PSGallery -InstallationPolicy Trusted"
```

---

#### 2. **Problemas de red o certificados**
A veces PowerShell falla con ese comando si no puede conectarse a `https://www.powershellgallery.com`.

**Solución:**
Verifica si dentro del contenedor se puede resolver ese dominio. Puedes entrar al contenedor base y probar:

```bash
docker run -it --rm <nombre-de-tu-imagen-base> bash
```

Y luego:

```bash
pwsh
```

En PowerShell:

```powershell
Find-Module -Name Pester
```

Si eso falla, tienes un problema de red o SSL en el contenedor. Podrías probar añadiendo este flag si es un tema de SSL:

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
```

---

#### 3. **Fallo al ejecutar en `Dockerfile` (ambiente no interactivo)**
Algunos comandos de PowerShell requieren un entorno interactivo o pueden comportarse diferente en el build.

**Solución alternativa:**
Si no necesitas ese comando en tiempo de build, puedes moverlo a un script de inicialización post-create en `.devcontainer`:

**`postCreateCommand` en `.devcontainer/devcontainer.json`:**

```json
"postCreateCommand": "pwsh -Command \"Set-PSRepository -Name PSGallery -InstallationPolicy Trusted\""
```

---

### 🛠️ ¿Qué revisar?

1. Verifica si `pwsh` está instalado dentro del contenedor.
2. Asegúrate que el comando funcione al ejecutarlo manualmente dentro del contenedor.
3. Evalúa mover el comando a `postCreateCommand` si no es crítico en `Dockerfile`.

---

¿Quieres que revise tu Dockerfile o tu `.devcontainer/devcontainer.json`? Me lo puedes compartir y te digo exactamente qué cambiar.

---
*Generado desde conversación con 2 mensajes.*
*DevOps*
