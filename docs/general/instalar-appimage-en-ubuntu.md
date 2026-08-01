---
title: Instalar AppImage en Ubuntu
date: 2026-05-26
category: General
slug: instalar-appimage-en-ubuntu
tags: ['General']
---

# Instalar AppImage en Ubuntu


> **Pregunta original:**
> 
quiero instal LM Studio 
> como s enstal un appimage en ubuntu 

---


## Respuesta


Para instalar **entity["software","LM Studio","Local LLM desktop application"]** en Ubuntu usando AppImage:

1. Entra en la web oficial:  
   urlLM Studiohttps://lmstudio.ai/

2. Descarga la versión para **Linux (.AppImage)**.

3. Abre una terminal y ve a Descargas:

```bash
cd ~/Descargas
```

4. Dale permisos de ejecución (cambia el nombre si el archivo descargado es distinto):

```bash
chmod +x LM-Studio-*.AppImage
```

5. Ejecuta el archivo:

```bash
./LM-Studio-*.AppImage
```

---

### Si aparece “Permission denied”
Ejecuta:

```bash
chmod +x ~/Descargas/LM-Studio-*.AppImage
```

y vuelve a abrirlo.

### Si no abre o sale un error relacionado con FUSE
Instala compatibilidad:

```bash
sudo apt update
sudo apt install libfuse2
```

(En Ubuntu más nuevos puede ser `libfuse2t64` si `libfuse2` no existe).

---

### Para dejarlo “instalado” y que salga en el menú

```bash
mkdir -p ~/Aplicaciones
mv ~/Descargas/LM-Studio-*.AppImage ~/Aplicaciones/
```

Después ejecútalo desde ahí una vez:

```bash
~/Aplicaciones/LM-Studio-*.AppImage
```

LM Studio suele crear integración con el escritorio.

Si te aparece algún error al ejecutar, pega aquí el texto exacto de la terminal.
---


En Ubuntu, un **AppImage** normalmente no se “instala” como un `.deb`. Es un archivo ejecutable que contiene la aplicación.

### Método rápido

1. **Descarga el archivo `.AppImage`**
   - Suele quedar en `Descargas`.

2. **Dale permisos de ejecución**
   - Desde el explorador:
     - Clic derecho → **Propiedades** → **Permisos**
     - Activa **Permitir ejecutar el archivo como programa**

   O desde terminal:

```bash
chmod +x nombre-del-archivo.AppImage
```

Ejemplo:

```bash
chmod +x Obsidian-1.9.3.AppImage
```

3. **Ejecútalo**

Desde terminal:

```bash
./nombre-del-archivo.AppImage
```

Ejemplo:

```bash
./Obsidian-1.9.3.AppImage
```

Si estás en otra carpeta:

```bash
~/Descargas/Obsidian-1.9.3.AppImage
```

---

### Para que aparezca en el menú de aplicaciones (opcional)

Muchos AppImage preguntan al abrir si quieres **integrarlo en el sistema** (crear acceso directo).

Si no aparece esa opción:

- Mueve el archivo a una carpeta fija, por ejemplo:

```bash
mkdir -p ~/Aplicaciones
mv *.AppImage ~/Aplicaciones/
```

- Luego crea un acceso manual o usa una herramienta como:

urlAppImageLauncherhttps://appimagelauncher.com/

AppImageLauncher detecta AppImages y los integra automáticamente en el menú.

---

### Si al abrir da error

Instala FUSE (algunas AppImage antiguas lo necesitan):

```bash
sudo apt update
sudo apt install libfuse2
```

En Ubuntu recientes puede ser necesario:

```bash
sudo apt install libfuse2t64
```

Si me dices **qué AppImage concreto estás intentando abrir** y **qué versión de Ubuntu tienes**, te doy los pasos exactos.

---
*Generado desde conversación con 4 mensajes.*
*General*
