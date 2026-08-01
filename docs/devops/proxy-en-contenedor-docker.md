---
title: Proxy en contenedor Docker
date: 2025-01-24
category: DevOps
slug: proxy-en-contenedor-docker
tags: ['DevOps']
---

# Proxy en contenedor Docker


> **Pregunta original:**
> 
Quiero montar un proxy en contenedor y configurarlo en otro PC para usarlo

---


## Respuesta


Montar un proxy en un contenedor Docker y configurarlo para que otro PC pueda usarlo como proxy requiere varios pasos. Aquí tienes una guía general para hacerlo:

---

### 1. **Elegir el software de proxy**
Hay muchas opciones de software para proxy. Algunas opciones populares son:
- **Squid**: Un proxy HTTP/HTTPS/FTP flexible y ampliamente utilizado.
- **TinyProxy**: Un proxy ligero para HTTP/HTTPS.
- **Shadowsocks**: Orientado a privacidad y seguridad.

En este ejemplo, usaremos **Squid**.

---

### 2. **Crear un contenedor con Squid**
#### a. Crear un archivo `Dockerfile`
Crea un archivo llamado `Dockerfile` con el siguiente contenido:

```dockerfile
FROM ubuntu:20.04

RUN apt-get update && apt-get install -y squid && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY squid.conf /etc/squid/squid.conf

EXPOSE 3128

CMD ["squid", "-N", "-f", "/etc/squid/squid.conf"]
```

#### b. Crear un archivo de configuración de Squid (`squid.conf`)
Crea un archivo `squid.conf` con una configuración básica. Por ejemplo:

```plaintext
http_port 3128

# Permitir todas las conexiones (ajusta según tus necesidades)
acl localnet src 0.0.0.0/0
http_access allow localnet

# Permitir solo ciertos tipos de tráfico (opcional)
http_access deny all
```

> **Nota**: La configuración permite acceso a todas las IPs, lo que no es seguro para entornos de producción. Ajusta esto según tus necesidades.

#### c. Construir la imagen Docker
En el directorio donde están el `Dockerfile` y el `squid.conf`, ejecuta:

```bash
docker build -t my-squid-proxy .
```

#### d. Ejecutar el contenedor
Inicia el contenedor y mapea el puerto 3128:

```bash
docker run -d --name squid-proxy -p 3128:3128 my-squid-proxy
```

---

### 3. **Configurar el proxy en el PC cliente**
#### a. Obtener la IP del host donde corre Docker
Si estás en la misma red, usa la IP del host. Por ejemplo:

```bash
hostname -I
```

Toma nota de la IP, como `192.168.1.100`.

#### b. Configurar el proxy en el cliente
En el PC cliente, configura el proxy utilizando la dirección IP del host y el puerto 3128:

- **Windows**:
  1. Ve a **Configuración** > **Red e Internet** > **Proxy**.
  2. Activa "Configuración manual del proxy".
  3. Introduce la IP (`192.168.1.100`) y el puerto (`3128`).

- **Linux**:
  Edita el archivo `/etc/environment`:

  ```bash
  http_proxy="http://192.168.1.100:3128"
  https_proxy="http://192.168.1.100:3128"
  ```

  O usa herramientas específicas del escritorio, como GNOME o KDE.

- **Navegador**:
  Configura el proxy directamente en la configuración de red del navegador.

---

### 4. **Probar el proxy**
Verifica que el tráfico pase a través del proxy:
1. Abre un navegador o terminal.
2. Accede a un sitio web, como `http://whatismyipaddress.com`, para verificar que la IP del proxy es visible.

---

### 5. **Consideraciones adicionales**
- **Seguridad**: Restringe el acceso al proxy solo a las IPs confiables.
- **Autenticación** (opcional): Puedes configurar Squid para requerir usuario y contraseña.
- **Logs**: Revisa los logs del proxy en `/var/log/squid/access.log` para monitorear el tráfico.

¿Te interesa añadir autenticación o realizar alguna configuración avanzada?

---
*Generado desde conversación con 2 mensajes.*
*DevOps*
