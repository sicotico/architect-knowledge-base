---
title: Diagrama red homelab
date: 2026-06-15
category: IA/ML
slug: diagrama-red-homelab
tags: ['IA/ML']
---

# Diagrama red homelab


> **Pregunta original:**
> 
Estoy terminando un homelab. Tengo un armario de oficina de Ikea en el que he agujereado el fondo de dos compartimentos con puertas y he metido en cada uno una regleta de 3 sukos. En uno de ellos también hay switch de 1Gb con impresora, hub domótico, NAS Synology 120j y do cables ethernet que van al segundo hueco del armario con una de las regleta de 3 sukos que mencionaba antes.En este segundo  hueco uno de los sukos alimenta un fuente de alimentación de 120w con 2 UBS-A y otros 2 USB-C, otro suko alimenta un switch de 2,5Gb que está situado en la mostré alta del mueble de oficina. En la parte alta hay una regleta pero los sukos están ocupados por un NAS DXP4800 y un router Deco x20. Problemas que me he encontrado es que se me ha caído uno de la cables ethernet que van del hueco uno  dos y la falta de sukos en la parte alta del mueble. Los cable de la norte alta del mueble los disimulo con una caja esconde cable del Ikea pero no da para mucho por la fuente del NAS.

Fuera del mueble en la
Mesa tengo otro switch de 2,5Gb con portátil de empresa y un MSI MSI Modern 15 H C13M-082XES i7 13620 con 32GB de RAM ddr4 conectado al switch.

La red parte de otra habitación , tengo ONT del proveedor y directamente mi nodo Deco x20 como router principal. Esté de une por cable al switch de mi mesa de 2,5Gb y esté así vez su upstream es el switch de encima del armario y aquí está enchufado el switch de 1Gb de dentro del armario con hub , 120, y lo que ponga en el segundo hueco.


Hazme los dirgarams de red y de infra en drawio y dime si detectas algún problema 
> El cable de red del Deco x20 principal está en la mesa y de ahí saco un cable de 7 metros escondido por la pared y el marco alto de la ventana.

Respecto a la temperatura no es problema , la parte alta no es armario , sino encima del armario , tiene una altura de 140cm y ahí encima está todo al aire 

---


## Respuesta


Con esa aclaración cambia bastante el diagnóstico: la cascada desde la mesa tiene sentido por restricción física, y el riesgo térmico baja mucho porque la parte superior está al aire. Voy a corregir la topología y te dejo ficheros `.drawio` reales.
---


Corregido. Te dejo los `.drawio`:

- [Diagrama de red lógico](sandbox:/mnt/data/homelab_red.drawio)
- [Diagrama de infraestructura física](sandbox:/mnt/data/homelab_infra.drawio)

## Diagnóstico actualizado

Lo bueno:

- La cascada `Deco → switch mesa → cable 7 m → switch armario` tiene sentido por la ubicación real del cableado.
- El tramo de 7 m no es problema si el cable es Cat 5e/6 decente.
- La temperatura ya no me preocupa tanto si el DXP4800 y el Deco están encima del armario y al aire.
- El DS120j está bien en el switch de 1Gb.

Lo malo / mejorable:

- El punto débil principal es mecánico: cables Ethernet sueltos entre huecos.
- Falta margen eléctrico en la parte superior.
- La caja ocultacables se queda pequeña por la fuente del NAS.
- El switch de la mesa es ahora un punto crítico: si falla o se desconecta, cae todo lo que está encima/dentro del armario.

## Haría estos cambios

1. **Poner keystones RJ45 o un mini patch panel** entre huecos/parte superior.  
2. **Cambiar la regleta superior** por una de más tomas y mejor separación para fuentes grandes.  
3. **Fijar el cable de 7 m** con bridas/clip adhesivo y dejar bucle de servicio.  
4. **Etiquetar cables**: `uplink mesa`, `NAS DXP`, `switch 1Gb`, `Deco`, etc.  
5. **No encadenar regletas**. Mejor una regleta buena con suficientes tomas.
---


He reconstruido tu topología a partir de la descripción. Hay algunos puntos que no me quedan 100% claros (especialmente si el switch de la mesa está realmente "entre" el Deco y el resto de la red), pero creo que la estructura es esta.

# Diagrama de red (lógico)

```text
┌─────────────┐
│ ONT ISP     │
└──────┬──────┘
       │
       │ WAN
       ▼
┌─────────────┐
│ Deco X20    │
│ Router      │
└──────┬──────┘
       │ LAN
       │
       ▼
┌────────────────────┐
│ Switch 2.5Gb Mesa  │
└──────┬─────────────┘
       │
       ├──────────── MSI Modern 15
       │
       ├──────────── Portátil empresa
       │
       ▼
┌────────────────────┐
│ Switch 2.5Gb       │
│ Encima armario     │
└──────┬─────────────┘
       │
       ├──────────── NAS DXP4800
       │
       ├──────────── Deco X20 (si es nodo mesh)
       │
       ▼
┌────────────────────┐
│ Switch 1Gb         │
│ Interior armario   │
└──────┬─────────────┘
       │
       ├──────────── Synology DS120j
       ├──────────── Impresora
       ├──────────── Hub domótico
       └──────────── Otros equipos
```

