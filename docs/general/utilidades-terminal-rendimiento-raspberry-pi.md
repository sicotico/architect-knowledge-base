---
title: Utilidades terminal rendimiento Raspberry Pi
date: 2024-10-29
category: General
slug: utilidades-terminal-rendimiento-raspberry-pi
tags: ['General']
---

# Utilidades terminal rendimiento Raspberry Pi


> **Pregunta original:**
> 
Hola , soy un linuxero un poco anticuado y tengo un Raspberry Pi 4 con 8GB de RAM. Estoy buscando pequeñas utilidades de terminal par ver el rendimiento 
> scripts pa mostrar OS en terminal de linux

---


## Respuesta


¡Hola! Entiendo que buscas herramientas ligeras para monitorear el rendimiento de tu Raspberry Pi desde la terminal. Aquí tienes algunas de las utilidades más recomendables para ver estadísticas en tiempo real y que funcionan muy bien en el Raspberry Pi 4:

### 1. `htop`
Es una versión mejorada de `top`, con una interfaz más amigable y organizada. Permite ver de forma gráfica el uso de la CPU, RAM, procesos y mucho más.

   ```bash
   sudo apt update
   sudo apt install htop
   htop
   ```

### 2. `vcgencmd`
Es una utilidad específica para Raspberry Pi que permite ver el estado de varios componentes, como la temperatura de la CPU, el voltaje, y la frecuencia de la GPU y CPU.

   ```bash
   vcgencmd measure_temp   # Ver temperatura
   vcgencmd measure_volts  # Ver voltaje
   vcgencmd measure_clock arm  # Ver frecuencia de la CPU
   ```

### 3. `iostat`
Ideal para ver el rendimiento del almacenamiento (SD, discos externos) y la carga de E/S. Muestra el uso de CPU y estadísticas de lectura/escritura en discos.

   ```bash
   sudo apt install sysstat
   iostat
   ```

### 4. `nload`
Para monitorear el tráfico de red en tiempo real. Muestra visualmente el tráfico entrante y saliente de cada interfaz de red.

   ```bash
   sudo apt install nload
   nload
   ```

### 5. `iftop`
También es una herramienta para monitorear el tráfico de red, pero muestra las conexiones activas en tiempo real, lo que puede ser útil para ver qué aplicaciones están utilizando la red.

   ```bash
   sudo apt install iftop
   sudo iftop
   ```

### 6. `dstat`
Esta utilidad combina varias métricas, como el uso de CPU, memoria, E/S, red, etc. Es ideal si deseas monitorear múltiples recursos al mismo tiempo.

   ```bash
   sudo apt install dstat
   dstat
   ```

### 7. `glances`
Glances es una herramienta de monitoreo de sistemas que permite visualizar estadísticas detalladas en una sola interfaz, como CPU, RAM, disco, red, etc. Es un poco más pesado que `htop`, pero sigue siendo liviano.

   ```bash
   sudo apt install glances
   glances
   ```

### 8. `stress`
Aunque no es una herramienta de monitoreo, `stress` es útil para realizar pruebas de estrés en el CPU, memoria y disco. Puedes utilizarlo para probar el rendimiento del sistema.

   ```bash
   sudo apt install stress
   stress --cpu 4 --timeout 30  # Por ejemplo, estresa los 4 núcleos de CPU por 30 segundos
   ```

### 9. `btop` (alternativa a htop, con interfaz visual más avanzada)
Si quieres algo moderno, `btop` tiene una interfaz avanzada y colores personalizables. Es una versión más amigable visualmente que `htop`.

   ```bash
   sudo apt install btop
   btop
   ```

Prueba estas herramientas para ver cuál se adapta mejor a lo que buscas.
---


Aquí tienes algunos scripts simples en Bash para mostrar información sobre el sistema operativo y el hardware en la terminal de Linux. Son útiles para obtener información básica del sistema, especialmente en una Raspberry Pi o en cualquier distribución de Linux.

### 1. **Mostrar información del sistema operativo**

Este script muestra el nombre del sistema operativo, versión, arquitectura y nombre del kernel.

```bash
#!/bin/bash

echo "Información del sistema operativo:"
echo "----------------------------------"
echo "Nombre del sistema operativo: $(lsb_release -d | cut -f2)"
echo "Versión del sistema operativo: $(lsb_release -r | cut -f2)"
echo "Arquitectura: $(uname -m)"
echo "Versión del kernel: $(uname -r)"
```

Guarda este código en un archivo llamado `info_os.sh`, dale permisos de ejecución y ejecútalo:

