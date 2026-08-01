---
title: Flasheo OPNsense y X520
date: 2026-06-18
category: General
slug: flasheo-opnsense-y-x520
tags: ['General']
---

# Flasheo OPNsense y X520


> **Pregunta original:**
> 
Qué es una x520 ?
> Me espero entonces y no imprimo nada?
Ya tengo la x520 y el raiser, estoy flasheando opnsense ahora mismo

Que me he cogido vacaciones para desempolvar la a1 mini y meterle mano a esto xD

---


## Respuesta


Una **Intel X520** es una **tarjeta de red PCIe de 10 GbE**.

En tu caso, probablemente es una **Intel Ethernet Server Adapter X520**, normalmente con puertos **SFP+**. Se usa para meter **red de 10 gigabits** a un servidor, firewall, NAS o mini-PC con PCIe.

## En cristiano

Es “la tarjeta que convierte tu máquina en algo con red 10G”.

Ejemplos típicos:

| Modelo | Puertos | Tipo |
|---|---:|---|
| **X520-DA1** | 1 puerto | SFP+ 10G |
| **X520-DA2** | 2 puertos | SFP+ 10G |
| **X520-SR1/SR2** | 1/2 puertos | Fibra óptica |

## Qué conector usa

La mayoría de X520 usan **SFP+**, no RJ45.

Eso significa que conectas cosas como:

- **DAC SFP+**: cable directo de cobre, barato y práctico para distancias cortas.
- **Módulos SFP+ fibra**: para fibra óptica.
- **Transceptor SFP+ a RJ45 10G**: posible, pero se calienta más y suele consumir más.

## Por qué se usa en OPNsense

Para un firewall/router con OPNsense, una X520 sirve para:

- LAN a **10 Gb/s**
- trunk VLAN hacia un switch
- enlace rápido a NAS/servidor
- separar redes si es dual port

## Lo bueno

- Muy soportada en FreeBSD/OPNsense.
- Barata de segunda mano.
- Robusta.
- Ideal para 10G con SFP+ DAC.
- Mejor opción que muchos adaptadores USB/Realtek para firewall.

## Lo malo

- Es vieja y puede consumir/calentar bastante.
- Necesita buena ventilación.
- Los módulos RJ45 10G en SFP+ pueden calentarse mucho.
- Hay muchas falsificaciones o variantes OEM.
- Necesita un slot PCIe/riser estable.

En OPNsense suele aparecer como interfaz **`ix0`** y **`ix1`** si es de dos puertos.
---


Sí: **espera y no imprimas nada todavía**.

Ahora mismo lo correcto es cerrar primero la parte de red:

1. **Termina de flashear OPNsense.**
2. **Arranca y confirma que detecta la X520.**
   - En OPNsense/FreeBSD debería aparecer como interfaz Intel `ix` / `ix0` / `ix1`.
3. **Comprueba que el riser es estable.**
   - Que la tarjeta no desaparezca tras reiniciar.
   - Que no haya errores PCIe raros.
   - Que no se caliente de forma absurda.
4. **Asigna interfaces:**
   - Puerto 10G como LAN/trunk o como enlace principal, según tu diseño.
   - WAN separada.
5. **Solo después prueba conectividad básica.**

La **A1 mini** ahora mismo déjala quieta. Lo bueno: ya tienes la parte clave —X520 + riser— y estás avanzando en el firewall. Lo malo: imprimir piezas antes de confirmar medidas, temperaturas, orientación de cables y estabilidad PCIe puede acabar en plástico inútil.

Cuando OPNsense arranque, mira esto:

```sh
pciconf -lv | grep -B3 -A3 -i intel
ifconfig
dmesg | grep -i ix
```

Si ves `ix0`/`ix1`, buena señal.

Mi criterio sería:

**No imprimir aún. Primero validar hardware real. Luego medir. Luego diseñar/imprimir.**

---
*Generado desde conversación con 4 mensajes.*
*General*
