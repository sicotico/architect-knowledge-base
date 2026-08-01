---
title: Descubrir dominios .local
date: 2025-06-01
category: General
slug: descubrir-dominios-local
tags: ['General']
---

# Descubrir dominios .local


> **Pregunta original:**
> 
Estoy en MAcOS15.4 y quiero descbir que dominios .local tengo en mi red domestica
> hay algún comando para descubrír los dominios .local de la red domestica 

---


## Respuesta


Sí, en macOS puedes utilizar el comando `dns-sd` para descubrir los servicios y dominios `.local` disponibles en tu red doméstica. Este comando interactúa con el servicio Bonjour (también conocido como mDNS o DNS-SD), que permite la detección automática de dispositivos y servicios en redes locales.

### 🔍 Descubrir dominios `.local` con `dns-sd`

Para listar los servicios disponibles en tu red local, abre la Terminal y ejecuta:

```bash
dns-sd -B _services._dns-sd._udp.
```


Este comando mostrará los tipos de servicios anunciados en la red. Para explorar servicios específicos, como servidores HTTP, puedes usar:

```bash
dns-sd -B _http._tcp.
```


Una vez identificado un servicio, puedes obtener más detalles con:

```bash
dns-sd -L "NombreDelServicio" _http._tcp local.
```


Reemplaza `"NombreDelServicio"` con el nombre exacto del servicio que deseas investigar.

### 🧰 Utilidades gráficas para exploración de servicios

Si prefieres una interfaz gráfica, puedes utilizar aplicaciones como **Bonjour Browser** o **iStumbler**. Estas herramientas muestran todos los servicios Bonjour activos en tu red local, permitiéndote explorar dispositivos y servicios sin necesidad de utilizar la Terminal.

### 🛠️ Consideraciones adicionales

- **Resolución de nombres `.local`**: macOS utiliza el protocolo mDNS para resolver nombres con el sufijo `.local`. Si tienes problemas para acceder a dispositivos mediante nombres `.local`, asegúrate de que el servicio Bonjour esté activo y que no existan conflictos con dominios `.local` configurados en servidores DNS internos.

- **Evitar conflictos con dominios `.local`**: Apple recomienda evitar el uso de `.local` como sufijo para dominios DNS unicast internos, ya que puede interferir con la resolución de nombres mediante Bonjour.

Si necesitas asistencia adicional para configurar o solucionar problemas relacionados con dominios `.local` en tu red doméstica, no dudes en preguntar.
---


Para descubrir los dominios `.local` disponibles en tu red doméstica desde macOS 15.4, puedes utilizar herramientas integradas como `dns-sd`, así como utilidades de terceros para facilitar la exploración.

### 🔍 Descubrir dominios `.local` con `dns-sd`

El comando `dns-sd` permite explorar servicios Bonjour (mDNS) en tu red local. Para listar todos los servicios disponibles, abre la Terminal y ejecuta:

```bash
dns-sd -B _services._dns-sd._udp.local.
```


Este comando mostrará los tipos de servicios anunciados en la red. Para explorar servicios específicos, como servidores HTTP, puedes usar:

```bash
dns-sd -B _http._tcp.local.
```


Una vez identificado un servicio, puedes obtener más detalles con:

```bash
dns-sd -L "NombreDelServicio" _http._tcp local.
```


Reemplaza `"NombreDelServicio"` con el nombre exacto del servicio que deseas investigar.

### 🧰 Utilidades gráficas para exploración de servicios

Si prefieres una interfaz gráfica, la aplicación gratuita [Discovery - DNS-SD Browser](https://apps.apple.com/us/app/discovery-dns-sd-browser/id1381004916?mt=12) está disponible en la Mac App Store. Esta herramienta muestra todos los servicios Bonjour activos en tu red local, permitiéndote explorar dispositivos y servicios sin necesidad de utilizar la Terminal.

### 🛠️ Consideraciones adicionales

- **Resolución de nombres `.local`**: macOS utiliza el protocolo mDNS para resolver nombres con el sufijo `.local`. Si tienes problemas para acceder a dispositivos mediante nombres `.local`, asegúrate de que el servicio Bonjour esté activo y que no existan conflictos con dominios `.local` configurados en servidores DNS internos. citeturn0search3

- **Evitar conflictos con dominios `.local`**: Apple recomienda evitar el uso de `.local` como sufijo para dominios DNS unicast internos, ya que puede interferir con la resolución de nombres mediante Bonjour. citeturn0search3

Si necesitas asistencia adicional para configurar o solucionar problemas relacionados con dominios `.local` en tu red doméstica, no dudes en preguntar.

---
*Generado desde conversación con 4 mensajes.*
*General*
