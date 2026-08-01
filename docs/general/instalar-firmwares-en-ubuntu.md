---
title: Instalar firmwares en Ubuntu
date: 2025-03-17
category: General
slug: instalar-firmwares-en-ubuntu
tags: ['General']
---

# Instalar firmwares en Ubuntu


> **Pregunta original:**
> 
Porque no se actualizan los 5 paquetes
> Que tengo que hacer para instalr los firmwares
> Cuando abro una ventana nueva del termina me cambia el tema

---


## Respuesta


Si al abrir una nueva ventana del terminal en macOS te cambia el tema, hay varias razones por las que podría estar ocurriendo. Aquí te dejo algunas soluciones para corregirlo:

### 🔹 **1. Configurar el tema predeterminado en Terminal**
1. Abre la aplicación **Terminal**.
2. Ve a **Preferencias** (`Cmd + ,` o `⌘ + ,`).
3. En la pestaña **Perfiles**, selecciona el tema que quieres usar de manera predeterminada.
4. Haz clic en **"Usar como predeterminado"**.
5. Cierra y abre una nueva ventana para comprobar si se mantiene el tema.

### 🔹 **2. Revisar el archivo de configuración del shell (`.zshrc` o `.bashrc`)**
Si usas **zsh** (que es el shell por defecto en macOS desde Catalina), revisa el archivo `.zshrc` en tu carpeta de usuario:

```bash
nano ~/.zshrc
```

Busca líneas que modifiquen el tema o carguen un framework como **Oh My Zsh**. Si ves algo como esto:

```bash
ZSH_THEME="random"
```

Cámbialo por un tema fijo, por ejemplo:

```bash
ZSH_THEME="agnoster"
```

Guarda los cambios (`Ctrl + X`, luego `Y` y `Enter`).

Si usas **bash**, revisa `.bashrc` o `.bash_profile`:

```bash
nano ~/.bashrc
```

o

```bash
nano ~/.bash_profile
```

### 🔹 **3. Verificar Oh My Zsh (si lo usas)**
Si tienes **Oh My Zsh** instalado, verifica si el archivo `~/.zshrc` está configurando un tema aleatorio:

```bash
ZSH_THEME="random"
```

Si está configurado así, cámbialo por un tema específico, por ejemplo:

```bash
ZSH_THEME="powerlevel10k/powerlevel10k"
```

Luego, recarga la configuración con:

```bash
source ~/.zshrc
```

### 🔹 **4. Revisar configuraciones de iTerm2 (si lo usas)**
Si en lugar del Terminal nativo usas **iTerm2**, revisa:
1. **Preferencias > Perfiles > Colores** y asegúrate de que el tema deseado esté seleccionado.
2. En **Preferencias > General > Configuración de sesión**, desactiva **"Auto ajuste de perfil basado en la conexión"** si está activado.

---

Prueba estos pasos y dime si el problema persiste. 🚀
---


Para instalar las actualizaciones de firmware disponibles en tu sistema Ubuntu, sigue estos pasos:

### 1️⃣ **Actualizar la base de datos de `fwupd`**
Ejecuta el siguiente comando para asegurarte de que `fwupd` tiene la última información sobre actualizaciones:

```bash
sudo fwupdmgr refresh
```

### 2️⃣ **Ver las actualizaciones disponibles**
Ya ejecutaste este comando, pero por si necesitas hacerlo nuevamente:

```bash
fwupdmgr get-upgrades
```

### 3️⃣ **Instalar las actualizaciones**
Para instalar todas las actualizaciones disponibles, usa:

```bash
sudo fwupdmgr update
```

Esto descargará e instalará los firmwares necesarios.

### 4️⃣ **Reiniciar el sistema**
Algunas actualizaciones requieren un reinicio para aplicarse correctamente. Si es el caso, reinicia tu computadora con:

```bash
sudo reboot
```

### 5️⃣ **Verificar que la actualización se instaló correctamente**
Después del reinicio, puedes ejecutar nuevamente:

```bash
fwupdmgr get-devices
```

Este comando te mostrará los dispositivos y sus versiones de firmware actualizadas.

---

⚠️ **Nota:** Si la actualización no se instala correctamente o hay errores, revisa los logs con:

```bash
journalctl -xe -u fwupd
```

Si tienes algún problema, dime qué error te aparece y te ayudo a solucionarlo. 🚀
---


Los 5 paquetes que no se están actualizando en tu Ubuntu 24.10 (`libplymouth5`, `plymouth`, `plymouth-label`, `plymouth-theme-spinner` y `plymouth-theme-ubuntu-text`) están siendo retenidos debido a **phasing** (implementación escalonada de actualizaciones).

### 🔹 ¿Qué es **phasing**?
Ubuntu usa un sistema llamado **phased updates** para desplegar actualizaciones de paquetes de manera progresiva en diferentes usuarios. Esto permite detectar posibles problemas antes de que una actualización llegue a todos los usuarios.

En tu caso, estos paquetes aún no han sido habilitados para el 100% de los usuarios, por eso `apt upgrade` no los instala.

---

### 🔹 🔧 **Cómo forzar la actualización**
Si estás seguro de que quieres actualizar los paquetes sin esperar la implementación escalonada, puedes forzar la instalación con:

```bash
sudo apt update
sudo apt -o APT::Get::Always-Include-Phased-Updates=true upgrade
```

Este comando **forzará la instalación de los paquetes en fase de actualización**.

Si quieres actualizar un solo paquete en específico, usa:

```bash
sudo apt -o APT::Get::Always-Include-Phased-Updates=true install <nombre-del-paquete>
```

Ejemplo:

```bash
sudo apt -o APT::Get::Always-Include-Phased-Updates=true install plymouth
```

---

### 🔹 Alternativa: Desactivar **phased updates** permanentemente
Si quieres desactivar esta restricción de manera permanente, edita el archivo de configuración de `apt`:

```bash
sudo nano /etc/apt/apt.conf.d/99phased-updates
```

Añade esta línea:

```
APT::Get::Always-Include-Phased-Updates "true";
```

Guarda con `Ctrl + X`, luego `Y` y `Enter`. A partir de ahora, todas las actualizaciones disponibles se instalarán sin esperar la implementación escalonada.

---

🔹 **Conclusión**: No es un error, sino una medida de seguridad de Ubuntu. Puedes esperar a que los paquetes sean liberados completamente o forzar la actualización con los comandos anteriores. 🚀

---
*Generado desde conversación con 6 mensajes.*
*General*
