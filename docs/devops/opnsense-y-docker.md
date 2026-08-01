---
title: OPNsense y Docker
date: 2026-06-06
category: DevOps
slug: opnsense-y-docker
tags: ['DevOps']
---

# OPNsense y Docker


> **Pregunta original:**
> 
OPNfense se puede utilizardocker
> GNS3se me esta haciendo dificl ,he pensado meterloen vmware workstation o en dokers 
> Tengo que monta runa red concliente , switchs , routers y opnfense , todo esto puede ser contenedores docker
> 
> *...y 1 preguntas de seguimiento*


---


## Respuesta


Si GNS3 se te está haciendo difícil, conviene analizar qué parte te está costando:

- **La topología de red** → cambiar a Docker no lo simplifica demasiado.
- **La instalación y gestión de imágenes** → Docker puede ser más sencillo.
- **La interfaz de GNS3** → VMware o Proxmox con VMs suele resultar más intuitivo.

### VMware Workstation

Para un laboratorio pequeño, una opción muy razonable es:

```text
VMware Workstation
├─ OPNsense
├─ Router Linux/FRR
├─ Cliente Ubuntu
├─ Cliente Windows
└─ Servidor Linux
```

Ventajas:
- Redes virtuales fáciles de visualizar.
- Snapshots.
- Menos curva de aprendizaje que GNS3.
- OPNsense funciona perfectamente.

Inconvenientes:
- Más consumo de RAM y CPU.
- Escala peor si quieres decenas de nodos.

### Docker

Docker es excelente para:

- Clientes Linux.
- Servidores Linux.
- Routers con FRR.

Pero cuando empiezas a necesitar:
- Varias NIC por equipo.
- VLANs complejas.
- Capturas de tráfico.
- Firewalls tipo OPNsense.

la complejidad de las redes Docker aumenta rápidamente.

### Una alternativa intermedia: Containerlab

urlContainerlabhttps://containerlab.dev está diseñado específicamente para laboratorios de red.

Ejemplo:

```text
Cliente1 --- Router1 --- Router2 --- Cliente2
```

Todo definido en un YAML y desplegado automáticamente.

Es bastante más simple que GNS3 para laboratorios basados en Linux/FRR.

### Mi valoración

**VMware Workstation**
- Más fácil de entender.
- Más parecido a equipos reales.
- Ideal para empezar.

**Docker puro**
- Menos recursos.
- Más automatización.
- Requiere entender redes Linux.

**GNS3**
- Más potente visualmente.
- Mayor curva de aprendizaje.

Si tu objetivo es aprender redes (VLAN, DHCP, NAT, OSPF, firewall con OPNsense) y no administrar una plataforma de simulación, probablemente obtendrás mejores resultados montando 4–6 VMs en VMware Workstation que intentando forzar todo dentro de Docker. Una vez que los conceptos estén claros, migrar a Containerlab o GNS3 suele resultar mucho más sencillo.
---


Si es un laboratorio, entonces sí puedes contenerizar casi todo.

## Opción A: Todo contenedores Linux (más ligera)

Usa:

- urlContainerlabhttps://containerlab.dev
- urlFRRouting (FRR)https://frrouting.org para routers
- Hosts Linux como clientes
- Bridges Linux como switches

Ejemplo:

```text
PC1 ---- SW1 ---- R1 ---- SW2 ---- PC2
                 |
                 R2
```

Todo ejecutándose en Docker.

### Ventajas
- Muy poco consumo de RAM.
- Se despliega en segundos.
- Fácil de versionar con YAML.
- Ideal para practicar:
  - VLANs
  - OSPF
  - BGP
  - NAT
  - ACLs
  - DHCP
  - DNS

### Inconvenientes
- No practicas específicamente OPNsense.
- Algunas funciones de firewall empresarial no están disponibles.

---

## Opción B: OPNsense + contenedores (más realista)

```text
                Internet
                    |
               OPNsense VM
                    |
                SW Docker
               /         \
          PC1 Docker   PC2 Docker

                    |
               Router FRR
```

- OPNsense en una VM (KVM, Proxmox, VirtualBox).
- Clientes y routers en Docker.

### Ventajas
- Aprendes la interfaz real de OPNsense.
- Puedes practicar:
  - NAT
  - Firewall Rules
  - VPN
  - IDS/IPS
  - DHCP
  - DNS Resolver
  - VLANs

### Inconvenientes
- Consume más recursos.
- Más complejidad.

---

## Opción C: GNS3 o EVE-NG

Si el objetivo es aprender redes de forma profesional, muchos laboratorios se montan con:

- urlGNS3https://www.gns3.com
- urlEVE-NGhttps://www.eve-ng.net

porque permiten mezclar:

- OPNsense
- Linux
- Cisco
- MikroTik
- Juniper
- Docker

en una misma topología visual.

## Evaluación

**Lo bueno de Docker puro**
- Muy rápido.
- Consume poco.
- Automatizable.

**Lo malo**
- Los "switches" son más abstracciones Linux que switches reales.
- Aprendes menos sobre appliances de seguridad.