```bash
chmod +x info_os.sh
./info_os.sh
```

### 2. **Mostrar información del CPU y memoria RAM**

Este script muestra el modelo de CPU, el número de núcleos y la cantidad de memoria RAM.

```bash
#!/bin/bash

echo "Información de la CPU y RAM:"
echo "----------------------------"
echo "Modelo de CPU: $(cat /proc/cpuinfo | grep 'model name' | uniq | cut -d ':' -f2)"
echo "Núcleos de CPU: $(nproc)"
echo "Memoria RAM total: $(free -h | grep 'Mem:' | awk '{print $2}')"
echo "Memoria RAM en uso: $(free -h | grep 'Mem:' | awk '{print $3}')"
echo "Memoria RAM disponible: $(free -h | grep 'Mem:' | awk '{print $7}')"
```

Guarda el script como `info_cpu_ram.sh`, y ejecútalo igual que el anterior:

```bash
chmod +x info_cpu_ram.sh
./info_cpu_ram.sh
```

### 3. **Mostrar información del almacenamiento**

Este script muestra el almacenamiento total y el espacio libre en el sistema.

```bash
#!/bin/bash

echo "Información de almacenamiento:"
echo "------------------------------"
df -h --output=source,size,used,avail,pcent | grep -E '^/dev/'
```

Guárdalo como `info_storage.sh` y ejecútalo:

```bash
chmod +x info_storage.sh
./info_storage.sh
```

### 4. **Mostrar estadísticas de red**

Para ver las interfaces de red, dirección IP y estadísticas de tráfico:

```bash
#!/bin/bash

echo "Información de red:"
echo "-------------------"
for interface in $(ls /sys/class/net); do
    echo "Interfaz: $interface"
    echo "Dirección IP: $(ip -4 addr show $interface | grep -oP '(?<=inet\s)\d+(\.\d+){3}')"
    echo "Tráfico de datos enviado: $(cat /sys/class/net/$interface/statistics/tx_bytes) bytes"
    echo "Tráfico de datos recibido: $(cat /sys/class/net/$interface/statistics/rx_bytes) bytes"
    echo "---------------------------------"
done
```

Guárdalo como `info_red.sh` y ejecútalo de la misma manera:

```bash
chmod +x info_red.sh
./info_red.sh
```

### 5. **Mostrar información completa del sistema**

Este script combina todo en una sola ejecución para obtener una visión completa del sistema.

```bash
#!/bin/bash

echo "======================================="
echo "       INFORMACIÓN COMPLETA DEL SISTEMA"
echo "======================================="

# Información del sistema operativo
echo "Información del sistema operativo:"
echo "----------------------------------"
echo "Nombre del sistema operativo: $(lsb_release -d | cut -f2)"
echo "Versión del sistema operativo: $(lsb_release -r | cut -f2)"
echo "Arquitectura: $(uname -m)"
echo "Versión del kernel: $(uname -r)"
echo ""

# Información de CPU y memoria RAM
echo "Información de la CPU y RAM:"
echo "----------------------------"
echo "Modelo de CPU: $(cat /proc/cpuinfo | grep 'model name' | uniq | cut -d ':' -f2)"
echo "Núcleos de CPU: $(nproc)"
echo "Memoria RAM total: $(free -h | grep 'Mem:' | awk '{print $2}')"
echo "Memoria RAM en uso: $(free -h | grep 'Mem:' | awk '{print $3}')"
echo "Memoria RAM disponible: $(free -h | grep 'Mem:' | awk '{print $7}')"
echo ""

# Información de almacenamiento
echo "Información de almacenamiento:"
echo "------------------------------"
df -h --output=source,size,used,avail,pcent | grep -E '^/dev/'
echo ""

# Información de red
echo "Información de red:"
echo "-------------------"
for interface in $(ls /sys/class/net); do
    echo "Interfaz: $interface"
    echo "Dirección IP: $(ip -4 addr show $interface | grep -oP '(?<=inet\s)\d+(\.\d+){3}')"
    echo "Tráfico de datos enviado: $(cat /sys/class/net/$interface/statistics/tx_bytes) bytes"
    echo "Tráfico de datos recibido: $(cat /sys/class/net/$interface/statistics/rx_bytes) bytes"
    echo "---------------------------------"
done
```

Guárdalo como `info_completo.sh` y ejecútalo:

```bash
chmod +x info_completo.sh
./info_completo.sh
```

Con estos scripts puedes acceder rápidamente a la información del sistema en Linux desde la terminal.

---
*Generado desde conversación con 4 mensajes.*
*General*
