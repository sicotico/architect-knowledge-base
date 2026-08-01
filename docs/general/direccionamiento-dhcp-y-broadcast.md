---
title: Direccionamiento DHCP y Broadcast
date: 2025-04-14
category: General
slug: direccionamiento-dhcp-y-broadcast
tags: ['General']
---

# Direccionamiento DHCP y Broadcast


> **Pregunta original:**
> 
Observe la ilustración. Una computadora portátil recién comprada se acaba de conectar a la red de área local. La red de área local utiliza un enrutador inalámbrico que proporciona direccionamiento dinámico como se muestra. ¿Qué dirección IP utiliza la computadora portátil como dirección de destino al solicitar una dirección asignada dinámicamente?

---


## Respuesta


La computadora portátil, al conectarse por primera vez a una red que utiliza direccionamiento dinámico (DHCP), enviará una solicitud para obtener una dirección IP. Esta solicitud es un **mensaje DHCP Discover**, que se envía como un **broadcast** en la red.

### Dirección de destino utilizada:
La dirección IP de destino utilizada en este proceso es:

> **255.255.255.255**

### Explicación:
- La computadora portátil aún no tiene una dirección IP asignada.
- No sabe la dirección del servidor DHCP.
- Por eso, utiliza la dirección de broadcast (**255.255.255.255**) para enviar la solicitud y asegurarse de que todos los dispositivos en la red la reciban, especialmente el servidor DHCP configurado (en este caso, el router con IP **192.168.0.1**).

¿Quieres que te explique también cómo sigue el proceso DHCP?

---
*Generado desde conversación con 2 mensajes.*
*General*
