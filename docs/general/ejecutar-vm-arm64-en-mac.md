---
title: Ejecutar VM ARM64 en Mac
date: 2025-11-11
category: General
slug: ejecutar-vm-arm64-en-mac
tags: ['General']
---

# Ejecutar VM ARM64 en Mac


> **Pregunta original:**
> 
Tengo un aVM para ARM64 con dos ficheros gns3vm-disk1.qcow2. y gns3vm-disk2.qcow2. Como la ejecuto en MacOS 26 con Apple Silicion
> como creo una MV en qemu con los ficheros qcow2
> como puedo abrir los qcow2 con VMware fusion

---


## Respuesta


Buena pregunta 👏 — te explico esto con claridad porque **VMware Fusion (incluso la versión para Apple Silicon)** **no puede abrir directamente archivos `.qcow2`**.  

Sin embargo, hay **formas indirectas** de usarlos.  
Vamos paso a paso 👇

---

## ⚠️ 1️⃣ Entiende el problema

- Los archivos `.qcow2` son discos de **QEMU**, no de VMware.  
- VMware usa **.vmdk** (Virtual Machine Disk).  
- Por tanto, **Fusion no reconoce ni abre `.qcow2` directamente**.

👉 Solución: **convertir `.qcow2` → `.vmdk`**, y luego crear una VM en VMware Fusion que use ese disco convertido.

---

## ✅ 2️⃣ Verifica tu entorno

### Si tu Mac tiene **Apple Silicon (M1/M2/M3)**:
- Solo puedes ejecutar **VMware Fusion 13+ (Tech Preview o versión oficial)**.
- Solo puedes usar **VMs ARM64 (no x86_64)**.
  - Esto significa que si tu `.qcow2` es de una VM **x86_64**, **no funcionará**, aunque la conviertas.

Para verificar la arquitectura del disco:
```bash
qemu-img info gns3vm-disk1.qcow2
```

Si ves algo como:
```
format: qcow2
virtual size: 8G
disk size: ...
cluster_size: ...
```
y **no dice “architecture”**, revisa la fuente del archivo:
- Si es una “GNS3 VM” oficial → casi seguro **x86_64** → ❌ no funcionará en Apple Silicon.
- Si viene de una imagen ARM (por ejemplo Ubuntu ARM64) → ✅ sí puedes convertirla.

---

## 🔄 3️⃣ Convierte el `.qcow2` a `.vmdk`

Instala `qemu-img` si no lo tienes:
```bash
brew install qemu
```

Luego convierte cada archivo:

```bash
qemu-img convert -O vmdk gns3vm-disk1.qcow2 gns3vm-disk1.vmdk
qemu-img convert -O vmdk gns3vm-disk2.qcow2 gns3vm-disk2.vmdk
```

Esto puede tardar unos minutos según el tamaño.

---

## 🧩 4️⃣ Crea la VM en VMware Fusion

1. Abre **VMware Fusion**.  
2. Haz clic en **Create a Custom Virtual Machine**.  
3. Selecciona el sistema operativo que corresponda (por ejemplo **Linux → Ubuntu 64-bit ARM**).  
4. En el paso de discos:
   - Elimina el disco que crea por defecto.
   - Elige **Add Existing Disk**.
   - Selecciona el `.vmdk` que convertiste.  
5. Guarda y arranca la VM.

Si te pide convertir el disco a formato VMware más nuevo, acepta.

---

## 🧠 5️⃣ Consideraciones importantes

| Situación | ¿Funciona en Apple Silicon? | Comentario |
|------------|-----------------------------|-------------|
| `.qcow2` con SO ARM64 (ej: Ubuntu ARM) | ✅ Sí | Convertir a `.vmdk` y usar “Linux ARM” en Fusion |
| `.qcow2` con SO x86_64 (ej: GNS3 VM oficial) | ❌ No | Apple Silicon **no puede ejecutar** x86 VM en Fusion |
| Quieres emular x86 igualmente | ⚠️ Sí, pero muy lento | Usa **UTM / QEMU**, no Fusion |

---

## 🚀 Alternativa: Usar UTM directamente

