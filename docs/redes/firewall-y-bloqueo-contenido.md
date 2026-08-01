---
title: Firewall y bloqueo contenido
date: 2025-03-11
category: Networking
slug: firewall-y-bloqueo-contenido
tags: ['Networking']
---

# Firewall y bloqueo contenido


> **Pregunta original:**
> 
Hola, quiero poner una raspberry pi o contratar un servicio de firwall y bloqueo de contenido de internet. Tengo un conexion de fibra casera normal. ¿Que opciones tengo?
> como se ven los dns en el terminal de linux
> Como le indico al router que todo el tráfico debe de pasar por el firewall de la raspberry 

---


## Respuesta


En Linux, puedes ver los **DNS configurados** de varias maneras. Aquí te dejo algunos comandos para consultar los servidores DNS actuales:

---

## 🔍 **1. Ver los DNS en uso (Método moderno - systemd-resolved)**
Si tu distribución usa **systemd-resolved**, puedes ver los DNS con:

```bash
resolvectl status
```
O más específico para una interfaz de red:

```bash
resolvectl dns
```

---

## 🔍 **2. Ver los DNS desde el archivo `resolv.conf`**
```bash
cat /etc/resolv.conf
```
Esto mostrará algo como:

```
nameserver 8.8.8.8
nameserver 1.1.1.1
```
> 📌 **Nota:** En sistemas modernos, `resolv.conf` puede estar administrado por `systemd-resolved`, por lo que los cambios pueden no persistir.

---

## 🔍 **3. Usar el comando `nmcli` (NetworkManager)**
Si usas **NetworkManager**, puedes ver los DNS con:

```bash
nmcli dev show | grep DNS
```

Ejemplo de salida:
```
IP4.DNS[1]:  8.8.8.8
IP4.DNS[2]:  1.1.1.1
```

---

## 🔍 **4. Ver la configuración de red con `ip` o `ifconfig`**
Puedes ver la configuración general de la interfaz de red con:

```bash
ip a
```
O con `ifconfig` (si está instalado):

```bash
ifconfig
```
> No muestra los DNS directamente, pero es útil para verificar la interfaz de red.

---

### 🛠 **¿Cómo cambiar los DNS en Linux?**
Si quieres cambiar los DNS manualmente, edita el archivo `/etc/resolv.conf`:

```bash
sudo nano /etc/resolv.conf
```
Y agrega:
```
nameserver 8.8.8.8
nameserver 1.1.1.1
```
> 📌 **Si usas `systemd-resolved`, debes cambiar los DNS en `/etc/systemd/resolved.conf` o usar `resolvectl`**.

---

¿Necesitas ayuda para configurar los DNS en tu sistema? 😊
---


Para forzar que todo el tráfico de tu red pase a través del firewall de la **Raspberry Pi**, necesitas configurar tu red de la siguiente manera:

---

## 🔥 **Método 1: Configurar la Raspberry Pi como un Gateway (Requiere Desactivar DHCP en el Router)**
Este método convierte la Raspberry Pi en el principal punto de acceso a internet para todos los dispositivos.

### **Pasos a seguir:**
1️⃣ **Configurar una IP Estática en la Raspberry Pi**  
   - Edita el archivo de configuración de red con:  
     ```bash
     sudo nano /etc/dhcpcd.conf
     ```
   - Agrega algo como:
     ```
     interface eth0
     static ip_address=192.168.1.2/24
     static routers=192.168.1.1
     static domain_name_servers=8.8.8.8 1.1.1.1
     ```
   - Guarda con `CTRL + X`, `Y` y `Enter`.

2️⃣ **Instalar y Configurar un Firewall en la Raspberry Pi (iptables o UFW)**
   - Instala `iptables`:
     ```bash
     sudo apt update && sudo apt install iptables-persistent
     ```
   - Configura las reglas del firewall para redirigir tráfico:
     ```bash
     sudo iptables -A FORWARD -i eth0 -o eth0 -j ACCEPT
     sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
     sudo netfilter-persistent save
     ```

3️⃣ **Activar el Forwarding de Tráfico en Linux**
   - Edita el archivo:
     ```bash
     sudo nano /etc/sysctl.conf
     ```
   - Busca la línea:
     ```
     #net.ipv4.ip_forward=1
     ```
   - Elimina el `#` y guarda los cambios.
   - Aplica los cambios:
     ```bash
     sudo sysctl -p
     ```

4️⃣ **Desactivar el DHCP en el Router y Activarlo en la Raspberry Pi**
   - Entra en la configuración del router (**192.168.1.1** o similar).
   - Desactiva el servidor **DHCP** del router.
   - Instala y configura un servidor DHCP en la Raspberry Pi:
     ```bash
     sudo apt install isc-dhcp-server
     ```
   - Edita su configuración en `/etc/dhcp/dhcpd.conf` y define el rango de IPs que entregará.

✅ **Resultado:** La Raspberry Pi actuará como firewall y punto de acceso a internet.

---

## 🔥 **Método 2: Redirigir Tráfico Desde el Router (Más Fácil)**
Si tu router permite configurar una **gateway personalizada** o **enrutamiento estático**, puedes hacer que todo el tráfico pase por la Raspberry sin desactivar el DHCP.

### **Pasos a seguir:**
1️⃣ **Configurar una IP estática en la Raspberry Pi (igual que el Paso 1 del Método 1).**

