---
title: Instalar Pi-Hole Docker
date: 2025-05-24
category: DevOps
slug: instalar-pi-hole-docker
tags: ['DevOps']
---

# Instalar Pi-Hole Docker


> **Pregunta original:**
> 
Quiero instalar Pi-Hole en un Docker Desktop en mi MacOS 15.5. La documentacion oficial https://github.com/pi-hole/docker-pi-hole me proporciona un docker-compose. ¿Como puedo hacerlo con Docker Desktop?

---


## Respuesta


Para instalar **Pi-hole en Docker Desktop en macOS 15.5** usando el `docker-compose` que se proporciona en la [documentación oficial](https://github.com/pi-hole/docker-pi-hole), sigue estos pasos:

---

### ✅ **Requisitos previos**

- Tener **Docker Desktop** instalado en tu Mac y funcionando.
- Tener acceso a **Terminal** y saber usar comandos básicos.
- Tener instalado **Docker Compose** (Docker Desktop ya lo incluye).

---

### 🛠️ **Pasos para instalar Pi-hole**

#### 1. **Crea una carpeta para tu configuración**

Abre Terminal y escribe:

```bash
mkdir ~/pi-hole
cd ~/pi-hole
```

#### 2. **Crea el archivo `docker-compose.yml`**

Copia el siguiente contenido en un nuevo archivo llamado `docker-compose.yml`:

```yaml
version: "3"

services:
  pihole:
    container_name: pihole
    image: pihole/pihole:latest
    ports:
      - "53:53/tcp"
      - "53:53/udp"
      - "80:80"
    environment:
      TZ: 'America/Argentina/Buenos_Aires'  # Ajusta según tu zona horaria
      WEBPASSWORD: 'tu-contraseña-aqui'
    volumes:
      - './etc-pihole/:/etc/pihole/'
      - './etc-dnsmasq.d/:/etc/dnsmasq.d/'
    restart: unless-stopped
```

#### 3. **Inicializa los volúmenes**

Crea los directorios para que Docker los monte correctamente:

```bash
mkdir etc-pihole
mkdir etc-dnsmasq.d
```

#### 4. **Inicia Pi-hole con Docker Compose**

Ejecuta:

```bash
docker-compose up -d
```

Esto descargará la imagen, creará el contenedor y lo ejecutará en segundo plano.

---

### 🔍 **Acceder a la interfaz web**

Abre tu navegador y ve a:

```
http://localhost/admin
```

Inicia sesión con la contraseña que definiste en `WEBPASSWORD`.

---

### ⚠️ Notas importantes

- **Limitación en macOS**: Pi-hole necesita escuchar en el puerto 53, pero **macOS y Docker Desktop no permiten hacer redirección de DNS como en Linux**. No puedes usar Pi-hole como DNS para toda tu red directamente desde Docker en macOS (excepto en dispositivos que manualmente lo apunten a `localhost` como DNS, y aun así puede haber conflictos).
  
- Para un uso completo como DNS a nivel de red, **lo ideal es correr Pi-hole en una Raspberry Pi o en un contenedor en una máquina Linux**.

---

¿Quieres que lo configuremos para que lo puedas usar localmente como DNS solo en tu Mac?

---
*Generado desde conversación con 2 mensajes.*
*DevOps*
