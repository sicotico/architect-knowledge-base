---
title: Administrar particiones macOS
date: 2025-01-29
category: General
slug: administrar-particiones-macos
tags: ['General']
---

# Administrar particiones macOS


> **Pregunta original:**
> 
Como hacer en MacOS para montar ext4
> administrar particiones en MacOS

---


## Respuesta


En macOS, la administración de particiones se realiza principalmente mediante la aplicación **Utilidad de Discos** y la línea de comandos con **diskutil**. Aquí te explico cómo administrar particiones en macOS usando ambas herramientas.

---

## 📌 **Usando Utilidad de Discos (Interfaz Gráfica)**
1. **Abrir la Utilidad de Discos**  
   - Ve a **Aplicaciones** > **Utilidades** > **Utilidad de Discos**, o usa Spotlight (**Cmd + Espacio**) y escribe *Utilidad de Discos*.

2. **Seleccionar el disco o volumen**  
   - En la barra lateral, selecciona el disco que deseas administrar.
   - Haz clic en **Vista > Mostrar todos los dispositivos** para ver todos los discos físicos.

3. **Administrar particiones**  
   - **Crear una nueva partición**:  
     - Selecciona el disco.
     - Pulsa **Partición** en la barra superior.
     - Haz clic en el botón "+" para agregar una nueva partición.
     - Define el nombre, formato (APFS, Mac OS Extended, exFAT, etc.) y tamaño.
     - Pulsa **Aplicar**.

   - **Eliminar una partición**:  
     - Selecciona la partición no deseada.
     - Pulsa el botón "-" y confirma la eliminación.

   - **Redimensionar una partición**:  
     - Arrastra el borde del gráfico de particiones o introduce un tamaño manualmente.

4. **Aplicar los cambios**  
   - Una vez realizados los ajustes, confirma y deja que macOS ejecute las operaciones.

---

## 🖥 **Usando la Terminal (diskutil)**
Si prefieres usar la línea de comandos, puedes utilizar `diskutil`.

### **Ver los discos y particiones**
```sh
diskutil list
```
Esto mostrará todos los discos conectados y sus particiones.

### **Crear una nueva partición**
Ejemplo para crear una partición de 50GB en un disco específico (`/dev/disk2`):
```sh
diskutil partitionDisk /dev/disk2 1 GPT APFS "NuevaParticion" 50G
```
- `1 GPT` → Una sola partición con formato GPT.
- `APFS` → Tipo de sistema de archivos (puedes cambiarlo a `ExFAT`, `HFS+`, etc.).
- `"NuevaParticion"` → Nombre de la partición.
- `50G` → Tamaño de la partición en GB.

### **Eliminar una partición**
Para eliminar una partición específica:
```sh
diskutil eraseVolume APFS "NombreDeLaParticion" /dev/disk2s3
```

### **Redimensionar una partición**
Si deseas cambiar el tamaño de una partición APFS:
```sh
diskutil apfs resizeContainer /dev/disk2 200G
```
Esto cambia la partición a 200GB.

### **Formatear un disco**
```sh
diskutil eraseDisk APFS "NuevoDisco" /dev/disk2
```
Esto borra completamente el disco y lo formatea en APFS.

---

## 🔥 **Consejos Importantes**
- **Haz una copia de seguridad antes de modificar particiones.**  
- Si tienes problemas, puedes iniciar en **Modo de Recuperación** (`Cmd + R` al arrancar) y usar **Utilidad de Discos**.  
- APFS es ideal para discos SSD y HFS+ para discos HDD.  
- Para compatibilidad con Windows, usa **exFAT** (pero no NTFS, que es solo lectura en macOS sin software adicional).  

Si necesitas ayuda con una operación específica, dime qué deseas hacer. 🚀
---


### **Cómo montar sistemas de archivos EXT4 en macOS**
macOS no admite de forma nativa el sistema de archivos **EXT4** (usado en Linux), por lo que necesitas herramientas de terceros para leer y escribir en particiones EXT4. Aquí te explico varias opciones:

---

## 🛠 **Opciones para montar EXT4 en macOS**
### **1️⃣ Opción 1: Usar FUSE y ext4fuse (Gratis, solo lectura)**
Si solo necesitas acceder a los archivos en una partición **EXT4**, puedes usar **macFUSE** junto con **ext4fuse**.

#### **Pasos:**
1. **Instalar macFUSE**  
   - Descarga e instala **macFUSE** desde aquí:  
     [https://osxfuse.github.io/](https://osxfuse.github.io/)

2. **Instalar Homebrew** (si no lo tienes)  
   Abre la Terminal y ejecuta:
   ```sh
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

3. **Instalar ext4fuse**
   ```sh
   brew install ext4fuse
   ```

4. **Montar la partición EXT4 manualmente**  
   Primero, encuentra la unidad:
   ```sh
   diskutil list
   ```
   Luego, monta la partición en modo solo lectura:
   ```sh
   sudo ext4fuse /dev/disk2s1 /mnt/ext4 -o allow_other
   ```
   *(Reemplaza `/dev/disk2s1` con la partición correcta.)*

5. **Acceder a los archivos**  
   Ahora puedes acceder a los archivos en **/mnt/ext4**.

✅ **Ventajas:**  
- Gratis.  
- Fácil instalación.  
❌ **Desventajas:**  
- **Solo lectura** (no permite escribir).  

---

### **2️⃣ Opción 2: Usar Paragon ExtFS (Pago, lectura/escritura)**
Si necesitas acceso completo de lectura y escritura, **Paragon ExtFS** es una opción comercial que funciona bien.

#### **Pasos:**
1. Descarga e instala **Paragon ExtFS** desde su página oficial:  
   [https://www.paragon-software.com/home/linuxfs-mac/](https://www.paragon-software.com/home/linuxfs-mac/)

2. Una vez instalado, abrir la aplicación y montar automáticamente la partición EXT4.

✅ **Ventajas:**  
- Soporte completo **lectura/escritura**.  
- Interfaz gráfica fácil de usar.  
❌ **Desventajas:**  
- Es **de pago** (aunque tiene una prueba gratuita).  

---

### **3️⃣ Opción 3: Usar Mounty + Virtual Machine (Alternativa con Linux)**
Si quieres acceso total sin pagar, puedes crear una máquina virtual con Linux y compartir la carpeta.

#### **Pasos:**
1. **Instala VirtualBox o UTM** en macOS.
2. **Crea una máquina virtual Linux** (como Ubuntu).
3. **Monta la partición EXT4** en la máquina virtual.
4. **Comparte los archivos con macOS** mediante una carpeta compartida.

✅ **Ventajas:**  
- Gratis.  
- Acceso total lectura/escritura.  
❌ **Desventajas:**  
- Requiere más recursos y configuración.

---

## **¿Cuál opción elegir?**
🔹 **Si solo necesitas leer archivos** → Usa **ext4fuse** (Opción 1, Gratis).  
🔹 **Si necesitas escribir archivos** → Usa **Paragon ExtFS** (Opción 2, Pago).  
🔹 **Si trabajas con EXT4 frecuentemente** → Usa **una máquina virtual Linux** (Opción 3).  

Si necesitas más ayuda, dime qué opción prefieres y te guío paso a paso. 🚀

---
*Generado desde conversación con 4 mensajes.*
*General*
