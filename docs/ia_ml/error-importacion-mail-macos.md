---
title: Error importación Mail macOS
date: 2025-04-06
category: IA/ML
slug: error-importacion-mail-macos
tags: ['IA/ML']
---

# Error importación Mail macOS


> **Pregunta original:**
> 
Acabo de actualizar a MacOS 15.4 y al arrancar Mail me pide importar correos. Al final  aparece el error adjunto en la imagen 

---


## Respuesta


Gracias por compartir la captura. El mensaje indica:

> **"Error en la importación.**  
> Se ha producido un error durante la importación. Asegúrate de que dispones de espacio suficiente en tu carpeta de inicio e inténtalo de nuevo."

Esto suele ocurrir en la app **Mail** de macOS tras una actualización importante del sistema operativo, como la que mencionas (macOS 15.4). Aquí te dejo algunos pasos para solucionar este problema:

---

### ✅ Pasos para resolverlo:

1. **Verifica el espacio en disco:**
   - Abre el **Finder** > menú **Apple**  > **Acerca de este Mac** > pestaña **Almacenamiento**.
   - Asegúrate de tener varios GB libres (idealmente más de 10 GB) en tu disco.

2. **Reinicia el sistema:**
   - A veces, tras una actualización, un simple reinicio puede solucionar procesos atascados.

3. **Intenta la importación manual:**
   - Si la app Mail falla automáticamente, intenta ir a:
     - **Mail > Archivo > Importar buzones…**
     - Ahí puedes intentar importar desde la carpeta:  
       `~/Library/Mail/`

4. **Reindexar Mail manualmente (si tienes conocimientos técnicos):**
   - Cierra Mail.
   - En Finder, ve a:
     - `~/Library/Mail/`
     - Renombra o mueve la carpeta `V10` (u otra que se parezca a la versión).
   - Abre Mail y este volverá a intentar importar todo de nuevo.

5. **Verifica permisos de la carpeta de inicio:**
   - En **Utilidad de Discos**, selecciona tu disco > botón **Primeros Auxilios**.
   - También puedes ir a **Preferencias del Sistema > Seguridad y privacidad > Archivos y carpetas**, y verificar que Mail tiene acceso a tu carpeta de inicio.

---

### 🛠 Si nada funciona:

Podrías crear un nuevo perfil de usuario temporal y ver si Mail funciona allí. Esto ayuda a detectar si el problema está en tu usuario actual o en el sistema.

¿Quieres que te guíe paso a paso en alguno de estos métodos?

---
*Generado desde conversación con 2 mensajes.*
*IA/ML*
