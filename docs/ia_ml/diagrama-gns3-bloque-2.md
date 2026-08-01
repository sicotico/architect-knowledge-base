---
title: Diagrama GNS3 Bloque 2
date: 2026-06-06
category: IA/ML
slug: diagrama-gns3-bloque-2
tags: ['IA/ML']
---

# Diagrama GNS3 Bloque 2


> **Pregunta original:**
> 
Comote dije  antes hazel diagram en draw.io 
> Crea un diagram en draw.io con estainfo:

Bloque 2 – Diseño e implementación de red en GNS3 3p 
Objetivo 
Aplicar conocimientos de configuración de red en un entorno realista de emulación, integrando los 
conceptos de las unidades didácticas previas. 
Tareas 
Tarea 2.1. Diseñar una red que incluya, como mínimo: 
• 2 routers. 
• 2 switches. 
• 2 redes distintas. 
• 2 VLANs. 
• Enrutamiento estático o dinámico. 
Tarea 2.2. Implementar la red en GNS3 con: direccionamiento IP, configuración de interfaces y 
pruebas de conectividad extremo a extremo. 
Tarea 2.3. Documentar el despliegue incluyendo: 
• Diagrama de la topología. 
• Configuración CLI completa de todos los equipos. 
• Capturas de funcionamiento (pings, traceroutes, tablas de enrutamiento).
> Bloque 3 – Implementación de un sistema UTM (pfSense o similar) 3p 
Objetivo 
Diseñar una arquitectura de seguridad de red real, desplegando un firewall UTM y configurando los 
servicios de seguridad asociados. 
Tareas 
Tarea 3.1. Desplegar un firewall tipo pfSense, OPNsense o similar dentro del entorno emulado. 
Tarea 3.2. Configurar las funcionalidades básicas de red: 
• NAT (Network Address Translation). 
• Reglas de firewall (allow/deny). 
• Segmentación de red en distintas zonas (LAN, WAN, DMZ). 
Tarea 3.3. Añadir al menos dos servicios avanzados a elegir entre los siguientes: 
• VPN (IPsec, OpenVPN o WireGuard). 
• IDS/IPS (Suricata o Snort). 
• Proxy (Squid). 
• Filtrado web por categorías. 
Tarea 3.4. Explicar la función de cada componente desplegado y describir un caso de uso real 
(empresa, universidad, entorno doméstico avanzado, etc.).

---


## Respuesta


Para el **Bloque 3**, una arquitectura coherente y relativamente sencilla de implementar en GNS3 sería la siguiente:

## Topología propuesta

```text
                    INTERNET
                        |
                  WAN 203.0.113.2
                        |
                 +---------------+
                 |   pfSense     |
                 | Firewall UTM  |
                 +---------------+
                   |           |
          LAN      |           | DMZ
   192.168.10.1    |           | 192.168.20.1
                   |           |
             +-----------+  +-----------+
             | Switch-LAN|  | Switch-DMZ|
             +-----------+  +-----------+
                 |              |
           PC Usuarios      Servidor Web
         192.168.10.10     192.168.20.10
```

---

# Tarea 3.1 – Despliegue del firewall UTM

Se despliega un firewall basado en la máquina virtual de:

- entity["software","pfSense","Firewall y router open source"]

Alternativamente:

- entity["software","OPNsense","Firewall y router open source"]

El firewall tendrá tres interfaces:

| Interfaz | Función | Red |
|-----------|----------|---------|
| WAN | Conexión exterior | 203.0.113.0/24 |
| LAN | Usuarios internos | 192.168.10.0/24 |
| DMZ | Servicios publicados | 192.168.20.0/24 |

---

# Tarea 3.2 – Funcionalidades básicas

## NAT

### NAT de salida (Outbound NAT)

Permite que los equipos de la LAN salgan a Internet utilizando la IP pública de la WAN.

Ejemplo:

```text
192.168.10.10
      ↓
203.0.113.2
```

### Port Forwarding

Publicación del servidor web situado en DMZ.

```text
WAN:80
   ↓
192.168.20.10:80
```

---

## Reglas de Firewall

### LAN

Permitir navegación:

```text
Origen: LAN Net
Destino: Any
Acción: Allow
```

---

### DMZ

Permitir únicamente tráfico necesario:

```text
Origen: Any
Destino: Servidor Web
Puerto: 80,443
Acción: Allow
```

Bloquear acceso DMZ → LAN:

```text
Origen: DMZ Net
Destino: LAN Net
Acción: Deny
```

---

### WAN

Bloquear todo excepto servicios publicados.

```text
Default Deny
```

---

## Segmentación de red

### Zona LAN

Usuarios internos.

