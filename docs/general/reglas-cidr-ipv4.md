---
title: Reglas CIDR IPv4
date: 2026-07-12
category: General
slug: reglas-cidr-ipv4
tags: ['General']
---

# Reglas CIDR IPv4


> **Pregunta original:**
> 
tengo un poco de lio con CDIR. damr dos reglas para que pueda contar bien el nuemro de ips ?
> Un host tiene la dirección IP 10.16.43.210 con una máscara de subred 255.255.248.0. ¿Cuál es la dirección de broadcast correspondiente a esta subred?

A.
10.16.39.255


B.
10.16.48.255


C.
10.16.43.255

(Tu respuesta)
Incorrectas
Este valor asume incorrectamente que el límite de la subred se encuentra en el octeto completo, ignorando los bits de la máscara.

D.
10.16.47.255

Correctas
La máscara 255.255.248.0 (/21) agrupa los bloques en pasos de 8 en el tercer octeto. Para el valor 43, la subred arranca en 40 y termina en el broadcast de la 47.255.

No lo entiendo 

---


## Respuesta


Para **CIDR en IPv4**, quédate con estas dos reglas:

1. **Número total de direcciones IP**
   
   \[
   2^{(32-\text{prefijo})}
   \]

   Ejemplo: `192.168.1.0/24`

   \[
   2^{32-24}=2^8=256\text{ IPs}
   \]

2. **Número de IPs utilizables para dispositivos**
   
   Normalmente:

   \[
   \text{IPs utilizables}=\text{IPs totales}-2
   \]

   Se restan:
   - La primera IP: dirección de red.
   - La última IP: broadcast.

   Por tanto, una `/24` tiene **256 IPs totales** y **254 utilizables**.

| CIDR | IPs totales | IPs utilizables |
|---|---:|---:|
| `/24` | 256 | 254 |
| `/25` | 128 | 126 |
| `/26` | 64 | 62 |
| `/27` | 32 | 30 |
| `/28` | 16 | 14 |
| `/29` | 8 | 6 |
| `/30` | 4 | 2 |

**Excepciones:** una `/31` suele usarse en enlaces punto a punto y puede tener 2 IPs utilizables; una `/32` representa una única IP.
---


La clave está en mirar **el tercer octeto**, porque la máscara es:

```text
255.255.248.0
```

Eso equivale a:

```text
/21
```

## Regla 1: calcular el tamaño del bloque

En el tercer octeto, la máscara es `248`.

```text
256 - 248 = 8
```

Por tanto, las subredes avanzan de **8 en 8**:

```text
0–7
8–15
16–23
24–31
32–39
40–47
48–55
...
```

## Regla 2: localizar dónde cae el 43

La IP es:

```text
10.16.43.210
```

El tercer octeto es `43`.

`43` está dentro del bloque:

```text
40–47
```

Así que:

- Dirección de red: `10.16.40.0`
- Primera IP utilizable: `10.16.40.1`
- Última IP utilizable: `10.16.47.254`
- Broadcast: `10.16.47.255`

Por eso la respuesta correcta es:

```text
D. 10.16.47.255
```

El error de elegir `10.16.43.255` consiste en tratar el tercer octeto como si estuviera completamente reservado para la red, como ocurriría con una máscara `/24`. Pero aquí la máscara es `/21`, así que el tercer octeto está dividido en bloques de 8.

---
*Generado desde conversación con 4 mensajes.*
*General*
