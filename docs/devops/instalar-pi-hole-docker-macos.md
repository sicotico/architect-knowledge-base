---
title: Instalar Pi-hole Docker MacOS
date: 2025-05-24
category: DevOps
slug: instalar-pi-hole-docker-macos
tags: ['DevOps']
---

# Instalar Pi-hole Docker MacOS


> **Pregunta original:**
> 
Es la configuración gráfica de la imagen de pihole. 
Esta es la configuración de la imagen:
# More info at https://github.com/pi-hole/docker-pi-hole/ and https://docs.pi-hole.net/
services:
  pihole:
    container_name: pihole
    image: pihole/pihole:latest
    ports:
      # DNS Ports
      - "53:53/tcp"
      - "53:53/udp"
      # Default HTTP Port
      - "80:80/tcp"
      # Default HTTPs Port. FTL will generate a self-signed certificate
      - "443:443/tcp"
      # Uncomment the below if using Pi-hole as your DHCP Server
      #- "67:67/udp"
    environment:
      # Set the appropriate timezone for your location (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones), e.g:
      TZ: 'Europe/London'
      # Set a password to access the web interface. Not setting one will result in a random password being assigned
      FTLCONF_webserver_api_password: 'correct horse battery staple'
    # Volumes store your data between container upgrades
    volumes:
      # For persisting Pi-hole's databases and common configuration file
      - './etc-pihole:/etc/pihole'
      # Uncomment the below if you have custom dnsmasq config files that you want to persist. Not needed for most starting fresh with Pi-hole v6. If you're upgrading from v5 you and have used this directory before, you should keep it enabled for the first v6 container start to allow for a complete migration. It can be removed afterwards
      #- './etc-dnsmasq.d:/etc/dnsmasq.d'
    cap_add:
      # See https://github.com/pi-hole/docker-pi-hole#note-on-capabilities
      # Required if you are using Pi-hole as your DHCP server, else not needed
      - NET_ADMIN
    restart: unless-stopped 

Lo quiero tener instalado en un docker desktop en MAcOS 15.5

---


## Respuesta


Perfecto, estás configurando la imagen de Pi-hole (`pihole/pihole:latest`) en Docker Desktop en macOS 15.5, y ya tienes la configuración de puertos, volúmenes y variables de entorno. Te ayudo a trasladar esa configuración del archivo `docker-compose.yml` al entorno gráfico que estás usando en Docker Desktop.

Aquí tienes una guía paso a paso para replicar exactamente esa configuración:

---

### 🔌 **Puertos**
En la ventana que tienes abierta en la imagen, introduce los siguientes puertos:

| Host Port | Container Port |
|-----------|----------------|
| `53`      | `53/tcp`       |
| `53`      | `53/udp`       |
| `80`      | `80/tcp`       |
| `443`     | `443/tcp`      |
| *(opcional)* `67` | `67/udp` *(solo si vas a usar DHCP con Pi-hole)*

> ⚠️ Ojo: Asegúrate de que estos puertos no estén en uso por otros servicios en tu sistema, especialmente el 53 (DNS) y 80 (HTTP).

---

### 📁 **Volúmenes**
En la sección "Volumes", pon:

| Host Path                                | Container Path   |
|------------------------------------------|------------------|
| `/Users/luis/Documents/Data` *(o donde quieras)* | `/etc/pihole`     |

> Puedes añadir más volúmenes si planeas usar configuraciones personalizadas de `dnsmasq`, por ejemplo:
> - Host: `/Users/luis/Documents/dnsmasq.d` → Container: `/etc/dnsmasq.d`

---

### 🌐 **Variables de entorno**
Añade las siguientes variables (usa el botón “+” para añadir más):

| Variable                         | Value                           |
|----------------------------------|---------------------------------|
| `TZ`                             | `Europe/London` *(o tu zona)*   |
| `FTLCONF_webserver_api_password` | `correct horse battery staple`  |

---

### 🛡️ **Capacidades adicionales**
La opción `cap_add: NET_ADMIN` no se puede configurar directamente desde la GUI de Docker Desktop. Para eso, **tendrías que usar la línea de comandos** o un archivo `docker-compose.yml`.

Si no necesitas DHCP, puedes ignorar esto.

---

### ▶️ **Listo para correr**
Una vez ingresados todos los puertos, volúmenes y variables, haz clic en **Run**.

---

### ✅ Alternativa recomendada (para más control)
Si en algún momento quieres más control (como `NET_ADMIN`), te recomiendo usar `docker-compose` en terminal con el archivo YAML que ya tienes. Para ejecutarlo:

```bash
cd /ruta/del/archivo
docker-compose up -d
```

---

¿Quieres que te ayude a convertir esta configuración en un comando `docker run` equivalente por si prefieres terminal?

---
*Generado desde conversación con 2 mensajes.*
*DevOps*
