---
title: Encontrar equipos por nombre
date: 2025-01-26
category: General
slug: encontrar-equipos-por-nombre
tags: ['General']
---

# Encontrar equipos por nombre


> **Pregunta original:**
> 
Tengo varios equipos en casa pero no quiero instalar un DNS , hay alguna forma de encontrarlos por nombre ?
> Tengo un MacOS y linux , como descubro los dispositivos mediante avahi

---


## Respuesta


Sí, puedes encontrar y comunicarte con los equipos en tu red local por nombre sin necesidad de instalar un servidor DNS dedicado. Aquí hay algunas opciones:

### 1. **Usar el servicio de mDNS (Multicast DNS)**
   - **Descripción**: Muchos sistemas operativos modernos tienen soporte para mDNS, que permite la resolución de nombres en redes locales sin un servidor DNS. 
   - **Cómo funciona**: Cada dispositivo anuncia su nombre y dirección IP en la red local mediante multicast.
   - **Requisitos**:
     - En sistemas **Windows**, habilita la función "Descubrimiento de red".
     - En **macOS** y **Linux**, esto suele estar habilitado de forma predeterminada gracias a `avahi` (Linux) o `Bonjour` (macOS).
   - **Ejemplo**:
     Si tienes un equipo llamado `equipo1.local`, puedes acceder a él usando su nombre seguido de `.local`, como `ping equipo1.local`.

---

### 2. **Editar el archivo `hosts`**
   - **Descripción**: Puedes asignar manualmente nombres a direcciones IP en el archivo `hosts` de cada dispositivo.
   - **Ubicación del archivo**:
     - **Windows**: `C:\Windows\System32\drivers\etc\hosts`
     - **Linux/macOS**: `/etc/hosts`
   - **Ejemplo de entrada**:
     ```
     192.168.1.10 equipo1
     192.168.1.11 equipo2
     ```
   - Esto te permitirá acceder a los equipos como `equipo1` o `equipo2` sin necesidad de un servidor DNS.

---

### 3. **UPnP o DHCP con asignación de nombres**
   - **Descripción**: Algunos routers modernos permiten asociar un nombre a cada dispositivo conectado mediante DHCP.
   - **Cómo configurarlo**:
     1. Accede a la interfaz de administración del router.
     2. Busca la configuración DHCP.
     3. Asigna nombres a las direcciones IP (en muchos routers se llama "Reserva DHCP" o "DHCP Static Lease").
   - Una vez configurado, deberías poder acceder a los dispositivos por su nombre.

---

### 4. **Usar herramientas de descubrimiento en red**
   - Puedes usar herramientas que escanean tu red y muestran los nombres de los dispositivos:
     - **Para Windows**: `arp -a` o herramientas gráficas como Fing.
     - **Para Linux/macOS**: `nmap -sn 192.168.1.0/24` o `arp-scan`.

Con estas opciones, no necesitas instalar un DNS completo, pero tendrás un sistema funcional para encontrar y comunicarte con los dispositivos de tu red local por nombre.
---


En sistemas **macOS** y **Linux**, puedes usar herramientas como **Avahi** (para Linux) y **Bonjour** (incorporado en macOS) para descubrir dispositivos en la red local mediante mDNS. A continuación, te explico cómo puedes hacerlo:

---

### **En macOS:**
macOS tiene soporte integrado para Bonjour, por lo que no necesitas instalar nada adicional.

1. **Descubrir dispositivos disponibles en la red**:
   - Abre la aplicación **Terminal**.
   - Usa el comando:
     ```bash
     dns-sd -B _services._dns-sd._udp
     ```
     Esto mostrará una lista de los servicios disponibles en la red.

2. **Explorar servicios específicos**:
   - Para listar dispositivos que proporcionan un servicio específico (por ejemplo, impresoras, servidores web):
     ```bash
     dns-sd -B _http._tcp
     ```
   - Esto mostrará todos los dispositivos en la red que tienen un servidor HTTP.

3. **Conectar a un dispositivo por su nombre**:
   - Puedes usar el nombre del dispositivo seguido de `.local`. Por ejemplo:
     ```bash
     ping nombre-del-dispositivo.local
     ssh usuario@nombre-del-dispositivo.local
     ```

---

### **En Linux:**
En Linux, necesitarás **Avahi**, que es una implementación de mDNS similar a Bonjour. En la mayoría de las distribuciones modernas ya está instalado, pero si no, puedes instalarlo fácilmente.

1. **Instalar Avahi**:
   - En distribuciones basadas en Debian/Ubuntu:
     ```bash
     sudo apt update
     sudo apt install avahi-daemon avahi-utils
     ```
   - En distribuciones basadas en Red Hat/Fedora:
     ```bash
     sudo dnf install avahi avahi-tools
     ```

2. **Iniciar y habilitar Avahi**:
   - Asegúrate de que el servicio Avahi esté en ejecución:
     ```bash
     sudo systemctl start avahi-daemon
     sudo systemctl enable avahi-daemon
     ```

3. **Descubrir dispositivos en la red**:
   - Usa el comando `avahi-browse` para explorar los servicios:
     ```bash
     avahi-browse -a
     ```
     Esto mostrará una lista de todos los servicios disponibles en la red.

4. **Conectar a un dispositivo por su nombre**:
   - Al igual que en macOS, puedes usar el nombre seguido de `.local`. Por ejemplo:
     ```bash
     ping nombre-del-dispositivo.local
     ssh usuario@nombre-del-dispositivo.local
     ```

---

### **Ejemplo práctico de uso:**

Supongamos que tienes un dispositivo con el nombre `raspberrypi` en la red:
1. Descúbrelo:
   ```bash
   avahi-browse -a
   ```
   O en macOS:
   ```bash
   dns-sd -B _ssh._tcp
   ```
2. Conéctate:
   ```bash
   ssh pi@raspberrypi.local
   ```

---

Estas herramientas hacen que sea muy sencillo descubrir y conectar dispositivos en tu red local mediante mDNS. ¡Pruébalo y avísame si necesitas más ayuda!

---
*Generado desde conversación con 4 mensajes.*
*General*
