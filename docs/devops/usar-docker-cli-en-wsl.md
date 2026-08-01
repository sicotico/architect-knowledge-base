---
title: Usar Docker CLI en WSL
date: 2025-01-23
category: DevOps
slug: usar-docker-cli-en-wsl
tags: ['DevOps']
---

# Usar Docker CLI en WSL


> **Pregunta original:**
> 
usar docker CLi en WSL
> Que es el paquete docker.io

---


## Respuesta


Para utilizar la CLI de Docker en WSL (Windows Subsystem for Linux), tienes dos opciones principales:

1. **Usar Docker Desktop con integración en WSL 2**:

   - **Instalación de Docker Desktop**: Descarga e instala la versión más reciente de Docker Desktop para Windows. Durante la instalación, asegúrate de habilitar la integración con WSL 2. citeturn0search2

   - **Configuración de WSL 2**:
     - Verifica que WSL esté instalado y actualizado a la versión 2. Puedes comprobar la versión con:
       ```powershell
       wsl --list --verbose
       ```
       Si es necesario, establece la versión 2 por defecto:
       ```powershell
       wsl --set-default-version 2
       ```

   - **Integración de Docker con WSL 2**:
     - Abre Docker Desktop y ve a "Settings" > "Resources" > "WSL Integration".
     - Activa la opción "Enable integration with my default WSL distro" y selecciona las distribuciones de WSL donde deseas habilitar Docker.

   - **Verificación**:
     - Abre una terminal en tu distribución de WSL y ejecuta:
       ```bash
       docker --version
       docker run hello-world
       ```
       Si todo está correctamente configurado, deberías ver un mensaje de bienvenida de Docker.

2. **Instalar Docker directamente en WSL 2 sin Docker Desktop**:

   Esta opción es útil si prefieres una solución más ligera o deseas evitar el uso de Docker Desktop. citeturn0search1

   - **Actualizar la distribución de Linux**:
     ```bash
     sudo apt update && sudo apt upgrade
     ```

   - **Instalar Docker**:
     ```bash
     # Instalar paquetes necesarios
     sudo apt install apt-transport-https ca-certificates curl software-properties-common

     # Añadir la clave GPG de Docker
     curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

     # Añadir el repositorio de Docker
     sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

     # Actualizar e instalar Docker
     sudo apt update
     sudo apt install docker-ce
     ```

   - **Configurar permisos**:
     Para evitar usar `sudo` con cada comando de Docker, añade tu usuario al grupo `docker`:
     ```bash
     sudo usermod -aG docker $USER
     ```
     Luego, cierra y vuelve a abrir la terminal o ejecuta `newgrp docker` para aplicar los cambios.

   - **Iniciar el demonio de Docker**:
     ```bash
     sudo service docker start
     ```

   - **Verificación**:
     Ejecuta:
     ```bash
     docker --version
     docker run hello-world
     ```
     Deberías ver el mensaje de bienvenida de Docker si todo está configurado correctamente.

**Nota**: Al instalar Docker directamente en WSL 2, es recomendable asegurarse de que no haya conflictos con instalaciones previas de Docker en Windows. Además, ten en cuenta que algunas características avanzadas pueden no estar disponibles sin Docker Desktop. citeturn0search2

Elige la opción que mejor se adapte a tus necesidades y preferencias.
---


El paquete `docker.io` es la versión de Docker disponible en los repositorios oficiales de distribuciones como Ubuntu y Debian. Este paquete es mantenido por la comunidad de dichas distribuciones y suele estar ligeramente desactualizado en comparación con la versión oficial proporcionada por Docker Inc. citeturn0search7

Para instalar `docker.io` en Ubuntu, puedes utilizar el siguiente comando:

```bash
sudo apt update
sudo apt install docker.io
```

Sin embargo, si prefieres obtener la versión más reciente de Docker directamente desde sus repositorios oficiales, es recomendable instalar `docker-ce` (Docker Community Edition). Este paquete es mantenido por Docker Inc. y suele estar más actualizado. citeturn0search2

En resumen, `docker.io` es el paquete de Docker proporcionado por los repositorios de Ubuntu y Debian, mientras que `docker-ce` es la versión oficial mantenida por Docker Inc. La elección entre uno u otro dependerá de tus necesidades específicas y de si prefieres estabilidad con versiones ligeramente más antiguas (`docker.io`) o las características más recientes con actualizaciones más frecuentes (`docker-ce`).

---
*Generado desde conversación con 4 mensajes.*
*DevOps*