---

# Diagrama físico (infraestructura)

```text
ARMARIO IKEA
│
├─────────────────────────────┐
│ HUECO 1                     │
│                             │
│ Regleta 3x Schuko          │
│ ├─ Switch 1Gb              │
│ ├─ Synology DS120j         │
│ ├─ Impresora               │
│ └─ Hub domótico            │
│                             │
│ Ethernet x2 hacia Hueco 2  │
└─────────────┬───────────────┘
              │
              │
├─────────────────────────────┐
│ HUECO 2                     │
│                             │
│ Regleta 3x Schuko          │
│ ├─ Fuente USB 120W         │
│ └─ Switch 2.5Gb superior   │
│                             │
│ Ethernet hacia parte alta  │
└─────────────┬───────────────┘
              │
              │
┌─────────────▼───────────────┐
│ PARTE SUPERIOR ARMARIO      │
│                             │
│ Regleta                    │
│ ├─ NAS DXP4800             │
│ └─ Deco X20                │
│                             │
│ Switch 2.5Gb               │
│ Caja ocultacables IKEA     │
└─────────────────────────────┘


MESA
│
├─ Switch 2.5Gb
├─ MSI Modern 15
└─ Portátil empresa
```

---

# Problemas que detecto

## 1. Punto único de fallo por cable Ethernet

Ya te ha pasado.

Tienes dos cables entre huecos pero parece que uno se ha soltado. Si ambos cables simplemente están tendidos por dentro del mueble:

- se moverán al manipular equipos
- terminarán desconectándose otra vez
- es difícil diagnosticar fallos

### Recomendación

Instalar entre compartimentos:

```text
Keystone RJ45
     ↓
Patch corto
     ↓
Switch
```

Aunque sean sólo 2 keystones.

Esto convierte el armario en algo mucho más mantenible.

---

## 2. Demasiados switches en cascada

Actualmente parece que tienes:

```text
Deco
 ↓
Switch mesa
 ↓
Switch 2.5Gb armario
 ↓
Switch 1Gb armario
```

No es grave.

Pero implica:

- más consumo
- más latencia (muy poca)
- más puntos de fallo

Lo ideal sería:

```text
Deco
 ↓
Switch principal 2.5Gb
 ├─ Mesa
 ├─ NAS DXP4800
 ├─ Switch 1Gb
 └─ resto
```

Es decir, un único switch principal distribuyendo.

---

## 3. El DS120j está limitado por el switch de 1Gb

Esto es normal.

El DS120j:

- sólo tiene puerto Gigabit
- nunca superará ~110 MB/s

Por tanto no merece la pena moverlo a 2.5Gb.

---

## 4. Falta de Schukos

Es el problema físico principal.

Ahora mismo:

```text
Parte superior
├─ DXP4800
└─ Deco
```

y estás sin margen.

### Opciones

#### Opción A (la mejor)

Cambiar la regleta superior por una de 5-6 tomas.

#### Opción B

Subir la fuente USB de 120W a la parte superior.

Ventajas:

- menos cable USB recorriendo el armario
- libera un Schuko en el hueco inferior

#### Opción C

Instalar una PDU vertical pequeña.

Muy típico en homelabs.

---

## 5. Temperatura

Esto es lo que más me preocuparía.

Tienes:

- DXP4800
- DS120j
- switches
- fuente USB 120W
- Deco

dentro de un armario cerrado.

Los agujeros traseros ayudan a los cables pero apenas ayudan a la ventilación.

### Vigilar

- temperatura discos del DXP4800
- temperatura discos del DS120j
- temperatura CPU del NAS

Si ves:

- HDD > 45°C sostenidos
- SSD > 60°C sostenidos

añadiría ventilación.

---

## 6. Topología poco intuitiva

Lo que más me llama la atención es:

```text
Deco
 ↓
Switch mesa
 ↓
Switch armario
```

Normalmente haríamos:

```text
Deco
 ↓
Switch armario
 ├─ Mesa
 ├─ NAS
 ├─ Domótica
 └─ Impresora
```

porque el armario parece ser el centro de distribución físico de la red.

Si puedes llevar el cable principal hasta el armario, simplificarías bastante todo.

---

# Diseño que yo intentaría dejar

```text
ONT
 ↓
Deco X20 Router
 ↓
Switch 2.5Gb principal (armario)
 ├─ NAS DXP4800
 ├─ Switch 1Gb
 │   ├─ Impresora
 │   ├─ DS120j
 │   └─ Hub domótico
 ├─ Switch mesa
 │   ├─ MSI
 │   └─ Portátil empresa
 └─ Nodo Deco secundario (si existe)
```

Con eso tendrías una jerarquía más limpia, menos dependencias raras y sería más fácil ampliar el homelab en el futuro.

---
*Generado desde conversación con 5 mensajes.*
*IA/ML*
