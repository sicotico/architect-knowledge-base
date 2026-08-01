---
title: Instalar FFmpeg en MacOS
date: 2025-02-16
category: General
slug: instalar-ffmpeg-en-macos
tags: ['General']
---

# Instalar FFmpeg en MacOS


> **Pregunta original:**
> 
ffmpeg en MacOS Sillicon 

---


## Respuesta


Para instalar FFmpeg en una Mac con Apple Silicon, puedes utilizar el gestor de paquetes Homebrew, que facilita la instalación y gestión de software en macOS. A continuación, se detallan los pasos para llevar a cabo la instalación:

1. **Instalar Homebrew**: Si aún no tienes Homebrew instalado, abre la aplicación Terminal y ejecuta el siguiente comando:

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

   Este script instalará Homebrew en tu sistema.

2. **Instalar FFmpeg**: Una vez que Homebrew esté instalado, puedes instalar FFmpeg ejecutando:

   ```bash
   brew install ffmpeg
   ```

   Este comando descargará e instalará la versión más reciente de FFmpeg compatible con Apple Silicon.

Además, FFmpeg ha mejorado su rendimiento en dispositivos con Apple Silicon al incorporar soporte para aceleración de hardware. Esto permite una codificación de video más rápida utilizando las capacidades del chip M1 o M2. Para aprovechar esta funcionalidad, puedes utilizar el codificador `h264_videotoolbox` al ejecutar comandos de FFmpeg. Por ejemplo:

```bash
ffmpeg -i input.mp4 -c:v h264_videotoolbox -q:v 50 output.mp4
```

Este comando transcodificará `input.mp4` a `output.mp4` utilizando la aceleración de hardware disponible en los chips de Apple. citeturn0search4

Para una guía visual sobre la instalación de FFmpeg en Mac con Apple Silicon, puedes consultar el siguiente video:

videoCómo instalar FFmpeg en MacBook (M1, M2, M3)turn0search2

Este video proporciona instrucciones paso a paso para completar la instalación y asegurarte de que FFmpeg funcione correctamente en tu dispositivo.

---
*Generado desde conversación con 2 mensajes.*
*General*
