---
title: Cambiar resolución VNC Raspberry
date: 2024-09-27
category: IA/ML
slug: cambiar-resolucion-vnc-raspberry
tags: ['IA/ML']
---

# Cambiar resolución VNC Raspberry


> **Pregunta original:**
> 
Tengo una raspberry Pi 4 de 8 gb, la quiero usar de forma permanente con VNC. Actualmente uso el cliente RealVNC pero no me da la posibilidad de variar la resolucion y lo veo muy pequeño.
¿Como puedo cambiar la resolucion?

---


## Respuesta


Para cambiar la resolución de la pantalla virtual de tu Raspberry Pi 4 cuando usas VNC, puedes modificar la configuración en el archivo de configuración del sistema. Sigue estos pasos para ajustar la resolución:

### Método 1: Configuración a través de `raspi-config`
1. Abre una terminal en tu Raspberry Pi o conecta a través de SSH.
2. Ejecuta el siguiente comando para abrir el menú de configuración:
   ```bash
   sudo raspi-config
   ```
3. Ve a la opción **"Display Options"**.
4. Luego selecciona **"Resolution"**.
5. Elige la resolución que prefieras de la lista de opciones disponibles.
6. Guarda los cambios y reinicia la Raspberry Pi con:
   ```bash
   sudo reboot
   ```

Esto cambiará la resolución de la pantalla virtual de VNC.

### Método 2: Modificar el archivo `config.txt`
Si el primer método no funciona o deseas más control sobre la resolución específica, puedes editar el archivo `config.txt`:

1. Abre el archivo de configuración con un editor de texto como `nano`:
   ```bash
   sudo nano /boot/config.txt
   ```
2. Busca las siguientes líneas (o agrégalas si no están presentes) y configúralas a la resolución que deseas:
   ```bash
   hdmi_force_hotplug=1
   hdmi_group=2
   hdmi_mode=82  # Modo 82 corresponde a 1920x1080 a 60 Hz, cambia a la resolución que prefieras
   ```
   Aquí hay algunos ejemplos comunes de `hdmi_mode` para el grupo 2:
   - `hdmi_mode=16`: 1024x768 a 60 Hz
   - `hdmi_mode=28`: 1280x1024 a 60 Hz
   - `hdmi_mode=82`: 1920x1080 a 60 Hz

   **Nota**: Puedes encontrar una lista completa de modos disponibles en la [documentación oficial de Raspberry Pi](https://www.raspberrypi.com/documentation/computers/config_txt.html).

3. Guarda los cambios y cierra el editor (`Ctrl + X`, `Y`, `Enter`).
4. Reinicia la Raspberry Pi para aplicar los cambios:
   ```bash
   sudo reboot
   ```

Esto cambiará la resolución de la pantalla virtual que VNC utiliza.

Con cualquiera de estos métodos, deberías poder ajustar la resolución de la sesión de VNC para que sea más cómoda de utilizar.

---
*Generado desde conversación con 2 mensajes.*
*IA/ML*