Si los `.qcow2` son ARM, puedes cargarlos directamente sin convertir nada:
- Instala [UTM](https://mac.getutm.app)
- “Create New VM” → Virtualize → Linux → Añadir disco `.qcow2`
- Inicia

UTM usa QEMU nativo y soporta `.qcow2` directamente.

---

¿Podrías decirme qué arquitectura tiene tu VM (ARM64 o x86_64)?  
Con eso te puedo dar el comando exacto y confirmarte si vale la pena intentar en VMware Fusion o si solo funcionará en UTM/QEMU.
---


Perfecto ✅ — vamos a hacerlo paso a paso.  
Te explico **cómo crear y arrancar una máquina virtual en QEMU usando tus ficheros `.qcow2`** en **macOS con Apple Silicon (ARM64)**.

---

## 🧩 Paso 1: Instalar QEMU
En tu Mac, abre **Terminal** y ejecuta:

```bash
brew install qemu
```

Comprueba que se instaló correctamente:

```bash
qemu-system-aarch64 --version
```

Si ves una versión, por ejemplo `QEMU emulator version 9.x`, estás listo.

---

## 🗂️ Paso 2: Verifica tus discos
Asegúrate de que tus archivos están en una ruta accesible, por ejemplo:

```
~/VMs/gns3vm-disk1.qcow2
~/VMs/gns3vm-disk2.qcow2
```

---

## 🧠 Paso 3: Saber qué arquitectura usa la VM
Antes de lanzarla, revisa si la VM es **ARM64** o **x86_64**:

```bash
qemu-img info ~/VMs/gns3vm-disk1.qcow2 | grep 'virtual size'
```

Si puedes, también abre el archivo `gns3vm-disk1.qcow2` en un editor hex o busca el archivo `.vmx` o `.ova` original, ya que normalmente las **GNS3 VMs oficiales son x86_64** (no ARM).  
Si es **x86_64**, tendrás que emular (lento pero posible).  
Si es **ARM64**, puedes virtualizar directamente (rápido).

---

## 🚀 Paso 4: Crear y arrancar la VM en QEMU

### 🔹 Caso A: Si es **ARM64 (Apple Silicon nativo)**
Ejecuta este comando:

```bash
qemu-system-aarch64 \
  -machine virt,accel=hvf \
  -cpu host \
  -m 4096 \
  -smp 4 \
  -drive file=~/VMs/gns3vm-disk1.qcow2,if=virtio \
  -drive file=~/VMs/gns3vm-disk2.qcow2,if=virtio \
  -device virtio-net-pci,netdev=net0 \
  -netdev user,id=net0,hostfwd=tcp::2222-:22 \
  -nographic
```

Esto:
- Usa aceleración por hardware (`hvf`).
- Asigna 4 GB de RAM y 4 CPUs.
- Conecta los dos discos QCOW2.
- Redirige el puerto SSH (puedes conectar luego con `ssh -p 2222 user@localhost`).
- No abre ventana gráfica (`-nographic`); puedes quitarlo si quieres GUI.

Si prefieres ver la pantalla:
```bash
... -display default,show-cursor=on
```

---

### 🔹 Caso B: Si es **x86_64 (emulación completa)**
Ejecuta este comando (más lento):

```bash
qemu-system-x86_64 \
  -accel tcg \
  -m 4096 \
  -smp 4 \
  -drive file=~/VMs/gns3vm-disk1.qcow2,if=virtio \
  -drive file=~/VMs/gns3vm-disk2.qcow2,if=virtio \
  -device e1000,netdev=net0 \
  -netdev user,id=net0,hostfwd=tcp::2222-:22 \
  -display default,show-cursor=on
```

---

## 🧱 Paso 5: Crear una “máquina” persistente (opcional)
Puedes guardar esta configuración en un archivo de texto `gns3vm.sh`:

```bash
#!/bin/bash
qemu-system-aarch64 \
  -machine virt,accel=hvf \
  -cpu host \
  -m 4096 \
  -smp 4 \
  -drive file=gns3vm-disk1.qcow2,if=virtio \
  -drive file=gns3vm-disk2.qcow2,if=virtio \
  -device virtio-net-pci,netdev=net0 \
  -netdev user,id=net0,hostfwd=tcp::2222-:22 \
  -display default,show-cursor=on
```

Luego dale permisos y ejecútalo:

```bash
chmod +x gns3vm.sh
./gns3vm.sh
```

---

## 🧩 Consejo extra
Si quieres algo más visual y fácil, **UTM** usa QEMU por debajo, pero te permite:
- Añadir tus `.qcow2` con clics.
- Configurar RAM, CPU y red gráficamente.
- Guardar el estado.

Solo tienes que:
1. Instalar [UTM](https://mac.getutm.app).  
2. Crear VM nueva → Virtualize → Linux → Añadir tus `.qcow2` como discos → Iniciar.

---

¿Quieres que te diga exactamente qué comando usar según la arquitectura **(x86_64 o ARM64)** de tus `.qcow2`?  
Puedo ayudarte a verificar eso si me copias la salida de este comando:

```bash
qemu-img info ~/VMs/gns3vm-disk1.qcow2
```
---


Perfecto 👍  
Tienes una **VM para ARM64** con dos discos (`gns3vm-disk1.qcow2` y `gns3vm-disk2.qcow2`), y quieres ejecutarla en **macOS 12+ (macOS 26 no existe aún, supongo que te refieres a macOS 15 o 14)** sobre **Apple Silicon (M1/M2/M3)**.  
Vamos paso a paso para ejecutarla correctamente.  

---

## 🧠 Qué tienes
- Dos discos en formato **QCOW2**, usados por **QEMU / GNS3 VM**.  
- Una arquitectura **ARM64**, así que no puedes usar VMware Fusion o VirtualBox tradicionales (que son x86).  
- En Apple Silicon, las opciones compatibles son:
  - **UTM (recomendado)** → interfaz gráfica sobre QEMU nativo ARM.  
  - **QEMU CLI** directamente.

---

## ✅ Opción 1: Usar **UTM** (fácil y visual)
UTM es básicamente QEMU con una interfaz Mac-friendly y soporte nativo para Apple Silicon.

### 1. Instala UTM
Descárgalo desde [https://mac.getutm.app](https://mac.getutm.app) o vía Homebrew:
```bash
brew install --cask utm
```

### 2. Crea una nueva VM
1. Abre UTM.  
2. Haz clic en **Create a New Virtual Machine**.  
3. Elige **Virtualize → Linux** (porque es ARM64, no Emulate).  
4. En “Boot ISO Image” puedes dejarlo vacío si ya tienes el sistema instalado en los `.qcow2`.  
5. En “Storage”, elimina el disco por defecto y **añade tus discos:**
   - `gns3vm-disk1.qcow2` como **Primary Disk**.  
   - `gns3vm-disk2.qcow2` como **Secondary Disk** (añadir otro disco con “+ Add Drive”).  
6. Ajusta CPU/RAM (por ejemplo, 4 cores, 4–8 GB RAM).  
7. Guarda la configuración.

### 3. Arranca la VM
Haz clic en **Play**.  
Si el disco tiene un sistema Linux o la GNS3 VM ya preinstalada, arrancará normalmente.  
Si no, necesitarás una ISO ARM64 de Ubuntu o Debian para reparar o reinstalar.

---

## ⚙️ Opción 2: Usar **QEMU por terminal** (avanzado)
Instálalo con Homebrew:
```bash
brew install qemu
```

Luego ejecuta algo como:
```bash
qemu-system-aarch64 \
  -machine virt,accel=hvf \
  -cpu host \
  -m 4096 \
  -smp 4 \
  -drive file=gns3vm-disk1.qcow2,if=virtio \
  -drive file=gns3vm-disk2.qcow2,if=virtio \
  -nographic
```

👉 Si tienes una ISO ARM64 (por ejemplo `ubuntu-22.04-server-arm64.iso`), puedes agregarla con:
```bash
-cdrom ubuntu-22.04-server-arm64.iso -boot d
```

---

## 🧩 Nota sobre GNS3 en Apple Silicon
GNS3 usa una “GNS3 VM” (normalmente en formato OVA x86).  
👉 Si tu `.qcow2` es de la versión x86 (no ARM64), **no funcionará en Apple Silicon**, salvo que uses **emulación completa**, lo cual es **muy lenta**.  
Verifica la arquitectura:
```bash
qemu-img info gns3vm-disk1.qcow2 | grep 'arch'
```
Si te dice `x86_64`, no es útil directamente en Apple Silicon — deberías usar la **GNS3 VM para ARM64** (disponible en GNS3 GitHub o puedes instalar GNS3 directamente sobre macOS con Homebrew + Docker).

---

¿Podrías confirmarme **la arquitectura real** de tu VM (ARM64 o x86_64)?  
Así te indico el comando exacto o cómo convertirla para Apple Silicon.

---
*Generado desde conversación con 6 mensajes.*
*General*
