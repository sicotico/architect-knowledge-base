---
title: Opciones para DNS local
date: 2024-11-04
category: Networking
slug: opciones-para-dns-local
tags: ['Networking']
---

# Opciones para DNS local


> **Pregunta original:**
> 
Quiero tener resolucion de nombres en casa pero no quiero montar un DNS

---


## Respuesta


Si no quieres montar un servidor DNS completo en casa, tienes otras opciones para gestionar la resolución de nombres de forma sencilla:

1. **Archivo `hosts` local**:
   - Puedes editar el archivo `hosts` en tu computadora para asociar nombres de dominio con direcciones IP específicas.
   - En sistemas Windows, el archivo se encuentra en `C:\Windows\System32\drivers\etc\hosts`.
   - En sistemas basados en Unix (Linux, macOS), el archivo está en `/etc/hosts`.
   - Simplemente añade una línea por cada entrada, como:
     ```
     192.168.1.10    servidor-casa
     192.168.1.20    nas-local
     ```

2. **Usar un router con soporte DNS básico**:
   - Algunos routers tienen funciones de DNS integradas, que permiten asignar nombres a las direcciones IP dentro de la red local.
   - Puedes entrar a la configuración de tu router y buscar si tiene una sección de "Hostnames" o "DHCP con DNS".
   - Esto permite que el router actúe como un servidor DNS ligero para tu red interna.

3. **Servidor DNS mas liviano (dnsmasq)**:
   - Si estás dispuesto a usar una herramienta más liviana pero sin la complejidad de un DNS completo, `dnsmasq` es una buena opción.
   - Es fácil de configurar y puede actuar tanto como servidor DNS cache como servidor DHCP.
   - Puedes instalarlo en un dispositivo ligero como una Raspberry Pi o incluso en tu router si tiene soporte para firmware como OpenWRT o DD-WRT.

4. **Usar servicios de DNS internos de NAS o dispositivos de red**:
   - Algunos NAS o dispositivos de almacenamiento en red tienen opciones integradas para proporcionar resolución de nombres dentro de la red local sin requerir la configuración de un servidor DNS completo.

5. **Servicios de DNS de dispositivos IoT o software tipo Pi-hole**:
   - Si tienes o planeas usar un Pi-hole para filtrar publicidad en tu red, también puedes usarlo para manejar la resolución de nombres de forma interna. Aunque Pi-hole es conocido por su función de bloqueo de anuncios, también actúa como un servidor DNS que puede gestionar resoluciones internas.

Estas opciones te permitirán manejar la resolución de nombres de manera sencilla sin necesidad de montar un servidor DNS completo en tu casa.

---
*Generado desde conversación con 2 mensajes.*
*Networking*
