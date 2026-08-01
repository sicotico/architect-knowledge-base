---
title: Problemas con binarios Brew
date: 2025-02-08
category: General
slug: problemas-con-binarios-brew
tags: ['General']
---

# Problemas con binarios Brew


> **Pregunta original:**
> 
en MacOS , tras instalar software con brew no puedo ejecutar los binarios desde terminal

---


## Respuesta


Si después de instalar software con Homebrew en macOS no puedes ejecutar los binarios desde la Terminal, es probable que el sistema no esté reconociendo la ruta donde Homebrew instala estos ejecutables. Para resolver este problema, sigue estos pasos:

1. **Verificar la instalación de Homebrew**:
   Asegúrate de que Homebrew esté correctamente instalado ejecutando:
   ```bash
   brew --version
   ```
   Si el comando devuelve la versión de Homebrew, significa que está instalado correctamente.

2. **Añadir Homebrew al PATH**:
   Es posible que la ruta de los binarios de Homebrew no esté incluida en la variable de entorno `PATH`, lo que impide que el sistema encuentre los ejecutables. Para solucionarlo:

   - **Para usuarios con procesadores Intel**:
     Ejecuta en la Terminal:
     ```bash
     echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc
     source ~/.zshrc
     ```
     Esto añadirá la ruta `/usr/local/bin` al inicio de tu `PATH` y recargará la configuración de la Terminal.

   - **Para usuarios con procesadores Apple Silicon (M1, M2, etc.)**:
     Homebrew se instala por defecto en `/opt/homebrew/bin`. Ejecuta:
     ```bash
     echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
     eval "$(/opt/homebrew/bin/brew shellenv)"
     ```
     Esto configurará el entorno para que reconozca la ruta de Homebrew.

3. **Recargar la configuración de la Terminal**:
   Después de realizar los pasos anteriores, cierra y vuelve a abrir la Terminal o ejecuta `source ~/.zshrc` (o `source ~/.zprofile` si modificaste ese archivo) para aplicar los cambios.

4. **Verificar la instalación del software**:
   Asegúrate de que el software que instalaste con Homebrew se haya instalado correctamente y que el binario esté presente en el directorio correspondiente. Por ejemplo, para verificar la instalación de `wget`:
   ```bash
   brew list wget
   ```
   Esto mostrará los archivos instalados para `wget`.

5. **Ejecutar `brew doctor`**:
   Homebrew ofrece una herramienta de diagnóstico que puede identificar problemas comunes:
   ```bash
   brew doctor
   ```
   Sigue las recomendaciones que aparezcan para resolver posibles conflictos o configuraciones incorrectas.

Si después de seguir estos pasos aún no puedes ejecutar los binarios desde la Terminal, podría haber un problema más específico con la instalación o configuración de tu sistema. En ese caso, proporcionar detalles adicionales o mensajes de error específicos ayudaría a diagnosticar y resolver el problema de manera más efectiva.

---
*Generado desde conversación con 2 mensajes.*
*General*