2️⃣ **En el Router, Configurar la Puerta de Enlace (Gateway)**
   - Entra en la configuración del router.
   - Busca la opción de **"Rutas Estáticas" o "Gateway"**.
   - Define una regla para que todo el tráfico use la Raspberry Pi como puerta de enlace:
     ```
     Destino: 0.0.0.0
     Máscara: 0.0.0.0
     Gateway: 192.168.1.2 (IP de la Raspberry Pi)
     ```

✅ **Resultado:** El router enviará el tráfico a la Raspberry Pi sin desactivar el DHCP.

---

## 🔥 **Método 3: Redirigir Todo el Tráfico Usando Reglas de Firewall en el Router**
Si tu router tiene la opción de **IPTables, OpenWRT o Firewall avanzado**, puedes configurar una regla para que todo el tráfico pase por la Raspberry.

1️⃣ **Entra al router y busca la opción de firewall.**
2️⃣ **Añade una regla para que todo el tráfico pase por la Raspberry Pi:**
   ```
   iptables -t nat -A PREROUTING -i eth0 -s 192.168.1.0/24 -j DNAT --to 192.168.1.2
   ```
3️⃣ **Guarda los cambios y reinicia el router.**

✅ **Resultado:** Todo el tráfico se filtrará por la Raspberry.

---

### 📌 **¿Qué Método Elegir?**
✔ **Método 1 (Gateway + DHCP en Raspberry Pi)** → Si quieres control total del tráfico (Firewall avanzado).  
✔ **Método 2 (Gateway en el router)** → Más fácil y suficiente para la mayoría de casos.  
✔ **Método 3 (Reglas de Firewall en el router)** → Si tu router lo permite y quieres control intermedio.  

🚀 **Si solo quieres bloquear contenido web**, una alternativa más sencilla es **configurar Pi-hole o NextDNS sin redirigir todo el tráfico**.

¿Te gustaría ayuda para configurar algo específico? 😊
---


Si quieres implementar un firewall y bloqueo de contenido en tu red doméstica, tienes varias opciones dependiendo del nivel de control y dificultad que estés dispuesto a manejar. Te resumo las opciones principales:

### 1️⃣ **Usar una Raspberry Pi como Firewall y Filtro de Contenido**
Si tienes una Raspberry Pi, puedes configurarla para que actúe como un firewall y bloqueador de contenido. Aquí hay algunas opciones:

✅ **Pi-hole** (Fácil)  
   - Funciona como un bloqueador de anuncios y rastreadores a nivel de red.  
   - Bloquea publicidad y sitios maliciosos en todos los dispositivos conectados a tu red.  
   - No es un firewall, pero combinado con Unbound o WireGuard, puedes mejorar la seguridad.  

✅ **OPNsense o pfSense en Raspberry Pi (Avanzado)**  
   - Puedes instalar OPNSense o pfSense en una Raspberry Pi (mejor en una mini PC x86).  
   - Te permite filtrar contenido, crear reglas de firewall avanzadas y monitorear el tráfico.  
   - Se necesita más configuración y algo de conocimientos de redes.  

✅ **Tinyproxy o Squid Proxy** (Intermedio)  
   - Puedes configurar la Raspberry como un proxy con Squid para filtrar tráfico HTTP/HTTPS.  
   - Permite bloquear sitios web y contenido específico.  

---

### 2️⃣ **Firewalls Comerciales o Servicios en la Nube**
Si prefieres una solución más sencilla sin configurar hardware, hay opciones comerciales:

✅ **OpenDNS (Cisco Umbrella) - Gratuito y de Pago**  
   - Fácil de configurar en tu router.  
   - Filtra sitios de malware, phishing y contenido adulto.  
   - Requiere solo cambiar los DNS en el router.  

✅ **NextDNS (Gratuito hasta 300,000 consultas/mes)**  
   - Como Pi-hole pero en la nube.  
   - Bloquea anuncios, rastreadores y sitios peligrosos.  
   - Se configura en el router o en dispositivos individuales.  

✅ **Firewalls Comerciales (FortiGate, Ubiquiti, Sophos, etc.)**  
   - Equipos físicos con protección avanzada.  
   - Recomendados para entornos más profesionales o pequeñas empresas.  
   - Costosos pero eficaces.  

---

### 3️⃣ **Configurar el Firewall en tu Router**
Si tu router lo permite, puedes usar su firewall integrado para bloquear contenido. Algunas opciones son:

- **Filtrado de DNS**: Configura OpenDNS o NextDNS en la configuración de red.  
- **Reglas de firewall**: Si el router lo permite, puedes bloquear rangos de IP o categorías de contenido.  
- **Control parental**: Algunos routers tienen esta función para limitar acceso a ciertos sitios.  

---

### 📌 **¿Cuál Opción Elegir?**
- **Si buscas algo fácil y gratuito** 👉 OpenDNS o NextDNS.  
- **Si quieres controlar todo con una Raspberry Pi** 👉 Pi-hole + Unbound o Tinyproxy.  
- **Si quieres un firewall completo y avanzado** 👉 pfSense en una mini PC.  
- **Si prefieres una solución lista para usar** 👉 Un firewall comercial (Ubiquiti, Fortinet, Sophos).  

🔹 **Mi recomendación**: Para una red doméstica estándar, empezar con **Pi-hole + OpenDNS/NextDNS** es una buena opción. Si después quieres más control, puedes considerar pfSense o un firewall dedicado.  

¿Necesitas ayuda para instalar o configurar alguna de estas opciones? 😊

---
*Generado desde conversación con 6 mensajes.*
*Networking*
