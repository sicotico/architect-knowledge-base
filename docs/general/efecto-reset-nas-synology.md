---
title: Efecto reset NAS Synology
date: 2024-12-10
category: General
slug: efecto-reset-nas-synology
tags: ['General']
---

# Efecto reset NAS Synology


> **Pregunta original:**
> 
Hola, tengo un NAS de synology y no sé que efecto tiene restablecer el sistema presionado 4 segundos el botón de reset


---


## Respuesta


En un NAS de Synology, presionar el botón de **reset** durante **4 segundos** tiene un efecto específico y controlado. Este procedimiento se utiliza para restablecer la configuración de red y la cuenta de administrador, pero **no borra los datos almacenados en los volúmenes del NAS**.

### Lo que ocurre al mantener presionado el botón de reset durante 4 segundos:
1. **Configuración de red restablecida**:
   - Se restablece la configuración de red a los valores predeterminados.
   - Esto incluye:
     - La dirección IP del NAS (se cambiará a DHCP).
     - Otras configuraciones de red, como puentes de red y configuraciones avanzadas, volverán a la configuración inicial.

2. **Contraseña del administrador eliminada**:
   - La cuenta de administrador tendrá la contraseña en blanco, lo que permite acceder sin una contraseña.
   - Necesitarás establecer una nueva contraseña al iniciar sesión.

### Cómo acceder después del reset:
1. Utiliza **Synology Assistant** o busca la dirección IP del NAS en tu red local (será asignada automáticamente por el router si tienes DHCP habilitado).
2. Ingresa al DSM (DiskStation Manager) usando el nombre de usuario **admin** sin contraseña.
3. Sigue los pasos para reconfigurar la red o establecer una nueva contraseña.

### Advertencia:
- **No presiones el botón por más de 4 segundos (como 10 segundos o más)** si no estás seguro de lo que haces. Esto puede activar un **restablecimiento completo del sistema**, que podría eliminar la configuración del sistema y afectar más aspectos del NAS.
- Siempre asegúrate de tener un respaldo de datos importantes antes de realizar cualquier acción en tu NAS.

Si necesitas más ayuda con el proceso o tienes dudas adicionales, házmelo saber. 😊

---
*Generado desde conversación con 2 mensajes.*
*General*
