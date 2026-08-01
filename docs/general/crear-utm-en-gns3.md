---
title: Crear UTM en GNS3
date: 2026-05-14
category: General
slug: crear-utm-en-gns3
tags: ['General']
---

# Crear UTM en GNS3


> **Pregunta original:**
> 
Tengo dudas con el UTM y el GNS3. como se crea un VM dentro del GNS para que tenga una solucion UTM
> hay algun utmmas sencillo ?
> el ufw de ubuntu valdria como utm ?

---


## Respuesta


Sí. En GNS3 el “UTM” no se crea como una función propia de GNS3, sino como una máquina virtual/firewall virtualizada dentro de la topología. Para tu PEC, lo normal es usar entity["software","pfSense","Firewall/UTM basado en FreeBSD"] o entity["software","OPNsense","Firewall/UTM basado en HardenedBSD"] porque cumplen exactamente el bloque 3. fileciteturn0file0L22-L33

## Concepto clave

GNS3 es un entorno de emulación.  
El UTM realmente es una VM que actúa como firewall/router avanzado.

Arquitectura típica:

```text
Internet/WAN
      |
   [Router]
      |
   [pfSense]
   |   |   |
 LAN DMZ VPN
```

---

# Cómo crear la VM UTM dentro de GNS3

## Opción recomendada: pfSense

### 1. Descargar la ISO

Desde la web oficial:

- AMD64
- Installer ISO
- VGA

Normalmente:
- `pfSense-CE-*.iso.gz`

---

# 2. Crear una VM en GNS3

En GNS3:

```text
Edit → Preferences → QEMU → QEMU VMs
```

Luego:

```text
New
```

Configura:

| Parámetro | Valor recomendado |
|---|---|
| Nombre | pfSense |
| RAM | 2048 MB |
| CPUs | 2 |
| Disco | 10-20 GB |
| Tipo | QEMU VM |
| ISO | La ISO descargada |

---

# 3. Añadir interfaces de red

El UTM necesita varias NICs.

Mínimo:

| Interfaz | Función |
|---|---|
| em0 | WAN |
| em1 | LAN |

Para DMZ:

| Interfaz | Función |
|---|---|
| em2 | DMZ |

En GNS3:

```text
Right click VM → Configure → Network
```

Añades:
- 2 o 3 adaptadores.

---

# 4. Arrancar e instalar pfSense

Arrancas la VM.

Aparece el instalador:

```text
Install pfSense
```

Configuración típica:
- ZFS o UFS (cualquiera sirve para PEC)
- Auto partition

Reinicia.

---

# 5. Asignar interfaces

Al arrancar:

```text
Assign interfaces?
```

Ejemplo:

| NIC | Zona |
|---|---|
| em0 | WAN |
| em1 | LAN |
| em2 | DMZ |

---

# 6. Integrarlo en la topología GNS3

Ejemplo simple para tu PEC:

```text
        [ISP Router]
              |
           WAN
         [pfSense]
         /       \
      LAN        DMZ
       |           |
   [Switch]    [Servidor]
    /    \
 VLAN10 VLAN20
```

Esto además te ayuda a cubrir:
- VLANs
- segmentación
- firewall
- NAT
- routing

que son requisitos del bloque 2 y 3. fileciteturn0file0L11-L21 fileciteturn0file0L22-L33

---

# 7. Configuración básica obligatoria

## NAT

En pfSense:

```text
Firewall → NAT
```

Modo:
- Automatic outbound NAT

---

## Reglas firewall

```text
Firewall → Rules
```

Ejemplo:
- Permitir LAN → Internet
- Bloquear DMZ → LAN

---

## DHCP

```text
Services → DHCP Server
```

Activar para LAN.

---

# 8. Servicios avanzados para sacar buena nota

Tu PEC pide al menos 2. fileciteturn0file0L30-L33

Lo más razonable:

| Servicio | Dificultad | Recomendación |
|---|---|---|
| WireGuard VPN | Baja | Muy recomendable |
| OpenVPN | Media | Clásico |
| Suricata IDS/IPS | Media | Muy valorado |
| Squid Proxy | Media | Bueno para filtrado |
| Snort | Media-Alta | Consume más |

## Mi recomendación

### Fácil y sólido:
- WireGuard
- Suricata

### Más empresarial:
- OpenVPN
- Squid

---

# Diferencia importante: VM vs Appliance

En GNS3 puedes:

| Método | Qué es |
|---|---|
| QEMU VM | Máquina virtual real |
| Appliance | Plantilla preparada |