```text
192.168.10.0/24
```

### Zona DMZ

Servicios expuestos.

```text
192.168.20.0/24
```

### Zona WAN

Internet.

```text
203.0.113.0/24
```

---

# Tarea 3.3 – Servicios avanzados

Se pueden implementar dos servicios avanzados:

## Servicio 1: VPN WireGuard

### Objetivo

Permitir acceso remoto seguro.

Ejemplo:

```text
Empleado remoto
      ↓ VPN
   WireGuard
      ↓
 LAN corporativa
```

Configuración:

```text
Red VPN: 10.10.10.0/24
Puerto: 51820 UDP
```

### Ventajas

- Bajo consumo.
- Alta velocidad.
- Configuración sencilla.

---

## Servicio 2: IDS/IPS Suricata

### Objetivo

Detectar ataques.

Suricata monitoriza:

- Escaneos de puertos.
- Fuerza bruta.
- Malware.
- Exploits conocidos.

Ejemplo:

```text
Atacante
    ↓
 Suricata
    ↓
 Alerta/Bloqueo
```

Modo recomendado:

```text
IPS Inline
```

---

# Tarea 3.4 – Función de cada componente

| Componente | Función |
|------------|----------|
| pfSense | Firewall principal |
| WAN | Conexión a Internet |
| LAN | Red interna de usuarios |
| DMZ | Servicios públicos |
| NAT | Traducción de direcciones |
| Firewall Rules | Control de acceso |
| WireGuard | Acceso remoto seguro |
| Suricata | Detección y prevención de intrusiones |
| Servidor Web | Servicio publicado |

---

# Caso de uso real

## Pequeña empresa

### Infraestructura

- 20 empleados.
- Servidor web corporativo.
- Acceso remoto para teletrabajo.

### Aplicación de la arquitectura

- Los empleados trabajan en la LAN.
- La web corporativa se publica desde la DMZ.
- Los teletrabajadores acceden mediante WireGuard.
- Suricata inspecciona el tráfico para detectar amenazas.
- pfSense controla el acceso entre zonas y hacia Internet.

### Beneficios

- Separación de redes críticas.
- Reducción de la superficie de ataque.
- Acceso remoto seguro.
- Monitorización continua de amenazas.
- Arquitectura similar a la utilizada en entornos empresariales reales.

Esta propuesta cumple todos los requisitos exigidos en las tareas 3.1, 3.2, 3.3 y 3.4 y es perfectamente implementable en GNS3 con una sola instancia de pfSense, dos switches virtuales y varios hosts de prueba.
---


He generado el archivo de Draw.io con una topología que cumple los requisitos mínimos:

- 2 routers (R1 y R2)
- 2 switches (SW1 y SW2)
- 2 redes distintas (192.168.10.0/24 y 192.168.20.0/24)
- 2 VLANs (VLAN 10 y VLAN 20)
- Enlace entre routers para aplicar enrutamiento estático o dinámico

**Descargar archivo:**

[Topologia_GNS3_Bloque2.drawio](sandbox:/mnt/data/Topologia_GNS3_Bloque2.drawio)

Observación: el diagrama es una base funcional para la memoria de la práctica. Si necesitas una versión más completa (con iconos Cisco, PCs finales, etiquetas de interfaces, gateways, VLAN trunk, direcciones IP de cada enlace y lista para exportar a PDF), puedo generar una versión académica más detallada.
---


He generado el archivo Draw.io para el **Bloque 3 – Implementación de un sistema UTM (pfSense)**:

📁 **Descarga:**

[Bloque3_pfSense_UTM.drawio](sandbox:/mnt/data/Bloque3_pfSense_UTM.drawio)

Incluye:

- Internet/WAN
- Firewall UTM pfSense
- NAT y reglas de firewall
- Segmentación en:
  - LAN (192.168.10.0/24)
  - DMZ (192.168.20.0/24)
- Switch LAN
- Switch DMZ
- PCs de usuarios
- Servidor Web en DMZ
- Usuario remoto mediante VPN WireGuard
- IDS/IPS Suricata integrado en pfSense

Punto a revisar: este diagrama cumple los requisitos funcionales, pero para una entrega académica suele quedar mejor añadiendo:
- Etiquetas de interfaces (WAN, LAN, OPT1/DMZ).
- Reglas Allow/Deny sobre los enlaces.
- NAT Port Forward (80/443 → servidor DMZ).
- Tabla de direccionamiento IP.
- Leyenda de los servicios (VPN, IDS/IPS).

Puedo generar una versión más profesional, similar a la documentación de redes Cisco o de un TFG, lista para incluir en la memoria.

---
*Generado desde conversación con 6 mensajes.*
*IA/ML*