**Lo bueno de incluir OPNsense**
- Más cercano a un entorno empresarial.
- Practicas firewalling real.

**Lo malo**
- Ya no es un laboratorio 100% contenedores.

Para un laboratorio personal en 2026, la combinación que suele dar mejor equilibrio es **Containerlab + FRR + una VM de OPNsense**. Obtienes realismo sin necesitar mucho hardware.
---


Técnicamente sí, pero depende de qué quieras conseguir.

### Si es para laboratorio, formación o pruebas

Puedes virtualizar prácticamente toda la red:

```text
Docker / Containerlab
 ├─ Clientes Linux
 ├─ Switches virtuales
 ├─ Routers virtuales
 └─ OPNsense
```

Sin embargo, **OPNsense normalmente no se ejecuta como contenedor Docker**. Al estar basado en FreeBSD y actuar como firewall/router completo, suele desplegarse como:

- Máquina virtual (VMware, KVM, Proxmox, VirtualBox).
- Equipo físico dedicado.

### Alternativas para una red 100% basada en contenedores

Herramientas como:

- urlContainerlabhttps://containerlab.dev
- urlGNS3https://www.gns3.com
- urlEVE-NGhttps://www.eve-ng.net

permiten crear topologías con:

- Hosts Linux (clientes).
- Routers FRR.
- Switches virtuales.
- Firewalls Linux.

Por ejemplo, usando urlFRRouting (FRR)https://frrouting.org como router en contenedor:

```text
Cliente A
    |
Switch virtual
    |
Router FRR
    |
Firewall
    |
Cliente B
```

Todo ello puede ejecutarse en contenedores.

### Si necesitas específicamente OPNsense

Lo más práctico sería:

```text
Host físico
 ├─ Docker
 │   ├─ Clientes
 │   ├─ Routers FRR
 │   └─ Servicios
 └─ VM OPNsense
```

Es decir, una VM para OPNsense y contenedores para el resto.

### Ventajas y desventajas

**Todo contenedores**
- Menor consumo de recursos.
- Despliegue rápido.
- Fácil automatización.

**Inconvenientes**
- No reproduce exactamente el comportamiento de equipos reales.
- Algunos switches/routers comerciales no tienen imágenes Docker oficiales.
- OPNsense no está pensado para ejecutarse como contenedor.

Si el objetivo es montar un laboratorio de redes completo (VLANs, OSPF, BGP, NAT, firewall, DHCP, DNS, etc.), hoy en día la combinación más utilizada es **Containerlab + FRR + una VM de OPNsense**. Es ligera, reproducible y muy cercana a un entorno real.
---


Sí. urlOPNsensehttps://opnsense.org puede utilizarse junto con Docker, pero hay varios matices importantes.

### Opción 1: OPNsense como firewall y Docker en otro servidor (recomendado)

La arquitectura más habitual es:

```text
Internet
    |
OPNsense
    |
Switch/LAN
    |
 ├─ Servidor Docker
 ├─ PCs
 └─ Otros dispositivos
```

Ventajas:

- Separación clara entre firewall y aplicaciones.
- Menor riesgo de comprometer el firewall.
- Actualizaciones independientes.
- Mejor rendimiento y estabilidad.

### Opción 2: OPNsense virtualizado y Docker en el mismo host

Por ejemplo:

```text
Proxmox
 ├─ VM OPNsense
 └─ VM Linux con Docker
```

Es una configuración muy común en laboratorios domésticos y pequeñas empresas.

Ventajas:
- Aprovechas el mismo hardware.
- Fácil gestión mediante hipervisor.

Inconvenientes:
- Si el host falla, pierdes tanto el firewall como los contenedores.
- Requiere configurar correctamente las interfaces de red.

### Opción 3: Instalar Docker directamente en OPNsense

No es lo habitual ni está oficialmente soportado.

OPNsense está basado en entity["software","FreeBSD","Unix-like operating system"], mientras que Docker está diseñado principalmente para Linux. Existen tecnologías equivalentes en FreeBSD como:
- Jails
- BastilleBSD
- Pot

Sin embargo:

- Docker no forma parte de la instalación estándar de OPNsense.
- Puede complicar actualizaciones.
- Aumenta la superficie de ataque del firewall.
- No suele recomendarse en entornos productivos.

### Si tu objetivo es...

| Objetivo | Recomendación |
|-----------|---------------|
| Tener OPNsense y varios contenedores | OPNsense en una VM y Docker en otra VM |
| Laboratorio casero | Proxmox + VM OPNsense + VM Docker |
| Router dedicado | OPNsense solo, sin Docker |
| Publicar servicios web detrás de OPNsense | Docker en un servidor aparte y OPNsense gestionando NAT, VLANs y firewall |

Si me indicas el hardware que tienes (por ejemplo Mini PC N100, N305, servidor Proxmox, etc.) puedo proponerte una arquitectura concreta.

---
*Generado desde conversación con 8 mensajes.*
*DevOps*