La mayoría usa:
```text
Marketplace → Download appliance
```

y GNS3 configura automáticamente la VM.

Para pfSense suele ser más rápido.

---

# Problemas habituales

## 1. No arranca

Suele ser:
- VT-x/AMD-V desactivado en BIOS
- Hyper-V activo en Windows

---

## 2. Sin Internet

Revisar:
- Cloud node
- NAT node
- interfaz WAN

---

## 3. Mucho consumo RAM

pfSense + Suricata puede consumir:
- 4 GB fácilmente.

---

# Qué te recomiendo para la PEC

## Topología mínima razonable

```text
Router ISP
    |
pfSense
 |     \
LAN    DMZ
 |
Switch
 |   |
PC1 PC2
```

Añade:
- VLAN10
- VLAN20
- NAT
- reglas firewall
- WireGuard
- Suricata

Con eso cubres prácticamente todo el bloque 2 y 3 de forma coherente.

---

# Consejo importante para la memoria

No hagas solo capturas.

Explica:
- por qué separas LAN y DMZ
- por qué usas VLANs
- por qué el IDS está en la WAN
- qué amenazas mitiga el firewall

Eso es lo que normalmente diferencia un aprobado justo de una nota alta.
---


Técnicamente puede servir parcialmente, pero académicamente tiene riesgos para esa PEC.

## El problema principal

entity["software","Uncomplicated Firewall","Frontend simplificado de iptables para Ubuntu"] no es un UTM completo.  
Es solo un frontend de firewall sobre `iptables/nftables`.

Un UTM normalmente integra:
- firewall,
- NAT,
- VPN,
- IDS/IPS,
- proxy,
- filtrado,
- segmentación,
- monitorización.

El enunciado pide explícitamente:

> “Desplegar un firewall tipo pfSense, OPNsense o similar” fileciteturn0file0L22-L24

Eso implica una solución dedicada de seguridad de red, no únicamente reglas básicas de firewall.

---

# Qué sí podrías hacer con Ubuntu + UFW

Puedes montar una VM Ubuntu en GNS3 y configurar:

| Función | Posible |
|---|---|
| Firewall | Sí |
| NAT | Sí |
| Routing | Sí |
| VLANs | Sí |
| VPN WireGuard | Sí |
| IDS Suricata | Sí |
| Proxy Squid | Sí |

Pero UFW por sí solo:
- no da interfaz UTM,
- no centraliza servicios,
- no parece una solución “enterprise”.

---

# Entonces… ¿aprobaría?

## Posiblemente sí, si lo justificas muy bien.

Pero hay diferencias:

| Solución | Riesgo académico |
|---|---|
| pfSense/OPNsense | Bajo |
| IPFire | Bajo |
| Ubuntu + UFW | Medio |
| Solo UFW básico | Alto |

---

# Lo que el profesor probablemente espera ver

Algo parecido a:

```text id="v2k3rm"
WAN → Firewall UTM → LAN/DMZ
```

Con:
- panel de administración,
- zonas,
- reglas,
- NAT,
- VPN,
- IDS.

Eso encaja naturalmente con:
- pfSense
- OPNsense
- IPFire

---

# Si quieres usar Ubuntu, mejor enfoque

No lo presentes como:
> “uso UFW como UTM”

Presenta:

```text id="6o3zvk"
“Ubuntu Server actuando como gateway/firewall multifunción”
```

y añade:
- `ufw` o `iptables`
- `wireguard`
- `suricata`
- `squid`

Entonces sí se parece más a una plataforma UTM modular.

---

# Ventajas reales de Ubuntu

## Pros
- Muy ligero.
- Fácil en GNS3.
- Menos problemas de virtualización.
- Aprendes networking Linux real.
- Más flexible.

## Contras
- Más trabajo manual.
- Menos visual.
- Más difícil demostrar “UTM”.
- Más difícil de documentar elegantemente.

---

# Mi recomendación objetiva

## Si quieres minimizar problemas:
Usa:
- OPNsense
o
- IPFire

## Si ya manejas Linux:
Ubuntu puede funcionar bien.

Pero:
- no usaría solo UFW,
- añadiría mínimo:
  - WireGuard
  - Suricata
  - NAT
  - reglas segmentadas LAN/DMZ.

---

# En términos de esfuerzo

| Solución | Complejidad |
|---|---|
| IPFire | Baja |
| OPNsense | Media |
| Ubuntu + UFW + Suricata + WG | Media-Alta |
| pfSense completo | Media-Alta |

---

# Conclusión

