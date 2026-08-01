---
title: Widget monitorización Ubuntu
date: 2026-05-06
category: General
slug: widget-monitorizacion-ubuntu
tags: ['General']
---

# Widget monitorización Ubuntu


> **Pregunta original:**
> 
tengo una ubuntu 26.04 LTS REcoon. Quiero poner un widget de monitorizacion en el escritorio 
> me quedo con Vitals

---


## Respuesta


En entity["software","Ubuntu 26.04 LTS","Linux distribution"], el concepto clásico de “widgets de escritorio” no viene activado por defecto (especialmente con entity["software","GNOME","desktop environment"]). Sin embargo, puedes lograr monitorización en tiempo real con varias herramientas bien establecidas. Las tres opciones más sólidas son: **Conky**, extensiones de GNOME o herramientas tipo panel.

---

## 1) Conky (la opción más potente y flexible)

image_group{"aspect_ratio":"1:1","query":["conky desktop system monitor linux","conky customization cpu ram widget","conky minimal theme desktop ubuntu","conky rings system monitor example"],"num_per_query":1}

**Conky** es un monitor de sistema altamente configurable que se dibuja directamente en el escritorio.

### Instalación
```bash
sudo apt update
sudo apt install conky-all
```

### Configuración básica
1. Crea un archivo:
```bash
nano ~/.conkyrc
```

2. Ejemplo mínimo:
```lua
conky.config = {
    alignment = 'top_right',
    background = true,
    update_interval = 1,
    double_buffer = true,
};

conky.text = [[
CPU: ${cpu}%
RAM: ${mem}/${memmax}
DISK: ${fs_used /}/${fs_size /}
]];
```

3. Ejecuta:
```bash
conky
```

### Ventajas
- Totalmente personalizable (CPU, RAM, red, temperatura, etc.)
- Bajo consumo de recursos
- Puedes usar temas avanzados (tipo panel futurista)

---

## 2) Extensiones de GNOME (más simple, menos flexible)

image_group{"aspect_ratio":"1:1","query":["gnome system monitor extension top bar cpu ram","gnome extensions vitals cpu temperature ram","gnome shell extensions system stats panel","ubuntu gnome extensions performance monitor"],"num_per_query":1}

Si usas GNOME (lo normal en Ubuntu), puedes añadir indicadores al panel superior.

### Ejemplo recomendado
- entity["software","Vitals","GNOME extension"]

### Instalación
1. Instala soporte:
```bash
sudo apt install gnome-shell-extensions gnome-shell-extension-manager
```

2. Abre:
```bash
gnome-extensions-app
```

3. Busca e instala **Vitals**

### Qué muestra
- Uso de CPU
- RAM
- Temperatura
- Red
- Disco

### Ventajas
- Muy fácil
- Integrado en la barra superior
- Sin configuración compleja

---

## 3) Plank + indicadores o docks (menos típico)

image_group{"aspect_ratio":"1:1","query":["plank dock linux system monitor plugin","ubuntu dock with cpu monitor widget","linux dock system stats widget","plank dock customization ubuntu"],"num_per_query":1}

No es un “widget flotante” puro, pero puedes usar docks con plugins de monitorización.

---

## Recomendación directa

- Si quieres algo tipo “widget en el escritorio”: **usa Conky**
- Si quieres algo limpio sin complicarte: **usa Vitals (GNOME)**

---

## Nota importante sobre Ubuntu 26.04

Las versiones modernas de GNOME:
- No soportan widgets clásicos tipo Windows
- Priorizan extensiones o apps externas como Conky

---

Si quieres, dime:
- qué quieres monitorizar (CPU, GPU, red, temperaturas…)
- y el estilo (minimalista, gamer, futurista)

y te paso un **tema de Conky listo para copiar/pegar** adaptado a tu escritorio.
---


Buena elección. entity["software","Vitals","GNOME extension"] es la forma más limpia de tener monitorización sin complicarte con configuraciones manuales.

---

## Instalación rápida (método recomendado)

### 1) Instala el gestor de extensiones
```bash
sudo apt update
sudo apt install gnome-shell-extension-manager
```

### 2) Abre el gestor
Ejecuta:
```bash
gnome-extensions-app
```

### 3) Instala Vitals
- Ve a la pestaña **“Explorar”**
- Busca: **Vitals**
- Instálalo y actívalo

---

## Qué puedes monitorizar

Vitals permite añadir indicadores en la barra superior de entity["software","GNOME","desktop environment"]:

- CPU (uso por núcleo)
- RAM
- Temperaturas (CPU/GPU si están disponibles)
- Red (subida/bajada en tiempo real)
- Disco
- Sensores del sistema

---

## Configuración recomendada (práctica)

Una vez instalado:

1. Abre **Extensiones → Vitals → Configuración**
2. Ajusta:

### Panel (lo visible arriba)
- Activa:
  - CPU usage
  - Memory
  - Network speed
- Desactiva lo que no necesites (para no saturar la barra)

### Sensores
- Activa **temperaturas** si aparecen
- Si no aparecen → instala sensores:

```bash
sudo apt install lm-sensors
sudo sensors-detect
```

(Reinicia sesión después)

---

## Ajustes útiles

- **Update interval**: 1–2 segundos (equilibrio entre precisión y consumo)
- **Units**: MB/s o Mbps según prefieras
- **Position**: puedes mover el widget dentro del panel

---

## Limitaciones (para que lo tengas claro)

- No es un widget “flotante” en el escritorio (es solo barra superior)
- GPU puede no aparecer sin drivers/sensores adecuados
- Mucha info activa = barra saturada

---

## Alternativa si se te queda corto

Si en algún momento quieres algo más visual (gráficos, gauges, etc.), vuelve a considerar:
- entity["software","Conky","system monitor"]

---

Si quieres optimizarlo fino (por ejemplo: mostrar solo núcleos específicos, o temperatura exacta de tu CPU), dime qué hardware tienes y lo ajustamos.

---
*Generado desde conversación con 4 mensajes.*
*General*