## ¿UFW solo = UTM?
No realmente.

## ¿Ubuntu puede actuar como plataforma UTM?
Sí, si integras varios servicios de seguridad.

## ¿Es la mejor opción para la PEC?
Solo si:
- ya conoces Linux,
- quieres evitar pfSense,
- y puedes justificar técnicamente la arquitectura.
---


Sí. entity["software","pfSense","Firewall/UTM basado en FreeBSD"] es potente, pero para alguien que empieza puede resultar pesado porque mezcla:
- routing,
- firewall,
- NAT,
- VPN,
- IDS,
- paquetes adicionales,
- interfaz bastante “enterprise”.

Hay alternativas más simples dependiendo de lo que necesites para la PEC.

# Opciones más sencillas

## 1. OPNsense — la más recomendable si quieres algo más amigable

entity["software","OPNsense","Firewall/UTM basado en HardenedBSD"]

### Ventajas
- Interfaz más moderna.
- Menús más claros.
- WireGuard integrado.
- Mejor experiencia visual.
- Muy similar a pfSense en funcionalidades.

### Inconvenientes
- Sigue siendo un firewall profesional.
- Consume recursos parecidos.

### Para la PEC
Cumple perfectamente:
- NAT
- Firewall
- VLAN
- DMZ
- VPN
- IDS/IPS

Probablemente es el mejor equilibrio.

---

# 2. IPFire — bastante más simple

entity["software","IPFire","Distribución Linux firewall/UTM"]

### Ventajas
- Muy fácil de instalar.
- Interfaz sencilla.
- Muy estable.
- Consume menos.

### Inconvenientes
- Menos “enterprise”.
- Menos flexible en laboratorios complejos.
- Menos documentación académica comparado con pfSense.

### Muy útil si:
Quieres:
- firewall,
- NAT,
- proxy,
- IDS básico

sin pelearte demasiado.

---

# 3. Sophos XG Home — muy visual

entity["software","Sophos Firewall Home Edition","UTM/firewall empresarial gratuito para laboratorio"]

### Ventajas
- Muy profesional visualmente.
- Dashboard excelente.
- IDS, web filtering y VPN integrados.

### Inconvenientes
- Más pesado.
- Más RAM.
- Más complejo internamente.
- Licenciamiento “home”.

### Para GNS3
Funciona, pero no es el más cómodo para empezar.

---

# 4. Router Linux simple (la opción más fácil técnicamente)

Puedes montar una VM Linux ligera:
- Ubuntu Server
- Debian

y usar:
- `iptables`
- `nftables`
- `dnsmasq`
- `wireguard`

### Ventajas
- Muy ligero.
- Aprendes más networking real.
- Muy flexible.

### Inconvenientes
- No es un “UTM visual”.
- Mucha CLI.
- Puede no encajar tan bien con el enunciado “pfSense o similar”. fileciteturn0file0L22-L24

---

# Mi evaluación realista

| Opción | Facilidad | Recursos | Adecuado PEC | Recomendación |
|---|---|---|---|---|
| OPNsense | Media | Media | Muy alta | Mejor opción |
| IPFire | Alta | Baja | Alta | Muy buena si vas justo |
| pfSense | Media-Alta | Media | Muy alta | Clásico académico |
| Sophos | Baja | Alta | Alta | Excesivo para PEC |
| Linux manual | Media | Baja | Media | Solo si dominas Linux |

---

# Lo que probablemente te conviene

Si tu objetivo es:
- terminar la PEC sin perder semanas,
- demostrar conceptos,
- tener capturas claras,

yo usaría:

## OPNsense
o
## IPFire

---

# Para GNS3 concretamente

La más sencilla de integrar suele ser:

## IPFire

Porque:
- arranca rápido,
- detecta NICs fácilmente,
- poca RAM,
- instalación simple.

Pero:

## OPNsense queda más “profesional” en la memoria.

---

# Recomendación práctica

## Si tienes poca experiencia:
- IPFire

## Si quieres equilibrio:
- OPNsense

## Si quieres parecer más “enterprise”:
- pfSense

---

# Lo importante para la nota

Normalmente no te evalúan por:
> “qué UTM elegiste”

sino por:
- segmentación,
- NAT,
- reglas firewall,
- documentación,
- coherencia de diseño,
- pruebas funcionales.

Muchos alumnos pierden tiempo intentando montar un UTM enorme cuando el profesor realmente quiere:
- topología coherente,
- pruebas,
- justificación técnica.

---
*Generado desde conversación con 6 mensajes.*
*General*
